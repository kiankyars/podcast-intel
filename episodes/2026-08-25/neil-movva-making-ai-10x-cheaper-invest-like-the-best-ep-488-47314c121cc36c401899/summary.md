# Neil Movva - Making AI 10x Cheaper - [Invest Like the Best, EP.488]

- Podcast: Invest Like the Best
- Published: 2026-08-25
- Source: https://colossus.com/episode/from-transistor-to-token/
- Relevance: 5/5

SAIL Research founder Neil Movva lays out a throughput-first inference thesis: long-running background agents could make cheap heterogeneous chips, fragmented power, unreliable data centers, and deeper memory hierarchies economically useful. He also argues that model improvement is shifting from exhausted web data toward verifiable RL environments, while enterprise adoption speed and unavoidable capability diffusion may compress frontier labs' pricing advantage.

**Why it matters:** If Movva's workload forecast is right, the lowest-cost inference providers may be those that orchestrate overlooked compute, memory, and power rather than only buying the newest tightly interconnected NVIDIA systems. His detailed but partly unverified claims identify KV-cache storage, failure-tolerant scheduling, and enterprise deployment cycles as potential constraints on both token economics and frontier-lab rents.

## Signals

- **Movva forecasts background inference will reach roughly half of workloads by year-end and eventually 90%, shifting optimization from interactive latency toward throughput economics.** [08:39.480] _agents_developer_tools; forecast; medium confidence._ He argues background token consumption is not bounded by human attention, then projects a 50/50 background-versus-real-time mix by year-end and 90/10 later; these are his projections, not measured adoption data.
- **Movva argues long-horizon inference can trade away NVLink's latency advantage and exploit non-NVIDIA chips with better FLOPs per operating dollar.** [23:08.900] _semiconductors_compute; inference; medium confidence._ He says eight-way sharding can consume eight times the hardware for only about four to five times the speed, while expert or pipeline parallelism and communication hiding can make less-connected accelerators useful for throughput.
- **Movva argues the internet's human-text subsidy is largely exhausted and model improvement is shifting toward verifiable RL environments and expert feedback.** [36:46.540] _frontier_labs_models; inference; low confidence._ He estimates about 30 trillion high-quality web tokens, or 300 trillion under a wider definition, says models have repeatedly consumed them, and contends generic user preference is now less useful than expert feedback or self-grading coding and math tasks.
- **Movva says SAIL can aggregate small data centers that mainstream buyers reject by trading reliability and tail latency for lower cost.** [53:19.940] _infrastructure_energy; observation; medium confidence._ He describes sites without backup generators or redundant fiber, says SAIL would buy 95% uptime and perhaps 80% at the right price, and relies on an asynchronous control plane to move long-running jobs after failures.
- **Movva identifies KV-cache memory as a major inference inefficiency and is exploring model and chip designs that offload it from HBM to flash at 1 to 10 tokens per second.** [01:09:19.360] _semiconductors_compute; inference; low confidence._ He estimates current KV-cache storage at multiple kilobytes per token and perhaps 10 to 100 times larger than necessary, then describes aggressive flash offload as a divergent SAIL design direction; neither magnitude is benchmarked in the interview.
- **Movva expects frontier labs' price premium for staying three to six months ahead of open models to face pressure.** [01:07:07.900] _companies_capital_allocation; forecast; medium confidence._ He argues enterprise deployment cycles are slower than frontier release cycles and AI-generated public code creates unavoidable latent distillation, continually diffusing capabilities into open models.
- **Movva's contrarian view is that losing TSMC access would cause a supply shock but not a catastrophic efficiency gap.** [01:11:51.300] _policy_geopolitics_security; opinion; low confidence._ He says BF16 performance per watt has improved little from Hopper through Rubin or across recent TSMC nodes and estimates leading Western processes may be only about two times worse; he supplies no benchmark, so this remains a low-confidence opinion.

## Changed Views Or Tensions

- Inference may bifurcate: interactive services reward tightly interconnected leading-edge systems, while background agents may reward cheaper heterogeneous hardware and tolerance for failures.
- Fragmented power, unreliable small data centers, and lower memory tiers could become usable supply when asynchronous workloads and global scheduling absorb outages.
- A three-to-six-month frontier-model lead may not create durable enterprise pricing power when deployment cycles are slower and public AI outputs diffuse capabilities.

## Follow-Ups

- Verify the 50/50 and 90/10 background-inference forecasts against SAIL customer workload data and broader provider telemetry.
- Benchmark SAIL's cost per token, utilization, tail latency, and failure recovery across NVIDIA, AMD, TPU, Trainium, and emerging accelerators.
- Test the claimed 10-to-100-times KV-cache compression opportunity and flash-offload economics at 1 to 10 tokens per second.
- Compare like-for-like BF16 performance per watt across Hopper, Blackwell, Rubin, and leading Intel and TSMC processes, separating efficiency from supply-shock effects.
