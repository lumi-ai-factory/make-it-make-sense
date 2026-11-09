---
title: "AI Software Environment | LUMI AI Factory"
url: https://lumi-ai-factory.eu/ai-software-environment
lang: en
source: aif
scraped: 2026-11-02
---

[AI software and solutions](https://lumi-ai-factory.eu/services/ai-software-and-solutions/)

# AI Software Environment

*The AI Software Environment by LUMI AI Factory provides a comprehensive and ready-to-use containerised software stack for artificial intelligence and machine learning workloads on the LUMI supercomputer. It helps researchers and developers avoid the complexity of building, deploying, and maintaining artificial intelligence and machine learning software environments in a high-performance computing setting.*

## Service features

The AI Software Environment enables running AI and machine learning workloads on LUMI using pre-built, tested, and documented container images. The environment is designed to provide a stable and high-performance starting point for AI development, experimentation, training, and inference.

Container images are packaged software environments that bundle applications, libraries, and their dependencies into a ready-to-use form. The container images provided by this service contain the core software components needed to run AI workloads effectively on LUMI. They build on each other in layers, from low-level GPU and networking components to PyTorch for AMD GPUs, MPI support for multi-node workloads, and a broader AI/ML software stack with commonly used tools and libraries. For many PyTorch-based workloads, the full image provides a practical starting point with software such as DeepSpeed, Flash Attention, vLLM, xFormers, Hugging Face tooling, Jupyter, MLflow, NumPy, pandas, and SciPy.

The environment is optimised for LUMI’s AMD GPU architecture and high-performance interconnect. By pre-integrating and testing core components such as ROCm, MPICH, libfabric, PyTorch, and selected AI/ML libraries, the service reduces the amount of low-level configuration, dependency management, and compatibility troubleshooting required from users.

The container images are also intended to serve as a foundation for customisation. Users can extend the provided images for their own workflows, add selected Python packages, or build new containers based on the public recipes. The AI Software Environment is also used as a building block for other LUMI AI Factory services and higher-level AI workflows.

All build artifacts are publicly available. This includes the container recipes, Containerfiles, build logs, software bills of materials, release documentation, and final container images. This transparent approach supports reproducibility, review, customisation, and reuse on suitable systems beyond LUMI.

Examples of what the AI Software Environment is intended for:

- Running PyTorch-based AI and machine learning workloads on LUMI
- Developing and testing deep learning applications with a ready-to-use software stack
- Large-scale model training and inference using LUMI’s GPU resources
- Building custom containers for project-specific AI/ML workflows
- Providing a software foundation for higher-level AI services and workflows

The container images are available directly on LUMI and through the LUMI AI Factory organisation on Docker Hub. Documentation and usage examples are available through the LUMI documentation and the LUMI AI Guide.

Support for the AI Software Environment is provided through the LUMI support channels. Issues related to the container images and their use on LUMI can be handled as part of the LUMI AI Factory support process. Consultation for adapting the environment for specific use cases can be part of the “Expert support for AI development” service.

**Access/Output Requirements**

- To use the AI Software Environment on LUMI, you need access to LUMI computing resources and a suitable LUMI project. Instructions for creating an account, applying for a LUMI project, and adding members to the project can be found [here](https://docs.lumi-supercomputer.eu/firststeps/accessLUMI/).
- The container images are available on LUMI in `/appl/local/laifs/containers/` as well as in [Docker Hub](https://hub.docker.com/u/lumiaifactory).
- The images and recipes are freely available for anyone from [Github](https://github.com/lumi-ai-factory/laifs-container-recipes/releases).
- Documentation for using the software environment on LUMI can be found [here](https://docs.lumi-supercomputer.eu/laif/software/ai-environment/).
- Use of the software environment is also covered by the [LUMI-AI Guide](https://github.com/Lumi-supercomputer/LUMI-AI-Guide).

## Target groups

The AI Software Environment is available for researchers and developers working with artificial intelligence and machine learning on LUMI. It can be used by private-sector, academic researchers, and public-sector organisations with suitable access to LUMI resources.

## Pricing

Use of the AI Software Environment is included for users with access to suitable LUMI computing resources; normal LUMI resource allocation conditions apply. The software images and their recipes are freely available for anyone.

## Request process

After a customer has been granted access to suitable LUMI computing resources, they can start using the AI Software Environment container images on LUMI. The public recipes and container images can also be accessed directly through the LUMI AI Factory GitHub repositories and Docker Hub organisation.

# Get in touch with us.

Have a question or want to learn more about our services? Fill out the form, and our experts will get back to you.
