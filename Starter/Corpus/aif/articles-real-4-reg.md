---
title: "Machine learning on sensitive data | LUMI AI Factory"
url: https://lumi-ai-factory.eu/articles/real-4-reg
lang: en
source: aif
scraped: 2026-11-02
---

1. News

# Machine learning on sensitive data

7 mins read

24.10.2025

 ![](https://lumi-ai-factory.eu/wp-content/uploads/2025/10/data-intesive-960x540.jpg)

Image copyright: Adobe Stock

As the need for data-intensive computing is growing in different fields such as medical research, for example, the interest in developing approaches that enable the direct processing of sensitive data on high-performance computing (HPC) clusters also increases. Enabling the processing of sensitive data using HPC is one of the goals of LUMI AI Factory. This blog, which was originally published on the [Real4Reg website](https://www.real4reg.eu/news-events/news/machine-learning-on-sensitive-data/), examines the different challenges and opportunities related to machine learning on sensitive data.

## Real-world data with machine learning

Machine learning (ML) has become widely used in all sectors of industry and academia. Succinctly, ML consists of a set of tools for solving computationally ill-posed problems in Statistics and Probability, particularly those arising in statistical inference. With the term “learning” it is meant that statistical associations between a set of measurements and their associated labels (that is, an assigned category to each measurement) are estimated from a given sample population. Should no labels exist, the statistical associations of measurements are estimated by identifying how many groups (or clusters) there are, using clustering or self-organization-based methodologies based on a similarity criterion (meaning, how similar measurements are in terms of their numerical “distance”). It is the responsibility of an investigator to define the suspected cardinality (number) of groups in a given dataset, and how the similarity between measurements is defined.

Unsupervised learning(UL) is an approach that can be used on measurements that either contain labels or not, and is dependent on the question to be answered. Should the measurements contain labels, or there is some inference about the possible number of categories, UL is used to estimate the cardinality and the “nature” of the measurement distributions. In the context of real-world data (RWD), that is, patient-level observational data collected from clinical care, ML may provide a flexible set of tools for conducting statistical analyses of data where the measurements may be a mixture of numerical and/or non-numerical types.

## Environments for sensitive data processing

Due to the nature of RWD, the EU General Data Protection Regulation (GDPR) poses limitations on how the data can be processed. This blog post concerns the processing of RWD using [Sensitive Data (SD) Desktop](https://research.csc.fi/service/sd-desktop/), hosted by CSC. Each EU member state has their own regulatory requirements for processing sensitive data under GDPR, thus this blog is restricted to Finland’s case.

SD Desktop is a registered environment for secondary use of health and social data including health register data. In practice, using SD Desktop is possible through a purpose-developed virtual desktop accessed via one’s web browser. SD Desktop provides a general-use environment for sensitive data processing that is available to researchers from all Finnish universities and research organisations.

All data intended for processing is accessed via a specific NetApp volume, which can then be accessed within SD Desktop. The data processing is carried out within a dedicated infrastructure located in Finland. SD Desktop provides virtual Linux machines, which are disconnected from the internet (for data security reasons), with the ability to (dis)connect to the machines via the access portal provided by SD Desktop. When creating a virtual machine environment, one can specify the required software tools & libraries that are needed for conducting data processing or data analysis.

SD Desktop relies on virtual machines, which poses limitations on the scale of data processing and/or statistical model development. Additional limits are set by the standard data input/output (I/O) libraries (for example, working with DataFrames with Python or R), which will hinder the speed and scale of data processing. In principle if the set of software library dependencies are met, executing a program in various secure environments should be a non-problem when considering transferring software solutions between sensitive data environments.

## Future developments

Reflecting the growing need for data-intensive computing in the field of medical research, there is increasing interest in developing approaches to enable the direct processing of sensitive (e.g. personal) data on HPC clusters. A significant challenge to devising such approaches is that the technical measures necessary, such as changes to cluster partitioning, are often impossible to implement in retrospect.

For this reason, careful consideration of the expected requirements for sensitive data processing is required already during the HPC infrastructure planning phase. In practice, the work involves developing software components to ease the management of confidential or otherwise sensitive data on the upcoming LUMI-AI supercomputing platform with a focus on selected domains and data types, including health data.

As HPC using sensitive data becomes increasingly possible, this is expected to directly benefit the application of advanced machine learning methods in the field of predictive medicine, including the large-scale analysis of RWD. Further to sensitive data processing on HPC platforms, there is considerable interest in the application of causal machine learning methods and generative Artificial Intelligence (AI) for the analysis of health data. The hope is the aforementioned approaches facilitate the proposal of effective actions in, for example, clinical decision-making.

However, the full implications of the newly passed AI Act on the healthcare sector are currently unknown, and will be crucial to consider for any real-life applications of these methods beyond basic research. The AI Act requires that AI models should be reliable and accurate, which has ramifications for model development and application in the healthcare sector, as well as the types of data used for this purpose. Since RWD are observational in nature and not empirical, the new and emerging topic of investigating the use of ML methods using RWD alone should currently be viewed as supplementary statistical methodology to basic empirical and controlled experimental research.

For example, causal ML methods face restrictions in medical decision-making, as these models provide only statistical associations (not cause-and-effect) based on ad hoc assumptions, which are typically unverifiable without controlled and randomized experiments. Similarly, data produced by generative methods could be used for creating datasets for theoretical research and educational purposes on ML methods, but they cannot be used for medical decision-making due to them being synthetic (that is, non-empirical) in nature.

Regardless of the methods used, a key goal for future research will be to ensure access to standardized and unified data sets, including the standardization of data formats across different nations and data-hosting organizations. One of the objectives of the Real4Reg project is to develop approaches to address discrepancies in terms of data quality and availability when comparing results obtained using information from different local (national) databases.

## Example use case within Real4Reg

One of the statistical analysis use cases in Real4Reg is to estimate the associations between the purchases of antibiotics and different medical diagnoses. Specifically, the interest is in finding the associations between the medical diagnoses per antibiotic item, and then evaluating the differences between groupings per antibiotic item. The evaluation is posed as an UL problem where Latent Dirichlet Allocation (LDA) is used to evaluate the group associations between the medical diagnosis. LDA is a method developed for evaluating the possible number of topics from a given dataset of written text. The method itself does not label the topics from its grouping contents, so the topic(s) is inferred by the human user.

A major benefit of the method is that it provides relative frequencies of the contents of each grouping, so that the (dis)similarities may be evaluated or visualized. It also helps with interpreting how the groups are related to each other (with respect to the relative frequencies of their contents). The major challenge is to find a plausible number of groupings to perform the statistical modelling. There are methods, for example, for evaluating the internal and external validity of groupings, but these methods are for evaluating the mathematical importance of groupings. When it comes to observational data in the form of RWD, the mathematical importance does not imply scientific, practical, nor clinical importance. Therefore, the method and its results should be iterated and validated in cooperation with healthcare professionals against relevant empirical observations.

### References:

1. Vapnik, Vladimir. “Statistical learning theory” *New York* 1.624 (1998): 2.
2. Young, Tzay Y., Calvert, Thomas W. “Classification, estimation, and pattern recognition” Elsevier, 1974.
3. Blei, David M., Andrew Y. Ng, and Michael I. Jordan. “Latent dirichlet allocation.” *Journal of machine Learning research* 3.Jan (2003): 993-1022.
4. Boring, Edwin G. “Mathematical vs. scientific significance.” *Psychological Bulletin* 16.10 (1919): 335.
5. McCloskey, Donald N. “The loss function has been mislaid: The rhetoric of significance tests.” *The American Economic Review*75.2 (1985): 201-205.
6. Mackie, John Leslie. *The cement of the universe: A study of causation*. Clarendon Press, 1980.

---

Author: Real4Reg
