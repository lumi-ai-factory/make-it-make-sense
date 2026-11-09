"""
rag.py — loading, chunking and searching the two web-scrape corpora.

Each organisation gets its own separate index, so a guide can only ever
find text that appears on its OWN organisation's website.

How it works:
  1. Load every .md file in a corpus folder.
  2. Split each page into chunks of about 800 characters.
  3. Encode each chunk with a simple TF-IDF vectoriser.
  4. Search by embedding the query and finding the nearest chunks
     via cosine similarity.

Test retrieval from the command line (no LLM involved):
  python rag.py "free computing for startups"
"""

import json
import math
import pathlib
import re
import string
import sys
from collections import Counter, defaultdict

# ---- where things live ------------------------------------------------------
BASE_DIR = pathlib.Path(__file__).resolve().parent
CORPUS_DIRS = {
    "thinkcompany": BASE_DIR / "corpus" / "thinkcompany",
    "aif": BASE_DIR / "corpus" / "aif",
}
MODEL_NAME = {
    "thinkcompany": "Helsinki Think Company",
    "aif": "LUMI AI Factory",
}

# ---- chunking settings ------------------------------------------------------
CHUNK_SIZE = 800
CHUNK_OVERLAP = 100

# ---- tokeniser (lightweight, handles Unicode letters) -----------------------
def tokenize(text):
    """Simple tokenizer: lowercase, split on non-alnum chars, drop short tokens."""
    return [
        m.lower()
        for m in re.findall(r'[a-zäöåéèêëàâùûüçéàâ]+', text.lower())
        if len(m) > 2
    ]

# ---- TF-IDF vectoriser (pure Python + numpy) -------------------------------
class TFIDFVectoriser:
    """Minimal TF-IDF vectoriser that supports incremental fit and transform."""

    def __init__(self, max_features=20000):
        self.max_features = max_features
        self.vocabulary = {}       # term -> index
        self.idf = {}              # term -> idf score
        self.n_docs = 0

    def _df(self, documents):
        """Calculate document frequency for each term."""
        df = Counter()
        for doc in documents:
            seen = set(doc)
            for term in seen:
                df[term] += 1
        return df

    def fit(self, documents):
        """Build vocabulary and IDF from corpus documents."""
        df = self._df(documents)
        n = len(documents)

        # Keep top terms by document frequency (but cap at max_features)
        common = [t for t, c in df.items() if c >= 2]      # appears in multiple docs
        rare = [t for t, c in df.items() if c < 2]          # appears in only one doc
        # Prefer common terms for vocabulary
        selected = common[:self.max_features]
        remaining = self.max_features - len(selected)
        if remaining > 0:
            selected.extend(rare[:remaining])

        self.vocabulary = {t: i for i, t in enumerate(selected)}
        self.idf = {}
        for term in self.vocabulary:
            doc_freq = df.get(term, 1)
            self.idf[term] = math.log((n + 1) / (doc_freq + 1)) + 1
        self.n_docs = n
        return self

    def _tf(self, document):
        """Calculate term frequency vector."""
        counts = Counter(document)
        total = max(len(document), 1)
        return {term: count / total for term, count in counts.items()}

    def transform(self, documents):
        """Transform documents to TF-IDF vectors."""
        matrices = []
        vocab_size = len(self.vocabulary)
        indices = list(self.vocabulary.values())
        terms = list(self.vocabulary.keys())

        for doc in documents:
            tf = self._tf(doc)
            vec = [0.0] * vocab_size
            for term, idx in zip(terms, indices):
                if term in tf:
                    vec[idx] = tf[term] * self.idf.get(term, 1.0)
            # L2 normalise
            norm = math.sqrt(sum(v * v for v in vec)) or 1.0
            vec = [v / norm for v in vec]
            matrices.append(vec)
        return matrices

    def cosine_similarity(self, a, b):
        """Cosine similarity between two L2-normalised vectors (dot product)."""
        return sum(x * y for x, y in zip(a, b))


# ---- front matter parsing ---------------------------------------------------
def parse_page(path):
    raw = path.read_text(encoding="utf-8")
    lines = raw.splitlines()

    if not lines or lines[0].strip() != "---":
        return path.stem, "", raw

    meta = {}
    end = None
    for i in range(1, len(lines)):
        line = lines[i].rstrip()
        if line.strip() == "---":
            end = i
            break
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if key in ("title", "url"):
                meta[key] = value

    if end is None:
        return path.stem, "", raw

    title = meta.get("title", path.stem)
    if title.startswith('"'):
        try:
            title = json.loads(title)
        except ValueError:
            pass
    url = meta.get("url", "")
    text = "\n".join(lines[end + 1:])
    return title, url, text


def clean_text(text):
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("#"):
            line = line.lstrip("#").strip()
            if not line:
                continue
        lines.append(line)

    cleaned = []
    for line in lines:
        if line:
            cleaned.append(line)
        else:
            if cleaned and cleaned[-1] != "":
                cleaned.append("")
    while cleaned and cleaned[-1] == "":
        cleaned.pop()
    return "\n".join(cleaned)


