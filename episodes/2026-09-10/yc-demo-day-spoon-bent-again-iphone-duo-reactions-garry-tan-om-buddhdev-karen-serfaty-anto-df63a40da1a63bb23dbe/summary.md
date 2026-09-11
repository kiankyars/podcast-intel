# YC Demo Day, Spoon = Bent (Again), iPhone Duo Reactions | Garry Tan, Om Buddhdev, Karen Serfaty, Antonio Li, Edward Ge, Alfredo Gonzalez

- Podcast: TBPN
- Published: 2026-09-10
- Source: https://share.transistor.fm/s/35e8db3b
- Relevance: 4/5

YC's demo-day interviews expose practical bottlenecks beyond model capability: proving training-data value through post-training experiments, completing agentic purchases through existing checkout defenses, abstracting robot control for LLMs, and handling genomic datasets in legacy healthcare systems. Garry Tan also reports a larger hard-tech presence and substantial token credits for YC companies.

**Why it matters:** The concrete opportunities are in integration and measurement, not merely better prompts. These founders describe how they sell model improvements, payments execution, physical control, and data infrastructure. Early revenue and production figures are company self-reports, not proof of durable economics, broad autonomy, or clinical effectiveness.

## Signals

- **Om Buddhdev says Olam Labs validates proposed training tasks by post-training open-source models on GPUs before selling the data to frontier labs.** [00:44:29; 00:44:47; 00:45:30; 00:49:30; 00:49:42] _frontier_labs_models; observation; high confidence._ He describes simulated workplaces and negotiation settings for measuring deception and collaboration, then explains that benchmarks demonstrate the capability a dataset can improve. Olam tests tasks through its own post-training runs. He says current GPU sourcing is manageable at its size but views future competition with larger labs for compute as a business risk.
- **Karen Serfaty says Agent Card charges personal-assistant companies a monthly fee for infrastructure that lets agents use consumers' existing cards, with checkout completion a harder problem than storing payment credentials.** [00:53:58; 00:54:33; 00:55:03; 00:56:35; 00:57:34] _applications_business_models; observation; high confidence._ Serfaty describes a card Vault and a purchase API intended to handle buying across merchants, preserving existing-card benefits. The account separates credential access, website navigation, and checkout execution, identifying anti-bot defenses at checkout as the hardest stage. Serfaty says merchant and payment-provider partnerships matter; no transaction volume or checkout-success rate is provided.
- **Antonio Li describes Nori's robot-control approach as simplifying existing navigation capabilities for LLMs, rather than eliminating the intermediate software between the model and the hardware.** [01:03:20; 01:05:37; 01:05:53; 01:06:16; 01:08:07] _agents_developer_tools; observation; high confidence._ He says substantial glue code remains necessary and describes calling an onboard 2D LiDAR navigation stack with a short command. He reports a 1.5-kilogram payload per arm and production of two to three robots daily for early research partners. Claws were chosen over dexterous hands because he sees limited benefit from extra hand complexity under current control policies; this is not a validated household-autonomy benchmark.
- **Garry Tan reports that roughly a quarter of YC's 200 presenting companies are hard tech and says YC companies can optionally access $2 million worth of OpenAI tokens.** [00:25:38; 00:27:32; 00:28:37; 00:29:39; 00:29:50] _companies_capital_allocation; observation; high confidence._ Tan gives the batch composition and describes YC's $500,000 investment plus cloud credits, then separately identifies the optional OpenAI token offer. He argues model access lets small teams advance technical prototypes before recruiting expensive specialists. These are his stated resources and mechanism, not a measured reduction in hardware development costs or a guarantee of credit eligibility and terms.
- **Alfredo Gonzalez reports Omanta reaching $319,000 in monthly recurring revenue with more than 150 patients roughly a month after launch, initially selling directly to patients or sponsors.** [01:15:57; 01:18:03; 01:18:58; 01:19:32] _applications_business_models; observation; medium confidence._ He describes an AI-assisted research service for interpreting patient genomic data and identifies infrastructure as a constraint: sequencing datasets can be tens to hundreds of gigabytes while legacy systems expect far smaller records. The interview supplies founder-reported traction but no revenue-recognition detail, retention data, or evidence establishing clinical effectiveness; insurance coverage is an expectation, not the stated current business model.

## Changed Views Or Tensions

- Olam's account puts the training-data business closer to applied model research than simple data brokerage: suppliers must demonstrate improvements and budget for their own post-training experiments.
- Agentic commerce needs an end-to-end execution path through merchant defenses; issuing or storing a card alone does not complete the transaction.
- Nori's account points to capable conventional control primitives and a simple model-facing interface as important complements to improving LLMs.

## Follow-Ups

- Check Olam's published evaluations for held-out task coverage, reward-hacking resistance, and evidence that training improvements transfer beyond the benchmark.
- Track Agent Card's merchant acceptance, transaction success, authorization controls, and fraud allocation before treating its purchase API as universally usable.
- Look for independently repeatable Nori task demonstrations and delivered-unit figures, separating developer hardware from dependable household autonomy.
- Verify the scope, conditions, and usable duration of the YC/OpenAI token-credit offer before comparing it with cash funding.
- Check Omanta's reported recurring-revenue definition, patient retention, clinical validation, and actual payer contracts separately.
