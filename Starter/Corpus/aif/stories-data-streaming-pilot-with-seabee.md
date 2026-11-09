---
title: "LUMI AI Factory’s data streaming pilot with SeaBee is revolutionising sea bird monitoring | LUMI AI Factory"
url: https://lumi-ai-factory.eu/stories/data-streaming-pilot-with-seabee
lang: en
source: aif
scraped: 2026-11-02
---

1. Success stories

# LUMI AI Factory’s data streaming pilot with SeaBee is revolutionising sea bird monitoring

5 mins read

11.3.2026

![Seabird detections on Langholmen (Vestfold) during June 2024. Image: Sindre Molværsmyr.](https://lumi-ai-factory.eu/wp-content/uploads/2026/03/ln_seabee-960x540.jpg)

LUMI AI Factory’s first data streaming pilots are ongoing. These data streaming case studies are essential for advancing the data streaming capabilities of the LUMI AI Factory. They demonstrate practical implementation scenarios and offer real-world validation for concepts, tools, and architectures. This approach ensures that the resulting capabilities in the LUMI AI Factory are both technically robust and practically aligned with user needs, tested in realistic settings with genuine workflows and datasets. SeaBee, the Norwegian national infrastructure for drone-based coastal research, is among the first data streaming pilots for the LUMI AI Factory.

## SeaBee: streaming data for adaptive coastal monitoring

Norway’s coastline is rugged, shaped by fjords and fjell. SeaBee is developing methods for habitat mapping, monitoring animal communities and assessing human impacts. The LUMI AIF data streaming pilot is focusing on seabird monitoring.

The SeaBee team conducts large-scale seabird surveys across Norway’s fragmented coastline. The drone-based method has revolutionised seabird colony counting in Norway. The bird counts are less intrusive with higher accuracy and repeatability. Mapping and documentation of different species and activities is quicker, based on an AI-pipeline.

Each drone mission captures thousands of overlapping images: both regular colour photos and wavelengths invisible to the human eye (multispectral images), generating tens of gigabytes of data per drone flight. These datasets are processed into orthophotos, which are raw drone photos that have been stitched together into larger images. These digitally corrected photos are then classified using machine learning models before ecologists can validate coverage and adjust drone flight plans.

![](https://lumi-ai-factory.eu/wp-content/uploads/2026/03/ln_seabee4-800x420.jpg)

*Image: Main components of the [SeaBee data exploration application](https://geonode.seabee.sigma2.no/)*

## Maximising valuable field time

The SeaBee data platform aims to provide researchers with an end-to-end solution for processing, analysing and sharing data collected by drones. The data platform is hosted on Norway’s National Infrastructure for Research Data (NIRD) at [Sigma2](https://www.sigma2.no/). Current workflows rely on batch uploads to NIRD, where automated AI-based pipelines handle geometric image correction (orthorectification) and machine learning classification. While effective, this approach struggles during peak survey periods, such as the annual seabird census, when tens of terabytes arrive within days. Processing queues grow, delaying results for ecologists and limiting adaptive fieldwork.

NIRD provides robust and powerful storage and high-capacity compute resources, but the GPU capacity is limited compared to LUMI supercomputer’s top-tier GPU capacity. Moving SeaBee’s data streams to LUMI is an effort where things such as high-speed and secure data transfer, metadata preservation, event-driven orchestration, containerised workflows, elastic resource allocation, and data consistency and recovery need to be taken into account.

– Our existing pipelines on NIRD work well, but as drones extend their range and sensor resolution improves, data volumes are becoming challenging. We see backlogs on the SeaBee platform during heavy workloads, so it’s exciting to have the opportunity to scale our AI processing onto the LUMI supercomputer. We’re just getting started, but I can see a lot of potential in the discussions we’ve had so far with teams from CSC and Sigma2, explains Senior Engineer **James Sample** from the SeaBee development team.

## From days to hours

In practice, the workflow with LUMI AI Factory will go as follows: The image correction (orthorectification) pipeline runs on the NIRD platform as usual. As soon as an orthophoto is ready, it will be streamed to LUMI AIF in chunks. LUMI supercomputer’s GPU nodes will immediately start parallel machine learning inference, classifying habitats and detecting seabirds at scale. Results will then be streamed back to NIRD, published via [GeoNode](https://geonode.seabee.sigma2.no/) (an open-source content management system for web geographic information system), and made available to ecologists in the field.

This hybrid, elastic model will reduce turnaround from days to hours, enabling adaptive survey strategies and maximising the value of limited field time, ultimately delivering precise data for mapping and monitoring purposes, and supporting decision-making in the area.

The future vision is to use the LUMI supercomputer especially during peak survey periods, e.g., during the seabird census, when field time for the ecologists is limited and valuable.

– Getting data online quickly makes it possible to check results and fix issues while staff are still in the field, which is a big benefit. For future applications, we are considering automated drone flights (so-called “drone-in-a-box”), which are capable of collecting time series imagery at much higher frequency than we can at present. Processing data from these missions would be challenging with the current pipeline, but should be possible on LUMI. Another goal for the future is to implement “direct georeferencing”. Right now, we have to stitch raw images together before we can process them, but this is slow and often fails over open water where image matching is hard. With the latest drone sensors, we could perform AI classification directly on the raw imagery. This approach has huge potential, but it requires more GPUs than we have available on NIRD. With LUMI, it should be possible!, Sample concludes.

## Have a look at videos:

Introduction to SeaBee:

This content requires cookies.

Change cookie settings

Description of the data processing workflows by James Sample:

This content requires cookies.

Change cookie settings

---

Image on top: *Seabird detections on Langholmen (Vestfold) during June 2024. Image: Sindre Molværsmyr.*

Written by **Anni Jakobsson**, CSC
