# OpenAI’s Compute Chief: We Can’t Build Fast Enough | Sachin Katti

- Podcast: The MAD Podcast with Matt Turck
- Published: 2026-07-16
- Source: https://podcasters.spotify.com/pod/show/firstmark/episodes/OpenAIs-Compute-Chief-We-Cant-Build-Fast-Enough--Sachin-Katti-e3m587t
- Relevance: 5/5

OpenAI Head of Industrial Compute Sachin Katti describes compute as a revenue-linked constraint rather than speculative excess: he says OpenAI has historically tripled revenue when it tripled compute, consumes new capacity immediately, and expects AI-assisted research to increase experiment volume further. He directionally confirms roughly $50 billion of OpenAI compute spending this year, explains an asset-light capacity model in which partners finance and build infrastructure while OpenAI acts as tenant and offtaker, and details custom silicon, inference-heavy workloads, cluster networking, and guaranteed-token capacity. These are first-party statements, but the spending, elasticity, and performance claims are not independently substantiated in the episode.

**Why it matters:** The interview sharpens both sides of the OpenAI infrastructure thesis. Demand and revenue are said to scale directly with compute, while financing and construction risk are pushed toward hyperscaler and infrastructure partners through capacity-purchase commitments. That can accelerate capacity without OpenAI owning every asset, but it may also create potentially large obligations. Jalapeño, workload-aware co-design, and MRC show OpenAI building a vertically integrated efficiency and reliability stack rather than relying only on merchant accelerators.

## Signals

- **Katti says OpenAI has historically tripled revenue when it tripled compute, consumes every increment of capacity immediately, and sees AI-assisted AI research increasing the number of experiments and therefore compute demand.** [15:42] _companies_capital_allocation; observation; medium confidence._ He presents the compute-to-revenue relationship and immediate utilization as OpenAI's evidence against overbuilding, while arguing that AI removes the human-researcher bottleneck on experiment volume.
- **Katti directionally confirms the host's estimate that OpenAI expects to spend about $50 billion on compute this year; the host separately cites roughly $700 billion of industry compute spending, which Katti says is probably continuing to grow.** [03:04] _companies_capital_allocation; observation; medium confidence._ The host supplies both figures. Katti says the OpenAI estimate sounds about right, then only comments that the industry total is probably continuing to grow.
- **Katti describes OpenAI's capacity model as tenant and offtaker: partners such as Microsoft, Google, Amazon, and Oracle finance or build the infrastructure, while OpenAI commits to consuming the compute rather than owning the underlying assets.** [33:32] _companies_capital_allocation; observation; high confidence._ He agrees that financing is outsourced to partners and says OpenAI commits to buying their capacity across its compute portfolio.
- **OpenAI taped out its Jalapeño custom accelerator in about nine months by combining an experienced former-TPU team, Broadcom's ASIC execution, foreknowledge of future model workloads, and AI-assisted design iteration.** [34:29] _semiconductors_compute; observation; high confidence._ Katti calls nine months the fastest design-to-tapeout cycle he has seen and says workload visibility short-circuited design choices while AI accelerated optimization experiments; the chip targets tokens per watt.
- **Speaking about AI compute broadly rather than OpenAI specifically, Katti says inference may already be the majority and argues that much of modern training is itself inference used for synthetic data, post-training, and test-time computation.** [14:16] _frontier_labs_models; observation; high confidence._ After the host explicitly frames the question as not necessarily about OpenAI, Katti rejects a clean training-versus-inference split and identifies inference as a fundamental building block across the model-development lifecycle.
- **OpenAI's MRC networking protocol is designed to keep 100,000-GPU training clusters running through frequent network-component failures by spraying traffic across multiple paths.** [36:27] _semiconductors_compute; observation; high confidence._ Katti says failures cannot be exhaustively enumerated at that scale, so MRC masks them from training jobs by maintaining alternate routes between chips.
- **OpenAI is selling guaranteed capacity as a committed dollar volume of tokens, positioning intelligence as a supply input that enterprises should secure in advance.** [40:52] _applications_business_models; observation; high confidence._ Katti equates guaranteed capacity with guaranteed tokens and says customers want assurance that scarce model output will be available for critical operations.

## Changed Views Or Tensions

- OpenAI's infrastructure strategy appears more asset-light than a simple owner-operator framing: partners fund and build much of the capacity while OpenAI assumes capacity-consumption obligations.
- Inference is not merely a product-serving cost; Katti says it may be the majority of AI compute broadly and is embedded inside synthetic-data generation, post-training, and test-time research workflows.
- OpenAI's custom-silicon advantage may come as much from private visibility into future workloads and AI-assisted design iteration as from chip-team execution alone.

## Follow-Ups

- Reconcile the directionally confirmed $50 billion figure with OpenAI's disclosed cash spending, lease costs, and multiyear compute commitments.
- Test the claimed one-for-one compute and revenue tripling relationship across periods and separate capacity-driven revenue from model, pricing, and distribution effects.
- Quantify OpenAI's minimum offtake obligations and determine which financing, utilization, and residual-value risks remain with OpenAI versus its partners.
- Track Jalapeño from tapeout to production, including process node, package, memory, deployment date, tokens-per-watt improvement, and merchant-accelerator displacement.
- Obtain MRC benchmarks for failure recovery, throughput, tail latency, and training-job completion at cluster scale.
- Review guaranteed-capacity contract terms, pricing premium, duration, rollover rights, and remedies when token supply is unavailable.
