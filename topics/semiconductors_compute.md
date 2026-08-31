# Semiconductors Compute

GPUs, accelerators, memory, networking, foundries, semiconductor equipment, and architecture.

<!-- episode:7b6b53d4dff291d5953c -->
## 2026-06-03 - [🔬Scaling Past Informal AI - Carina Hong, Axiom Math](https://www.latent.space/p/axiom)

- **The episode identifies hardware verification as a likely killer app for Axiom's verified-generation stack.** [43:57] The show notes explicitly call out hardware verification and critical systems as areas where formal proof demand grows with system complexity.

<!-- episode:19dd142ca585f51ce8cd -->
## 2026-06-01 - [Why Video Agent models are next — Ethan He, xAI Grok Imagine](https://www.latent.space/p/video-agents)

- **He says coding-model improvements are making compute the bottleneck for model iteration again.** [00:07:05] He argues ideas that previously took weeks to implement can now be built in hours, so teams need enough compute to immediately test many more model and data experiments.

<!-- episode:172f188e9414764b980f -->
## 2026-06-11 - [Bezos AI Play, Future of Airports, CAA Fund | David Reger, Mike Wior, Ariel Cohen, Jeff Tatarchuk, Matt Joseph, Ade Ajao, Jeremy Fraenkel](https://share.transistor.fm/s/7b97840c)

- **TensorWave's Jeff Tatarchuk says AMD's constraint is closing the software and ecosystem gap, not proving the chips can work for AI inference.** [01:37:06] He says early customers tried AMD because NVIDIA supply was constrained, AMD hardware initially got ahead of software, Databricks showed NVIDIA-to-AMD could work out of the box for important use cases, and CUDA's moat is really the developer ecosystem and libraries.

<!-- episode:91720efd7d609c680ef9 -->
## 2026-06-09 - [Siri AI, Fable 5 Launch, Rivian CEO Joins | RJ Scaringe, Chris Miller, Evan Beard, Nick Fleisher, Chris Matarese, Alex Heath, Rob Schroder Jr.](https://share.transistor.fm/s/e343af3e)

- **Chris Miller says AI has doubled semiconductor spend as a share of GDP over four years, with further growth gated by manufacturing capacity more than end demand.** [01:04:32] Miller says semiconductor spend was flat as a GDP share for two decades, roughly doubled in the last four years due to AI, and now faces TSMC and broader manufacturing-capacity constraints.
- **Miller says the AI chip supply chain is underbuilt because TSMC, advanced-packaging suppliers, materials vendors, and ASML all face bullwhip incentives to be more conservative than Silicon Valley wants.** [01:04:32] He says single-company choke points appear deeper in the supply chain, skepticism increases the farther suppliers are from end AI demand, and TSMC's decision to delay high-NA lithography purchases creates a medium-term ASML challenge.

<!-- episode:bd4abdfdd12e2dd63579 -->
## 2026-06-15 - [Ep. 015 - DG Matrix Explains 800V DC vs Legacy AC Distribution (Datacenter, Energy) | Jordan Nanos, Jeremie Eliahou Ontiveros, Nicolas Bontigui, Haroon Inam](https://podcasters.spotify.com/pod/show/jordan-nanos/episodes/Ep--015---DG-Matrix-Explains-800V-DC-vs-Legacy-AC-Distribution-Datacenter--Energy--Jordan-Nanos--Jeremie-Eliahou-Ontiveros--Nicolas-Bontigui--Haroon-Inam-e3kqvco)

