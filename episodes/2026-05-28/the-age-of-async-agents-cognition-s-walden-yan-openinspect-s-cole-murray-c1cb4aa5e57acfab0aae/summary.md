# The Age of Async Agents — Cognition's Walden Yan & OpenInspect's Cole Murray

- Podcast: Latent Space
- Published: 2026-05-28
- Source: https://www.latent.space/p/cognition
- Relevance: 5/5

Cognition's Walden Yan and OpenInspect's Cole Murray describe the move from local coding assistants to background cloud agents that take specs, run in managed environments, test work, and return PRs. The strongest signals are Devin's reported internal PR growth, the security architecture of separating brain from machine, the hidden VM/filesystem work needed for usable agents, and SRE/support/security use cases beyond ordinary coding.

**Why it matters:** This is a first-hand look at what production agent infrastructure actually requires. The market is not just paying for model calls; it is paying for secure execution environments, repo setup, snapshotting, testing loops, integrations, onboarding, and operational trust.

## Signals

- **Cole Murray says a December 2025 model shift made spec-to-PR background agents practical.** [00:00:51] _agents_developer_tools; observation; high confidence._ He says Opus 4.5 and GPT-5.2 reached a point where agents could go from a sufficiently good spec to a completed PR with little handholding.
- **Yan says Devin merged PR usage grew 7x while Cognition engineering headcount grew about 10%.** [00:02:01] _agents_developer_tools; observation; high confidence._ He says internal merged PR usage grew roughly 7x over two to three months, while a shown chart put Devin commits across Cognition repos at 16% in January and 80% in March.
- **Both guests argue background agents should separate the agent brain from the machine for permission and secret isolation.** [00:10:39] _policy_geopolitics_security; observation; high confidence._ Murray says in-box agents require secrets in the sandbox and risk exfiltration, while Yan says Devin scopes user permissions on the machine and keeps the brain inaccessible from it.
- **Yan says Cognition had to build deep VM and filesystem infrastructure because ordinary cloud VMs were not built for repeated agent suspend-resume cycles.** [00:47:48] _infrastructure_energy; observation; high confidence._ He says raw EC2-style machines could take about 10 minutes to sleep and wake, network filesystems made grep slow, and Cognition built diff-proportional disk formats to speed boot.
- **Yan says teams need local-testable codebases so agents can run and verify changes without broad production credentials.** [00:56:10] _agents_developer_tools; observation; high confidence._ He recommends local DB, Docker Compose, Postgres, and mockable services so coding agents can test end-to-end work without live-service access, especially in older microservice codebases.
- **Murray says SRE auto-triage is the most common cloud-agent use case among his clients.** [01:01:15] _agents_developer_tools; observation; high confidence._ He says agents connected to alerts, logs, databases, and playbooks can gather context, explain incidents, and often produce PRs; OpenInspect supports Sentry and generic webhook triggers.
- **Yan expects hybrid frontier and subfrontier systems to become a major agent-cost pattern.** [01:05:13] _frontier_labs_models; forecast; medium confidence._ He says the coming year will feature very expensive frontier models plus systems that use cheaper subfrontier models for fast work and call frontier models only when needed.

## Changed Views Or Tensions

- Background coding agents have moved from demo workflow to production workflow for some teams, but the moat is agent infrastructure and adoption support, not just model access.
- Cloud coding-agent systems should be evaluated as VM, filesystem, permission, testing, and review products as much as model wrappers.

## Follow-Ups

- Track whether Devin's 80% internal commit share persists as Cognition scales engineering headcount.
- Watch whether enterprises standardize on brain-machine separation and full VMs for coding agents.
