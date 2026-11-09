---
title: "AI agents and agent infrastructure on LUMI | LUMI AI Factory"
url: https://lumi-ai-factory.eu/articles/agent-infrastructure-on-lumi
lang: en
source: aif
scraped: 2026-11-02
---

1. News

# AI agents and agent infrastructure on LUMI

4 mins read

5.6.2026

AI coding agents like [Claude Code](https://code.claude.com/docs/en/overview) and [OpenAI Codex](https://openai.com/codex/) have become popular tools for coding on LUMI. When used responsibly, they can lower the barrier to entry for new users and speed up everyday work for experienced ones. To help users get the most out of agents, we have released the new [LUMI AI agent guide](https://docs.lumi-supercomputer.eu/development/ai-tools/ai-agent-guide/).

The guide covers different aspects of agent usage, such as best practices, relation to the LUMI Terms of Use, as well as the user’s responsibilities. These are required reading for all LUMI users who use agents, since the user who starts an agent is ultimately and unequivocally accountable for it.

In addition to this guidance, we provide the initial version of our [LUMI AI Factory AI agent infrastructure](https://docs.lumi-supercomputer.eu/laif/software/agent-infrastructure). The agent infrastructure currently comprises two components. The LUMI AI Factory agent environment is a containerised environment that allows users to run AI coding agents on LUMI securely and with sensible defaults. The LUMI AI Factory MCP (Model Context Protocol) server can be connected to any AI agent to provide it with additional context about LUMI, which allows agents to give more accurate answers grounded in LUMI’s user documentation.

## Agent environment

The [LUMI AI Factory agent environment](https://docs.lumi-supercomputer.eu/laif/software/agent-infrastructure/#agent-environment) is a [containerised environment](https://docs.lumi-supercomputer.eu/software/containers/singularity/) that allows users to run AI coding agents more securely and effectively on LUMI. Currently, we provide a container for using the open-source, terminal-based [OpenCode](https://opencode.ai/) AI coding agent. For more information on using OpenCode, see the blog post on [connecting OpenCode to a vLLM instance running on LUMI](https://lumi-supercomputer.eu/connecting-opencode-to-lumi/).

The LUMI-specific configuration files included in the agent environment transform OpenCode  into a capable AI assistant for using LUMI, but users should remember to follow the [LUMI AI agent guide](https://docs.lumi-supercomputer.eu/development/ai-tools/ai-agent-guide/) and read the agent environment’s documentation to understand potential risks before using it.

## Using OpenCode as an AI assistant for LUMI

We demonstrate the usefulness of the agent environment using a practical example. Making use of the LUMI-specific configuration included in the environment, we ask the agent how to install PyTorch on LUMI. Rather than, e.g., erroneously walking us through a manual installation, the agent, using the LUMI AI Factory MCP server, correctly refers us to the [LUMI AI Factory AI software environment](https://docs.lumi-supercomputer.eu/laif/software/ai-environment/), which is exactly the guidance a beginning user should be presented with. Using this same setup, we may also draft Slurm scripts or ask questions about different aspects of the LUMI. As with any AI tool, the outputs of the agent should always be validated against the [LUMI documentation](https://docs.lumi-supercomputer.eu/).

![](https://lumi-ai-factory.eu/wp-content/uploads/2026/06/Code.png)

Example use of OpenCode as an AI assistant for LUMI. The user asks questions about installing PyTorch on LUMI. The agent replies correctly, as it retrieves documentation using the LUMI AI Factory MCP server.

## MCP server

The LUMI AI Factory provides a public [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) server. The [LUMI AIF MCP server](https://docs.lumi-supercomputer.eu/laif/software/agent-infrastructure/#mcp-server) features a tool called *retrieve\_docs,* which allows agents to search a regularly updated knowledge base of [LUMI documentation](https://docs.lumi-supercomputer.eu/) and the [LUMI AI Guide](https://github.com/Lumi-supercomputer/LUMI-AI-Guide). The search functionality is implemented using an embedding model that is run locally on the MCP server host.

Access to this tool allows AI agents to, e.g., answer questions about LUMI with greater accuracy and write code that takes into account LUMI’s particular system architecture and software environment. You can find more about the server in the LUMI documentation, including how to add it to a local software development environment like VSCode, OpenCode, Claude Code or Codex.

Are you an industry user and need more in-depth support? Check out our [blogpost on consulting](https://lumi-ai-factory.eu/articles/ai-expert-consultation/). If you want more information on why to use supercomputing and LUMI, check out [this blogpost](https://lumi-ai-factory.eu/articles/blog-why-supercomputing-and-lumi/).

Read also other blogs in the series:

[Why supercomputing and LUMI?](https://lumi-ai-factory.eu/articles/blog-why-supercomputing-and-lumi/)

[What is LUMI AI Factory’s Artificial Intelligence expert consultation?](https://lumi-ai-factory.eu/articles/ai-expert-consultation/)

[Trustworthy AI: Turning compliance into competitive advantage](https://lumi-ai-factory.eu/articles/trustworthy-ai-turning-compliance-into-competitive-advantage/)

[Local agents, remote brains: connecting OpenCode to LUMI](https://lumi-ai-factory.eu/articles/local-agents-remote-brains-connecting-opencode-to-lumi/)

---

## **Written by**

![](https://lumi-ai-factory.eu/wp-content/uploads/2026/06/Mitja-S-edited-2.jpg)

Mitja Sainio

Junior Application Specialist at LUMI AI Factory

![Marlon Tobaben](https://lumi-ai-factory.eu/wp-content/uploads/2026/03/marlonto_LThumb.jpg)

Marlon Tobaben

Machine Learning Specialist at LUMI AI Factory
