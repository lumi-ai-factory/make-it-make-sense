---
title: "Benefits of the LUMI AI software environment | LUMI AI Factory"
url: https://lumi-ai-factory.eu/articles/benefits-of-the-lumi-ai-software-environment
lang: en
source: aif
scraped: 2026-11-02
---

1. News

# Benefits of the LUMI AI software environment

5 mins read

7.10.2026

 ![The LUMI supercomputer](https://lumi-ai-factory.eu/wp-content/uploads/2026/10/ln_lumi-1024x538-1-960x538.jpg)

The AI software environment in LUMI AI Factory consists of prebuilt containers that lower the threshold for developing many AI applications on LUMI. This allows you to get started faster with your AI workloads on LUMI instead of installing software yourself. By using the containers, you save effort and time required to set up the environment.

We ensure that the containers are optimally tuned for running on LUMI. They contain the most common AI libraries required and can be used as they are or adapted to your own needs. Using the containers is easy, and adapting requires no more knowledge than installing similar libraries on your laptop or in a cloud environment. See examples in our [documentation](https://docs.lumi-supercomputer.eu/laif/software/ai-environment/) and the [LUMI AI Guide](https://github.com/Lumi-supercomputer/LUMI-AI-Guide). Our AI experts provide further user support and consultation if needed, as described in our [earlier blog post](https://lumi-ai-factory.eu/articles/ai-expert-consultation/).

The containers are optimized for LUMI’s AMD MI250x GPUs, and the Slingshot interconnect provides a high-speed network that enables fast communication between nodes and within a node from GPU to GPU. You do not need to worry about installing PyTorch or others like the inference library vLLM or the model training library DeepSeek on LUMI.

While the provided containers cover many use cases, some projects require additional tools or custom software. We offer documentation on how to [extend the containers](https://docs.lumi-supercomputer.eu/laif/software/ai-environment/#build-new-containers-based-on-the-images) in these circumstances.

An important design decision with the containers is the transparency of the build process, which is the process that creates the containers. In our [public GitHub repository](https://github.com/lumi-ai-factory/laifs-container-recipes/releases), you can inspect the full build pipeline, including build logs, known issues, test results, and see exactly how the images are built. This ensures transparency and reproducibility for your AI workloads on LUMI.

## What’s inside the containers?

At the moment each software environment release includes multiple container images, each building on the previous one by adding new major functionality. This is visualised in the image below.

![](https://lumi-ai-factory.eu/wp-content/uploads/2026/10/Picture1.png)

Figure: Illustration of the different images building on top of each other. The images are 0: Ubuntu, 1: ROCm, 2: libfabric, 3: MPICH, 4: torch, and 5: full.

The first images [0: Ubuntu, 1: ROCm, 2: libfabric, and 3: MPICH] include support for the GPUs and Slingshot interconnect, allowing for fast communication between nodes and within a node from GPU-to-GPU.

The fourth image (4: torch) adds the popular deep learning framework PyTorch to the image while the final image (5: full) adds a selection of AI and machine learning libraries (e.g., Bitsandbytes, DeepSpeed, Flash Attention, Megatron LM, vLLM). Based on user feedback, we anticipate that the final image includes the required packages for most AI applications on LUMI.

In case the images do not contain all the software you require, you can install it yourself by following the [documentation](https://docs.lumi-supercomputer.eu/laif/software/ai-environment). Note that for some packages installing GPU versions or the correct communication libraries might require significant work. We recommend starting with a suitable image that includes most of the required software to mitigate the risk of that happening.

## Where to find LUMI AI Factory containers and documentation

The container images are available from the following locations:

- LUMI supercomputer in directory: /appl/local/laifs/containers/
- Docker Hub in the [LUMI AI Factory organisation](https://hub.docker.com/u/lumiaifactory)

A [public GitHub repository](https://github.com/lumi-ai-factory/laifs-container-recipes/releases) includes full details of the provided container images. You can:

- Subscribe to new releases
- Inspect container contents in detail
- Review known issues and test results
- See exactly how the images are built

This transparency helps users trust the environment where they are running their workloads in.

We provide documentation and examples:

- [AI Software Environment](https://docs.lumi-supercomputer.eu/laif/software/ai-environment/) in the LUMI Documentation
- Practical examples in the [LUMI AI Guide](https://github.com/Lumi-supercomputer/LUMI-AI-Guide). Here we demonstrate both simple single‑node runs and multi‑node distributed training setups.

## Getting help and support

If you encounter problems, LUMI User Support (LUST) is your first point of contact. Support information is available at: <https://lumi-supercomputer.eu/user-support/need-help/>

---

## **Written by**

![](https://lumi-ai-factory.eu/wp-content/uploads/2026/06/Mitja-S-edited-2.jpg)

Mitja Sainio

Machine Learning Engineer at the LUMI AI Factory

![Marlon Tobaben](https://lumi-ai-factory.eu/wp-content/uploads/2026/03/marlonto_LThumb.jpg)

Marlon Tobaben

Machine Learning Specialist at the LUMI AI Factory

![Kalle Huhtala](https://lumi-ai-factory.eu/wp-content/uploads/2026/03/kahuht_LThumb.jpg)

Kalle Huhtala

Senior Project Manager at the LUMI AI Factory

---

Read also other blogs in the series:

[Scaling reinforcement learning with verifiable rewards for LLMs on LUMI](https://lumi-ai-factory.eu/articles/scaling-reinforcement-learning/)

[What is LUMI AI Factory’s Artificial Intelligence expert consultation?](https://lumi-ai-factory.eu/articles/ai-expert-consultation/)

[Trustworthy AI: Turning compliance into competitive advantage](https://lumi-ai-factory.eu/articles/trustworthy-ai-turning-compliance-into-competitive-advantage/)

[AI agents and agent infrastructure on LUMI](https://lumi-ai-factory.eu/articles/agent-infrastructure-on-lumi/)

[Local agents, remote brains: connecting OpenCode to LUMI](https://lumi-ai-factory.eu/articles/local-agents-remote-brains-connecting-opencode-to-lumi/)

[Why supercomputing and LUMI?](https://lumi-ai-factory.eu/articles/blog-why-supercomputing-and-lumi/)
