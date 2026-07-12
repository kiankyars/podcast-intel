# Inside Nemotron & NVIDIA’s AI Lab | Bryan Catanzaro

- Podcast: The MAD Podcast with Matt Turck
- Published: 2026-07-02
- Source: https://podcasters.spotify.com/pod/show/firstmark/episodes/Inside-Nemotron--NVIDIAs-AI-Lab--Bryan-Catanzaro-e3li7o6
- Relevance: 5/5

Bryan Catanzaro explains Nemotron as NVIDIA's model-building instrument for post-Moore hardware/software co-design: open models grow the CUDA ecosystem, while FP4 pretraining, hybrid SSM/attention, MoE/NVL72, latent MoE, and multi-token prediction feed directly back into Blackwell-era inference economics.

**Why it matters:** The episode makes NVIDIA's open-model work look strategically central rather than charitable. Catanzaro ties model architecture choices to GPU architecture, power limits, agent workloads, and NVIDIA's inference-cost roadmap.

## Signals

- **Catanzaro says Nemotron's first job is to help NVIDIA design future accelerated-computing systems in a post-Moore-law world.** [22:19] _semiconductors_compute; observation; high confidence._ He says NVIDIA has to deeply understand AI to co-design systems and software, and that specialization now requires understanding rather than simple transistor shrinkage.
- **NVIDIA's open-model strategy is explicitly ecosystem development, not an attempt to be the only AI-model provider.** [23:20] _companies_capital_allocation; observation; high confidence._ Catanzaro says whenever AI is further developed and deployed it creates opportunity for NVIDIA's business, so open technology lets companies build and deploy their own AI on NVIDIA platforms.
- **Nemotron Ultra and Super were pretrained in NVFP4, which Catanzaro frames as an energy and throughput answer to hard compute and power limits.** [35:42] _semiconductors_compute; observation; high confidence._ He says FP4 pretraining required invention because training can diverge, but Blackwell Ultra has higher throughput on these formats and much lower memory/energy movement costs.
- **NVIDIA found hybrid state-space/attention models can be smarter than either architecture alone while lowering sequence-memory requirements.** [39:48] _frontier_labs_models; observation; medium confidence._ Catanzaro says their sweep found mostly state-space plus some attention had lower perplexity, with constant-size SSM cache improving GPU utilization for long sequences.
- **Catanzaro says Blackwell NVL72 was built around MoE inference because dynamic token routing requires fast, low-latency GPU-to-GPU memory access.** [42:31] _semiconductors_compute; observation; high confidence._ He says NVL72 lets up to 72 GPUs read and write each other's memory so experts can be partitioned across GPUs while tokens route dynamically through layers.
- **Nemotron's latent MoE compresses routed vectors to reduce NVLink communication and claims four times as many experts for the same inference cost.** [46:00] _semiconductors_compute; observation; medium confidence._ Catanzaro says latent MoE down-projects token vectors before network transfer, uncompresses them later, saves bandwidth, and expands the expert library at fixed cost.
- **Multi-token prediction is positioned as a direct agent-inference cost lever, especially for low-batch interactive workloads.** [49:31] _agents_developer_tools; observation; medium confidence._ Catanzaro says fetching weights dominates at low batch size, so predicting multiple tokens can reuse the same weights, preserve accuracy through verification, and offer roughly 3x to 4x speed or cost improvement when acceptance rates are high.

## Changed Views Or Tensions

- Nemotron should be tracked as an input to NVIDIA hardware strategy, not just as another open-weight model family.
- Inference acceleration may increasingly depend on model-internal mechanisms such as MoE routing, latent compression, and multi-token prediction rather than only raw GPU supply.

## Follow-Ups

- Read the Nemotron 3 technical report for actual benchmark deltas from NVFP4 pretraining and latent MoE.
- Compare NVIDIA's claimed FP4 pretraining success with Google/Meta/OpenAI low-precision training disclosures.
- Track whether NVL72 utilization or latent MoE materially affects Blackwell inference demand and margins.
