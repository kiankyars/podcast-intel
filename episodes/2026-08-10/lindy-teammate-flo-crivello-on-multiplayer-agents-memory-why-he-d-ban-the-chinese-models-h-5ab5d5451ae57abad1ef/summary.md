# Lindy Teammate: Flo Crivello on Multiplayer Agents, Memory & Why He'd Ban the Chinese Models He Uses

- Podcast: The Cognitive Revolution
- Published: 2026-08-10
- Source: https://www.cognitiverevolution.ai/lindy-teammate-flo-crivello-on-multiplayer-agents-memory-why-he-d-ban-the-chinese-models-he-uses/
- Relevance: 5/5

Lindy CEO Flo Crivello describes a Slack-native AI teammate whose shared memory is maintained by agents, backed by Git, and queried through recursively nested context buckets. The most consequential disclosures are commercial and operational: the new product is again running at negative gross margin despite an 85% cache rate; DeepSeek is the default model but needs more turns than US frontier models; Lindy's code output has accelerated while headcount stayed flat; and internal inference spend is approaching payroll. He also advocates restricting unsanitized Chinese frontier models in the US while accepting an audit, fine-tuning, and insurance-based alternative to a blanket ban.

**Why it matters:** This is unusually specific first-party evidence about the architecture, reliability techniques, model-routing constraints, and still-unsettled unit economics of a general-purpose enterprise agent. It suggests the near-term application moat is less raw model access than context management, caching, validation, and organizational integration, while also showing that rapid internal adoption can shift spend from labor toward inference before the product itself reaches positive gross margin.

## Signals

- **Crivello reports that Lindy's modular council of LLM validators and an online self-improvement loop reduced agent error rates eightfold in the first week.** [22:23] _agents_developer_tools; observation; medium confidence._ Validators intercept proposed actions at multiple points, fan out to several model judges, and feed failures into a self-improvement process; Crivello says the measured error curve fell by 8x after launch.
- **Lindy Teammate is currently operating at negative gross margin even with an 85% cache rate, making cache integrity a first-order business constraint.** [26:05] _applications_business_models; observation; medium confidence._ Crivello says the more complex teammate workload pushed the company back into negative gross margins; he estimates that a cache-rate decline from 85% to 65% nearly doubles serving cost.
- **Lindy preserves access to long-horizon ground truth by turning oversized tool results and conversation compactions into recursively queryable context buckets organized as a high-fanout self-balancing tree.** [26:05–30:51] _agents_developer_tools; observation; medium confidence._ Crivello describes 200,000-token buckets, each represented by a subagent, and a roughly 100-way tree that can reach 10,000 buckets in two model calls—about 2 billion tokens of addressable context by his calculation.
- **Crivello reports that Lindy's weekly pull-request count and lines per pull request each tripled in three months while headcount stayed flat, and expects internal inference spend to exceed payroll within three to six months.** [55:43–1:00:34] _companies_capital_allocation; observation; medium confidence._ He attributes the output increase to agents writing and reviewing code and optimizing systems such as CI; payroll still exceeds internal inference spend, but he says the two are now within striking distance.
- **DeepSeek is Lindy's default driver because of its cost advantage, but Crivello says it is more behaviorally spiky, often needs extra turns, and remains roughly three to six months behind the leading US models.** [1:19:22–1:28:55] _frontier_labs_models; observation; medium confidence._ He characterizes DeepSeek Flash as approximately Sonnet 4.6-level and about 100x cheaper for many tasks, says all of Lindy currently defaults to DeepSeek, and notes that extra turns erode some of the nominal savings.
- **Model portability remains expensive because Lindy finds meaningful behavioral differences across model families and reoptimizes its prompts against more than 1,000 evals for each major model release.** [1:30:19] _agents_developer_tools; observation; medium confidence._ Crivello says the homegrown optimization loop changes prompts materially by model and costs about $10,000 to run for a major release, undercutting the idea that frontier models are interchangeable commodities at the application layer.
- **Crivello supports excluding unsanitized Chinese frontier models from the US on competition, censorship, and security grounds, but is open to audited fine-tuning and insurance requirements instead of an unconditional ban.** [1:40:57–1:55:47] _policy_geopolitics_security; opinion; high confidence._ After arguing for a sweeping ban, he accepts a framework in which a new AI regulator would test whether Chinese models had been sufficiently fine-tuned and sanitized, with risk-priced insurance as another possible control.

## Changed Views Or Tensions

- High cache rates do not by themselves guarantee attractive agent unit economics: a sophisticated enterprise agent can still run at negative gross margin at an 85% cache rate.
- The strongest near-term enterprise-agent differentiation may sit in memory topology, validation, and cache-preserving orchestration rather than in exclusive access to a single frontier model.
- AI adoption can materially increase engineering throughput without immediate layoffs while still moving the company's internal cost base from payroll toward inference.

## Follow-Ups

- Ask Lindy for the denominator, evaluation design, and absolute error rates behind the claimed 8x reliability improvement.
- Track whether Lindy restores positive gross margin and whether its cache rate improves above 85% after the teammate launch.
- Benchmark the recursive context-bucket design against long-context and retrieval baselines, including latency and stale-summary failure modes.
- Monitor whether Lindy changes its default model from DeepSeek and how much reoptimization is required for the next frontier-model release.
- Separate the policy claims about distillation, censorship, and model backdoors and verify each against primary technical and legal evidence.
