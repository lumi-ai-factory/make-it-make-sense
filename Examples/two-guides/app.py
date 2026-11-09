"""
app.py — Flask server for "Two Guides"

Wires together rag.py (RAG retrieval), prompts.py (system prompts),
and the Ahjo LLM API (qwen3.6-35b-a3b).

Serves static frontend and exposes /api/health + /api/ask endpoints.
Listens on 127.0.0.1:8000 (localhost only).
"""

import json
import os
import pathlib
import re
import time

import openai
from flask import Flask, Response, jsonify, request, send_from_directory

from prompts import ORGANISATIONS, system_prompt_for
from rag import load_all

# ── paths ────────────────────────────────────────────────────────────────
BASE_DIR = pathlib.Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

# ── app ─────────────────────────────────────────────────────────────────
app = Flask(
    __name__,
    static_folder=str(STATIC_DIR),
    static_url_path="",
)

# ── RAG index (loaded once at startup) ──────────────────────────────────
indexes = load_all()

# ── LLM client ──────────────────────────────────────────────────────────
def get_api_key():
    """Read key from .env, ahjo-key.txt, or environment variable."""
    key = os.environ.get("AHJO_API_KEY", "").strip()
    if key:
        return key
    env_path = BASE_DIR / ".env"
    if env_path.is_file():
        with open(env_path) as f:
            for line in f:
                m = re.match(r'^AHJO_API_KEY=(.+)$', line.strip())
                if m:
                    return m.group(1).strip()
    key_path = BASE_DIR / "ahjo-key.txt"
    if key_path.is_file():
        return key_path.read_text(encoding="utf-8").strip()
    return ""


LLM_CLIENT = openai.OpenAI(
    api_key=get_api_key(),
    base_url="https://api.ahjo.csc.fi/v1",
)
LLM_MODEL = os.environ.get("AHJO_MODEL", "qwen3.6-35b-a3b")
MAX_TOKENS = 4096


# ── SSE helpers ─────────────────────────────────────────────────────────
def sse(msg, event=None):
    """Format a single SSE frame. msg is JSON-encoded to preserve newlines."""
    encoded = json.dumps(msg)
    if event is not None:
        return f"event: {event}\ndata: {encoded}\n\n"
    return f"data: {encoded}\n\n"


def ask_llm_stream(system, user_text):
    """Stream tokens from the LLM. Yields each token immediately."""
    response = LLM_CLIENT.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user_text},
        ],
        stream=True,
        max_tokens=MAX_TOKENS,
    )
    for chunk in response:
        if chunk.choices and chunk.choices[0].delta.content:
            token = chunk.choices[0].delta.content
            if token:
                yield token


def build_rag_user(chunks, question):
    """Build user message for a single organisation."""
    from prompts import build_user_message
    return build_user_message(chunks, question)


def send_with_error(guide_key, stream_gen, sent_token):
    """Drain a token generator, sending SSE, with error handling."""
    full_text = ""
    try:
        for token in stream_gen:
            full_text += token
            if sent_token:
                sent_token(token)
    except Exception as e:
        # Send partial answer on error
        if full_text:
            yield f"{guide_key}\t{full_text}"
        else:
            yield f"{guide_key}\tError: {e}"
    yield f"{guide_key}\t{full_text}"


# ── routes ──────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return send_from_directory(STATIC_DIR, "index.html")


@app.route("/api/health")
def health():
    info = {}
    for key in indexes:
        idx = indexes[key]
        info[key] = {
            "pages": idx.page_count,
            "chunks": len(idx.chunks),
            "name": idx.model_name,
        }
    # Try a quick model check
    model_ok = False
    try:
        LLM_CLIENT.chat.completions.create(
            model=LLM_MODEL,
            messages=[{"role": "user", "content": "Hi"}],
            max_tokens=3,
        )
        model_ok = True
    except Exception:
        pass
    return jsonify({"status": "ok", "corpus": info, "model_reachable": model_ok})


@app.route("/api/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    question = data.get("question", "").strip()
    if not question:
        return jsonify({"error": "Missing question"}), 400
    if len(question) > 500:
        return jsonify({"error": "Question too long (max 500 chars)"}), 400

    def generate():
        results = {}
        for key in indexes:
            chunks = indexes[key].search(question, top_k=5)
            results[key] = chunks

        # Send sources for both guides
        sources_json = {k: v for k, v in results.items()}
        yield sse(sources_json, event="sources")

        # Build per-guide prompts
        prompt_data = {}
        for key in indexes:
            sys_prompt = system_prompt_for(key)
            other_key = "aif" if key == "thinkcompany" else "thinkcompany"
            prompt_data[key] = {
                "sys": sys_prompt.format(
                    name=ORGANISATIONS[key]["name"],
                    role=ORGANISATIONS[key]["role"],
                    other_name=ORGANISATIONS[other_key]["name"],
                    other_role=ORGANISATIONS[other_key]["role"],
                ),
                "user": build_rag_user(results[key], question),
            }

        # Run both LLM streams concurrently, collect frames, write with a lock
        from queue import Queue, Empty
        import threading

        frame_queues = {k: Queue() for k in indexes}
        output_lock = threading.Lock()
        started = [0]

        def stream_guide(key):
            try:
                pd = prompt_data[key]
                for token in ask_llm_stream(pd["sys"], pd["user"]):
                    frame = sse(f"{key}\t{token}", event="token")
                    frame_queues[key].put(frame)
            except Exception as e:
                frame = sse(f"{key}\tError: {e}", event="error")
                frame_queues[key].put(frame)
            finally:
                frame_queues[key].put(None)

        def drain(key):
            while True:
                frame = frame_queues[key].get()
                if frame is None:
                    break
                with output_lock:
                    yield frame

        threads = {}
        for key in indexes:
            t = threading.Thread(target=stream_guide, args=(key,), daemon=True)
            t.start()
            threads[key] = t

        # Interleave frames from both guides (non-blocking)
        while True:
            yielded = False
            for key in indexes:
                try:
                    frame = frame_queues[key].get_nowait()
                    if frame is None:
                        continue
                    yield frame
                    yielded = True
                except Empty:
                    pass
            if not yielded:
                if all(not t.is_alive() for t in threads.values()):
                    break
                time.sleep(0.02)

        yield sse("done", event="done")

    return Response(generate(), mimetype="text/event-stream")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
