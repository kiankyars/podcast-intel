# Building an AI Guardian for Enterprise with Onyx Security CEO Maxim Bar Kogan

- Podcast: No Priors
- Published: 2026-05-28
- Source: 
- Relevance: 4/5

Onyx CEO Maxim Bar Kogan describes agent security as a new control-plane problem: enterprises want agents to inherit flexible user permissions, but existing identity and API tools cannot infer the agent's intent. Onyx's answer is a hierarchy of small specialized models that cheaply route suspicious actions to more capable oversight agents.

**Why it matters:** As coding and workflow agents gain permission to touch real systems, the security surface shifts from static access control to contextual intent verification. That creates a new vendor category between model labs, enterprise security teams, and the applications agents act on.

## Signals

- **Bar Kogan says human review will not scale as enterprise agent actions grow by 100x to 1,000,000x.** [05:31] _policy_geopolitics_security; observation; high confidence._ He says Onyx trains models and agents to oversee other agents because enterprises cannot stop adoption but need legitimacy checks on exponentially more autonomous actions.
- **Bar Kogan says existing identity, endpoint, and API controls lack enough context to secure autonomous agents.** [09:57] _policy_geopolitics_security; observation; high confidence._ He argues agents need broad user-like permissions for diverse tasks, while current tools cannot tell whether a database deletion is intended or an unrelated hallucinated action.
- **Onyx uses small specialized models to decide when expensive oversight agents should inspect an action.** [14:11] _frontier_labs_models; observation; high confidence._ Bar Kogan says running a full smart agent for every protected agent would be too slow and costly, so Onyx trains small routers that trigger deeper review only when needed.
- **Bar Kogan says AI has sharply lowered the cost of vulnerability discovery and security teams should assume stronger cyber-capable models are coming.** [25:10] _policy_geopolitics_security; forecast; high confidence._ He says automated vulnerability research looked decades away ten years ago but is arriving suddenly, so enterprises need foundational controls rather than relying on gradual model rollouts.
- **Bar Kogan argues independent AI-security vendors are better placed than model vendors to certify agent behavior.** [33:12] _companies_capital_allocation; opinion; medium confidence._ He says security buyers do not want the product vendor certifying its own safety, and enterprises may let Onyx inspect historical behavior they would not share with OpenAI or Anthropic.
- **Bar Kogan expects security products to become agent-facing as security teams themselves become agent-run.** [39:31] _applications_business_models; forecast; medium confidence._ He says Onyx still sells to humans today but is already making systems convenient for agents, where UX means not wasting tokens or context rather than avoiding information overload.

## Changed Views Or Tensions

- Agent security is becoming an intent-context problem that existing identity, endpoint, and API security tools were not designed to solve.
- Independent oversight vendors may have a data-access advantage over model labs because enterprises may share historical agent behavior with security vendors but not with labs.

## Follow-Ups

- Track whether agent-control-plane vendors can prove low false-negative rates without adding prohibitive latency.
- Watch model-lab rollout policies for cybersecurity-capable models and enterprise access programs.