- **The SemiAnalysis speakers argue that AI accelerator demand is overwhelming TSMC N3 capacity.** [10:24] They model AI rising from 9% of 3 nm wafer demand in 2025 to about 60% in 2026 and 85-90% in 2027 as Rubin, MI400, TPU v7/v8, and Trainium ramp.
- **Shravan says TSMC capex increases will not provide near-term relief.** [04:39] He cites TSMC moving from roughly $30 billion in recent annual capex to a $52-54 billion guide, expects closer to $70 billion in 2027, and says new capacity still takes 12-24 months.
- **The speakers say consumer-device weakness is not a large enough release valve for accelerator supply.** [16:21] Their modeling says reallocating 5% of 2026 N3 smartphone wafers yields only slightly above 100,000 Rubin GPUs or 300,000 TPU v7s; even 25% reallocation yields about 700,000 Rubin GPUs and 1.5 million TPU v7s.
- **The speakers frame HBM tightness as structural through at least the second half of 2027.** [17:26] They say HBM consumes about 3x the wafer capacity per bit of commodity DRAM, HBM4/4E can rise to 4x, and some vendors struggle to meet NVIDIA's requested 11 Gbps pin speeds.
- **Dan says NVIDIA's CPO path appears to start with scale-out and inter-rack expansion rather than the originally expected scale-up-first path.** [40:21] He says CPO can remove pluggable optics and DSP energy, scale beyond copper's 2 meter reach, and that NVIDIA announcements such as NVO 576 and NVO 1152 connect racks with scale-up CPO.

<!-- episode:7f12967d6d478b19c616 -->
## 2026-06-18 - [Re-engineering the Semiconductor Supply Chain with Intel CEO Lip Bu Tan]()

- **Tan argues agentic AI and inference are increasing CPU importance relative to the training-era CPU/GPU mix.** [05:28] He says AI model developers told him CPUs are useful for reinforcement learning and agent orchestration, and he sees the CPU-to-GPU ratio moving from about 1:8 in training toward roughly 1:4 or 1:5.
- **Tan says Intel is collaborating weekly with Elon Musk's Terafab team to help accelerate production using Intel technology and process capabilities.** [08:06] He says he and Musk share the view that semiconductor infrastructure has not caught up with AI growth, and that Intel is working with Musk's team on capacity, productivity, and efficiency.
- **Tan points to advanced packaging and new substrate/material choices as major bottlenecks after leading-edge process work.** [16:16] He says packaging is becoming a bottleneck, highlights Intel's next-generation packaging effort, and says he is looking at glass, artificial diamond, gallium nitride, silicon carbide, and indium phosphide related investments.
- **Tan concedes Intel is far behind TSMC in foundry trust and performance, but expects the opportunity to become visible around 2030-2032.** [37:37] He says Intel must improve IP, yield, defect density, and cycle time before customers trust it with wafers, while describing PC client, edge, physical AI, and agentic AI as areas where Intel can still compete.

<!-- episode:83a81550380d0d9c9981 -->
## 2026-06-18 - [The Neocloud Boom: State of AI Compute 2026 | Stephen Balaban](https://podcasters.spotify.com/pod/show/firstmark/episodes/The-Neocloud-Boom-State-of-AI-Compute-2026--Stephen-Balaban-e3kut0h)

- **Balaban frames Nvidia's moat as the deep software and networking stack, not just CUDA or chip price.** [25:33] Lambda has deployed Nvidia chips from V100s through B-series systems, and Balaban highlights cuDNN kernel optimization plus NCCL topology-aware networking as hard for alternative silicon entrants to match.
- **Balaban says 2023 H100s now lease at higher rates than at original deployment and argues GPU economic useful life exceeds common depreciation assumptions.** [40:30] He says Lambda's H100s deployed in 2023 lease at higher rates today, disputes three- to five-year discard assumptions, and notes usable life can exceed the roughly six-year accounting depreciation schedule.

<!-- episode:8d9fef4d070751773d4a -->
## 2026-06-18 - [The Professor of Outputmaxxing — Anjney Midha, AMP](https://www.latent.space/p/anj)

- **Midha says MatX's non-Nvidia accelerator strategy benefits from adopting Nvidia's reference data-center architecture instead of competing across the whole stack.** [00:29:51] He says MatX chose an Nvidia-compatible footprint so its chips can plug into sites planned for Nvidia racks, letting the startup focus on logic-die and systems co-design while piggybacking on the existing deployment standard.

<!-- episode:f293f09dc3502ac2d969 -->
## 2026-06-18 - [Midjourney Medical, AI Talent Wars 2.0, Jake Paul Joins | Derek Thompson, Rene Haas, Robert Slaughter, Rob Reid, Thais Castello Branco, David Senra, Jake Paul & Geoffrey Woo](https://share.transistor.fm/s/6eb6780f)

