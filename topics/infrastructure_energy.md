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

<!-- episode:28518f58ac1a89962451 -->
## 2026-07-30 - [The Biggest AI Deployment Nobody Talks About | Samsara CEO Sanjit Biswas](https://podcasters.spotify.com/pod/show/firstmark/episodes/The-Biggest-AI-Deployment-Nobody-Talks-About--Samsara-CEO-Sanjit-Biswas-e3mn7h1)

- **Biswas relays that one large energy utility expects to triple the power it delivers over the next five years after building its existing capacity over 125 years, and attributes 90% of the new demand to data centers.** [57:23] He says the figures came from a utility field visit the prior week and uses them to illustrate customers' inability to build grid infrastructure fast enough; the utility and capacity baseline are not identified.

<!-- episode:24b95606131009e94812 -->
## 2026-08-11 - [Eric Vishria - A Decade of Lessons Investing in Software & Hardware - [Invest Like the Best, EP.486]](https://colossus.com/episode/sandcastles-and-silicon/)

- **Vishria identifies energy as a potential binding constraint on intelligence supply and asserts that China will add about 10 times as much energy as the United States next year.** [00:28:22] His mechanism is that models convert compute into intelligence; if power limits compute while demand stays high, the United States gets fewer tokens or more expensive tokens. The episode does not source or define the 10x comparison.

<!-- episode:56309a23920236fe7754 -->
## 2026-08-11 - [NVIDIA's $500B Compute Deal, Paramount Threatens to Bounce, Record Europe Tourism | Ernie Garcia, Alex Edelson, Nico Simko, Ian McGinley, Conor Sen](https://share.transistor.fm/s/9e551a21)

- **Nvidia CEO Jensen Huang expects AI infrastructure to remain constrained across nearly every layer of the physical supply chain.** [00:03:10] Huang names chips, memory, packaging, systems, photonics, connectors, land, power, and construction labor as simultaneous constraints and ties the pressure to AI beginning to perform productive work globally.

<!-- episode:e1c45cb0cf2c7d28a0e7 -->
## 2026-08-16 - [Let There Be Germicidal Light: This $500 Fixture Could Stop the Next Pandemic, from Complex Systems](https://www.cognitiverevolution.ai/let-there-be-germicidal-light-this-500-fixture-could-stop-the-next-pandemic-from-complex-systems/)

- **AeroLamp chief scientist Vivian Belenky says 222-nanometer far-UVC can provide roughly 30-50 equivalent air changes per hour while protein absorption sharply limits penetration through skin, but she treats eye-dose limits and long-term safety as unfinished work.** [03:19] Belenky explains that pathogens' nucleic acids and proteins absorb the light and that the roughly 20-micron dead outer skin layer absorbs almost all of it. Eyes lack that barrier, receive protection mainly from anatomy and shallow tissue absorption, and have only limited long-duration study data.
- **Gurevich and Belenky say one AeroLamp covers about 250 square feet, a classroom generally needs two to four fixtures, the current fixture price is about $500, and professional installation can add roughly the hardware cost again.** [20:04] They describe dozens of lamps for a school and hundreds for a university. Belenky gives installation-cost parity as a conservative rule of thumb and says the present bulbs retain 70% output for at least 10,000 hours, or roughly five to six years at weekday occupational use.
- **Belenky reports preliminary 90% transmission suppression in a South African tuberculosis-ward animal study, even though she estimates TB is about ten times more resistant to far-UVC than flu or coronavirus.** [27:11] She says guinea pigs were exposed to ward patients only through shared air and monitored for infection. She also cautions that respiratory viruses do not necessarily transmit through the air in exactly the same way, so the result is encouraging rather than directly generalizable.

<!-- episode:e1a3b37534ebf5a4d408 -->
## 2026-08-04 - [Bending Spoons Buys Airtable, Snap Rips, Ads in BMW | Grace Li, Samir Kaji, John Quinn, Nikhil Reddy, Art Levy & Russell Kaplan, Brendan Carr](https://share.transistor.fm/s/b35b3f03)

- **Quinn expects some AI data-center projects to require workouts or reorganizations because their SPV, tenant, bond, securitization, and private-credit structures can transmit a default across the financing stack.** [01:41:14; 01:42:05] He said not every contracted project will arrive on time and relayed that one neocloud called electricians its largest constraint, alongside shortages of power, chips, and compute.

<!-- episode:97a3346678ba03fddb55 -->
## 2026-08-20 - [Ep. 026 - PJM's $12B Modeling Mistake Is Hitting Ratepayers Again (Datacenter, Energy) | Robert Boswell, Jordan Nanos](https://podcasters.spotify.com/pod/show/jordan-nanos/episodes/Ep--026---PJMs-12B-Modeling-Mistake-Is-Hitting-Ratepayers-Again-Datacenter--Energy--Robert-Boswell--Jordan-Nanos-e3nkns1)

