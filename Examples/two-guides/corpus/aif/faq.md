---
title: "FAQ | LUMI AI Factory"
url: https://lumi-ai-factory.eu/faq
lang: en
source: aif
scraped: 2026-11-02
---

# Frequently asked questions

*This FAQ is designed to address common questions about the confidentiality, security, and compliance of the LUMI AI Factory’s computing and data management environment. It provides clear and transparent information to help especially commercial organisations understand how our services meet industry standards and support secure deployment in business-critical scenarios.*

#### LUMI AI Factory

# What is the LUMI AI Factory?

The LUMI AI Factory (LUMI AIF) is one of Europe’s first AI Factories, designed to accelerate AI innovation by combining world-class supercomputing, high-quality datasets, and top-tier AI expertise. It provides an open and collaborative environment for startups, SMEs, researchers, and public organizations to develop and deploy AI solutions. LUMI AIF offers services such as HPC resource packages for AI workloads, dataset-as-a-service, training, technical support, and consulting. Its role is to serve as a hub for AI-driven research and development, fostering European competitiveness and technological sovereignty.

# What is LUMI, why does it exist, and who owns it?

LUMI is one of the world’s fastest and greenest supercomputers, located in CSC’s data center in Kajaani, Finland. It is owned by the EuroHPC Joint Undertaking and hosted by a consortium of 11 European countries: Finland, Belgium, Czech Republic, Denmark, Estonia, Iceland, the Netherlands, Norway, Poland, Sweden, and Switzerland. LUMI provides world-class computing resources for research, innovation, and industry across Europe, enabling breakthroughs in science, AI, and data-intensive applications.

# How is LUMI AI Factory funded and operated?

The LUMI AI Factory is funded through European Union initiatives and national contributions from its consortium countries. It is hosted by CSC and operates as a non-profit service platform. The services are offered free of charge to startups, SMEs, and academic researchers to lower barriers to AI adoption and innovation. The business model focuses on providing access to computing power, data, and expertise as shared infrastructure.

# Why were LUMI AI Factory and other AI factories established in Europe?

The European Commission launched the AI Innovation Package in January 2024 to accelerate AI innovation, strengthen Europe’s technological sovereignty, and provide easy access to high-performance computing, data, and expertise. By offering shared infrastructure and free services for startups, SMEs, and researchers, AI factories lower barriers to AI adoption and help Europe remain competitive in science, industry, and emerging technologies.

# Want to know more about AI Factories in general?

Find more information on The European High Performance Computing Joint Undertaking (EuroHPC JU) website here: <https://www.eurohpc-ju.europa.eu/ai-factories/faqs-ai-factories_en>

# How is LUMI AI Factory organised?

LUMI AI Factory is hosted and coordinated by CSC – IT Center for Science and organised as a consortium of six countries: Czechia, Denmark, Estonia, Finland, Norway, and Poland. It builds on national AI strategies, aligns with the EU Coordinated Plan on AI, and promotes collaboration to create a competitive, society-benefiting AI ecosystem.

# What does openness mean in LUMI AI Factory projects?

LUMI AI Factory is publicly funded, so we are expected to publicise our customer’s success stories, while respecting their requirements related to trade secrets and intellectual property rights.

Openness requirements of free of charge computing resources are explained in the access calls through which the resources are applied. Small and medium companies can benefit from access calls that require only a brief public report to be provided. All customers can opt for open research access calls where they are expected to share results openly to support research, development, and innovation. Alternatively, paid access is available and does not come with openness requirements, allowing full confidentiality when desired. There are also national mechanisms (e.g., Business Finland) allowing the same while being free of charge.

# How can I get started?