# ---- chunking -----------------------------------------------------------------
def _split_paragraphs(text):
    return [line for line in (l.strip() for l in text.splitlines()) if line]


def _cut_long_paragraph(paragraph):
    pieces = []
    rest = paragraph
    while len(rest) > CHUNK_SIZE:
        cut = CHUNK_SIZE
        for end in (". ", "! ", "? "):
            pos = rest.rfind(end, 0, CHUNK_SIZE)
            if pos > CHUNK_SIZE // 2:
                cut = pos + len(end)
                break
        pieces.append(rest[:cut].rstrip())
        rest = rest[cut:].lstrip()
    if rest:
        pieces.append(rest)
    return pieces


def chunk_text(text):
    blocks = _split_paragraphs(text)
    if not blocks:
        return []

    pieces = []
    for block in blocks:
        if len(block) > CHUNK_SIZE:
            pieces.extend(_cut_long_paragraph(block))
        else:
            pieces.append(block)

    chunks = []
    current = []
    current_len = 0
    for piece in pieces:
        joined = current_len + len(piece) + (1 if current else 0)
        if current and joined > CHUNK_SIZE:
            chunks.append("\n".join(current))
            current = []
            current_len = 0
            joined = len(piece)
        current.append(piece)
        current_len = joined
    if current:
        chunks.append("\n".join(current))
    return [c for c in chunks if c.strip()]


def _with_overlap(chunks):
    if len(chunks) <= 1:
        return chunks
    result = [chunks[0]]
    for prev, cur in zip(chunks, chunks[1:]):
        overlap = prev[-CHUNK_OVERLAP:]
        if overlap and " " in overlap:
            overlap = overlap[overlap.index(" ") + 1:]
        if overlap.strip():
            result.append(overlap.rstrip() + "\n" + cur)
        else:
            result.append(cur)
    return result


# ---- embedding index ---------------------------------------------------------
class CorpusIndex:
    """TF-IDF index over one organisation's pages."""

    def __init__(self, key, directory):
        self.key = key
        self.model_name = MODEL_NAME[key]
        self.chunks = []        # list of dicts: {title, url, text, vec}
        self.page_count = 0
        self.vectoriser = TFIDFVectoriser(max_features=10000)
        self._load(directory)

    def _load(self, directory):
        path = pathlib.Path(directory)
        if not path.is_dir():
            print(f"[rag] WARNING: {self.model_name!r} corpus dir not found")
            return

        for file in sorted(path.glob("*.md")):
            title, url, raw = parse_page(file)
            text = clean_text(raw)
            if not text.strip():
                continue
            self.page_count += 1
            page = {"title": title, "url": url}
            for chunk in _with_overlap(chunk_text(text)):
                self.chunks.append({**page, "text": chunk, "vec": None})

        # Build TF-IDF vectors
        texts = [c["text"] for c in self.chunks]
        tokens = [tokenize(t) for t in texts]
        print(
            f"[rag] {self.model_name!r}: "
            f"{self.page_count} pages, {len(tokens)} chunks, vectorising..."
        )
        self.vectoriser.fit(tokens)
        vecs = self.vectoriser.transform(tokens)

        for i, c in enumerate(self.chunks):
            c["vec"] = vecs[i]

        print(
            f"[rag] {self.model_name!r}: done "
            f"({self.page_count} pages, {len(self.chunks)} chunks)"
        )

    def search(self, query, top_k=5):
        """Return top_k most relevant chunks via cosine similarity."""
        if not self.chunks:
            return []
        q_tokens = tokenize(query)
        q_vec = self.vectoriser.transform([q_tokens])[0]

        scored = []
        for i, c in enumerate(self.chunks):
            sim = self.vectoriser.cosine_similarity(c["vec"], q_vec)
            scored.append((i, sim))

        scored.sort(key=lambda x: x[1], reverse=True)

        results = []
        for n, (idx, score) in enumerate(scored[:top_k], start=1):
            results.append(
                {
                    "n": n,
                    "title": self.chunks[idx]["title"],
                    "url": self.chunks[idx]["url"],
                    "text": self.chunks[idx]["text"],
                    "score": round(float(score), 3),
                }
            )
        return results


def load_all():
    """Load every corpus and print a summary. Called at app startup."""
    indexes = {}
    for key, directory in CORPUS_DIRS.items():
        index = CorpusIndex(key, directory)
        indexes[key] = index
        print(
            f"[rag] {MODEL_NAME[key]!r}: {index.page_count} pages, "
            f"{len(index.chunks)} chunks loaded"
        )
    return indexes


# ---- command line test ---------------------------------------------------------
if __name__ == "__main__":
    question = " ".join(sys.argv[1:]) or "free computing for startups"
    print(f'Searching for: "{question}"\n')
    indexes = load_all()
    for key, index in indexes.items():
        print(f"\n=== {MODEL_NAME[key]} ===")
        results = index.search(question, top_k=5)
        if not results:
            print("  (no chunks found)")
        for r in results:
            preview = r["text"].split("\n")[0][:90]
            print(f"  [{r['n']}] (score {r['score']}) {r['title']}")
            print(f"       url: {r['url']}")
            print(f"       {preview}...")
