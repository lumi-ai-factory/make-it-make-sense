---
title: "Towards robots that can make you a drink | LUMI AI Factory"
url: https://lumi-ai-factory.eu/stories/grove
lang: en
source: aif
scraped: 2026-11-02
---

1. Success stories

# Towards robots that can make you a drink

6 mins read

26.2.2026

![](https://lumi-ai-factory.eu/wp-content/uploads/2026/02/AdobeStock_421646932-960x540.jpeg)

Most of us imagine a future where a robot can cook dinner, put on a wash, and maybe even pour us a drink. For that vision to become reality, robots must be trained to understand the movements, actions, tools and step-by-step procedures that are part of everyday tasks for humans. Artificial intelligence can contribute to research in this direction by processing raw visual data at scale.

In this use case, originally published on the [EuroHPC JU’s website](https://www.eurohpc-ju.europa.eu/eurohpc-success-story-towards-robots-can-make-you-drink_en), researchers automatically annotated more than one million YouTube videos, opening the possibility of training robots directly from demonstrations. **Dr. Evangelos Kazakos**, **Dr. Cordelia Schmid** and **Dr. Josef Sivic** developed a grounded video captioning method ([GROVE](https://ekazakos.github.io/grounded_video_caption_generation/)) that links language to specific objects and regions in each video. This framework can be used in a variety of contexts and provides a powerful foundation for pre-training models on large-scale web videos.

## **Learn by watching 1 million YouTube videos**

In this project, the research team proposed an approach that can perform *Grounded Video Caption Generation*.  This began with a novel automatic annotation method which was used to label 1 million YouTube videos.  The videos showed people completing everyday tasks such as cooking a meal, sweeping the floor or doing arts and crafts.

In each task, the machine identifies key elements in the activities in the video.  The research team also created a set of human-labelled videos. This was used for accurate evaluation of how the model was performing. The proposed datasets from this research are publicly available [online](https://ekazakos.github.io/grounded_video_caption_generation/).

Next, the LLM identifies the noun phrases in the caption, which are essentially the key elements in the video. In the final step, a second VLM predicts bounding boxes over the video frames, linking each noun phrase in the caption to the corresponding object in the scene. This makes the caption clearly tied to where objects are and how they move through space.

Through each step, the model gains a better understanding of the video, obtaining the ability to not only recognise what is in the video, but also to point out these entities and make more accurate predictions and explanations of the actions taking place – a great example of machine learning!

The [developed machine learning method was accepted to ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/html/Kazakos_Large-scale_Pre-training_for_Grounded_Video_Caption_Generation_ICCV_2025_paper.html) – the IEEE/CVF International Conference on Computer Vision. ICCV is one of the most influential conferences in computer vision (along with CVPR and ECCV) and is consistently ranked among the top venues in computer science and artificial intelligence.

## **Hardware and Hard Work**

EuroHPC JU supercomputing resources were used at two main stages of the project:

(i) large-scale automatic annotation to build the HowToGround1M dataset, and

(ii) model development, training and evaluation.

For the task of automatic annotation, access to the LUMI supercomputer was crucial, as the project pipeline required per-frame captioning and object detection over millions of video frames.  By parallelising the workload and splitting videos across many compute nodes and GPUs, the researchers were able to run visual foundation models and LLMs in parallel and complete pseudo-labelling in a reasonable timeframe.

The vLLM library played a key role here: it enabled high-throughput and memory-efficient LLM inference with techniques like continuous batching, [PagedAttention](https://huggingface.co/docs/text-generation-inference/en/conceptual/paged_attention), and model parallelism, which allowed the research team to feed the LLM with multiple inputs from multiple video frames and scale up to billions of tokens across millions of videos on the supercomputer.

When the team began working on model development, they used EuroHPC JU resources to train and evaluate their GROVE architectures on the large-scale video–language data created in stage one. The entire stack was [implemented](https://huggingface.co/docs/transformers/main/index) in Python, using [PyTorch](https://pytorch.org/) as the main deep learning framework and the Hugging Face transformers library for LLM/VLM components.

Access to LUMI enabled the team to run large-scale pseudo-labelling with vLLM and to perform memory and compute-intensive multi-node training with [DeepSpeed](https://github.com/deepspeedai/DeepSpeed) and PyTorch, which would not have been feasible on conventional hardware.

Overall, this extensive research project made some important observations:

1. The volume of the automatically annotated data was crucial for obtaining good performance.
2. The human-labelled data provided significant boosts in the model’s ability to ground objects in the video.
3. The proposed model outperformed all previous strong approaches on five different video grounding benchmarks.

## **Real Potential**

Research outputs from this project have impact beyond the core grounded captioning task. The data and models produced in the project are already being applied to new research areas including 3D object pose estimation and a project transferring human trajectories to robotic trajectories; where large-scale grounded visual data is currently a key bottleneck. Another project is focused on building a robotic manipulation model that leverages visual grounding to improve object understanding, localisation and manipulation.

Finally, the team is now working towards extending their model to cover temporal grounding and language-guided understanding of object state changes. This direction is particularly relevant for long-horizon robotic tasks where understanding how objects evolve over time is essential. As an example, imagine a robot helping to prepare dinner by chopping a carrot. After cutting, the “carrot” is no longer a single object but a pile of slices. The robot needs to understand that all these pieces are the same carrot in a new state, and to be able to find, pick up, and move them on to the next part of the task—even though their shape and appearance have changed dramatically.

## **The potential for innovation doesn’t stop there!**

The ideas and tools developed in this project can benefit applications such as autonomous driving: a driver could verbally refer to an event or object on the road, and the system could ground this reference in the scene and, in turn, point to specific locations or objects to explain its decisions and planned actions. In this way, this research contributes not only new datasets and models, but also building blocks for more transparent, interactive and capable vision–language systems in robotics and intelligent vehicles.

In the longer term, such models and datasets can underpin assistive robots operating in homes or hospitals, for example supporting elderly or disabled individuals with everyday activities such as preparing food, tidying up, or handling medical equipment, where robots must interpret verbal instructions, ground them in complex, dynamic scenes, and understand how objects change over time. The grounding and object state-change understanding developed in this project can also support robots sorting and handling packages in logistics centres or picking fruits in agriculture. In all these settings, it is crucial that robots can link spoken instructions to the right places and objects in the real world and show what they plan to do by clearly pointing to specific items or areas. This grounding of both instructions and intentions can contribute to safer, more reliable and more helpful human–robot interaction in everyday and clinical environments.

The team intends to apply to the [EuroHPC JU AI for Science and Collaborative EU Projects](https://www.eurohpc-ju.europa.eu/eurohpc-ju-call-proposals-ai-science-and-collaborative-eu-projects_en) access to extend their current work towards 4D Understanding with Vision & Language. This new project will develop large-scale multimodal models that learn rich, explicit representations of 3D space, objects, and their temporal interactions from video, language, and 3D signals, moving beyond describing “what happens” to reasoning about where things are, how far apart they are, how they move, and how they can be manipulated. Using EuroHPC resources, they aim to train and evaluate foundation-style vision-language models that integrate 2D videos, textual descriptions, and 3D data (including simulated 3D environments, to overcome the cost of large-scale 3D annotation), and that can generalise across domains such as robotic manipulation, scene understanding, and remote sensing, ultimately providing a reusable core for spatial reasoning in diverse scientific workflows.

---

Author: EuroHPC JU

Image: Adobe Stock
