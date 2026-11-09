# Make It Make Sense

Starter kit for the **Make It Make Sense** vibe coding hackathon by **LUMI AI Factory** and **Helsinki Think Company**.

Monday 9 November, 17:00–20:00, Think Company, Exactum, Kumpula campus.

## The rules

- **Build with Ahjo only.** Ahjo is LUMI AI Factory's inference platform. It runs open-weight models on-prem at CSC – IT Center for Science, the company that connected Finland to the internet in 1988, manages eduroam and runs Finnish supercomputers including Roihu and LUMI. You can brainstorm with any tool and LLM you like, but the code has to be written by OpenCode running on Ahjo. Using other LLMs via API or subscriptions is not allowed as the point of the hackathon is to see how capable medium sized LLMs already are, and what we can already achieve using sovereign tools. 
- **Your team shares one Ahjo API key.** I (Arthur) send it to all three of you, and you can all use it at the same time. Never share it outside your team or put it online: a leaked key can be used up by strangers within minutes, and then your team is out of tokens. All keys are revoked after the event.
- **Each key has a token limit, and a token rate limit per minute.** If your team hits the token limit, ask me and I can raise it. Ask me too if you're curious about your real time spending.
- **Don't run many subagents in parallel.** Ahjo can only generate so many tokens per minute, and that limit is shared by everyone at the hackathon. An agent that starts lots of subagents at once slows down Ahjo for all the other teams. One concurrent agent per person is plenty.
- **Extra points** for using LUMI AI Factory and Think Company branding: logos and colours.

## What's in this repo

| Folder | What it is |
|---|---|
| `Starter/` | Your workspace. Start OpenCode here. |
| `Starter/opencode.json` | Connects OpenCode to Ahjo. You don't need to edit it. |
| `Starter/AGENTS.md` | Instructions the agent reads automatically: container rules, port, Ahjo. Don't change anything here |
| `Starter/NOTES.md` | The agent's memory between sessions. It reads and updates this file itself. |
| `Starter/Brand/` | Logos and colours of LUMI AI Factory and Think Company. |
| `Starter/Corpus/` | Both organisations' websites scraped to Markdown (about 340 pages, English and Finnish). Good material for chatbots, quizzes, search and more. |
| `Examples/` | Three projects built with Ahjo models, for your inspiration. |

### Examples

- **AI Startup Idea Slot Machine** (`Examples/ai-slot-machine/`): spin the reels to get a random AI startup idea. A single HTML file; open it in your browser.
- **Swipe the Startup, AI Act Edition** (`Examples/swipe-the-startup/`): swipe through startup ideas and guess how the EU AI Act treats them. A single HTML file; open it in your browser.
- **Two Guides, One Question** (`Examples/two-guides/`): a chatbot where a Think Company guide and a LUMI AI Factory guide each answer from their own website, using the corpus (RAG). This example is very ambitious, probably too ambitious for the ~2h of the hackathon using the MoE Qwen3.6. Consider aiming for smaller projects. 

## Setup (about 5 minutes)

You should already have Podman set up from our email. **On Mac and Windows, open Podman Desktop first and wait until the machine is running.**

### 1. Get the repo

With Git:

```bash
git clone https://github.com/lumi-ai-factory/make-it-make-sense.git
```

Without Git: on the GitHub page, click **Code → Download ZIP**, then unzip it.

### 2. Open a terminal in the `Starter` folder

- **Mac:** right-click the `Starter` folder, then **Services → New Terminal at Folder**.
- **Windows:** open the `Starter` folder, right-click inside it and choose **Open in Terminal**. Make sure it says **PowerShell**.
- **Linux:** `cd make-it-make-sense/Starter`

You can also copy `Starter` somewhere else first, for example into the hackathon folder you made earlier, and use that copy.

I couldn't test the instructions for Mac and Windows, so please let me know if something doesn't work and, if you know, how to fix it.

### 3. Save your Ahjo key

Create a file called `ahjo-key.txt` in the `Starter` folder that contains only your key. In the command below, **replace `YOUR_KEY` with the Ahjo key I sent you**. Keep the quotes.

Mac and Linux:

```bash
echo "YOUR_KEY" > ahjo-key.txt
```

Windows (PowerShell):

```powershell
Set-Content ahjo-key.txt "YOUR_KEY"
```

### 4. Start OpenCode in the container

**Use the command below, not the one from our email.** This one adds two things:

- `127.0.0.1:` in front of the port, so your app is reachable only from your own laptop, not by everyone on the event wifi.
- `-v opencode-data:...`, which keeps your chat sessions when OpenCode closes.

Mac and Linux:

```bash
podman run -it --rm -p 127.0.0.1:8000:8000 -v opencode-data:/root/.local/share/opencode -v "$(pwd)":/workspace:Z -w /workspace ghcr.io/anomalyco/opencode:1.19.5
```

Windows (PowerShell):

```powershell
podman run -it --rm -p 127.0.0.1:8000:8000 -v opencode-data:/root/.local/share/opencode -v "${PWD}:/workspace" -w /workspace ghcr.io/anomalyco/opencode:1.19.5
```

If you use Docker, write `docker` instead of `podman`.

Note on the IP address: inside the container, the coding agent should use 0.0.0.0 for serving the web app. If **you** are starting the web app **outside** the container, use 127.0.0.1 instead to avoid opening the app to all devices connected to the same wi-fi network. This instruction is already in AGENTS.md, but the coding agent might not be very obedient. 