- **Arm CEO Rene Haas says agentic AI demand has changed Arm from a pure IP royalty beneficiary into a direct supply-constrained chip-product participant.** [01:00:57] Haas says Arm's AGI CPU launched at the end of March has huge demand, claims 2x performance at the same power as competing parts, and says agents spawn workloads where CPUs do substantial work.
- **Haas says AI is already helping Arm chip design mainly through verification, bug triage, and some bug fixing rather than one-click tapeout.** [01:00:57] He says chip design still depends on hard power, frequency, area, and validation constraints, but AI can automatically prioritize weekend verification failures and sometimes fix issues that engineers previously triaged manually.

<!-- episode:780e4321f53f8b9011ff -->
## 2026-07-08 - [Why AI Infrastructure must evolve for Agent Experience — Akshat Bubna, Modal CTO](https://www.latent.space/p/modal2026)

- **Elastic inference and RL rollouts have extremely bursty compute shapes that traditional Kubernetes was not built for.** [00:11:27] Bubna says Modal customers need rapid regional scaling from roughly 1000 to 1500 GPUs, GPU snapshotting to reduce torch.compile cold starts, and sometimes 100000 sandboxes for RL rollouts.
- **Agent and post-training infrastructure is becoming a memory-movement and networking problem, not just a GPU rental problem.** [00:26:40] The discussion covers sidecars, private IPv6, eBPF controls, RDMA, and about 3 Tbps internal networking; Bubna says moving KV cache and weights between training and inference GPUs has many systems degrees of freedom.

<!-- episode:3a32f702d444a89ffbb1 -->
## 2026-07-02 - [Inside Nemotron & NVIDIA’s AI Lab | Bryan Catanzaro](https://podcasters.spotify.com/pod/show/firstmark/episodes/Inside-Nemotron--NVIDIAs-AI-Lab--Bryan-Catanzaro-e3li7o6)

- **Catanzaro says Nemotron's first job is to help NVIDIA design future accelerated-computing systems in a post-Moore-law world.** [22:19] He says NVIDIA has to deeply understand AI to co-design systems and software, and that specialization now requires understanding rather than simple transistor shrinkage.
- **Nemotron Ultra and Super were pretrained in NVFP4, which Catanzaro frames as an energy and throughput answer to hard compute and power limits.** [35:42] He says FP4 pretraining required invention because training can diverge, but Blackwell Ultra has higher throughput on these formats and much lower memory/energy movement costs.
- **Catanzaro says Blackwell NVL72 was built around MoE inference because dynamic token routing requires fast, low-latency GPU-to-GPU memory access.** [42:31] He says NVL72 lets up to 72 GPUs read and write each other's memory so experts can be partitioned across GPUs while tokens route dynamically through layers.
- **Nemotron's latent MoE compresses routed vectors to reduce NVLink communication and claims four times as many experts for the same inference cost.** [46:00] Catanzaro says latent MoE down-projects token vectors before network transfer, uncompresses them later, saves bandwidth, and expands the expert library at fixed cost.

<!-- episode:837cff33e75593cdf629 -->
## 2026-07-02 - [How Nuclear Will Unlock Energy Abundance with Valar Atomics Founder Isaiah Taylor]()

- **Valar demonstrated AI-compute power coupling by running an NVIDIA Blackwell system directly from its reactor.** [35:01] Taylor says Valar connected a Blackwell chip to the nuclear reactor and hosted a reactor-powered website that tracked uranium atoms split per page view.

<!-- episode:37a3e5ce40dc6af73462 -->
## 2026-07-09 - [AI:AM Highlights: Exploring the J-Space, AI Superforecasters, SambaNova's Chips, & LTX Video Gen](https://www.cognitiverevolution.ai/ai-am-highlights-exploring-the-j-space-ai-superforecasters-sambanova-s-chips-ltx-video-gen/)

