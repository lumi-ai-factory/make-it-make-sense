# Two Guides

A local RAG app that answers questions using two knowledge bases (Helsinki Think Company and LUMI AI Factory) with a Qwen3.6 LLM.

## Setup

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## API Key

Copy `.env.example` to `.env` and paste your Ahjo API key into `AHJO_API_KEY`.

Alternatively, you can place your key in `ahjo-key.txt` (in this directory) and copy the content to `.env`. The file `ahjo-key.txt` is listed in `.gitignore` so it won't be committed.

The key stays on your machine — never sent to the browser.

## Run

```
source .venv/bin/activate
python app.py
```

Then open http://127.0.0.1:8000 in your browser.

The server binds to 127.0.0.1 only — it is not reachable from the network.

## Verify

```bash
curl http://127.0.0.1:8000/api/health
```

Should report that the corpus is loaded and the model is reachable.

## Test retrieval (no LLM)

```
python rag.py "your question"
```

## Customisation

- **Brand colours**: edit the `--tc-*` / `--aif-*` CSS variables in `static/index.html`
- **Guide personas**: `prompts.py`
- **Token budget** (for thinking models): `MAX_TOKENS` in `app.py`
