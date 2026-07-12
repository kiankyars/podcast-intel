# 🔬 The Coolest Diffusion Research Isn't in LLMs — Evan Feinberg & Sergey Edunov, Genesis Molecular AI

- Podcast: Latent Space
- Published: 2026-07-01
- Source: https://www.latent.space/p/the-coolest-diffusion-research-isnt
- Relevance: 4/5

Genesis Molecular AI argues that diffusion-based 3D protein-ligand modeling has crossed a practical threshold: PEARL models protein flexibility and induced fit, current co-folding benchmarks are too loose for medicinal chemistry, and higher-accuracy models now enable agentic drug-discovery loops.

**Why it matters:** This is a concrete example of non-LLM generative AI crossing from benchmark performance into potentially workflow-changing scientific automation. The evidence is strong but less timestamped because the available transcript is a Latent Space article-style transcript rather than a timed dialogue.

## Signals

- **Genesis argues diffusion became the right primitive for high-value 3D structure prediction rather than another transformer variant.** _frontier_labs_models; opinion; medium confidence._ Evan Feinberg says some of the most innovative diffusion research is happening in 3D structure prediction, where PEARL can model ligand placement plus protein adjustments.
- **Genesis claims PEARL can model protein flexibility and induced fit without long molecular-dynamics simulations.** _applications_business_models; observation; medium confidence._ The article says PEARL understands protein flexibility, adjusts protein and ligand together, and later modeled EV-A71 induced fit without long MD runs.
- **Genesis says its model quality has crossed the threshold needed for agentic drug-discovery loops.** _agents_developer_tools; observation; medium confidence._ The writeup says SAPPHIRE can inspect poses, form hypotheses, read literature, use internal tools, and propose next-round candidates, with automated lab partnerships such as Incyte closing the loop.
- **Feinberg argues the field's common 2 Angstrom RMSD pose benchmark is too weak for real medicinal-chemistry use.** _frontier_labs_models; opinion; medium confidence._ The article says a 2 Angstrom threshold can miss crucial interactions such as flipped aromatic rings, while hydrogen bonds have about a 0.6 Angstrom validity range and PEARL targets closer to 1 Angstrom.
- **PEARL reportedly beat public models on OpenBind's 802 unseen EV-A71 co-complexes without target fine-tuning or homologous-target data.** _applications_business_models; observation; medium confidence._ The article says the benchmark target was released after PEARL's training cutoff, the task stresses induced fit, and PEARL was ahead across metrics, often well ahead of public models.

## Changed Views Or Tensions

- Small-molecule AI progress may be bottlenecked less by generic model scale and more by physically accurate pose thresholds, protein flexibility, and wet-lab integration.
- The standard 2 Angstrom co-folding benchmark may overstate practical readiness for drug discovery.

## Follow-Ups

- Read the PEARL technical report and OpenBind evaluation details.
- Compare Genesis results with Isomorphic and Deep Origin claims, noting that closed models limit direct comparison.
- Track whether SAPPHIRE/Incyte produces measured cycle-time or hit-rate improvements.
