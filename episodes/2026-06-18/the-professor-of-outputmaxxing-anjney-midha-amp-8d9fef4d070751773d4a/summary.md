# The Professor of Outputmaxxing — Anjney Midha, AMP

- Podcast: Latent Space
- Published: 2026-06-18
- Source: https://www.latent.space/p/anj
- Relevance: 5/5

AMP founder Anjney Midha argues that the AI scaling bottleneck is not just GPU acquisition but realized output from clusters, data centers, teams, and capital structures. The episode is unusually dense on compute utilization targets, AMP's grid model, gigawatt-scale demand, community constraints, non-Nvidia chip deployment, and why Anthropic's coding lead may have come from cultural and resource discipline rather than a random lucky break.

**Why it matters:** The strongest implication is that frontier AI infrastructure should be underwritten like a utilization and coordination problem, not just a raw capex problem. If Midha's view is right, the winners in AI infrastructure may be teams that raise MFU, pool burst demand, align community incentives, and shorten trust boundaries between labs, chip designers, and data-center operators.

## Signals

- **Midha says best-in-class AI clusters should be near 95% node utilization and 60-70% MFU, while many single-tenant clusters fall short.** [00:00:09] _infrastructure_energy; observation; high confidence._ He says Google treated 95% node utilization as an outage threshold, distinguishes node allocation from model FLOPs utilization, and argues wasted utilization compounds quickly when clusters are scaled too fast.
- **Midha says data-center community backlash may put a material share of U.S. AI data-center projects at risk unless local incentives improve.** [00:03:17] _infrastructure_energy; opinion; medium confidence._ He cites an estimate that up to 20% of U.S. data centers this year may face community-support risk and says compute buyers would pay a higher hourly rate if the increment reduced local electricity bills or otherwise created visible community benefit.
- **Midha frames AMP as an independent system operator for compute, pooling supply and demand rather than owning a vertically integrated cloud.** [00:06:07] _infrastructure_energy; observation; high confidence._ He says AMP is aggregating trusted supply and demand at about 1.3GW scale over four years, with labs guaranteed base load while burst jobs are scheduled through interruptible demand and dynamic priority mechanisms similar to Google's internal systems.
- **Midha says AMP has started to secure 1.2GW of demand and estimates its teams need roughly 6GW of spike capacity over four years.** [00:14:42] _companies_capital_allocation; forecast; medium confidence._ He equates 1.2GW to roughly $40B of cloud spend, says the full amount is not yet secured, and describes the steady-state target as 1.2GW of base-load capacity plus much larger burst capacity.
- **Midha argues that unpublished DeepMind research creates a market failure when strong work is embargoed or never productized.** [00:12:41] _frontier_labs_models; opinion; medium confidence._ He says DeepMind papers can face internal business review and long-lived embargoes, creating adverse selection in what reaches the public and motivating AMP Foundry to back researchers leaving existing labs.
- **Midha says MatX's non-Nvidia accelerator strategy benefits from adopting Nvidia's reference data-center architecture instead of competing across the whole stack.** [00:29:51] _semiconductors_compute; observation; medium confidence._ He says MatX chose an Nvidia-compatible footprint so its chips can plug into sites planned for Nvidia racks, letting the startup focus on logic-die and systems co-design while piggybacking on the existing deployment standard.
- **Midha says Anthropic's coding success came from long preparation and a day-one P0 focus on coding as a path to AGI.** [00:46:17] _agents_developer_tools; opinion; medium confidence._ He rejects a pure lucky-break explanation, says Anthropic operated with much higher efficiency than OpenAI, and argues scarce resources forced the company to define coding as the core capability that could accelerate computer work broadly.

## Changed Views Or Tensions

- Compute scarcity should be judged by realized utilization and scheduler design, not just headline GPU inventory.
- AI data-center acceptance may require local economic participation rather than generic job-creation arguments.
- Non-Nvidia chip startups may gain more by adopting Nvidia deployment standards than by trying to replace the entire rack and data-center stack.

## Follow-Ups

- Track whether AMP publicly confirms secured 2026 capacity, total base-load contracts, and the claimed 1.2GW demand target.
- Compare Midha's 60-70% MFU best-in-class range with frontier-lab and neocloud utilization disclosures.
- Watch whether MatX and other accelerator startups converge on Nvidia-compatible physical deployment standards.
