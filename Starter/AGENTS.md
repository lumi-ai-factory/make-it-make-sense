# Agent instructions

- You run in a Podman container (Alpine Linux, root) at the Make It Make Sense hackathon.
  Only /workspace is shared with the user's laptop. Stay inside /workspace.
- Nothing is preinstalled. Install with `apk add <pkg>`
  (e.g. python3 py3-pip nodejs npm curl). Re-run it after a container restart.
- Python packages: use a venv in /workspace (`python3 -m venv .venv`).
  System-wide pip install is blocked.
- Web apps must listen on 0.0.0.0, port 8000, because that is how the port leaves the container.
  Podman publishes it only on the user's 127.0.0.1, so the app stays private to their laptop.
  The user opens http://localhost:8000. If you ever tell the user to run something
  on their laptop directly, outside the container, it must bind to 127.0.0.1, never 0.0.0.0.
  Start servers only as `nohup <command> > server.log 2>&1 & echo $! > server.pid`.
  A plain `<command> &` without the redirect keeps your shell tool waiting until it times out.
  Stop a server with `kill $(cat server.pid)`. Never use `pkill -f` or `killall`:
  `pkill -f` also matches your own shell command and hangs or kills the tool.
  Put the app in /workspace/app/ and serve only that folder, never /workspace itself.
  After starting a server, check server.log and test it with `wget -qO- localhost:8000`.
- `ahjo-key.txt` contains the API key for Ahjo, the LLM inference platform.
  Never open, print, copy or commit it yourself. Never serve the whole /workspace
  folder, because the key file is in it.
- If an app needs an LLM, it calls only Ahjo (OpenAI-compatible):
  base URL https://api.ahjo.csc.fi/v1, model qwen3.6-35b-a3b.
  The app's server-side code reads the key from ahjo-key.txt at runtime.
  Never hardcode the key or send it to the browser.
- Before a big or risky change, back up the files you're about to change into
  /workspace/backups/<HHMM>/. Never delete anything in backups/.
- NOTES.md is your long-term memory.
  Update it when something important changes: what you're building, how to run it,
  what you installed, decisions, known problems. Keep it short and meaningful.
