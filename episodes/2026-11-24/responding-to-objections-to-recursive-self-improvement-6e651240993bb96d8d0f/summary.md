# Responding to objections to recursive self-improvement

- Podcast: Dwarkesh Podcast
- Published: 2026-11-24
- Source: https://www.dwarkesh.com/p/rsiobjections
- Relevance: 4/5

Dwarkesh Patel revisits his forecast for automated AI research with Max. His own pretraining comparison, a worked example of partial automation and a counterexample involving unreliable experiment records make the forecast easier to test. Patel still puts his median for fully automating the best AI researchers in 2028.

**Why it matters:** A lab deciding whether to buy more researcher inference or more experiment compute needs to know where its researchers spend time, how long experiments take and how often results survive verification. Patel gives a way to ask those questions without assuming that every additional token produces a useful experiment.

## Signals

- **Patel reports that newer pretraining data explained more improvement than newer architectures in his comparison of public corpora and architectures from 2019 to 2026.** [00:06:29; 00:06:42; 00:06:54; 00:07:11] _frontier_labs_models; observation; medium confidence._ He attributes much of the dataset improvement in his study to filtering and synthetic-data methods that ML researchers could iterate on themselves. This makes data preparation a candidate for research automation. The episode gives no effect sizes, model scales or full experimental design, leaving the result’s applicability to frontier runs open.
- **Patel’s worked example puts the payoff from research automation in the share of baseline work it covers.** [00:49:49; 00:50:49; 00:51:05; 00:51:10; 00:51:30] _agents_developer_tools; inference; medium confidence._ If assisted work runs 50 times faster, accelerating 90% of baseline work time yields about 8.5 times total speed. At 99% coverage the same calculation yields about 34 times. These are illustrations using Amdahl’s law. Actual gains depend on coordination, human review and which tasks sit on the critical path.
- **Patel identifies a failure mode for automated research: plausible but inaccurate experiment records can consume the time saved by agents.** [00:38:10; 00:38:49; 00:39:00] _frontier_labs_models; inference; medium confidence._ He imagines an agent reporting a favorable loss curve for a run that actually performed differently. Subsequent work follows a false lead, and relying on equally unreliable agents for debugging compounds the cost. He presents this as an objection to his forecast. Independently reproducible logs and the time spent verifying results would help test it.
- **Patel’s forecast for an automated lab still depends on how much more information it can extract per GPU experiment.** [00:57:27; 00:57:53; 00:58:03; 00:58:56; 01:00:16] _semiconductors_compute; forecast; medium confidence._ He suggests three to six years of algorithmic progress per calendar year in his scenario. Faster researchers could scrutinize loss spikes and design better follow-up runs while experiments continue to take real time. The forecast depends on returns to that extra analysis. He also accepts that slowing compute growth could slow progress if research automation arrives late.

## Changed Views Or Tensions

- Patel identifies unreliable research records as a potential constraint on his own acceleration forecast. The cost of checking results belongs in an estimate of researcher productivity.

## Follow-Ups

- Look for the full corpus-by-architecture experiment, including datasets, scaling regimes and held-out tests.
- Track elapsed time to a replicated research improvement alongside token use, experiment compute, and human review time.
