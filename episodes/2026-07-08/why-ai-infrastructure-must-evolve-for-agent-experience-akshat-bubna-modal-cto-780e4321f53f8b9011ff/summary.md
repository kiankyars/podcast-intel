# Why AI Infrastructure must evolve for Agent Experience — Akshat Bubna, Modal CTO

- Podcast: Latent Space
- Published: 2026-07-08
- Source: https://www.latent.space/p/modal2026
- Relevance: 5/5

Modal CTO Akshat Bubna lays out a detailed agent-cloud thesis: AI workloads need elastic inference, runtime sandboxes, agent-accessible observability, hard guardrails, networked containers, capacity strategy, and cloud primitives that agents can operate directly.

**Why it matters:** This is first-party infrastructure signal from a company now positioned as a production substrate for AI applications, coding agents, custom inference, post-training, and sandboxed background agents.

## Signals

- **Modal has shifted its SDK/product thinking from developer experience to agent experience.** [00:04:54] _agents_developer_tools; observation; high confidence._ Bubna says agents should not have to read hundreds of Kubernetes files or write untyped YAML; typed decorators and self-provisioning runtimes let agents see changes live, while logs and metrics need to move into the CLI.
- **Modal is operating as a capital-light supercloud across 17 providers rather than building its own data centers.** [00:24:08] _infrastructure_energy; observation; high confidence._ Bubna says Modal's capacity pool spans 17 cloud providers, with its own reliability layer so customers can use capacity that would be hard to operate directly when GPUs fail or providers vary in reliability.
- **Elastic inference and RL rollouts have extremely bursty compute shapes that traditional Kubernetes was not built for.** [00:11:27] _semiconductors_compute; observation; high confidence._ Bubna says Modal customers need rapid regional scaling from roughly 1000 to 1500 GPUs, GPU snapshotting to reduce torch.compile cold starts, and sometimes 100000 sandboxes for RL rollouts.
- **Speculative decoding gains can be multiplicative when accept length improves, unlike small kernel-only gains.** [00:16:52] _frontier_labs_models; observation; high confidence._ Bubna says speculative decoding verifies draft-model tokens in batches, that accept length can yield 2x to 4x speedups without quality loss, and that Modal open-sourced DeFlash as a block-based speculator.
- **Agent and post-training infrastructure is becoming a memory-movement and networking problem, not just a GPU rental problem.** [00:26:40] _semiconductors_compute; observation; high confidence._ The discussion covers sidecars, private IPv6, eBPF controls, RDMA, and about 3 Tbps internal networking; Bubna says moving KV cache and weights between training and inference GPUs has many systems degrees of freedom.
- **Compute strategy is now a core unit-economics function for AI infra providers.** [00:37:36] _companies_capital_allocation; observation; high confidence._ Bubna describes a compute-strategy team modeling one-year versus three-year reservations, GPU types, regions, and supply-chain bets, plus a cheaper batch tier for latency-insensitive evals, synthetic data, and computational biology jobs.
- **Production agents need hard sandbox boundaries and specialized runtime primitives beyond managed-agent harnesses.** [00:43:06] _agents_developer_tools; opinion; high confidence._ Bubna is skeptical of LLM-mediated permissions at the sandbox layer and says production agents need control over persisted files, snapshots, networking, and GPUs; he cites Ramp's external-facing accounting agent running on Modal.

## Changed Views Or Tensions

- Agent infrastructure is not just hosted model inference; it is a combined runtime, sandbox, observability, networking, storage, and capacity-management surface.
- The cloud abstraction for AI may shift from human-operated DevX toward agent-operated AX, where product gaps are exposed by what agents cannot inspect or control.

## Follow-Ups

- Watch Modal Bench for emerging failure modes in agent-operated infrastructure.
- Track adoption of DeFlash, Auto Endpoints, and draft-model evolution from shadow traffic.
- Compare Modal's hard-sandbox posture with OpenAI, Anthropic, Google, and Ona/Codex Cloud agent runtimes.
