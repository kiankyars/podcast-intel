# The Neuron Basis: Goodfire's Curt Tigges on Agentic Interp, Monosemanticity & Reverse Engineering

- Podcast: The Cognitive Revolution
- Published: 2026-11-10
- Source: https://www.cognitiverevolution.ai/the-neuron-basis-goodfire-s-curt-tigges-on-agentic-interp-monosemanticity-reverse-engineering/
- Relevance: 4/5

Goodfire's Curt Tigges presents experiments on Qwen3.6-35B-A3B that make individual MLP neurons more credible units for interpretability: strong activations carry much of the tested behavior, modest post-training repairs sparse-model reasoning, and an agent's neuron descriptions support causal reconstruction tests. Gated neurons can participate in several context-specific computations. These results strengthen the experimental case beyond the earlier clean-neurons essay, while leaving long-context behavior, weak-activation mechanisms and whole-model understanding unresolved.

**Why it matters:** The practical shift is toward testing explanations directly against the original model's neurons and their effects, potentially reducing reliance on learned replacement features for MLP analysis. The evidence supports a tractable research program, not a completed model audit: Tigges explicitly distinguishes a neuron inventory from understanding interacting circuits, attention and the residual stream. Monitoring or safety benefits still require behavior-specific validation.

## Signals

- **Tigges reports that the model preserves substantial capability when only its strongest routed MLP activations are retained for each token.** [27:14; 28:46; 30:28; 1:23:04] _frontier_labs_models; observation; high confidence._ He describes near-baseline non-reasoning performance under heavy dynamic ablation. The [published study](https://www.goodfire.com/research/neurons-as-an-interpretable-basis#router-weighted-top-k-filtering) specifies retaining 320 of 4,096 routed neurons per layer per token, suppressing 92.2%; shared-expert neurons remain unchanged. This is a changing activation mask, not permanent neuron removal or a measured inference-speed gain.
- **Tigges says 100 million tokens of post-training restored sparse-model reasoning to parity or better on the benchmarks tested.** [1:37:01; 1:37:07; 1:39:55; 1:44:19] _frontier_labs_models; observation; high confidence._ He corrects the host's 10-million-token figure to 100 million and describes loops and excessive self-checking before recovery. The [paper](https://www.goodfire.com/research/neurons-as-an-interpretable-basis#fine-tuning-for-performance-recovery) specifies 91M SFT plus 9M RL tokens, with all weights trained under the mask. Tigges interprets recovery as recalibration of largely retained knowledge; the mechanism is unproven. Coding tests reached 32k context, while million-token behavior remains untested.
- **Goodfire's Neuron Scientist tests and revises neuron explanations, then evaluates whether another model can reconstruct their causal effects.** [41:31; 44:02; 45:59; 48:06; 51:09] _agents_developer_tools; observation; high confidence._ Tigges describes counterfactual text experiments and independent prediction feedback; one difficult neuron tracked a reformatted list introduced far earlier in the context. Predicted activations are patched into the model after ablation. The interview cites 74% damage recovery; the [published simulation result](https://www.goodfire.com/research/neurons-as-an-interpretable-basis#simulation) is 73% of the perfect-reader recovery ceiling in the strongest activation regime. This measures scoped single-neuron reconstruction, not the fraction of the whole model understood.
- **Tigges describes gated MLP neurons as context-dependent computations whose distinct meanings can feed different downstream readers.** [12:26; 18:04; 59:18; 1:04:03] _frontier_labs_models; observation; medium confidence._ He explains how separate gate and up projections combine signals and how context prepares different readers for a neuron associated with oral health in one setting and marine wildlife in another. Positive and negative activations can also have different meanings. His proposed target is an enumerable set of computational roles, including reasoning control signals, rather than requiring every neuron to encode one human concept.
- **Tigges reports that some difficult-to-interpret double-negative activations can rescue reasoning even when their sequence information is disrupted.** [1:33:32] _frontier_labs_models; observation; medium confidence._ When both SwiGLU branches are negative, their product is positive. Tigges says removing these activations sometimes damages reasoning, yet restoring them in reversed token order or from another sequence can repair it. He explicitly leaves their mechanism unresolved. This is a concrete limitation on interpreting weak, incoherent activations as dispensable noise.

## Changed Views Or Tensions

- The new ablation and reconstruction experiments provide stronger grounds for studying MLP neurons directly than the earlier qualitative clean-neurons claim alone.
- Apparent polysemanticity need not make a neuron intractable: context-dependent readers and a bounded set of computational roles offer a more useful test than one-concept labels.
- Sparse benchmark recovery supports further experimentation but does not establish runtime savings, long-horizon reliability or a solved alignment problem.

## Follow-Ups

- Check independent replication across architectures and tasks, with attention to whether dynamic sparsity preserves behavior beyond 32k context and through repeated agent turns.
- Track released neuron labels and tools, then compare agent-generated descriptions with simple labeling and learned-feature baselines on held-out causal reconstruction.
- Follow experiments that explain double-negative activations and connect neuron-level descriptions to complete circuits and validated behavior monitors.
