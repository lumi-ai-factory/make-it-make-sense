---
title: "Bris: A high-resolution data-driven weather forecasting model | LUMI AI Factory"
url: https://lumi-ai-factory.eu/stories/bris
lang: en
source: aif
scraped: 2026-11-02
---

1. Success stories

# Bris: A high-resolution data-driven weather forecasting model

3 mins read

19.9.2025

![](https://lumi-ai-factory.eu/wp-content/uploads/2025/09/ln_weather-960x540.jpg)

Image: Adobe Stock

The LUMI supercomputer, one of Europe’s top-tier supercomputers, provides the compute backbone for the LUMI AI Factory, enabling cutting-edge RDI at the intersection of AI and HPC. This success story demonstrates how the LUMI supercomputer has already been used to develop AI solutions, and serves as inspiration for further innovation with LUMI AI Factory.

Global weather forecasting models based on Artificial Intelligence (AI), have demonstrated skill surpassing the best conventional weather forecasting models, requiring only a fraction of the computational cost. In this project, [the Norwegian Meteorological Institute](https://www.met.no/en)[(MET)](https://www.met.no/en) collaborates with [the European Centre for Medium-Range Weather Forecasts (ECMWF)](https://www.ecmwf.int/) and meteorological institutes across Europe to develop a purely data-driven, high-resolution regional weather forecasting model. This article was originally published on [the Sigma2 website](https://www.sigma2.no/research/bris-high-resolution-data-driven-weather-forecasting-model).

The new model is named Bris, after the Norwegian word for “light wind”. The goal of the project is for Bris to become MET Norway’s best weather forecasting model, delivering more accurate forecasts to a 10 million unique weekly users on [Yr](https://www.yr.no/), a popular Norwegian weather forecasting service provided by the Norwegian Meteorological Institute and the Norwegian Broadcasting Corporation (NRK).

## Innovative architecture and advanced training

Bris is based on graph neural networks (GNNs) and employs an innovative stretched-grid architecture. This architecture allocates higher spatial resolution to regions of interest while maintaining lower resolution elsewhere on the globe. This design allows weather patterns to seamlessly move into the region and enables accurate forecasting over the complex topography of Scandinavia. The model architecture is flexible, allowing the integration of multiple observation sources, such as crowd-sourced data, to enhance forecast accuracy.

The current version of Bris features 246 million trainable parameters, and essential to its development have been the supercomputing resources provided by Sigma2. The model has been trained on 128 GPUs in parallel on the LUMI supercomputer.

– Crucial to the rapid development of Bris has been access to the large number of high-performance GPUs on the LUMI supercomputer, said **Ivar Ambjørn Seierstad**, Project Leader and Researcher at MET Norway.

## 10-day global forecast in just 2-3 minutes

One year into the project, Bris is already producing temperature forecasts for Norway that outperform the state-of-the-art forecasts on Yr. The model is currently semi-operational, providing updated 10-day forecasts four times per day. Unlike conventional physics-based models, once Bris is trained, it can produce a 10-day global forecast in just 2-3 minutes on a single high-end GPU.

![](https://lumi-ai-factory.eu/wp-content/uploads/2025/09/Bris-model-graph_small.jpg)

Image: The figure illustrates the skill of temperature forecasts in Norway, averaged over a year. The red line represents the current forecast model used on Yr, while the blue line represents the new data-driven forecast model Bris.

Author: Sigma2

Image on top: Adobe Stock