- **SambaNova co-founder Kunle Olukotun says inference is primarily a memory-bandwidth and data-movement problem, and claims its RDU architecture can raise resource utilization from the 10% to 20% he attributes to GPUs toward 70% to 80%, enabling a 5x to 10x improvement.** [1:37:37; 1:47:32; 1:50:31] He describes fusing decode into one looping kernel, retaining intermediates in SRAM, and overlapping cross-chip communication with compute instead of repeatedly crossing the HBM boundary; he also says SN50 can scale to 32,000 chips and use wider tensor parallelism than the four-to-eight-chip range he attributes to GPUs.

<!-- episode:c752e1f0326372f9c412 -->
## 2026-07-04 - [Intelligence on the Edge: Liquid AI's Ramin Hasani on the Search for Device-Native Foundation Models](https://www.cognitiverevolution.ai/intelligence-on-the-edge-liquid-ai-s-ramin-hasani-on-the-search-for-device-native-foundation-models/)

- **Hasani said Liquid works with AMD and Qualcomm against their silicon roadmaps, using architecture search to inform future ASIC support and to build foundation-model computation graphs tailored to their processors.** [1:04:05] He described joint work that uses expected hardware constraints to reduce inference cost and identify model operators the next device generation should support.
- **Hasani argued that device-chip vendors will increasingly need to own an efficient foundation-model layer because software-model co-design can offset disadvantages in memory or processor bandwidth and become the basis for application distribution.** [1:16:32] He pointed to Nvidia's Nemotron effort as the model and argued that an optimized default intelligence layer could differentiate otherwise similar PC and device hardware.

<!-- episode:3cb0cb256e144a024dd6 -->
## 2026-07-09 - [Meta Releases Muse 1.1, GPT-5.6 Sol Reactions, New Robot Hand Alert | Eric Seufert, Bernt Børnich, Josh Lindgren, Jeffrey Morgan, Thibault Sottiaux, Sean Frank](https://share.transistor.fm/s/5676e6f2)

- **Sottiaux says a Cerebras-served version of GPT-5.6 Soul reaches roughly 750 tokens per second, about an order of magnitude faster than the default API and product path, at a higher cost.** [01:39:32] He frames the Cerebras deployment as a situational speed tier alongside medium, high, and multi-day Ultra modes, explicitly noting that the performance premium comes at a cost.

<!-- episode:80069c98a38295124c20 -->
## 2026-07-13 - [Apple vs OpenAI, Paramount Threatens to Leave CA, Mark Gurman Joins | Alexis Ohanian, Morgan Housel, Nico Christie & Michael Jarman](https://share.transistor.fm/s/39ef732a)

- **Gurman says memory costs have raised Apple's cost to build each upcoming iPhone by $150 to $200 and forecasts a September retail price increase of roughly the same amount to protect margins.** [01:47:34] He attributes the higher bill of materials to the memory shortage and argues Apple's Vision Pro pricing behavior shows the company is unwilling to absorb the hit to gross margin.

<!-- episode:84e9b288a1a32728cee6 -->
## 2026-07-16 - [🔬 The Lab of the Future Should Feel Like a Data Center — Andy Beam & Rafa Gómez-Bombarelli, Lila Sciences](https://www.latent.space/p/the-lab-of-the-future-should-feel)

- **Lila reports that its reinforcement-learning training runs achieve only about 5% mean FLOP utilization, making utilization a major scaling constraint.** The show notes identify roughly 5% mean FLOP utilization as one of the bottlenecks the guests would remove immediately.

<!-- episode:10e21a6cc7fada9b845d -->
## 2026-07-16 - [OpenAI’s Compute Chief: We Can’t Build Fast Enough | Sachin Katti](https://podcasters.spotify.com/pod/show/firstmark/episodes/OpenAIs-Compute-Chief-We-Cant-Build-Fast-Enough--Sachin-Katti-e3m587t)

- **OpenAI taped out its Jalapeño custom accelerator in about nine months by combining an experienced former-TPU team, Broadcom's ASIC execution, foreknowledge of future model workloads, and AI-assisted design iteration.** [34:29] Katti calls nine months the fastest design-to-tapeout cycle he has seen and says workload visibility short-circuited design choices while AI accelerated optimization experiments; the chip targets tokens per watt.
- **OpenAI's MRC networking protocol is designed to keep 100,000-GPU training clusters running through frequent network-component failures by spraying traffic across multiple paths.** [36:27] Katti says failures cannot be exhaustively enumerated at that scale, so MRC masks them from training jobs by maintaining alternate routes between chips.