- **Boswell estimates PJM could have avoided $12 billion of the $63 billion spent across its last four capacity auctions: $7 billion in 2025-26 and $5 billion in 2026-27, both from crediting existing winter capability more accurately.** [07:39; 09:44; 11:50] He says PJM effectively applies summer capability year-round and extrapolates historical cold-weather outages even after mandated winterization, understating cold-air output and reliability. Because the supply curve is near vertical, his modeled quantity correction produces an unusually large reduction in the uniform clearing price; the estimate is not independently audited in the episode.
- **Boswell argues PJM is manufacturing part of its scarcity by running auctions only one to two years ahead while its interconnection process is slow, leaving too little time for new generation to qualify and shifting the supply curve left.** [05:15; 08:57] He says the auctions are intended to provide roughly three years of warning, which he already considers tight, but recent delays compressed the interval further. New plants therefore cannot arrive in response to the capacity signal even as forecast demand rises.
- **Boswell explains that PJM's capacity auction can magnify small modeling errors because every cleared generator, including fully paid-off existing plants, receives the marginal systemwide price rather than its own bid.** [03:48; 14:41] Boswell explains that the auction pays for the ability to generate, not delivered electricity, and gives the example of a resource bidding $5 per MW-day still receiving $300 per MW-day if the last required unit sets that price. A small quantity change at the steep end of supply can therefore reprice a very large installed base.
- **For 2028-29, PJM projects a 6.8 GW capacity shortfall, but Boswell's seasonal-output and winterization adjustments reduce the estimated need to about 3 GW, implying the planned emergency auction could overprocure roughly 3.8 GW.** [26:46; 27:24] Boswell attributes part of the official gap to price-capped auctions that did not procure the target quantity. He says recognizing higher winter output and improved cold-weather reliability would eliminate more than half of the remaining modeled deficit.
- **Boswell argues that data-center load can lower rather than raise average electricity costs if it finances incremental supply and improves utilization of a high-fixed-cost grid.** [19:23; 40:04; 42:22] He points to batteries, bring-your-own or backup generation, and load flexibility as ways to pair demand with supply, and says data centers may accept paying more than a pro-rata share in exchange for being connected. He presents this as the upside case, not evidence that PJM has achieved it.

<!-- episode:47314c121cc36c401899 -->
## 2026-08-25 - [Neil Movva - Making AI 10x Cheaper - [Invest Like the Best, EP.488]](https://colossus.com/episode/from-transistor-to-token/)

- **Movva says SAIL can aggregate small data centers that mainstream buyers reject by trading reliability and tail latency for lower cost.** [53:19.940] He describes sites without backup generators or redundant fiber, says SAIL would buy 95% uptime and perhaps 80% at the right price, and relies on an asynchronous control plane to move long-running jobs after failures.

<!-- episode:a9d533f584aa39a0fa8b -->
## 2026-08-25 - [Dylan Patel – Anthropic & OpenAI will have most of the world’s compute by 2028](https://www.dwarkesh.com/p/dylan-patel-3)

- **Patel forecasts that labs would need to pay roughly $25-50 million per megawatt to absorb 70% or more of incremental compute in 2028, shifting more surplus toward owners of already-financed capacity.** [00:13:08] He contrasts ordinary compute transacting near $10-15 million per megawatt with the premium available to balance-sheet-backed builders such as SpaceX and Meta, which can wait to lease completed capacity to the highest-value user.

<!-- episode:8c50b0067c5cc3e1ad5b -->
## 2026-08-30 - [Ep. 027 - OpenAI Jalapeño: Better Than Nvidia Blackwell (Accelerators)](https://podcasters.spotify.com/pod/show/jordan-nanos/episodes/Ep--027---OpenAI-Jalapeo-Better-Than-Nvidia-Blackwell-Accelerators-e3o3oms)

- **The hosts argue that Jalapeño weakens Nvidia's kernel-software moat but does not yet reproduce Nvidia's systems moat: OpenAI still has to move from engineering racks to a 100-megawatt fleet with manufacturing, deployment, monitoring, and reliability at scale.** [00:18:18-00:25:49] They distinguish faster AI-assisted bring-up from Nvidia's purchasing, support, logistics, and supply-chain ecosystem, and point to Broadcom and Celestica as partners with TPU-scale production experience. The 100-megawatt target is the next proof point, not demonstrated operating capacity.

<!-- episode:3fe8ed5694552d2c5742 -->
## 2026-08-31 - [WE'RE BACK, Meta Addiction, Tim Cook's Last Day | Jordan Schneider, Robert Mendelsohn & Eric Olszewski, Billy Thalheimer, Aaron Cannon, Stephen Balaban](https://share.transistor.fm/s/1b7b60f3)

- **Actinide's co-founders said the company became the first startup to enrich uranium and produce research quantities of HALEU by modernizing Calutron electromagnetic separation with superconducting magnets, while acknowledging that commercial HALEU still requires substantial technical and regulatory scaling.** [01:35:19; 01:36:16; 01:39:51; 01:40:10] The team said superconducting magnets address the legacy Calutron's dominant energy-efficiency problem and that the principle is the only separation method besides centrifuges proven at scale. They reported a few commercial deliveries of a roughly $30,000-per-gram medical isotope to a customer transcribed as Oklo Isotopes, but said HALEU customer discussions had only just begun after leaving stealth.
- **Lambda CEO Stephen Balaban said most new AI data centers use closed-loop dry cooling, and that Lambda's 10,000-GPU Kansas City facility used about 300 construction workers, supports 50 permanent jobs with many paying more than $100,000, and will pay at least $47 million in property taxes over five years.** [02:06:07; 02:08:25; 02:10:35] Balaban contrasted closed-loop systems with older evaporative cooling and supplied the Kansas City figures as a company-specific example of local benefits. The episode did not identify the facility's GPU model, load, water and power measurements, tax agreement, or sources supporting his industry-wide claim.

<!-- episode:d1dd51069537abbd8cde -->
## 2026-09-01 - [Sarah Guo - Funding the Frontier - [Invest Like the Best, EP.489]](https://colossus.com/episode/no-priors-just-conviction/)

- **Guo says an infrastructure leader at an unnamed hyperscaler told her that nothing under development would add enough capacity to move the company's needle before 2030, while industry planning is already focused on 2032-scale compute.** [00:15:58-00:17:48] She identifies sufficient natural gas, data-center siting, nuclear construction, regulation, community acceptance, physical supply chains, and tacit labor knowledge as the binding constraints rather than a lack of technical ideas or private capital. The 2030 statement is second-hand and the hyperscaler is not identified.
