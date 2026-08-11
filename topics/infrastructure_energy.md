# Infrastructure Energy

Data centers, power, cooling, networking, capital expenditure, and physical constraints.

<!-- episode:1bf240c7e8316a75d9c2 -->
## 2026-06-04 - [The Rise of the Full-Stack Builder and Hyper-Leveraged Generalist with Microsoft CEO Satya Nadella]()

- **Nadella says Microsoft built more Azure capacity in 15 months than in its first 15 years.** [00:29:00] He uses Azure networking as an example of teams reconceptualizing work around an agentic system called Miles and asking for tokens rather than headcount.

<!-- episode:4aad641f1dcb3066c5d8 -->
## 2026-06-04 - [Alex Imas and Phil Trammell – What remains scarce after AGI?](https://www.dwarkesh.com/p/alex-imas-phil-trammell)

- **The guests treat unsaturated compute demand as the central variable behind rising capital share.** [00:00:00] They discuss H100 rental prices rising despite better technology, using that as evidence that smarter models can raise the opportunity cost of compute.

<!-- episode:f9b0862f3eccf09711fd -->
## 2026-06-02 - [GitHub's plan for Agents — Kyle Daigle, GitHub](https://www.latent.space/p/github)

- **GitHub's reliability bottleneck is now Actions CPU, permissions databases, monorepos, and job queues rather than a single obvious service.** [00:51:18] Daigle says more agents and PRs mean more builds and CPUs, while permissioning in MySQL One, bigger repos, and job-queue changes are forcing deeper rewrites.

<!-- episode:64782ec72ea2e1cdbf5b -->
## 2026-05-28 - [State of Enterprise AI 2026: Aaron Levie on Tokenmaxxing, Rise of Headless, and AI-Proofing Your Job](https://podcasters.spotify.com/pod/show/firstmark/episodes/State-of-Enterprise-AI-2026-Aaron-Levie-on-Tokenmaxxing--Rise-of-Headless--and-AI-Proofing-Your-Job-e3k0gsp)

- **Levie says frontier-token prices are not falling like normal compute because the industry compressed a decade of rollout into roughly 12-18 months.** [11:34] He argues bigger models, hardware scarcity, capacity constraints, and lab/provider pricing power have delayed the usual scale-driven cost declines.

<!-- episode:c1cb4aa5e57acfab0aae -->
## 2026-05-28 - [The Age of Async Agents — Cognition's Walden Yan & OpenInspect's Cole Murray](https://www.latent.space/p/cognition)

- **Yan says Cognition had to build deep VM and filesystem infrastructure because ordinary cloud VMs were not built for repeated agent suspend-resume cycles.** [00:47:48] He says raw EC2-style machines could take about 10 minutes to sleep and wake, network filesystems made grep slow, and Cognition built diff-proportional disk formats to speed boot.

<!-- episode:096034669fedb0cbc4bb -->
## 2026-06-10 - [Cloudflare CEO Predicts AI Agents Will Outnumber Humans 1,000-to-1](https://share.transistor.fm/s/b5f0e80c)

- **Prince says container-based agent execution would exhaust implausible amounts of global CPU capacity.** He estimates one containerized agent for each of 100 million US knowledge workers would require about half of all CPU capacity produced today, and global deployment would be tens of times larger than existing CPU and GPU capacity.
- **Prince says Cloudflare's edge inference thesis has shifted toward long-running handoffs from devices to the network.** He says Cloudflare now runs inference at the edge across more than 350 cities, but he expects less than his prior 50% on-device assumption because many agent tasks will run for minutes, hours, or days.

<!-- episode:01c3d87bcabde7e7204a -->
## 2026-06-15 - [Freedom 250 Recap with Bo Nickal, The Hand Anthropic Was Dealt, Fox Buys Roku | Bo Nickal, Gavin Baker, Leif Abraham, Aaron Ginn, Rafael Vivas](https://share.transistor.fm/s/07ad1b46)

