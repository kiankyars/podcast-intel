# 🔬“We have foundation models for language, not for physics” — Anima Anandkumar, Bren Professor of Computing

- Podcast: Latent Space
- Published: 2026-08-26
- Source: https://www.latent.space/p/anima
- Relevance: 4/5

Anima Anandkumar argues that scientific AI needs structured, resolution-aware architectures rather than a direct extension of token-scale transformers: physical datasets are small, industrial 3D-plus-time grids are enormous, and useful systems must preserve geometry and physical constraints. She describes Fourier Neural Operators, FourCastNet 3, TorchLean, fusion digital twins, and inverse design, while explicitly identifying large-scale formal verification and physically valid long-horizon climate rollouts as unresolved.

**Why it matters:** The episode gives a mechanistic case for a distinct physical-AI stack: global but near-linear operator layers instead of quadratic attention, inference speed that makes large probabilistic ensembles practical, and verification or simulation loops for safety-critical control and design. The strongest deployment and speed claims are first-party and need benchmark-level follow-up, but they could materially change views on where compute, model architecture, and application value accrue outside language models.

## Signals

- **Anandkumar says TorchLean can express PyTorch-like neural networks inside Lean and attach formal robustness and finite-precision bounds, but that large-model verification is not yet scalable because the current Lean backend is CPU-based and moving it to GPUs remains difficult.** [00:06:41.648] _agents_developer_tools; observation; high confidence._ She describes a Lean-native network framework with CROWN-style certified robustness and perturbation-sensitivity bounds, then says transformer-scale efficiency still requires substantial work.
- **Anandkumar argues that language-model scaling assumptions break for high-fidelity physical systems because both the data regime and the effective context size are radically different.** [00:28:28.847] _frontier_labs_models; inference; medium confidence._ She says FourCastNet used about 50,000 global weather samples and other domains have fewer; industrial 3D-plus-time grids can imply hundreds of billions to roughly a trillion positions, motivating physics constraints and non-transformer architectures.
- **Anandkumar attributes Fourier Neural Operators' usefulness to combining global receptive fields with quasi-linear computational complexity and learned nonlinear features, rather than using a fixed linear Fourier representation.** [00:20:08.385] _frontier_labs_models; inference; high confidence._ She contrasts quadratic all-to-all attention with Fourier transforms that retain global connections at quasi-linear cost, while nonlinear and residual layers learn a more expressive latent basis for non-local physics.
- **Anandkumar reports that FourCastNet approached traditional numerical-weather accuracy while running tens of thousands of times faster on a consumer-grade GPU, and that permissive open sourcing enabled weather-agency and company adoption.** [00:34:08.976] _applications_business_models; observation; medium confidence._ She contrasts a small GPU-resident model with supercomputer-based forecasting, says DeepMind and Huawei followed, and reports that smaller weather agencies can now access capabilities previously limited to large agencies.
- **Anandkumar says incorporating spherical geometry lets FourCastNet 3 remain stable for much longer rollouts than rectangular-grid weather architectures, despite training primarily on six-hour prediction steps; she also says fully trustworthy climate-length rollouts remain an open problem.** [00:36:58.260] _frontier_labs_models; observation; medium confidence._ She attributes months-long rollout stability to spherical harmonics and geometry-aware operators, but notes that long trajectories can still violate physical constraints or lose fine detail and require new guardrails.
- **Anandkumar reports that a neural-operator plasma model predicts tokamak disruptions from only a few thousand samples and runs about one million times faster than traditional simulation; her team is now coupling the simulator with control design.** [00:43:53.036] _applications_business_models; observation; medium confidence._ She describes a plasma digital twin developed with the UK Atomic Energy Authority and says the next step is jointly designing magnetic control and simulation to prevent damaging disruptions, while calling the work an early step.
- **Anandkumar says her collaborators use physics simulators inside an AI inverse-design loop for lithography masks, quantum-dot gates, and nonlinear photonics, turning fast forward models into optimized designs rather than mere predictions.** [01:16:03.304] _semiconductors_compute; observation; medium confidence._ She describes optimizing inverse-lithography masks and gate or photonic structures against an embedded simulator, but does not provide fabrication results or comparative design metrics in the interview.

## Changed Views Or Tensions

- Physical foundation models may be constrained less by parameter count than by resolution, geometry, and the availability of real or simulated physical data.
- Inference speed is a capability multiplier for weather and climate because it makes large probabilistic ensembles feasible, not merely a cost reduction.
- Geometry-aware inductive bias can materially improve autoregressive stability, but it does not by itself establish physically valid climate-scale forecasts.
- Formal neural-network verification now has a familiar model-authoring interface, but its CPU-bound proof backend remains a serious scale bottleneck.
- Simulation-trained models may create more value through inverse design and control loops than through surrogate prediction alone.

## Follow-Ups

- Benchmark FourCastNet 3 against ECMWF numerical forecasting and contemporary AI weather models on identical short-range, extreme-event, ensemble-calibration, and months-long drift tests.
- Inspect TorchLean's supported operators, proof coverage, CROWN implementation, and GPU roadmap before treating it as viable for large safety-critical networks.
- Verify the plasma model's one-million-times speedup baseline, disruption-prediction accuracy, sample provenance, and whether the proposed controller has been tested on hardware.
- Check whether the inverse-lithography, quantum-dot, and photonics designs were fabricated and how they compare with expert-designed or conventional-optimization baselines.
