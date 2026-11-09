---
title: "LUMI AI Guide | LUMI AI Factory"
url: https://lumi-ai-factory.eu/trainings/lumi-ai-guide
lang: en
source: aif
scraped: 2026-11-02
---

1. Training

# LUMI AI Guide

[access the materials here](https://github.com/Lumi-supercomputer/LUMI-AI-Guide)

This guide is designed to assist users in migrating their machine learning applications from smaller-scale computing environments to the LUMI supercomputer.

We will walk you through a detailed example of training an image classification model using [PyTorch’s Vision Transformer (VIT)](https://pytorch.org/vision/main/models/vision_transformer.html) on the [ImageNet dataset](https://www.image-net.org/).

All Python and bash scripts referenced in this guide are accessible in this [GitHub repository](https://github.com/Lumi-supercomputer/LUMI-AI-example/tree/main). We start with a basic python script, [visiontransformer.py](https://github.com/Lumi-supercomputer/LUMI-AI-Guide/blob/main/01-quickstart/visiontransformer.py), that could run on your local machine and modify it over the next chapters to run it efficiently on LUMI. This guide also covers the transition from training to production with a chapter on LLM Inference (Chapter 10), focusing on memory-efficient hosting with vLLM.

Even though this guide uses PyTorch, most of the covered topics are independent of the used machine learning framework. We therefore believe this guide is helpful for all new ML users on LUMI while also providing a concrete example that runs on LUMI.

## Requirements

Before proceeding, please ensure you meet the following prerequisites:

- A basic understanding of machine learning concepts and Python programming. This guide will focus primarily on aspects specific to training models on LUMI.
- An active user account on LUMI and familiarity with its basic operations.
- If you wish to run the included examples, you need to be part of a project with GPU hours on LUMI.