<!-- episode:2e34a2048d878e763162 -->
## 2026-07-20 - [The AI Cold War, Odyssey Rips, Tyler Cowen Joins | Danny Yeung, Connor Love, Kahlil Lalji, Tarek Mansour, Tony Zhao](https://share.transistor.fm/s/898ba371)

- **Kalshi has launched an early GPU forward curve intended to turn compute-price expectations into a hedgeable market.** [02:00:06] CEO Tarek Mansour says Kalshi lists weekly GPU-price markets for the next four weeks and monthly markets thereafter using an index that aggregates transaction prices. He says the initial H200 curve is roughly flat, which he interprets as model and hardware innovation keeping pace with consumption, while acknowledging that the underlying benchmark is still being standardized.

<!-- episode:0a353092bee29557d746 -->
## 2026-08-03 - [Why smarter AI models could drive up compute prices 10x](https://www.dwarkesh.com/p/why-compute-might-get-10x-more-expensive-video)

- **Patel argues that annual AI-compute supply growth near 3x has limited room to accelerate and that leading-edge wafer reallocation will soon saturate.** He decomposes growth into about 1.4x from Moore's Law, 1.2x from new fabs constrained by EUV-tool supply through at least 2030, and 1.8x from reallocating leading-edge wafers; he expects AI's N3 share to rise from 60% to 86% by end-2027.

<!-- episode:9a0cf4921142d3474545 -->
## 2026-08-07 - [8 Predictions for the Era of Continual Learning](https://www.dwarkesh.com/p/era-of-continual-learning)

- **Patel argues that full-weight personalization could make continual-learning inference far more economical for large organizations than for individuals.** His back-of-the-envelope estimate puts DeepSeek V3's efficient sparse-model batch above 2,400 concurrent sequences and suggests batch-one personalized serving could incur a compute-efficiency penalty exceeding 100x.

<!-- episode:6c0ee0f6b696c2f3fd90 -->
## 2026-08-03 - [The Inference Engineering Masterclass — Philip Kiely & Ali Taha, Baseten](https://www.latent.space/p/inference-eng)

- **Ali Taha says Baseten found that quantizing more GLM-5.2 layers could preserve better fidelity than a less-quantized alternative when layer-level errors were selected to cancel, while yielding about 20% more throughput.** [00:29:27] Baseten's method selected low-precision layers using predicted error cancellation and compared the resulting logit distribution with the full-precision model using KL divergence; Taha says the result had more layers in NVFP4 and better fidelity than another provider's quant.
- **Philip Kiely estimates that inference software alone can improve performance roughly 2–4x on normalized hardware, while an aggressively tuned stack can approach 10x versus a naive deployment.** [00:34:44] He decomposes the stack into roughly 30–40% gains for each precision step from 16 to 8 and 8 to 4 bits, about 2x from a speculator, about 2x from prefill/decode disaggregation at sufficient scale, and additional double-digit runtime gains; he frames 4–6x as more common than 10x.
- **Taha says identical model weights can exhibit repeated-token collapse on one inference engine or cluster but not another because kernel synchronization bugs and interconnect timing expose hardware-dependent races.** [00:22:30] Baseten observed GLM-family looping that disappeared after changing the TensorRT-LLM image or switching between SGLang and vLLM; a slower inter-node KV-cache path on one cluster could expose a race that another cluster did not.
- **Kiely says a roughly 2.8-trillion-parameter Kimi model occupies about 1.4 TB at NVFP4 and needs GB300-class memory to fit on one eight-GPU node, before reserving space for KV cache.** [01:10:09] He calculates half a byte per parameter and cites 288 GB per GB300 GPU; long context then competes with weights for VRAM, making KV-cache offloading increasingly important for models at this scale.

<!-- episode:ae4a0a34d8b74065dcc9 -->
## 2026-08-06 - [Chasing Trillion-Dollar Companies, Founder Ambition, Token Budgets, and Regulatory Capture with Sarah & Elad]()