**To continue where you left off** after closing OpenCode and its container, run the same command with ` -c` added at the very end. That reopens your last session. Or start it normally, type `/sessions` and pick the session you want.

### 5. Check that it works

At the bottom of the OpenCode screen you should see **Qwen3.6 35B A3B** and **Ahjo**. Type `Hello` and press Enter. If it answers, you're ready to build.

When the agent builds a web app, open **http://localhost:8000** in your browser.

<details>
<summary><b>New to OpenCode? Click here!</b></summary>

Type `/` to see all commands.

| Key or command | What it does |
|---|---|
| **Esc** twice | Stops the agent mid-answer, for example when it's going the wrong way or if it's stuck with a hanging command. |
| **Tab** | Switches between **Build** (makes changes) and **Plan** (only discusses and plans, doesn't touch files). Plan is good for thinking an idea through first. |
| `@` | Mentions a file, for example `@README.md`, so the agent looks at it. |
| `/undo` | Takes back your last message and the file changes it caused. `/redo` brings them back. |
| `/new` | Starts a fresh session with empty context. Useful when the agent gets confused or if you notice context rot (outputs getting worse at long context). |
| `/sessions` | Lists your earlier sessions so you can go back to one. |
| `/compact` | Summarises a long session so it fits the model's memory again. OpenCode will do that automatically when you get close to the model's context size limit. |
| `/models` | Switches the model. Qwen is the default. You can also pick **Nemotron 3.5 Lightning 30B A3B**: it's another model on Ahjo, with a much longer memory (1M tokens) and it's a bit faster, but a bit worse coding skills than Qwen. |
| **Ctrl+P** | Opens the list of all commands. |
| **Ctrl+C** or `/exit` | Quits OpenCode and closes the container. Your sessions and the files in your folder are kept, but anything the agent installed is gone. |

**Saving:** you never need to save. The agent edits the files in your folder and saves them itself.

**Chat history** is saved automatically after every message. To continue an earlier session, type `/sessions` and pick it, or add ` -c` at the end of the start command to reopen the last one (see step 4).

**Sending us your chat log:** type `/export`. A small window opens with a file name like `session-1a2b3c4d.md`. Then press **Enter**. The whole chat is saved as that file in your folder.

**Copying text:** hold **Shift** while you select with the mouse, then copy as usual (while holding Shift since ctrl+C exits OpenCode). OpenCode's own copy doesn't work in the container in most terminals.

</details>

## Good to know

- **Keep the context short.** The model gets worse as a session grows long. Run /compact when the context grows large (and make use of NOTES.md!). Start /new sessions when switching to a brand new task that does not need any previous context. If the agent is stuck trying to fix a bug for too long, consider opting for a simpler solution. 
- **The agent runs on full auto.** It edits files and runs commands without asking. That's safe because the container can only see the `Starter` folder (or your copy of it). It can't touch the rest of your laptop.
- **Your files are saved on your laptop.** Quitting OpenCode (Ctrl+C) closes the container. Run the same command with ` -c` at the end to continue your last session (see step 4). Things the agent installed (Python, Node and so on) are deleted after a restart, so the agent needs to reinstall them after every restart. Python packages in `.venv` survive. The agent also keeps notes in `NOTES.md` and reads them when it starts. Remind the agent to use notes after important decisions or changes. 
- **Back up your folder regularly**. In your file manager, copy the whole folder to somewhere else on your computer as a backup. The copy is outside the container, so even a confused agent can't delete it.
- **Work in steps.** Describe what you want, let the agent build a small version, try it in the browser, then ask for the next change. Tell the agent exactly what's wrong ("the button does nothing", "the text is unreadable on mobile").
- **Your team has one driver.** Split the tasks. One of you drives the agent and writes the code, while the other two have plenty to do at the same time:
  - **Shape the idea:** decide what the app does and for whom, and draft the next prompt for the driver. You can brainstorm with any chatbot. You may find or generate images using other LLMs (ChatGPT, Gemini, etc). 
  - **Write the content:** texts, quiz questions, game levels, example questions. Find good material in `Corpus/`.
  - **Test:** try the app on the driver's laptop and report exactly what's broken or confusing.
  - **Prepare the presentation:** slides, screenshots, and a 1-minute demo script that shows the best part first.
- **Apps that use LLMs** call Ahjo too. The agent knows how from `AGENTS.md`, and your app reads the key from `ahjo-key.txt`.

## Troubleshooting

| Problem | Fix |
|---|---|
| OpenCode says the API key is missing or invalid | `ahjo-key.txt` must be in the folder where you started the container, and contain only the key. On Windows, check that it isn't called `ahjo-key.txt.txt`. |
| `Cannot connect to Podman` (Mac and Windows) | Open Podman Desktop and start the Podman machine. |
| `user namespaces are not enabled` (Linux) | Run `sudo sysctl kernel.unprivileged_userns_clone=1` and try again. |
| `address already in use` for port 8000 | Another container is still running. Run `podman ps`, then `podman stop <id>`. |
| http://localhost:8000 doesn't load | Ask the agent: "Is the server running on 0.0.0.0 port 8000?" |
| The agent has been stuck on one command for minutes | Press **Esc** twice to interrupt. Tell it: "Start the server with `nohup <command> > server.log 2>&1 &`." |
