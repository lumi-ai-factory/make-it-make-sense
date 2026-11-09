---
title: "Dataset-as-a-Service from the LUMI AI Factory – data close to compute | LUMI AI Factory"
url: https://lumi-ai-factory.eu/articles/dataset-as-a-service
lang: en
source: aif
scraped: 2026-11-02
---

1. News

# Dataset-as-a-Service from the LUMI AI Factory – data close to compute

1 min read

1.4.2026

 ![general image for datasets](https://lumi-ai-factory.eu/wp-content/uploads/2026/04/AdobeStock_1891470878_daas_website-960x540.jpg)

*Developing artificial intelligence (AI) applications requires expertise, computing power, and data – preferably a lot of it, and fast. LUMI AI Factory’s entirely new [Dataset-as-a-Service](https://lumi-ai-factory.eu/dataset-as-a-service/) (DaaS) solution brings data and compute closer together in a way that directly meets the growing needs of AI and data-intensive research.*

Traditionally, large datasets have been moved from one environment to another based on individual use cases – from archives to compute services and back again – a process that consumes both time and resources. The LUMI AI Factory’s DaaS service approaches the issue from the opposite direction: it makes data visible at the very location where the computing power already resides. This shortens the distance from data to results and makes experimentation and research more seamless.

The DaaS user interface is a data catalogue in which data producers can publish their datasets in a controlled manner, and data users can discover them without manual searching or separate services. The service brings together metadata, access rights and data locations into a single whole, making datasets not only discoverable but immediately usable on the LUMI supercomputer. This is especially important in AI development, where training models require large volumes of data, and where the physical proximity of data to compute significantly affects performance and the reproducibility of workflows.

LUMI AI Factory’s DaaS creates value for two user groups at once: data users and data providers. For data users, DaaS streamlines the search for AI-ready datasets and eliminates the bottleneck of copying a large dataset elsewhere before analysis. For data producers, the service offers a clear publication path that makes datasets discoverable in a controlled, standardised way and available for broader use. A published dataset does not disappear into an archive – it gains visibility and utilisation.

## What is new about the LUMI AI Factory’s DaaS?

The LUMI AI Factory’s DaaS is not yet another data repository, and its primary purpose is not the storage or publication of datasets with citation information. A data repository and DaaS are complementary service models: the former supports long-term preservation and citability, while the latter focuses on use.

A traditional data repository is a place where datasets are archived and from which they can be downloaded elsewhere for use. DaaS, by contrast, orchestrates access to the data, guides users through permissions, and combines metadata, authorisation and data location into a single process. Datasets included in DaaS may physically reside in different systems, but DaaS presents them as a unified selection and enables their use without requiring users to move data between systems.

Because DaaS is not an archive, it is also not intended for long-term preservation. Data is stored in DaaS only as long as it is in demand for AI development. When demand decreases, data can be removed from DaaS – but a preserved version remains available in an appropriate data repository if needed.

## Architecture built on existing components

DaaS is a service, not a standalone IT system. Its value comes from the combination of metadata, access rights and technical integration. The service is built modularly on top of existing, widely used components. CSC’s [Fairdata-Metax](https://www.fairdata.fi/en/metax/) provides the metadata warehouse, and [Fairdata-Etsin](https://www.fairdata.fi/en/etsin/) serves as the user interface and search tool. [LUMI-O](https://docs.lumi-supercomputer.eu/storage/lumio/) brings object storage close to compute, CSC’s [Resource Entitlement Management System (REMS)](https://github.com/cscfi/rems) manages access rights and related approval processes, and IT4I’s [LEXIS](https://www.lexis.tech/) enables data transfer and orchestration across different systems. This approach is cost‑effective and low‑risk compared to building an entirely new system: each component is already proven in practice, and combining them enables a flexible, scalable and sustainable service.

Modularity also means the service can be expanded piece by piece to meet   user needs. The architecture is not rigid, and new capabilities do not need to be built from scratch – speeding up development and keeping costs under control.

## Service available, functionalities advancing

The LUMI AI Factory’s DaaS is not yet a fully productised service, but its first pre‑productised version is already available to both data providers and data users. In this version, some integrations between service components are still under development , and certain parts of the service operate manually through support from LUMI AI Factory experts. However, the automation of functionalities is continuously progressing.

The set of available datasets is also evolving. Currently, the data catalogue contains ten extensive dataset collections, each composed of multiple datasets. One of these is the Open Web Search Index, a continuously updated resource comprising more than 1,000 datasets with a combined volume exceeding one petabyte. The Open Web Index consists of structured, indexed web document data collected using open methods and intended for reuse without the need to crawl the entire web independently. It provides a foundational infrastructure upon which search services, analytics, research and AI models can be built. It enables users to “slice and dice” web data according to their own needs, making it particularly valuable for search engine development and training large language models.

As the LUMI AI Factory’s DaaS matures toward a fully productised service, it will increasingly become a vital tool for both data providers and data users. The goal is to create a service that improves data discoverability, reduces manual work, and above all accelerates AI development. DaaS is not merely a new technical platform – it is part of a broader shift toward data that is immediately usable exactly where its value is created.

Explore the LUMI AI Factory’s Dataset-as-a-Service in more detail and contact LUMI AI Factory experts here: <https://lumi-ai-factory.eu/dataset-as-a-service/>
