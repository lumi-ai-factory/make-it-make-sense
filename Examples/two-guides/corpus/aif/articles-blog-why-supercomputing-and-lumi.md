---
title: "Why supercomputing and LUMI? | LUMI AI Factory"
url: https://lumi-ai-factory.eu/articles/blog-why-supercomputing-and-lumi
lang: en
source: aif
scraped: 2026-11-02
---

1. News

# Why supercomputing and LUMI?

8 mins read

19.3.2026

 ![LUMI supercomputer. Image: CSC](https://lumi-ai-factory.eu/wp-content/uploads/2026/03/ln_lumi_blog_post-960x540.jpg)

Image: Mikael Kanerva, CSC

This blog post aims to explain supercomputing and [the LUMI supercomputer](http://www.lumi-supercomputer.eu) to industry customers interested in leveraging LUMI for their R&D efforts. LUMI is the current computational backbone for the LUMI AI Factory. We explain the concepts of supercomputers and high‑performance computing (HPC), provide use-case examples leveraging a supercomputer, and explain what kind of tasks a supercomputer like the LUMI supercomputer is good for. Finally, we explain what knowledge is required to use a supercomputer.

## What is supercomputing and high-performance computing (HPC)?

A supercomputer is a large cluster of smaller computers (“nodes”) that work together to solve a numerical task. High-performance computing (HPC) leverages multiple nodes by dividing heavy computational tasks into smaller subtasks and distributing them across multiple nodes. Each node processes its part at the same time, a method known as parallel processing. This approach reduces the time needed to reach a solution compared to using a single node.

*Example: Imagine trying to conduct a monthly municipality level analysis about the housing market in Finland: Running the analysis takes up to two hours on your laptop for the largest municipality in Finland. Extending it to all 308 municipalities in Finland is possible on your laptop, but it will take a day or longer. On a supercomputer it might be possible to run it in parallel by letting each node compute the analysis for only one municipality. Now the result will be finished in two hours showcasing the benefit of parallel computing. This becomes especially obvious when extending to other countries , e.g., Germany, which has more than 10,000 municipalities.*

In daily work, we often use laptops or personal computers. A laptop usually only contains a central processing unit (CPU), but a personal computer can additionally contain a graphic processing unit (GPU). Each supercomputer node contains multiple CPUs, and optionally also multiple GPUs. The LUMI supercomputer, for example, has 2,048 nodes with CPUs only and 2,978 nodes that additionally have 4 GPUs each. In total LUMI contains more than 7,000 CPUs and approximately 12,000 GPUs. Note that the CPUs and GPUs in LUMI are more powerful than those usually included in personal computers.

![Visualisation about LUMI's GPU nodes. Copyright: CSC](https://lumi-ai-factory.eu/wp-content/uploads/2026/03/LUMI_GPU_Node_visualisation_for_blog_post1-800x450.jpg)

Image: Visualisation about LUMI’s GPU nodes. Copyright: CSC

Each node has (large amounts of) local memory that can be used to store data for immediate use, but is also connected to more permanent storage spaces for saving large amounts of data. The different nodes of a supercomputer are connected via a fast connection, which is essential in supercomputing, as multiple nodes often work together to solve a numerical task.

## Use case examples

We will introduce some use cases for LUMI, but you can find more [here](https://lumi-supercomputer.eu/news-and-articles/use-cases/):

- The space technology company ICEYE [moved the development of its automated image interpretation to LUMI](https://lumi-supercomputer.eu/space-technology-company-iceye-praises-lumi-user-support-expert-guidance-step-by-step/).
- The company Scorable (formerly Root Signals) [developed a large language model (LLM) to judge the reliability of other LLMs](https://lumi-supercomputer.eu/root-signals/). The LUMI documentation allowed for a smooth start to their R&D project on LUMI.
- Digifarm, a Norwegian company, uses LUMI to [improve its machine learning model](https://lumi-supercomputer.eu/digifarm-revolutionises-agriculture-with-artificial-intelligence/) that supports agriculture in many countries based on large amounts of satellite data. The use of LUMI significantly shortens the path from testing to market-ready.

## What kind of tasks LUMI is good for, and other reasons to use a supercomputer

HPC leverages multiple nodes by dividing a heavy computational task into smaller subtasks. This enables parallelism, allowing a solution to be reached faster with multiple nodes than with a single node.

Common use cases for leveraging parallelism in HPC sometimes arise naturally from the problem domain of the heavy computational task. For example, analysing housing data in Finland can be done for each municipality separately in parallel. The results from the single municipalities are then combined to obtain the result for the whole of Finland. This approach is sometimes called “divide and conquer” as the problem is broken down into smaller problems that are then feasible to compute on one node.

![Training time comparison: LUMI vs. laptop. Original version of the figure by Kim Takala, CSC.](https://lumi-ai-factory.eu/wp-content/uploads/2026/03/training_comparison2.gif)

*Image: Training time comparison for example workload that can be highly parallelisable: LUMI vs. laptop. Original version of the figure by Kim Takala (LUMI User Support Team, CSC).*

Another example of this approach is the training of deep learning models using large datasets, where the training data at every step of the optimisation process is distributed over multiple nodes to compute updates. These individual updates are then combined. See an example in the [LUMI AI Guide](https://github.com/Lumi-supercomputer/LUMI-AI-Guide/tree/main/5-multi-gpu-and-node).

However, a computational task does not have to be massive to use a supercomputer. Perhaps you have many smaller experiments, e.g., when trying out different configurations of your program. Using the many nodes of a supercomputer you can run all of them at the same time, which is an example of trivial parallelism. There is no limit to the scalability as the individual smaller experiments are independent from each other.

There are other good reasons for using a supercomputer such as LUMI:

- Outsourcing heavy/specialised computations: One can outsource heavy/specialised computations to a remote server.
- Prebuilt environment and software: Supercomputers offer comprehensive [pre-installed stacks of software and libraries](https://docs.lumi-supercomputer.eu/software/).
- Easy to collaborate: On LUMI it is easily possible to invite collaborators to your project, which might be more complicated with an internal computing environment. This also enables public-private co-innovation.
- Expert support: The LUMI AI Factory not only has hardware, but also [supercomputing and machine learning experts](https://lumi-ai-factory.eu/user-support/). These experts can help you with anything from setting up your experiments or programs, troubleshooting problems to setting up complete computing pipelines. The European Union project [EPICURE](https://epicure-hpc.eu/) provides similar support to non-AI applications.
- Training: LUMI and the LUMI AI Factory also [frequently organise on-site courses](https://lumi-ai-factory.eu/trainings/), webinars, hackathons, and have [self-learning material available](https://lumi-supercomputer.github.io/LUMI-training-materials/). These are done in collaboration with the manufacturers of LUMI’s hardware and software, as well as with other European HPC centres and projects.
- Data: The LUMI AI Factory [Dataset-as-a-Service (DaaS)](https://lumi-ai-factory.eu/services/dataset-as-a-service/) offers access to high-quality datasets. This allows you to more easily access datasets from the LUMI supercomputer.

## What basic skills are needed to use a supercomputer?

A common misconception is that advanced programming skills are required to use a supercomputer. While these programming skills can be useful, they are only required when writing lower-level program code. So what skills are actually required?

- Understanding batch jobs and resource management: Supercomputers work (mostly) with batch jobs, where a batch script acts as a kind of recipe for the computation on the supercomputer. This recipe specifies the requested resources in terms of the number and type of nodes, the program to be executed, and the time that should be reserved. The batch job is added to a queue, so it will be executed once sufficient computational resources are available. [See the introduction to batch jobs on LUMI docs](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/slurm-quickstart/).
- Supercomputers run on Linux: Basic Linux commands and shell scripting knowledge are useful when formulating batch scripts to run your computational problem on a supercomputer and when transferring data and results. See a [tutorial on Linux basics](https://docs.csc.fi/support/tutorials/env-guide/) in the CSC documentation.
- Connecting to a supercomputer: A supercomputer is a remote server that one connects to via SSH or the [LUMI web interface](https://docs.lumi-supercomputer.eu/runjobs/webui/).
- Software environments: It is usually not required to install software or library environments yourself, but many common libraries and software are pre-installed. We provide documentation and support to do the final touches yourself when a particular software provided requires adjustments. [See an overview of software in the LUMI docs](https://docs.lumi-supercomputer.eu/software/).
- Your own domain expertise: While the LUMI staff can assist you with moving your computational tasks to LUMI, we are not experts in your domain. We offer courses and self learning tutorials for many domains.

Rest assured, if you do not have all the skills, the LUMI AI Factory, with its [service offering](https://lumi-ai-factory.eu/service-catalogue/), is here to help!

## But isn’t supercomputing super expensive?

A supercomputer is a multi-million euro investment. The European Commission wants to make supercomputing resources available free of charge for startups, SMEs, research organisations and public administration by establishing AI Factories. Their aim is to speed up European business and science development by providing easy access to AI and HPC resources. LUMI AI Factory’s services are free of charge for startups, SMEs, and academic researchers – contact us, explain your AI challenge or idea, and let’s solve it together! To start, [fill in a contact form](https://lumi-ai-factory.eu/contact-us/), and a customer manager will contact you.

This is the first blogpost of a series. In the next blog post, we will discuss LUMI AI Expert Consulting Expert consultation where LUMI AI Factory’s specialists work directly with companies and researchers on substantial AI development challenges and join projects with a stronger time commitment.

Read also other blogs in the series:

[What is LUMI AI Factory’s Artificial Intelligence expert consultation?](https://lumi-ai-factory.eu/articles/ai-expert-consultation/)

[Trustworthy AI: Turning compliance into competitive advantage](https://lumi-ai-factory.eu/articles/trustworthy-ai-turning-compliance-into-competitive-advantage/)

[AI agents and agent infrastructure on LUMI](https://lumi-ai-factory.eu/articles/agent-infrastructure-on-lumi/)

[Local agents, remote brains: connecting OpenCode to LUMI](https://lumi-ai-factory.eu/articles/local-agents-remote-brains-connecting-opencode-to-lumi/)

---

## **Written by**

![Marlon Tobaben](https://lumi-ai-factory.eu/wp-content/uploads/2026/03/marlonto_LThumb.jpg)

Marlon Tobaben

Machine Learning Specialist at the LUMI AI Factory

![Kalle Huhtala](https://lumi-ai-factory.eu/wp-content/uploads/2026/03/kahuht_LThumb.jpg)

Kalle Huhtala

Senior Project Manager at the LUMI AI Factory
