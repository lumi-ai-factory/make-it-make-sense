---
title: "Road to production | LUMI AI Factory"
url: https://lumi-ai-factory.eu/user-support/road-to-production
lang: en
source: aif
scraped: 2026-11-02
---

User support materials

# Road to production

Moving ML Workloads from the LUMI Supercomputer to a Production Environment

This guide is for startups that have trained or developed a machine learning workflow on LUMI and now need to serve it to users or run it continuously. Developing a machine learning workflow is one thing. Running it as a service that people depend on is another. The guide goes through why the move is needed, what to find out about your workload before you start, which criteria to use when choosing where to run it, what the options are, how to do the migration and what to think about once the service is running. **In short: train on LUMI, serve elsewhere.**

###### **1. Why move off LUMI?**

LUMI is not a production system, but is built for R&D. There are a few reasons not to use it for production. LUMI uses Slurm to schedule the computations. You submit a job to the Slurm scheduler, the job waits in a queue and runs when resources are free. There is no guaranteed start time, which is fine for training but does not work for a service that should answer a request within a second. There are also scheduled maintenance breaks and other downtime, during which nothing runs. While the location of LUMI in Kajaani (Finland) is great for cooling and clean energy, your users might be distributed over the whole world, so if you need very low latency, the service has to run closer to your users. Finally, according to the [Terms of Use](https://lumi-supercomputer.eu/termsandpolicies/), LUMI is intended for research and innovation, and you can only use it for the purpose your project was granted for.

LUMI is great for what it is designed for: large-scale training, experimentation and HPC simulations. You get access to a lot of GPUs at once, at a scale that would be otherwise expensive to rent or buy. So use LUMI to develop and evaluate your workload at scale, and run the production service somewhere else. See also the blog post [Why supercomputing and LUMI?](https://lumi-ai-factory.eu/articles/blog-why-supercomputing-and-lumi/).

## **2. Before you start: know your workload**

Before choosing a provider, it is worth writing down what you actually need to run, since this determines most of the later choices. Start with the kind of workload. Model inference behind an API has to answer quickly and be available all the time. Scheduled batch jobs run at certain times and can tolerate some delay. Data pipelines move and transform data, often without needing a GPU at all. An interactive app has users waiting for every response. Next is the resource profile. Do you need GPUs, or are CPUs enough? How much memory and storage, and how much traffic do you expect? This can be very different from what you used for R&D on LUMI, since training needs a lot more compute and memory than inference. With quantised inference of LLMs, for example, a model can run on much smaller hardware than it was trained on (see 3.1). Then list the dependencies: the software stack and the modules you use. Pay special attention to ROCm-specific code, since [LUMI-G uses AMD MI250X GPUs](https://docs.lumi-supercomputer.eu/hardware/lumig/), while most cloud providers offer NVIDIA GPUs with CUDA. The [LUMI AI Factory containers](https://lumi-ai-factory.eu/articles/benefits-of-the-lumi-ai-software-environment/)) are optimised for LUMI, so they are not something to deploy elsewhere, but they are a good source for the package versions you have been using (see 5.1).

Think about what data has to move. How large is it and is it sensitive? Often only the trained model weights are needed for serving, and the training data can stay where it is. Production also brings new data that never existed on LUMI: user inputs, logs and feedback. Where is it stored, who can access it and how sensitive is it? If users send personal data to your model, this matters a lot (see 3.3). Finally, plan how the model will be retrained. Models get worse over time when the world changes, which is called model drift. Will you retrain on LUMI with new data, and how does the new model get back to production? Is there constant evaluation? (see 5.4)

## **3. Decision criteria**

### 3.1 Performance

Look at throughput, storage and network performance, and compare them to what your workload needs. You do not necessarily need the newest hardware. A smaller and older GPU may be enough, especially with quantised models. Quantisation stores the model weights with lower precision, for example 8 or 4 bits instead of 16, which cuts memory use a lot with usually only a small loss in quality. Some models can even run on CPUs only. For LLMs, the inference server and batching matter as much as the GPU. Inference servers like vLLM group requests from many users together and manage GPU memory efficiently, which can increase throughput many times compared to a simple implementation. Measure before you decide. The important numbers are latency, either per request or per generated token for LLMs, and throughput, meaning how many requests or tokens per second the system can handle.

### 3.2 Availability

Decide what SLA (service level agreement) and latency you need. An SLA is usually given as the share of time the service is available: 99% means about 3.7 days of downtime per year, 99.9% means about 8.8 hours per year, and 99.99% means about 53 minutes per year. Every higher SLA costs a lot more money, because it requires redundant hardware and people to react.

Are there peaks in demand, like pre-Christmas or Black Friday in e-commerce? Predictable peaks can be planned for by adding capacity in advance. Unpredictable peaks need autoscaling, where the system adds and removes capacity automatically based on load. Where are the users? If they are from around the world, the service may need to run in several regions. If they are mostly in one time zone, there will be a big difference in demand between day and night. Both affect geographic placement. Uneven demand also affects costs. With autoscaling you do not pay for capacity you do not use, and spot instances can make the extra capacity cheaper (see 3.4).

### 3.3 Security and compliance

Check which regulations and certifications apply to you. GDPR applies whenever you process personal data of people in the EU. The EU AI Act sets obligations that depend on the risk class of the AI system, and the obligations come into force in phases, so check the timeline. ISO 27001 is a common certification for information security, and customers may require it from you or your provider. Some sectors, like health and finance, have their own rules on top.

Sovereignty is another question. Data residency means the data stays physically in the EU. But even if the data is in an EU data centre, the US CLOUD Act allows US authorities to request data from US companies regardless of where it is stored. This is often the reason to pick a European provider.

Remember that the model itself can be sensitive. Models can [memorise and leak parts of their training data](https://not-just-memorization.github.io/extracting-training-data-from-chatgpt.html). If you trained on sensitive data, the model weights need the same care as the data. More on this in the earlier blogpost [Trustworthy AI: Turning compliance into competitive advantage](https://lumi-ai-factory.eu/articles/trustworthy-ai-turning-compliance-into-competitive-advantage/).

### 3.4 Costs

Look at the total cost of ownership, not only the price of a GPU hour. Some costs are easy to forget. GPUs cost the same whether they are used or not. Someone has to keep the service running, so staff and operations cost money, and so do monitoring and storage for models, data and logs. Incoming (ingress) traffic is often free, but outgoing (egress) traffic is often charged and can become expensive.

Spot instances are spare capacity that providers sell at a discount, but they can be taken away at any time. That is fine for batch jobs that can be restarted, but a service with an SLA needs redundancy on top (see 3.2). Reserved capacity, where you commit to using resources for a longer time, is cheaper when demand is steady.

Training on LUMI happens now and then, but serving runs all the time. Over the lifetime of the model, serving often costs more than training. This is why the size of the model matters. Distillation, where a smaller model is trained to imitate a larger one, or fine-tuning a smaller model for your specific task can cut serving costs more than any hardware choice. Other techniques, such as speculative decoding, can also help, but they are beyond the scope of this blog post.

### 3.5 Other considerations

Committing too much to one provider can cause so-called vendor lock-in. Provider-specific tooling can be convenient and sometimes cheaper, but it makes it harder to move later. An open-source stack, for example containers, Kubernetes and an open inference server, is one way to avoid this. It makes sense to think now about how hard it would be to leave the provider later, and to create an exit strategy. Lock-in and costs for moving data out are the main obstacles.

Also check the licence of the machine learning models. If you build on an existing open model, check that its licence allows commercial use. Consider sustainability, too: LUMI [runs on 100% renewable energy](https://www.lumi-supercomputer.eu/sustainable-future/). What is the energy mix of the production provider? This may matter for your own sustainability goals or for your customers. Finally, what support and training is available for your move, from the provider or from others?

## **4. Deployment options**

The options below are roughly ordered from least work to most control. Note that there is a wide range of deployment offerings, so this guide only covers the most popular kinds of production environments.

### 4.1 Managed inference platforms

You upload the model and the provider runs it. You do not have to manage servers, GPUs, drivers or scaling. This is the least work and gives the least control, and it is often the realistic first step for a small startup. With your own model, you usually pay per hour or minute that the endpoint is running, since the GPUs are reserved for you. If you use one of the provider’s off-the-shelf models (often called serverless or catalogue models), you usually pay per token instead. The downside is that you are limited to the models, formats and settings the platform supports, and at high volume the price per request may be higher than running it yourself. Managed inference is widely available from both European providers and hyperscalers.

### 4.2 Cloud

With plain virtual machines with GPUs, you rent a machine and install everything yourself. Of the cloud options, this gives the most control but is also the most work: you handle the operating system, drivers, inference server, scaling and updates. Managed Kubernetes or container platforms are a middle ground. You package the workload in containers and the platform runs them, handles restarts and can scale them. This is less work than plain virtual machines, but it needs Kubernetes skills in the team. There are both European providers and hyperscalers offering this. The hyperscalers have the most services, EU regions and EU “sovereign cloud” offerings, but they are US companies (CLOUD Act, see 3.3).

### 4.3 Own or dedicated hardware

Running on your own hardware gives full control and predictable costs at scale. If the GPUs are busy most of the time, owning them can be cheaper than renting. At a large scale, the upfront and operations costs are high: you buy the hardware, replace broken parts and need people who know how to run it. It is also hard to scale out, since buying and installing new servers takes weeks or months. The servers can be in your own server room, or you can use co-location: you buy the servers (e.g. NVIDIA DGX or other GPU servers) and rent rack space, power, cooling and network in someone else’s data centre. It might also be possible to offer to run the servers on your customers’ premises so that their data never leaves their site.

That said, owning hardware does not have to be expensive. For a small or quantised model and no need for instant answers, such as overnight batch jobs or a few users, a desktop PC with a good graphics card (under €2,000) can be enough. It will not handle many users at once, but it is a cheap start, and your data stays in-house.

Between owning hardware and the cloud is renting dedicated bare-metal servers. You get a whole physical server for yourself without virtualisation, but you do not have to buy the hardware.

### 4.4 Multi-cloud and hybrid cloud

Multi-cloud and hybrid cloud are often mixed up. Multi-cloud means using several cloud providers at the same time. For example, the same model is served on two European providers and traffic switches to the second one if the first goes down. This protects against the outage of a single provider. Hybrid cloud means combining own hardware with the cloud. For example, a few own GPU servers handle the normal load, and extra cloud instances start at peak times. This gives the lower operating cost of own hardware for the steady load and the flexibility of the cloud for the peaks.

Both are easier to manage with tooling that works the same everywhere, such as Kubernetes for running the workloads and Terraform/OpenTofu for describing the infrastructure as code. This portability also reduces vendor lock-in. However, all of this adds complexity, so most startups do not need it at first. It is worth it for very high availability or when regulation requires it.

### 4.5 Which one?

Start from what you wrote down in Section 2. As a rough guide, a small team with a first launch is usually best off with managed inference. With sensitive data, look at your own hardware or an EU provider that offers isolated environments and meets the certifications you need (see 3.3). A steady, high load and an ops team make reserved cloud capacity or own hardware worth it. Multi-cloud is mainly worth it for very high availability, for regulatory requirements, or for the flexibility to move to another provider when pricing changes. Hybrid cloud fits when you have a steady base load on your own hardware but also clear peaks. The choice is not permanent. Many start with managed inference and move to more control when they know their load and costs better.

## **5. Migration and operation**

### 5.1 Package the workload and check it gives similar results

Do not reuse the [LUMI AI Factory containers](https://lumi-ai-factory.eu/articles/benefits-of-the-lumi-ai-software-environment/), since they are optimised for LUMI hardware and software. Instead, export the package versions from them with `pip freeze` and build a new container for the target environment using only the packages you really need for serving. Then validate that the model behaves similarly enough, for example by running the same test inputs on both and comparing the outputs. Small numerical differences between hardware are normal.

Going from ROCm (AMD) to CUDA (NVIDIA) is usually not a problem, as PyTorch code is mostly device-agnostic, but it is good to test on the target hardware anyway. The exception is libraries with their own GPU kernels, such as flash-attention, bitsandbytes and vLLM. They have separate builds for AMD and NVIDIA, so you need to install the right one.

### 5.2 Move data and models

You can export data from LUMI through [LUMI-O](https://docs.lumi-supercomputer.eu/storage/lumio/), the S3-compatible object storage, with tools like rclone or other S3-compatible clients. Most cloud providers support S3 as well, which makes the transfer simpler. Check which model formats the provider supports. Common ones are safetensors, ONNX and GGUF. Use checksums to verify that the files arrived intact. With files of tens or hundreds of gigabytes, a broken transfer is not unusual.

### 5.3 Get ready to go live

On LUMI the model runs as a job that starts and ends. In production it has to run as a service that waits for requests. Use an inference server for this. vLLM, for example, runs on both AMD and NVIDIA, so you can test the same setup on LUMI and the target. How to run vLLM on LUMI is described in [chapter 10 of the LUMI AI Guide](https://github.com/Lumi-supercomputer/LUMI-AI-Guide/blob/main/10-LLM-inference/). Think about automation. Building containers, deploying and setting up the infrastructure should not depend on someone doing manual steps. Before going live, test scaling with load tests that simulate the expected traffic and peaks, and check correctness once more in the real environment. Also do a security review: who can access the service, the model and the data?

### 5.4 After going live

You need monitoring and alerting so that you notice problems before your users do, and a plan for what users see when the model is down or slow. Public LLM endpoints also need rate limiting and protection against prompt injection and misuse. Models drift, so evaluate the model constantly on fresh data, retrain on LUMI or in another computing environment when needed and roll out new models carefully, with a way back to the old version. Running a service also needs different skills than running Slurm jobs. Who in the team does that, and who is on call?

## **6. Conclusion**

Are you an industry user and need more in-depth support? Check out our [blog post on consulting](https://lumi-ai-factory.eu/articles/ai-expert-consultation/). If you want more information on why to use supercomputing and LUMI, [check out this blog post](https://lumi-ai-factory.eu/articles/blog-why-supercomputing-and-lumi/). Reaching out is easy: You can contact the LUMI AI Factory experts by filling out the [contact form](https://lumi-ai-factory.eu/contact-us/) below, and your inquiry will be directed to the appropriate AI specialists! To learn more about what free of charge access means and who is entitled to it, take a look [here](https://lumi-ai-factory.eu/pricing-and-eligibility/).

We like to acknowledge the authors [of this ENCCS article](https://enccs.se/2025/09/news/from-supercomputer-to-cloud) for the good discussions that started the work on this article.

# Get in touch with us.

Have a question or want to learn more about our services? Fill out the form, and our experts will get back to you.