- **Gavin Baker frames SpaceX's near-term equity story around terrestrial compute buildout and monetized gigawatts.** [30:24] He says the next year depends on how quickly SpaceX can bring compute online, cites a Google deal at about $50 billion per gigawatt, and says energizing two to four gigawatts would be a major revenue driver.
- **Hydra Host CEO Aaron Ginn says Hydra is an asset-light neo-cloud software company rather than a GPU owner.** [01:46:44] He says the $100 million Series A will not be used to buy GPUs, claims Hydra manages GPUs across nearly two dozen countries and close to 60 data centers, and says several billions in contracts have been signed.

<!-- episode:bd4abdfdd12e2dd63579 -->
## 2026-06-15 - [Ep. 015 - DG Matrix Explains 800V DC vs Legacy AC Distribution (Datacenter, Energy) | Jordan Nanos, Jeremie Eliahou Ontiveros, Nicolas Bontigui, Haroon Inam](https://podcasters.spotify.com/pod/show/jordan-nanos/episodes/Ep--015---DG-Matrix-Explains-800V-DC-vs-Legacy-AC-Distribution-Datacenter--Energy--Jordan-Nanos--Jeremie-Eliahou-Ontiveros--Nicolas-Bontigui--Haroon-Inam-e3kqvco)

- **Dan says GPU server pricing is being driven more by demand than by memory cost inflation alone.** [24:36] He estimates memory added only 5-10% to average server cost while market price increases exceeded that, and he describes large AI labs signing 4-5 year, hundreds-of-megawatts off-take contracts.

<!-- episode:83a81550380d0d9c9981 -->
## 2026-06-18 - [The Neocloud Boom: State of AI Compute 2026 | Stephen Balaban](https://podcasters.spotify.com/pod/show/firstmark/episodes/The-Neocloud-Boom-State-of-AI-Compute-2026--Stephen-Balaban-e3kut0h)

- **Balaban says the AI compute market remains generally underbuilt because scaling laws and expanding AI use cases keep widening demand.** [07:00] He ties demand growth to LLMs moving from assistants and search substitutes into code generation and broader software work, and says efficiency gains would likely be spent on more tokens rather than lower total compute demand.
- **Balaban identifies the broad industry bottleneck as powered land and data center shell, not simply GPU availability.** [10:44] He describes the key constraint as land entitled for utility megawatts plus mechanical, electrical, plumbing, and shell buildout, while noting local projects can hit narrower bottlenecks such as generators or UPS systems.
- **Balaban gives a capital-stack estimate in which servers dominate gigawatt-scale AI factory cost.** [23:45] He estimates power generation at roughly $2-3B per gigawatt, the data center at roughly $10-15B per gigawatt, and servers at roughly $35-45B per gigawatt.

<!-- episode:8d9fef4d070751773d4a -->
## 2026-06-18 - [The Professor of Outputmaxxing — Anjney Midha, AMP](https://www.latent.space/p/anj)

- **Midha says best-in-class AI clusters should be near 95% node utilization and 60-70% MFU, while many single-tenant clusters fall short.** [00:00:09] He says Google treated 95% node utilization as an outage threshold, distinguishes node allocation from model FLOPs utilization, and argues wasted utilization compounds quickly when clusters are scaled too fast.
- **Midha says data-center community backlash may put a material share of U.S. AI data-center projects at risk unless local incentives improve.** [00:03:17] He cites an estimate that up to 20% of U.S. data centers this year may face community-support risk and says compute buyers would pay a higher hourly rate if the increment reduced local electricity bills or otherwise created visible community benefit.
- **Midha frames AMP as an independent system operator for compute, pooling supply and demand rather than owning a vertically integrated cloud.** [00:06:07] He says AMP is aggregating trusted supply and demand at about 1.3GW scale over four years, with labs guaranteed base load while burst jobs are scheduled through interruptible demand and dynamic priority mechanisms similar to Google's internal systems.

<!-- episode:cf0acaaad1b675d62b16 -->
## 2026-06-20 - [Dean Ball, on Joining OpenAI: New Power Centers, Frontier AI Policy, & Main Character Energy](https://www.cognitiverevolution.ai/dean-ball-on-joining-openai-new-power-centers-frontier-ai-policy-main-character-energy/)

- **Ball views frontier AI as already approaching an implicit government-backstop regime because AI infrastructure now finances nationally important supply-chain and energy IP.** [1:46:19] He points to interlocking lab, VC, semiconductor, energy, SMR, fusion, battery, cooling, and water-treatment commitments, and says a modest growth slowdown could trigger balance-sheet stress that becomes a public-interest problem.

