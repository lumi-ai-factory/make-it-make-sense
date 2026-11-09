---
title: "SICS AI: HPC access to LUMI supercomputer for AI and robotics | LUMI AI Factory"
url: https://lumi-ai-factory.eu/stories/sics-ai
lang: en
source: aif
scraped: 2026-11-02
---

1. Success stories

# SICS AI: HPC access to LUMI supercomputer for AI and robotics

6 mins read

15.12.2025

![](https://lumi-ai-factory.eu/wp-content/uploads/2025/12/2.jpg)

[SICS AI](https://sics.ai/)leverages the LUMI supercomputer to accelerate development of its proprietary AI model for advanced robot control. By accessing HPC resources through the AI Factory Playground, the team shortened development cycles by a factor of 100 and optimized workflows for large-scale GPU training. This hands-on experience prepares SICS AI for future robotics research and large-scale HPC projects. This article was originally published on the [ENCCS website](https://enccs.se/success-story/2025/09/sics-hpc-access-lumi-supercomputer-ai-robotics/).

## Organisations involved

Superintelligence Computing Systems (SICS AI AB) is a deep-tech B2B AI software company with the mission to build a universal AI brain for industrial robots. The goal is to create a robot-agnostic, environment-independent AI capable of controlling any type of robot, regardless of geometry, mechanics, or function. SICS pioneers solutions that enable robots to learn and adapt autonomously, transforming industries such as warehousing and industrial assembly. By making robots more flexible and autonomous, SICS strengthens the European industry’s competitive edge in automation.

## Technical/scientific challenge

In a world increasingly dependent on automation to meet the growing demands of industry and commerce, current robotics and AI technologies face a major limitation: handling the complexity and variability of real-world environments.

### Limits of today’s automation

- Automation performs well in structured settings such as production lines with repetitive tasks.
- But in dynamic and unpredictable environments — like manufacturing and warehouse logistics — it often fails.
- This capability gap restrains productivity and increases costs for businesses under constant pressure to optimize operations.

### Why current AI falls short

The root problem lies in the rigidity of traditional process automation and the limitations of today’s AI technologies:

- Current AI-driven automation systems lack robustness, flexibility, and adaptability.
- They are error-prone, unreliable in performance, and costly to maintain.

### Example: Robots in assembly

- Robots perform intricate tasks with high precision — but only when conditions are ideal.
- Any deviation (different shape, size, or position of a component) requires recalibration or reprogramming.
- This slows production and increases waste from defective products.

### Hybrid solutions and scaling issues

- Current AI-guided pick-and-place robots can manage some variation, but rely on heavy training, batch learning, and significant human intervention.
- These hybrid systems are difficult to scale due to their reliance on legacy code.

### The limitations of LLMs

- Contemporary AI models such as Large Language Models (LLMs) generate results based on statistical probabilities without true real-world understanding.
- They are prone to “hallucinations” and are therefore unsuitable for mission-critical tasks.
- Improving their accuracy requires massive amounts of data and high computational power, which is costly and not scalable.

## Proposed solution

The main objective of this project was to gain hands-on experience with high-performance computing (HPC) systems and to explore how the LUMI supercomputer could accelerate the development of SICS AI’s proprietary AI model. These objectives were successfully achieved, and the development team together with the system infrastructure is now fully prepared to run larger projects on LUMI in the near future.

### Optimized use of the LUMI architecture

The SICS AI team learned how to use LUMI in an optimal way and received valuable input on how to plan for larger workloads in the next phase. By running many short jobs that occupied one node with multiple processors, they achieved a perfect match for their development setup and computational needs. These short, single-node jobs were easy to schedule and aligned well with the LUMI architecture. As a result, the LUMI computing power reduced their development cycle time by a factor of 100.

### Integration with their AI environment

SICS AI successfully integrated their Python-based proprietary AI system and internally developed code with the LUMI supercomputer. The team conducted tests on both single- and multi-GPU training using readymade containers built with their own runtime environment. These containers were created with Singularity, LUMI’s recommended cluster container system, and included PyTorch 2.6 and AMD ROCm 6.24.

## Scalability and performance results

Another important objective was to explore how SICS AI’s model behaves under larger workloads across multiple GPUs. The model is specifically designed for distributed execution on GPU clusters, and the tests verified that both single- and multi-GPU training worked seamlessly. Most of the work was done on single GPU training, where the team achieved near-linear scalability. Tests demonstrated scalability up to 56 GPUs, with a total of 5000 GPU hours consumed during the project.

![](https://lumi-ai-factory.eu/wp-content/uploads/2025/12/LeRobot-stacking-cubes-1024x677-1-800x529.jpg)

LeRobot stacking cubes, controlled by SICS AI’s proprietary model. Full E2E AI robot integration and control, all the way down to the joint angles (no legacy code).

## Business impact

### Accelerating AI training with HPC

Advanced AI training for robot control requires significant computing power. By leveraging HPC access through the LUMI supercomputer and the AI Factory Playground, SICS AI has gained a strategic advantage:

- Shorter development cycles
- Faster time-to-market
- Improved product quality

– This access puts our organization on par with leading innovation hubs such as Silicon Valley, giving us a stronger competitive edge in the global AI and robotics market.

### Building HPC expertise

Initial access to LUMI has provided the SICS AI development team with valuable experience in:

- Integrating workflows with a high-performance computing (HPC) environment
- Exploring how their proprietary AI model performs under large-scale workloads
- Learning to use LUMI in an optimal way to prepare for larger jobs

This foundation enables the company to design better processes and build proficiency in parameter optimization and large-scale AI training.

### Preparing for large-scale robotics R&D

Hands-on work with the LUMI infrastructure has allowed SICS AI to:

- Adapt their development workflows to supercomputing environments
- Seamlessly interface with the HPC system using optimized processes
- Conduct preliminary training and optimization of AI models at scale

This preparation is a crucial step toward leveraging the full potential of LUMI for future large-scale projects in robotics research and advanced AI development.

![](https://lumi-ai-factory.eu/wp-content/uploads/2025/12/Karim-Nouira-and-Martin-Pettersson-1024x653-1-800x510.jpg)

Karim Nouira and Martin Pettersson are working with LeRobot. AI training by human imitation learning. This type of training principle is used by company’s AI system today in commercial operation at Nowaste Logistics.

## Benefits

They have also optimized their processes and aligned their workflows to use LUMI in an optimal and future-proof way by scheduling many short jobs that take up one node with multiple processors during a short time, well adapted for the LUMI architecture and scheduling system.

The LUMI computing capabilities significantly shortened SICS AI’s development cycle time by at least a factor of 100 and increased the quality and precision of their AI model and results. This gives the company an edge in the global competition.

SICS AI has designed and tested its proprietary AI model for distributed execution on GPU clusters, both single- and multi-GPU training, and developed support in their general infrastructure and processes to execute code quickly and seamlessly on HPC systems. The team is now well prepared for efficient handling of large-scale jobs on LUMI in the next step.

![](https://lumi-ai-factory.eu/wp-content/uploads/2025/12/SICS-1024x683-1-800x534.jpg)

Screen showing camera-on-hand robot view and top camera view, and graph of robot joint angle values.

Author: Team ENCCS

Photos: SICS AI