- **Gil argues that physical compute scarcity currently reinforces an oligopoly by capping each major lab's rate of progress and keeping competitors closer than they would be with unconstrained compute.** [20:00] He says compute is effectively prorated across the large labs, imposing similar ceilings on progress until the physical constraint lifts.

<!-- episode:1697f085e7cf5416df66 -->
## 2026-08-11 - [🔬The BioAI Phase Shift - Matthew McPartlon & Neil Patil, Chai Discovery](https://www.latent.space/p/chai-discovery)

- **Chai says frontier protein-model workloads are poorly matched to hardware systems optimized primarily for LLM inference: AlphaFold-like pair representations scale as L-squared and batched attention as L-cubed, creating high FLOP and memory-bandwidth costs while molecule-design jobs fan out across many GPUs.** [01:03:13; 01:04:27] Patil calls B300 and Vera Rubin configurations LLM-forward, citing large KV caches and 72-GPU systems; McPartlon describes pair-state, layer-normalization, and SRAM-transfer bottlenecks and says chip suitability differs between training and inference.

<!-- episode:41c79f865a6221e78dec -->
## 2026-08-11 - [Ryan Greenblatt – What happens once AI can automate AI research?](https://www.dwarkesh.com/p/ryan-greenblatt)

- **Greenblatt argues broad transfer into politics or executive persuasion is not required for radical economic transformation if AIs master AI, chip, fab, factory, and robotics R&D.** [00:39:47] He describes that technical bundle as sufficient for an industrial explosion that builds far more compute and automates the future production base, even if agents remain weaker in hard-to-verify social domains.

<!-- episode:24b95606131009e94812 -->
## 2026-08-11 - [Eric Vishria - A Decade of Lessons Investing in Software & Hardware - [Invest Like the Best, EP.486]](https://colossus.com/episode/sandcastles-and-silicon/)

- **Eric Vishria says Fireworks can serve the same stock open-source model on the same Nvidia hardware about 5x faster than a cloud-provider alternative, with an additional multiple in throughput.** [00:03:26] He contrasts externally visible speed with throughput visible in the providers' economics, then notes that specialist inference companies can pay cloud margins and still make money, which he takes as evidence that efficient model serving is not pure commodity resale.
- **Vishria says deep-learning hardware has three primary speed levers—more cores, more core-to-core communication, and memory closer to compute—and Cerebras's wafer-scale design pushed all three toward their practical limits.** [00:31:35] He describes the early design as roughly 450,000 cores and 20 GB of on-chip SRAM, while warning that a logical architecture is only a small fraction of hardware execution and that first silicon can begin near 10% of its simulated roofline.
- **Vishria sees room for a new CPU architecture cycle because LLMs generate code on accelerators but the generated code still runs on legacy CPUs carrying constraints that may no longer be necessary; Benchmark has made an unannounced investment in this thesis.** [00:35:38] He calls this a potential sixth compute generation, distinct from the current accelerator wave, but gives no company name or architectural details.

<!-- episode:1dc93465b4f4bd3344c9 -->
## 2026-08-17 - [Ep. 25 - DYLAN IS HERE, LIVE! | Dylan Patel & Jordan Nanos](https://podcasters.spotify.com/pod/show/jordan-nanos/episodes/Ep--25---DYLAN-IS-HERE--LIVE---Dylan-Patel--Jordan-Nanos-e3ng78i)

- **Patel argues the 2027 alternative-accelerator wave is unlikely to displace incumbent economics soon: startup volumes are tiny beside Nvidia and Google TPUs, many headline orders are only LOIs, and high-interactivity chips must earn enough premium to match roughly $100 million of annual revenue per megawatt.** [24:36; 25:01; 25:44; 27:03] He expects startups to win limited allocations while most cash flow stays with Nvidia or Broadcom; his commercial test is revenue per megawatt, not peak token speed.

<!-- episode:ed374a3cbf0d24f35c21 -->
## 2026-08-18 - [Ben Thompson on Big Tech, China, and the AI Boom Running Out of Money - [Invest Like the Best, EP.487]](https://colossus.com/episode/winners-losers-ai-era/)

