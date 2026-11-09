---
title: "OpenWebSearch.eu and LUMI AI Factory: powering Dataset-as-a-Service with a European Open Web Index | LUMI AI Factory"
url: https://lumi-ai-factory.eu/articles/openwebsearch
lang: en
source: aif
scraped: 2026-11-02
---

1. News

# OpenWebSearch.eu and LUMI AI Factory: powering Dataset-as-a-Service with a European Open Web Index

3 mins read

16.6.2026

 ![](https://lumi-ai-factory.eu/wp-content/uploads/2026/06/AdobeStock_1997300701-960x540.jpeg)

Image: Adobe Stock

OpenWebSearch.eu ([OWS](https://openwebsearch.eu/)) started as a collaborative European research project under the Horizon Europe umbrella. The idea: Building a federated, open and transparent web index and web data infrastructure to enable sovereign European web-search and AI services. The project was realized by a consortium of 14 organizations (mainly universities, HPC data centers and non-for-profit associations), who were spread across seven European countries. The University of Passau took on the project lead. While the project has officially ended in February 2026, the results carry on. By running continuous large-scale crawls and maintaining a searchable Open Web Index ([OWI](https://openwebindex.eu/)) that spans many languages and domains, OWS provides access to the raw web material needed to build, evaluate and improve information retrieval and large-scale AI systems.

## OWS datasets within LUMI AI Factory’s Dataset-as-a-Service offering

LUMI AI Factory’s Dataset-as-a-Service (LUMI AIF DaaS) packages curated, high-value datasets together with HPC resources, tooling and operational support. This allows researchers and innovators to use web-scale data without building and operating crawling/indexing pipelines first. As part of that offering, the OWS datasets are made available inside the LUMI environment — ingested, formatted and connected to the compute stack so users can immediately start running experiments.

## What the OWS datasets enable?

- Training and fine‑tuning large language and retrieval models on European-centric, multilingual web data.
- Building domain-specific Retrieval-Augmented Generation Pipelines based on pre-computed embeddings.
- Enriching your Agentic AI Search System with documents, scholarly articles, products and other structured metadata extracted from open web data.

## Who can benefit from this?

- Academic researchers studying IR (Information Retrieval), NLP (Natural Language Processing), or knowledge extraction.
- HPC users and data scientists who require large, multi-terabyte datasets co-located with compute for efficient training.
- Consortiums and projects that require transparent, auditable data sources for regulatory or reproducibility reasons.

However, under the current set-up, the datasets are only available under a research license. Commercial exploitation is not currently allowed.

## How to use the datasets (practical steps)

1. Find the Open Web Search Index as part of the [LUMI AIF DaaS catalog](https://lumi-aif.fairdata.fi/dataset/a30776de-af6d-4b46-9b15-8ba5f80b1a17) and follow the instructions to access dataset
2. Choose an ingestion profile: Pre-processed JSONL extracts for faster prototyping, or pre-built metadata+URL indexes for retrieval experiments.
3. Mount or copy the dataset into your LUMI project workspace (co-located with compute to minimize I/O overhead).
4. Start using the dataset
   - For RAG: run the provided preprocessing pipeline to extract text, clean HTML, deduplicate, and generate document chunks; then create embeddings (e.g. using open or private models) and build a vector store (FAISS/HNSW/ScaNN). See also [IT4I’s Github](https://opencode.it4i.eu/openwebsearcheu-public).
   - For training: convert to model-ready formats (sharded JSONL/TFRecord/ WebDataset), apply tokenization and filtering policies, and launch distributed training on LUMI GPUs.
   - For evaluation and IR research: use the included metadata and crawl timestamps to construct temporal evaluation sets and perform relevance studies across languages.
5. Follow the provided compliance and license guidelines: OWS metadata and WARC records include provenance so you can trace sources and apply content-level policies

## Paving the way for European innovation

Combining OpenWebSearch.eu’s open, multilingual web index with LUMI AI Factory’s Dataset-as-a-Service removes the heavy lifting of crawl and index management and places a production-ready web-scale dataset directly into a powerful HPC environment. That pairing makes it practical for European researchers and innovators to build, test and deploy responsible, reproducible AI systems grounded in a trustworthy, transparent web dataset.

---

Authors are from the OWS project
