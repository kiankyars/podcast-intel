# Intelligence on the Edge: Liquid AI's Ramin Hasani on the Search for Device-Native Foundation Models

- Podcast: The Cognitive Revolution
- Published: 2026-07-04
- Source: https://www.cognitiverevolution.ai/intelligence-on-the-edge-liquid-ai-s-ramin-hasani-on-the-search-for-device-native-foundation-models/
- Relevance: 5/5

Liquid AI CEO Ramin Hasani described a hardware-aware model-design strategy that has moved from research into named production deployments. He said Liquid's models are improving Shopify's commerce metrics and that a 600 MB model will power audio and visual intelligence in Mercedes-Benz vehicles, while the company's automated search system designs architectures against device latency, memory, speed, and downstream quality. His broader thesis is that specialized local models and hardware-native intelligence layers can capture workloads that are too costly, private, or latency-sensitive for frontier cloud models.

**Why it matters:** This is unusually concrete evidence that alternative architectures are becoming a commercial device-AI stack rather than remaining a research curiosity. The Shopify and Mercedes claims, if independently confirmed, strengthen Liquid AI's position in applications where inference economics and hardware fit matter more than maximal benchmark capability. The hardware-in-the-loop approach also implies that chip vendors may need model-design capability, not merely optimized kernels, to differentiate their devices.

## Signals

- **Hasani said Liquid AI models are already in production at Shopify across recommendations, search, product-catalog understanding, and multimodal tasks, improving click-through rates and other internal metrics.** [1:07:19] _applications_business_models; observation; medium confidence._ He named the Shopify workloads and said the deployed models are improving click-through rate and Shopify's internal quality criteria, but did not provide uplift figures.
- **Hasani said Liquid AI signed a major contract with Mercedes-Benz under which a roughly 600 MB model will power in-car audio and visual functions locally.** [1:07:19] _applications_business_models; observation; medium confidence._ He said the model will provide the vehicle's voice and visual intelligence while fitting on the car's smallest processor, with quality comparable to leading audio models.
- **Hasani said Liquid's Automated Foundation Model Design system searches architectures with target hardware in the loop, optimizing memory, latency, speed, and approximately 100 downstream quality benchmarks rather than perplexity alone.** [36:40] _frontier_labs_models; observation; medium confidence._ He described an evolutionary search over roughly 50 to 100 operators and scaling experiments from 10 million to 72 billion parameters; the resulting LFM2 architecture is reportedly 70-80% double-gated one-dimensional convolutions chosen to replace much of attention on CPUs.
- **Hasani said Liquid AI has released more than 50 model variants and reached over one million weekly Hugging Face downloads using about 1,000 GPUs in house.** [12:50] _companies_capital_allocation; observation; medium confidence._ He contrasted Liquid's relatively small internal GPU fleet with its claimed number of releases, enterprise use, and rank as the fifth-most-downloaded US model organization.
- **Hasani said Liquid works with AMD and Qualcomm against their silicon roadmaps, using architecture search to inform future ASIC support and to build foundation-model computation graphs tailored to their processors.** [1:04:05] _semiconductors_compute; observation; medium confidence._ He described joint work that uses expected hardware constraints to reduce inference cost and identify model operators the next device generation should support.
- **Hasani argued that device-chip vendors will increasingly need to own an efficient foundation-model layer because software-model co-design can offset disadvantages in memory or processor bandwidth and become the basis for application distribution.** [1:16:32] _semiconductors_compute; inference; medium confidence._ He pointed to Nvidia's Nemotron effort as the model and argued that an optimized default intelligence layer could differentiate otherwise similar PC and device hardware.
- **Hasani forecast that production-quality specialized local agents could be fine-tuned for tens to low thousands of dollars, with Liquid planning an automated fine-tuning platform announcement within months.** [1:26:43] _agents_developer_tools; forecast; low confidence._ He said current local models are not frontier-equivalent off the shelf, but a tuned local orchestrator could route among private-data filters, specialized models, and cloud models; he characterized the cost and launch timing as targets rather than demonstrated results.

## Changed Views Or Tensions

- Liquid AI appears to have progressed from alternative-architecture research into production commerce and automotive deployments, though the performance claims remain company-reported.
- For constrained inference, architecture choice may be a hardware-specific search problem rather than a simple choice between a transformer and one universal alternative.
- The strategic control point in device AI may shift upward from kernels toward a vertically optimized, tunable model layer supplied with the hardware.

## Follow-Ups

- Confirm Shopify's production scope and obtain quantitative click-through-rate or cost improvements.
- Verify the Mercedes-Benz contract, vehicle rollout timing, supported modalities, and whether the 600 MB figure covers one model or the full stack.
- Compare LFM2 latency, memory, energy use, and downstream quality against similarly sized transformer and hybrid baselines on the named CPU and NPU targets.
- Track Liquid AI's promised fine-tuning platform announcement and test whether production specialization actually falls within the stated tens-to-low-thousands-dollar range.
