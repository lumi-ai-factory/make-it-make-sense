---
title: "International Data Protection Day special: data protection and AI, what are the current and future challenges? | LUMI AI Factory"
url: https://lumi-ai-factory.eu/articles/international-data-protection-day
lang: en
source: aif
scraped: 2026-11-02
---

1. News

# International Data Protection Day special: data protection and AI, what are the current and future challenges?

5 mins read

28.1.2026

 ![](https://lumi-ai-factory.eu/wp-content/uploads/2026/01/AdobeStock_472181971-960x540.jpeg)

Image: Adobe Stock

International Data Protection Day is on January 28! What a perfect chance to talk about data protection and artificial intelligence!

I’m **Enrico Glerean**, a staff scientist at Aalto University, neuroscientist turned hands-on data protection and research ethics teacher. For Data Protection Day, I’d like to highlight some of the current topics at the intersection of AI/Machine Learning and data protection.

We all know by now that you wouldn’t just upload your sensitive personal data like medical records to any random (generative) AI tool… right? And more in general, we can’t blindly trust these systems with their predictions when they are going to make decisions about individuals.

Good news: data protection authorities have been proactive when it comes to AI and personal data. For example, the [French Data Protection Authority CNIL](https://www.cnil.fr/en) has published excellent practical guidelines on the risks of combining large language models, cloud computing, and personal data, especially aimed at small and medium enterprises (see their most recent “[Analysing the status of an AI model with regard to the GDPR](https://www.cnil.fr/en/analysing-status-ai-model-regard-gdpr)“).

Likewise, the [European Data Protection Supervisor](https://www.edps.europa.eu/_en) and the [European Data Protection Board](https://www.edpb.europa.eu/edpb_en) have offered great reports ([Tech Sonar report series](https://www.edps.europa.eu/data-protection/technology-monitoring/techsonar_en)) and training materials on AI and personal data. Through their [Support Pool of Experts](https://www.edpb.europa.eu/support-pool-experts-spe-programme_en), EDPB has produced materials on both the legal side ([Law & Compliance in AI Security & Data Protection](https://www.edpb.europa.eu/our-work-tools/our-documents/support-pool-experts-projects/law-compliance-ai-security-data_es?ref=blog.marcoalmada.com) by **Dr. Marco Almada**), privacy and large language models ([AI Privacy Risks & Mitigations Large Language Models](https://www.edpb.europa.eu/our-work-tools/our-documents/support-pool-experts-projects/ai-privacy-risks-mitigations-large_en) by **Isabel Barbera**) and practical fundamentals especially targeted at SMEs ([Fundamentals of Secure AI Systems with Personal Data](https://www.edpb.europa.eu/our-work-tools/our-documents/support-pool-experts-projects/fundamentals-secure-ai-systems-personal_en) by yours truly Dr. Enrico Glerean).

To celebrate International Data Protection Day with LUMI AI Factory and its amazing researchers, I interviewed our (inter)national expert on privacy enhancing technologies and machine learning: [**Professor Antti Honkela**](https://www.cs.helsinki.fi/u/ahonkela/) from the Department of Computer Science at the University of Helsinki. Antti and his team are leading experts in topics like differential privacy (adding the right noise on top of personal data to make it “less personal”) and synthetic data (generating data about individuals who do not exist, but with statistical properties similar to the real population). This is not just academic theoretical work, it has real life implications for the technologies that daily process our personal data.

*Enrico: Hi Antti, thanks for being with us. Differential privacy sounds promising (I hope I explained it easily enough), but how close are we to seeing small businesses or public services actually using it easily?*

Antti: There are some ready-made tools for specific tasks that can be used relatively easily, but if one wants something else, things can get difficult very quickly. Implementing differential privacy (DP) securely is hard, because bugs do not cause any apparent errors but may leave important vulnerabilities. There are projects like OpenDP that are working to build good open source implementations, but it takes time. My group is also working on making DP easier for end users. Another practical challenge is deciding a suitable privacy-utility tradeoff for a particular application. Stronger privacy guarantees require adding more noise which makes the result less accurate. My group has recently contributed to better understanding the guarantees and developing methods for interactively finding the optimal tradeoff, but more work in translating this to practice remains.

*Enrico: Another topic you have worked with is synthetic data. Synthetic data could indeed help many fields if one can truly synthesise realistic medical data, financial transactions, and so on. In your view, which areas could benefit the most from using it? And what are the challenges as in “all that glitters is not gold”?*

Antti: It is likely impossible in most cases to create synthetic data that would both provide sufficient privacy and provide accurate answers to all possible questions. Therefore, synthetic data seems most promising as a preview that can lower barriers for data access because it can be shared more freely, but it cannot substitute real data in tasks where accuracy is critical. Applications where synthetic data would likely be useful include data used in teaching, algorithm, and software development as well as pilot studies.

*Enrico: In the privacy-tech info sphere, privacy professionals have been discussing “Machine unlearning”, the ML equivalent of the data subject “right to be forgotten”. How realistic is it to remove someone’s personal data from a ML model once it’s already trained? Is it even possible up to a level to guarantee the total erasure of the personal data, or is it just wishful thinking and we just have to accept that our pictures and faces might be forever somewhat memorised in some AI model?*

Antti: There are no unlearning methods that could just take an existing model and reliably remove someone’s data, so that part remains a fantasy. There are methods that allow strong unlearning, but only when the target model has been trained in a specific way to enable unlearning, but this requires compromises elsewhere and such methods are not widely used.

*Enrico: Thank you so much for this exchange! Two last questions about the future: What are you going to work on next? And what’s the next big challenge to make privacy-friendly AI tools simple enough for everyday organizations to adopt?*

Antti: There has been a lot of recent progress on so-called tabular foundation models that allow creating classifiers from tabular data in a single forward computation through a pre-trained neural network without any new training. Adding privacy to such models could be a game-changer that removes worries of secure implementation because the security could be built into the network.

Hopefully we got you excited about data protection and the possibilities that machine learning and AI can bring in fields like healthcare and finance. Data Protection Day bonus: the EDPB has put two open source books [[1](https://law-and-compliance-in-ai-security-and-data-protection-e4e0c8.pages.code.europa.eu/)][[2](https://fundamentals-of-secure-ai-systems-with-personal-data-9cd9e2.pages.code.europa.eu/)] online that you can use for learning more about the intersection between AI and data protection. They are also on [EU GitLab waiting for your contributions](https://code.europa.eu/edpb/)!

Enjoy International Data Protection Day!

---

## **Written by** **Enrico Glerean, DSc**