- **Thompson argues TSMC's conservative capacity policy transferred overbuild risk to hyperscalers as foregone revenue; the resulting shortage may finally make qualifying Intel or Samsung economical and provide geopolitical diversification that pure insurance spending could not justify.** [38:44; 41:12; 43:54; 44:15] He says TSMC's growth rate fell in 2024 and 2025 before rising in 2026, notes that customers previously avoided Intel because TSMC was easier and better, and expects a major Intel partner announcement as scarcity outweighs qualification pain.

<!-- episode:77e4ba8b8b10a6e4ea71 -->
## 2026-08-22 - [AI in the AM — Weekly Highlights: Relaunch Week (Aug 17–20, 2026)](https://www.cognitiverevolution.ai/ai-in-the-am-weekly-highlights-relaunch-week-aug-17-20-2026/)

- **Lemurian Labs CEO Jay Dawani argues that AI systems are now primarily memory-, network-, communication-, and power-bound, making scheduling software a faster source of effective compute than hand-tuned kernels or new hardware.** [2:07:12; 2:08:18; 2:11:37] Dawani estimates that full hardware-workload coverage would require about 106 billion kernels while only roughly 2,000 engineers can write high-performance kernels and 90% sit in one vendor ecosystem. He claims software can raise utilization three- to tenfold while turbines and power delay new silicon capacity.

<!-- episode:47314c121cc36c401899 -->
## 2026-08-25 - [Neil Movva - Making AI 10x Cheaper - [Invest Like the Best, EP.488]](https://colossus.com/episode/from-transistor-to-token/)

- **Movva argues long-horizon inference can trade away NVLink's latency advantage and exploit non-NVIDIA chips with better FLOPs per operating dollar.** [23:08.900] He says eight-way sharding can consume eight times the hardware for only about four to five times the speed, while expert or pipeline parallelism and communication hiding can make less-connected accelerators useful for throughput.
- **Movva identifies KV-cache memory as a major inference inefficiency and is exploring model and chip designs that offload it from HBM to flash at 1 to 10 tokens per second.** [01:09:19.360] He estimates current KV-cache storage at multiple kilobytes per token and perhaps 10 to 100 times larger than necessary, then describes aggressive flash offload as a divergent SAIL design direction; neither magnitude is benchmarked in the interview.

<!-- episode:a9d533f584aa39a0fa8b -->
## 2026-08-25 - [Dylan Patel – Anthropic & OpenAI will have most of the world’s compute by 2028](https://www.dwarkesh.com/p/dylan-patel-3)

- **Dylan Patel projects that OpenAI and Anthropic will take 40-50% of next year's incremental compute and could control most of the world's usable AI FLOPs by the end of 2028.** [00:00:00] He says the labs already account for about 30% of compute added this year, signed commitments lift their share next year, and new systems deliver roughly 3-5 times the performance per watt of prior generations, making their share of usable FLOPs larger than their share of watts.
- **Patel argues that semiconductor-tool capacity will remain a hard near-term constraint even when downstream AI economics justify much faster expansion.** [00:07:01] He says Carl Zeiss has only recently moved toward planning enough mirrors for about 100 EUV tools annually by 2030, and that expanding every tier of the tool supply chain takes years despite large prospective returns.

<!-- episode:df0a3284607954090268 -->
## 2026-08-26 - [🔬“We have foundation models for language, not for physics” — Anima Anandkumar, Bren Professor of Computing](https://www.latent.space/p/anima)

- **Anandkumar says her collaborators use physics simulators inside an AI inverse-design loop for lithography masks, quantum-dot gates, and nonlinear photonics, turning fast forward models into optimized designs rather than mere predictions.** [01:16:03.304] She describes optimizing inverse-lithography masks and gate or photonic structures against an embedded simulator, but does not provide fabrication results or comparative design metrics in the interview.

<!-- episode:6c9acda833e3c57e8620 -->
## 2026-08-28 - [AI:AM Highlights: Recursive Self-Improvement, Rushed and Vibe-Coded?](https://www.cognitiverevolution.ai/ai-am-highlights-recursive-self-improvement-rushed-and-vibe-coded/)

