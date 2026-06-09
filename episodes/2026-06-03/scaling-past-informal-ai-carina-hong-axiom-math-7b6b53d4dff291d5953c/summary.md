# 🔬Scaling Past Informal AI - Carina Hong, Axiom Math

- Podcast: Latent Space
- Published: 2026-06-03
- Source: https://www.latent.space/p/axiom
- Relevance: 4/5

Axiom CEO Carina Hong argues that coding progress is necessary but insufficient for AGI because informal reasoning does not compound the way verified proofs do. The episode frames Lean-based proof generation as a stronger RL signal, a scalable training corpus, and a practical route into hardware verification and science.

**Why it matters:** If Axiom's reported results hold up, formal verification could become a distinct scaling path for reasoning models and a competitive wedge against frontier labs that still rely heavily on informal proofs.

## Signals

- **Hong reports Axiom achieved 99% on Verina ProofGen, far above the last cited OpenAI o3 result.** [30:42] _frontier_labs_models; observation; medium confidence._ The episode notes Axiom's 187 of 189 Verina code-and-proof result and compares it with a 4.9% result for OpenAI o3 in the last known run.
- **Axiom's thesis is that verified Lean proofs create a higher-quality RL signal than informal proof rollouts.** [13:42] _frontier_labs_models; inference; medium confidence._ The discussion compares Lean verification to compiling and testing code, arguing that correctness checks improve sample efficiency, maximum performance, and corpus compounding.
- **Hong says specification, not proving, becomes the bottleneck once proofs are cheap to verify.** [25:12] _agents_developer_tools; opinion; medium confidence._ The notes quote her view that anything specifiable can be proven, while humans remain bad at specifying everything they want.
- **The episode identifies hardware verification as a likely killer app for Axiom's verified-generation stack.** [43:57] _semiconductors_compute; forecast; medium confidence._ The show notes explicitly call out hardware verification and critical systems as areas where formal proof demand grows with system complexity.

## Changed Views Or Tensions

- Formal proof generation may be a separate reasoning frontier rather than a niche math benchmark.
- Frontier labs that optimize informal reasoning could miss a compounding data advantage if Lean proof generation scales.

## Follow-Ups

- Look for independent replication of Axiom's Verina and Putnam results.
- Track whether OpenAI, DeepMind, Anthropic, or xAI disclose direct Lean-proof RL training.
