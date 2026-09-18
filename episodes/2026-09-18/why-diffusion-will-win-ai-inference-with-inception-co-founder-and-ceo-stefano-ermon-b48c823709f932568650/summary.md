# Why Diffusion Will Win AI Inference with Inception Co-Founder and CEO Stefano Ermon

- Podcast: No Priors
- Published: 2026-09-18
- Source: https://www.youtube.com/watch?v=N1rjtDs8blY
- Relevance: 4/5

Inception co-founder Stefano Ermon argues that diffusion language models improve GPU inference efficiency by processing many tokens in parallel, while retaining Transformer components. He describes OpenCall moving its voice-agent LLM from Cerebras-served autoregressive models to Mercury on Nvidia GPUs, and explains why Inception built its own serving and post-training stack. The strongest evidence concerns latency-sensitive deployment and engineering tradeoffs; Ermon explicitly says current models are below frontier intelligence, and broader capability advantages remain speculative.

**Why it matters:** Model generation algorithms can change the hardware required to meet an application's latency target. The OpenCall account makes that a concrete procurement question, although it is a vendor-reported comparison rather than an independently controlled hardware benchmark. Inception's compatible API also masks substantial proprietary infrastructure beneath it, with consequences for adoption, customization and on-premises deployment.

## Signals

- **Ermon argues that parallel diffusion generation can improve GPU utilization enough to change the economics of latency-sensitive inference.** [08:51; 09:25; 09:55] _semiconductors_compute; inference; medium confidence._ He contrasts sequential autoregressive decoding, which he describes as spending heavily on weight movement, with diffusion processing many tokens together in a workload resembling training matrix multiplications. This is a mechanism for better arithmetic utilization, not evidence of a universal efficiency advantage across batch sizes, quality targets or workloads.
- **Ermon reports that OpenCall switched its voice-agent LLM from Cerebras-served autoregressive models to Mercury running on Nvidia GPUs.** [17:37; 18:04; 18:19; 18:29; 25:12] _applications_business_models; observation; medium confidence._ He describes an ASR-to-reasoning-LLM-to-TTS pipeline and says OpenCall obtained comparable model speed with greater hardware availability, lower cost and higher quality after the switch. He also says OpenCall retained its application harness through an OpenAI-compatible API and structured outputs. The episode provides no controlled latency distribution, cost calculation or end-to-end voice comparison, so the result should remain a customer-specific vendor account.
- **Ermon says a familiar API sits on top of a substantially custom diffusion serving and post-training stack, creating both proprietary know-how and adoption friction.** [12:58; 25:12; 30:12; 31:14] _agents_developer_tools; observation; high confidence._ He says Inception built its own production serving engine, kernels and supervised/RL post-training stack because available infrastructure did not meet its needs. Keeping that work proprietary protects know-how but limits community contributions and makes on-premises deployment harder. OpenAI-compatible text and JSON interfaces reduce application migration work without making the underlying training or serving stack interchangeable.
- **Ermon positions Mercury's present opportunity around latency-constrained tasks, while explicitly stopping short of frontier-intelligence parity.** [12:23; 27:36; 28:06; 29:20; 29:45] _frontier_labs_models; opinion; medium confidence._ He compares current quality to speed-oriented Haiku, Flash and smaller OpenAI models, then states that Inception is not at frontier intelligence and many workloads still require it. His estimate that 20–30% of workloads are highly latency-sensitive comes from his own reading of OpenRouter categories, not a measured market-share forecast. Superior intelligence or data efficiency at scale remains a research possibility in his account.

## Changed Views Or Tensions

- The OpenCall account strengthens the case for evaluating model algorithm and accelerator together when buying low-latency inference; it does not establish a general Nvidia-versus-Cerebras winner.
- API compatibility can make a diffusion model easy to trial while leaving serving, post-training and on-premises deployment materially different from an autoregressive stack.

## Follow-Ups

- Compare Mercury and OpenCall's previous model at matched instruction-following and tool-use quality, concurrency and output lengths; measure p50/p95 full voice-turn latency and cost per successfully completed call, not output tokens per second alone.
- Keep model generations and hardware explicit in benchmark comparisons. The episode's historical 10x claim concerns a sub-billion-parameter academic prototype, not an identified current Mercury production configuration.
- Track whether Inception's serving and post-training tooling becomes available for customer customization or on-premises deployment, and whether latency advantages persist on workloads that require frontier-level reasoning.
