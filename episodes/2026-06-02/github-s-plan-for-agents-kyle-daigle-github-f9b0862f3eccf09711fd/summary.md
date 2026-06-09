# GitHub's plan for Agents — Kyle Daigle, GitHub

- Podcast: Latent Space
- Published: 2026-06-02
- Source: https://www.latent.space/p/github
- Relevance: 5/5

GitHub COO Kyle Daigle describes how agent-generated work is forcing GitHub to rethink infrastructure, trust, Copilot, and enterprise context. The most concrete signal is scale: GitHub went from about 1 billion commits in 2025 to roughly 275 million commits per week, with growth still accelerating, creating bottlenecks in Actions compute, permissioning, monorepos, and legacy databases.

**Why it matters:** GitHub is a live sensor for software agent adoption. Its infrastructure failures, trust-model changes, and Copilot product shifts show what happens when code production moves from human-speed collaboration to agent-speed automation.

## Signals

- **Daigle says GitHub commit volume is on pace for roughly 14x year-over-year growth.** [00:50:32] _agents_developer_tools; observation; high confidence._ He cites about 1 billion commits in 2025 and around 275 million commits per week in 2026, with growth still speeding up.
- **GitHub's reliability bottleneck is now Actions CPU, permissions databases, monorepos, and job queues rather than a single obvious service.** [00:51:18] _infrastructure_energy; observation; high confidence._ Daigle says more agents and PRs mean more builds and CPUs, while permissioning in MySQL One, bigger repos, and job-queue changes are forcing deeper rewrites.
- **GitHub's internal AI rollout favors small micro-skills over brittle mega-skills.** [00:07:09] _agents_developer_tools; observation; high confidence._ Daigle says GitHub gives employees CLI access plus context across GitHub, Teams, email, Slack, and WorkIQ MCP, while shifting to atomic skills that do one thing well.
- **Daigle frames agent PR review as a social-trust problem, not just a verification problem.** [00:33:57] _policy_geopolitics_security; inference; high confidence._ He says vouching, sponsors, age, accepted PR history, and project-specific heuristics matter because stars and passive signals are gamifiable by attackers.

## Changed Views Or Tensions

- Agent adoption is already creating infrastructure load that looks qualitatively different from ordinary user growth.
- The next PR workflow may need project-specific trust heuristics, not one universal GitHub-controlled standard.

## Follow-Ups

- Track GitHub availability over the next three months against Daigle's claim that material rewrites should reduce outages.
- Watch whether GitHub exposes first-class trust/vouching primitives for agent-generated PRs.
