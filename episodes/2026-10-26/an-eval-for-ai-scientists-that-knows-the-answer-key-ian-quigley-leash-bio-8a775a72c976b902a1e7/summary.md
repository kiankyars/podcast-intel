# ⚡ An Eval for AI Scientists That Knows the Answer Key - Ian Quigley, Leash Bio

- Podcast: Latent Space
- Published: 2026-10-26
- Source: https://www.youtube.com/watch?v=vhPCo-8K78U
- Relevance: 3/5

This short follow-up adds decision-level results to Leash Bio's experimental sandbox already covered on October 15. Ian Quigley describes a cold-start, 100-molecule search task, roughly 90,000 rollouts at recording, and a pattern in which stronger models abandon unproductive chemical neighborhoods sooner. He also reports that withholding molecule information impairs choices, while explicitly separating this use of feedback from weight updates. The Minos release was published October 14; this episode is a later discussion of it, not a new launch.

**Why it matters:** A fully measured search space can evaluate the quality of decisions an agent did not take, not just its final score. That makes Minos useful for diagnosing wasted experimental budgets and testing whether model improvements reflect better adaptation to evidence. The remaining question is whether language-model agents outperform matched search baselines and transfer beyond the fixed measured catalog; the interview does not establish either result.

## Signals

- **Quigley reports that stronger models leave unproductive chemical neighborhoods sooner in Minos; a fully measured landscape lets evaluators distinguish useful exploration from merely moving around.** [02:24; 03:00; 03:28; 04:05; 04:41; 05:06] _agents_developer_tools; observation; medium confidence._ At 02:24–03:04 he describes providing only a target and molecular catalog, allowing 100 molecule tests, and accumulating about 90,000 rollouts. At 03:28–05:24 he says known outcomes across the entire landscape expose early stopping, repeated tests, and persistence in poor neighborhoods; stronger models move more overall and particularly leave bad regions faster. He says the cause is not yet understood. The October 14 [Minos write-up](https://leashbio.substack.com/p/making-reality-replayable) corroborates this qualitative pattern. The increment over the earlier sandbox account is a specific search-policy diagnostic, not proof of new drug discovery or an isolated causal explanation of model intelligence.
- **Quigley reports that removing molecule information worsens agents' subsequent choices, supporting use of task evidence within a run; he does not demonstrate weight learning, superiority to Bayesian search, or transfer to new biology.** [10:58; 11:12; 11:25; 11:42; 15:05] _frontier_labs_models; observation; medium confidence._ At 10:58–11:24 he describes iterative molecular choices and says decisions suffer when molecule information is removed, then explicitly corrects learning to using information because model weights are unchanged. At 11:25–11:49 he says Leash has not tried the interviewer's proposed Bayesian-search baseline; the belief that the landscape is too spiky is an expectation, not a comparison result. At 15:05–15:17 he says whether reinforcement-learning progress in these environments transfers to new biology remains unknown. No ablation effect size or matched baseline score is supplied in the interview.

## Changed Views Or Tensions

- The update strengthens the case for Minos as an agent-decision evaluation environment: known counterfactual outcomes expose when a model should abandon a search neighborhood. It does not establish a general scientific-reasoning mechanism.
- The information-removal result is evidence that agents use task inputs during an episode; controlled reinforcement-learning gains, matched non-LLM comparisons, and transfer to unmeasured biology remain separate claims requiring evidence.

## Follow-Ups

- Use the [Minos preprint](https://github.com/Leash-Labs/minos-paper/blob/trunk/Minos_Leash.pdf) and released [environments and traces](https://strelka.leash.bio/) to quantify the information ablation, per-target variability, repeated-query waste, and exploration decisions under an identical experimental budget.
- Compare cold-start agents with random, heuristic, and Bayesian or active-learning search at matched query and compute budgets. Keep training targets and chemical libraries separate from held-out tests, then test transfer beyond the measured catalog.
- Verify exact model identifiers and run settings against the published benchmark before using the interview's garbled captioned model rankings. Keep the podcast's roughly 90,000 rollouts at recording separate from the October 14 article's roughly 100,000 trajectories.