Simply contact the LUMI AI Factory team through the website’s service request form. They will guide you through the next steps, including selecting the right computing package or training option for your needs. Access is quick and lightweight, and many services are free for AI startups and SMEs. Click here to find the [contact form.](https://lumi-ai-factory.eu/contact-us/)

# Who can use LUMI AI Factory services?

LUMI AI Factory services are for research, development, and innovation (RDI). They are free for startups, SMEs, research organizations, and the public sector, while large companies pay a fee. Access to major resources is through competitive calls, usually requiring some openness of results. Fully confidential projects can use national mechanisms (e.g., Business Finland).

# Which countries can LUMI AI Factory provide services to?

Researchers from academia, research institutes, public authorities, and industry established or located in an EU Member State or in a Participating State or in a third country associated to the Digital Europe Programme or to Horizon Europe shall be granted the Union’s share of access time to EuroHPC supercomputers acquired after 2020. [Supercomputers Access Policy and FAQ](https://www.eurohpc-ju.europa.eu/supercomputers/supercomputers-access-policy-and-faq_en).

[EuroHPC JU countries at the moment](https://www.eurohpc-ju.europa.eu/switzerland-officially-rejoins-eurohpc-joint-undertaking-2025-11-11_en): Albania, Austria, Belgium, Bulgaria, Croatia, Cyprus, Czechia, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Iceland, Ireland, Israel, Italy, Latvia, Lithuania, Luxembourg, Malta, Moldova, Montenegro, Netherlands, North Macedonia, Norway, Poland, Portugal, Romania, Serbia, Slovakia, Slovenia, Spain, Sweden, Switzerland, Türkiye, United Kingdom More information about [third countries associated to Horizon Europe at the moment.](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/common/guidance/list-3rd-country-participation_horizon-euratom_en.pdf)

#### Data storage

# How is data encrypted at rest?

LUMI doesn’t automatically encrypt data at rest, but you can  encrypt your data as needed. You can find more details in the LUMI documentation: <https://docs.lumi-supercomputer.eu/storage/>.

# How is data encrypted in transit?

Data in transit encryption depends on the protocol, the source and the destination. For example TLS and SSH protocols encrypt data by default. For more information, please see <https://docs.lumi-supercomputer.eu/firststeps/SSH-keys/>

# How can we ensure our data is permanently removed after the project is finished?

When your project ends, you’ll still be able to access LUMI and your data for up to 90 days. Please remember to back up anything you want to keep. After 90 days, the data will be deleted. You can find more information from LUMI documentation: <https://docs.lumi-supercomputer.eu/storage/>

#### Data transfer

# How to securely move data to and from the HPC system?

Users can use `rclone`, `s3cmd` and `restic`for transferring data.

Tools to transfer data to LUMI-O*:* <https://docs.lumi-supercomputer.eu/storage/lumio/clients-general/>

Sharing access to data*:*<https://docs.lumi-supercomputer.eu/storage/lumio/advanced/>

# What encryption protocols are used for data transfer?

Encryption depends on the protocol, the source and the destination. For example TLS and SSH protocols encrypt data by default. For more information, please see: <https://docs.lumi-supercomputer.eu/firststeps/SSH-keys/>

LUMI only accepts SSH keys based on the RSA (4096 bit) or ed25519 algorithms. If possible, ed25519 is recommended.

# How to access data on cloud storage from the HPC system?

You can access data on cloud storage. Login nodes provide internet access.

#### Controlling access

# Which kind of access controls are there for different users and/or teams?

Each user has a private home directory, plus a shared project directory that is only accessible to members of that project. Access is managed using regular Unix/POSIX permissions.

# What information can others see about my project?

When it comes to computing jobs in the processing queue (Slurm), the visibility depends on what information your job setup reveals. All users can see basic job metadata in the active job queue, such as the user name, project name, number of nodes used, and the output directory.

# What measures are in place to protect user identities in the login information?

LUMI uses identity federation and token-based authentication to ensure secure access. User identity information is never exposed in plain text during authentication. While future improvements will fully align with pseudonymization principles, some user details may currently be inferred from usernames. Access credentials are time-limited and revocable.

# How to use virtualised or containerised environments?

LUMI supports Singularity/Apptainer containers. You can find more information here:
<https://docs.lumi-supercomputer.eu/software/containers/singularity/>

#### Administrative access

# In which situations can a system administrator access my information?

LUMI system administrator  access  is restricted to specific environments. Administrator can access user data only based on  explicit request from the user or in case administration detect an incident (i.e., data breach, security breach…). In the case of an incident, we follow  our certified  Incident Response procedure which requires notification of the incident to the involved users.

# Will you use my data to train other AI models?

No. We will never use your data to train AI models.

#### Availability, backup and recovery

# Are there backup procedures in place?

System backups are maintained by system administrators.

There are no backups provided for user data on any storage systems of LUMI. Users are recommended to keep copies of their data outside of LUMI to ensure data security.
This is described on <https://docs.lumi-supercomputer.eu/storage/>.

# How should users back-up their data? How can we recover data if needed?

Users are responsible for backing up their own data. Users are recommended to keep copies of their data outside of LUMI.

#### Monitoring and auditing

# What monitoring tools are in place?

LUMI public status dashboard provides real-time system status monitoring: <https://metrics.hpc.csc.fi/grafana/d/-8RWOzyVz/lumi-public-status>

# What is logged? How can logs be accessed?

Security logs are stored in CSC central log storage. Only LUMI system administrators and CSC security team have the access.

Logs are stored for the duration of at least 6 months, but no more than 5 years, considering the legal and other applicable requirements.

#### Regulatory compliance

# How does your facility support in ensuring General Data Protection Regulation (GDPR) compliance?

The privacy notice for processing of user data on the LUMI can be found here: [Privacy notice for processing of user data on the LUMI Service – LUMI](https://www.lumi-supercomputer.eu/privacy-notice-for-processing-of-user-data-on-the-lumi-service/)

# How does your facility support in ensuring Network and Information Security Directive(NIS2) compliance?

LUMI is classified as critical IT infrastructure and must hence be NIS2 compliant.

Ensuring of NIS2 compliance has been implemented by adding LUMI hosting in the scope of the ISO 27001 certification of CSC and by adding procedures for incident reporting to national security authority.

The statement of applicability also includes security controls for providers and partners.

# Which security certifications do you have?

CSC holds  ISO 27001 certification since 2013, LUMI hosting is included in the scope of the certification.

CSC has also been granted official and formal approval by designated national security  authority on physical security and security management.

# Where is the data stored? Where are the data centers located?

Your data is stored in LUMI data center in Kajaani, Finland. LUMI is hosted and the data center is operated by CSC – IT Center for Science Ltd.

#### Incident response

# What is your plan for responding to data breaches or security incidents?

Ensured incident handling procedures, roles and guidelines are in place in case of security incidents, data breaches, attacks and system compromises. Information security incident management planning and preparation responsibilities, identification, classification, reaction, communication and recovery are also covered. Incident handling controls are verified by exercises and by ISO 27001 audits.

Incidents related to LUMI are processed in accordance with NIS2 requirements.

#### Confidentiality assurance

# Do you offer non-disclosure agreements (NDAs) or confidentiality agreements?

We require NDA’s and/or security agreements by partners  with administrative access or access to restricted information.
We do not require NDA’s for standard LUMI/LUMI AIF projects.

However, NDA’s can be exceptionally negotiated on a case-by-case basis. Please contact us through the LUMI AI Factory website contact form for more information: <https://lumi-ai-factory.eu/contact-us/>

# Do you offer other types of agreements and assurances of liability with respect to data security?

Use of the Services is at the User’s own risk, and LUMI is not liable for any loss or injury.

More information in LUMI General Terms of use: <https://www.lumi-supercomputer.eu/lumi-general-terms-of-use_1-0/>
