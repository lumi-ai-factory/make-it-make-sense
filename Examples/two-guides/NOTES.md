# Project notes

The agent's long-term memory. It reads this file at the start of every session and keeps it up to date.

## What we're building

A two-guide RAG chatbot. A single question is sent to both Helsinki Think Company (entrepreneurship) and LUMI AI Factory (AI building/compute), each answering from their own website corpus. The LLM streams back results concurrently via Server-Sent Events.

- **Stack**: Flask, sentence-transformers (RAG), OpenAI-compatible client (Ahjo/qwen3.6-35b-a3b)
- **Corpora**: `corpus/aif/` (LUMI AI Factory) and `corpus/thinkcompany/` (Helsinki Think Company), both .md files
- **Frontend**: `static/index.html`
- **Backend**: `app.py` (Flask), `rag.py` (RAG indexing/search), `prompts.py` (personas)

## How to run it

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://localhost:8000

## Decisions

- Two organisations with separate RAG indexes, queried in parallel
- Ahjo (CSC) as LLM provider: base URL `https://api.ahjo.csc.fi/v1`, model `qwen3.6-35b-a3b`
- API key sourced from `AHJO_API_KEY` env var → `.env` → `ahjo-key.txt` (fallback chain)
- Streaming tokens via SSE, interleaved from both guides

## Known problems

(none yet)