<!-- episode:780e4321f53f8b9011ff -->
## 2026-07-08 - [Why AI Infrastructure must evolve for Agent Experience — Akshat Bubna, Modal CTO](https://www.latent.space/p/modal2026)

- **Modal is operating as a capital-light supercloud across 17 providers rather than building its own data centers.** [00:24:08] Bubna says Modal's capacity pool spans 17 cloud providers, with its own reliability layer so customers can use capacity that would be hard to operate directly when GPUs fail or providers vary in reliability.

<!-- episode:837cff33e75593cdf629 -->
## 2026-07-02 - [How Nuclear Will Unlock Energy Abundance with Valar Atomics Founder Isaiah Taylor]()

- **Taylor says Valar is already running a live 100 kW reactor and collecting empirical data, not just producing simulation-backed paper reactors.** [10:37] He says the company is making 100 kW and splitting about 10^17 atoms per second in the reactor while recording operational data.
- **Valar frames nuclear economics as a manufacturing tick-rate problem rather than a fuel-cost problem.** [24:36] Taylor says first atom split took 2 years and 4 months, the next reactor took about 7 months, and the target is eventually new reactors turning on every few minutes because uranium fuel is already cheap.
- **Valar's gigasite strategy assumes cheap power with land and fiber will pull data-center load to the power source.** [51:43] Taylor says Valar can put a gigawatt on the ground on its own timing, then asks whether a data center will come if there is power, land, and fiber; his answer is yes.

<!-- episode:08455bb0b941050e2953 -->
## 2026-07-06 - [XBOX Layoffs, "Manual" Ferrari, Circle K Lottery Dispute | Baiju Bhatt, Daniel English, Michele Catasta](https://share.transistor.fm/s/5fcc7e7e)

- **Daniel English says AI-era density lets Legacy Investments target 50 megawatts in roughly 40,000 square feet of a converted Chicago exchange building, versus about 4 megawatts in the same footprint in 2010.** [01:31:17] English says power, fiber, and latency now dominate site selection; he describes 30 megawatts as small today, compared with 5 megawatts as a good facility and 30 megawatts as peak scale around 2010.

<!-- episode:f74ab0c9a2e627acb665 -->
## 2026-07-02 - [SpaceX Phone, U.S. Stake in OpenAI, Jersey Mike's IPO | Andrew Collins, Vipul Ved Prakash, Isaiah Taylor, Dean Ball, Rob Toews, Tuhin Srivastava](https://share.transistor.fm/s/eebe04f7)

- **Valar Atomics founder Isaiah Taylor said the Ward 250 produced electricity for the first time, making Valar the first nuclear startup to generate electricity, and that the reactor powered an NVIDIA Spark.** [01:02:46] Taylor said Valar progressed from a bare site after the May 2025 executive orders to criticality, thermal operation, and electricity production outside a national lab before its July 4 target; he also argued that one truckload of uranium can supply a year of fuel where gas projects face turbine and pipeline constraints.

<!-- episode:84e9b288a1a32728cee6 -->
## 2026-07-16 - [🔬 The Lab of the Future Should Feel Like a Data Center — Andy Beam & Rafa Gómez-Bombarelli, Lila Sciences](https://www.latent.space/p/the-lab-of-the-future-should-feel)

- **Lila is designing its lab as data-center-like infrastructure: instruments are graph nodes, automated transport acts as an interconnect, and experiments are dispatched through a queue, while humans remain below the API boundary when automation is uneconomic.** The source maps instruments, magnetic plate transport, and orchestration to nodes, a PCI-like bus, and a Slurm-style scheduler, emphasizing flexibility over maximum fixed-workflow throughput.

<!-- episode:0a353092bee29557d746 -->
## 2026-08-03 - [Why smarter AI models could drive up compute prices 10x](https://www.dwarkesh.com/p/why-compute-might-get-10x-more-expensive-video)

- **Patel says the secure, large-scale compute tranche frontier labs need is already priced well above headline spot markets.** He cites reports that Google pays SpaceX $900 million per month for 110,000 blended GB200 and GB300 GPUs, about twice spot pricing, while spot itself had risen more than 40% from its February trough.