- **Arm's Mohamed Awad argues that agent workloads elevate the CPU from a background host to the coordination layer for accelerator scheduling, model routing, tool execution, and recursively spawned agents.** [54:45-57:13] Awad says always-on agents can fan out into many subagents, making predictable per-core memory and I/O bandwidth important to accelerator utilization and latency; he frames CPU energy as an opportunity cost because each milliwatt cannot be spent on accelerators or additional users.
- **David Li says China's compute-constrained startup opportunity is shifting toward compact edge-inference modules, with roughly 13-14 companies already targeting local 30B-40B models and DRAM cost as the main current constraint.** [1:01:30-1:06:04] Li reports laptop-sized modules running 30B-40B models at about 70-100 tokens per second and forecasts that, within one to two years, a roughly $2,300 device could run a model adequate for 99% of needs. The vendor count, performance, price, and forecast are interview claims and the automatic transcript may have garbled some technical terms.
- **Q.ANT's CEO presents photonic computing as a data-movement and manufacturability bet: keep operations optical long enough to amortize conversion, then scale on mature-node fabrication rather than compete for leading-edge logic capacity.** [1:36:12-1:45:08] Förtsch says optical memory is unavailable and electro-optical conversion can erase compute-energy gains, so the design chains more work before returning to digital memory; he also says Q.ANT has demonstrated a 90nm pilot and that fabs expressed willingness to convert 45nm or 90nm lines to lithium niobate if demand supports it. All performance and fab-conversion claims are company-reported.

<!-- episode:8c50b0067c5cc3e1ad5b -->
## 2026-08-30 - [Ep. 027 - OpenAI Jalapeño: Better Than Nvidia Blackwell (Accelerators)](https://podcasters.spotify.com/pod/show/jordan-nanos/episodes/Ep--027---OpenAI-Jalapeo-Better-Than-Nvidia-Blackwell-Accelerators-e3o3oms)

- **SemiAnalysis's hosts say Jalapeño A0 beats GB300 and the best public July-era Vera Rubin results across the reported DeepSeek R1, Kimi K2.5, and GPT-OSS tests; on DeepSeek they read the curve as roughly twice GB300's tokens per megawatt at matched interactivity and about 700 versus 350 tokens per second at low batch size.** [00:02:33-00:03:17; 00:09:14-00:12:07; 00:15:23-00:16:37] They explicitly narrow the finding: Jalapeño uses HBM4 while GB300 uses HBM3, Rubin software has likely improved since July, and the single-turn 8K-input/1K-output workload does not exercise AgentX-style prefix caching, routing, or long-context behavior. This is a strong early lab benchmark, not proof of production-wide superiority.
- **The hosts estimate that Jalapeño's likely Samsung HBM4 delivers 15.4 terabytes per second at a 700-watt TDP and roughly twice Rubin's HBM bandwidth per watt.** [00:32:17-00:35:35; 00:39:06-00:40:14] They attribute the result partly to Samsung's 1C DRAM process and SF4 logic base die, contrasting those choices with the processes used by SK hynix and Micron. The supplier attribution and causal comparison are SemiAnalysis's assessment rather than a confirmed disclosure in the episode.
- **The hosts say every published benchmark uses Jalapeño's A0 stepping, while B0 is already in the fab and should add compute throughput at approximately the same power without increasing the already-limited HBM bandwidth.** [00:40:22-00:41:16] They distinguish memory-bound workloads, where B0 may add little, from compute-constrained workloads that should benefit from more FLOPs. This is a specific near-term silicon forecast rather than measured B0 performance.
- **The hosts attribute Jalapeño's efficiency across latency and throughput regimes to smaller systolic arrays that avoid utilization cliffs on skinny or irregular matrix multiplications, combined with careful weight and KV placement, selective synchronization, and sparing use of the network on chip.** [00:50:53-00:53:54] They contrast this design with larger TPU-like arrays that waste resources on low-concurrency mixture-of-experts workloads or awkward matrix dimensions, arguing that Jalapeño combines GPU-like flexibility with a simpler accelerator architecture. This is their mechanistic interpretation of the disclosed design and benchmarks.
