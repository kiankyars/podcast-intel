# Red-Teaming after Mythos — Zico Kolter & Matt Fredrikson, Gray Swan

- Podcast: Latent Space
- Published: 2026-06-22
- Source: https://www.latent.space/p/gray-swan
- Relevance: 5/5

Gray Swan cofounders Zico Kolter and Matt Fredrikson give a concrete operating view of the AI security stack now forming around frontier models and agents. The strongest signals are that specialized red-team models can outperform humans in fixed-time attack windows, robustness does not automatically improve with model scale, agent tool use creates enterprise-specific policy problems that prompting cannot solve, and AI insurance/compliance may become a forcing function after the first public prompt-injection breach.

**Why it matters:** The episode reframes AI security as a separate platform layer around agents rather than a generic cybersecurity feature or model-spec problem. It directly affects how to evaluate Claude Code, Codex, OpenClaw-style computer-use agents, guardrail vendors, enterprise adoption timelines, and the emerging market for third-party AI risk assessment.

## Signals

- **Fredrikson says Gray Swan's automated red-team models are still finding indirect prompt injections and jailbreaks for frontier labs, including agents with tool use.** [00:07:47] _agents_developer_tools; observation; high confidence._ He says the company trains red-teaming models for base chat systems and agents, and that the search space has not saturated because labs still come to them and receive new breaks.
- **Kolter argues frontier models do not become safe, robust, or useful as red-teamers merely by getting bigger; they need explicit specialized training.** [00:09:58] _frontier_labs_models; opinion; high confidence._ He says frontier models often refuse to jailbreak other models because of safeguards, and that both safety and adversarial red-teaming capability require targeted training rather than naive scale.
- **Kolter says Gray Swan's Shade system is now better than human red-teamers at finding model breaks in recent fixed-time competitions, while Fredrikson caveats that this is not full superhuman red teaming.** [00:10:58] _agents_developer_tools; observation; medium confidence._ They describe a recent competition where Shade found more breaks than humans within a fixed task window, while limiting the claim to automated throughput under defined conditions.
- **Kolter says Cygnal works because enterprise agent safety is a custom policy-enforcement problem, not just a generic open-source guardrail problem.** [00:26:19] _applications_business_models; observation; high confidence._ He describes Cygnal as a configurable filter between users, LLMs, and tool calls, trained with red-team data to enforce organization-specific rules that are too amorphous for simple scripts or prompts.
- **Fredrikson says the most severe enterprise failures appear when agents control tools such as browsers or batch prompts, because prompt fixes do not reliably preserve task context and policies.** [00:30:03] _agents_developer_tools; observation; medium confidence._ He cites credentials exposure, production-database deletion, and attackers exploiting ambiguity about context and policies as examples of failures that system-prompt reminders only partially address.
- **Kolter and Fredrikson say OpenClaw-style computer-use agents expose a broad attack surface, and Cygnal is useful for code agents like Codex or Claude Code but not yet a complete answer for arbitrary tool use.** [00:45:30] _agents_developer_tools; observation; high confidence._ They say Gray Swan found breaks across many OpenClaw trajectories, describe computer use as the biggest unlock because it operates as the user, and still require isolation, authentication, and access controls alongside AI guardrails.
- **Kolter and Fredrikson expect AI insurance and compliance to grow around third-party risk assessment, but say the market lacks a settled SOC 2-like framework.** [01:00:38] _policy_geopolitics_security; forecast; medium confidence._ They describe insurers using Shade or Arena-like evaluations, Cygnal-style mitigation for uninsurable deployments, no universally accepted compliance framework, and a likely demand shock after a major public prompt-injection breach.

## Changed Views Or Tensions

- Agent security should be evaluated as a separate platform layer with its own red-team and policy-enforcement products, not as a model-provider checklist item.
- Bigger frontier models may remain poor automated red-teamers and imperfectly robust unless the specific safety or adversarial capability is trained directly.
- Computer-use agents create the highest-value and highest-risk deployment surface because their usefulness depends on broad access to the user's real permissions.
- The first visible prompt-injection breach may become the commercial catalyst for AI insurance and third-party AI compliance.
- Enterprise guardrails need to inspect intended tool actions and organization-specific policies, not merely detect that an input contains prompt injection.

## Follow-Ups

- Watch Gray Swan for public benchmarks comparing Shade against human red-teamers on agent tasks.
- Track Anthropic, OpenAI, and other labs for model-card evidence that indirect prompt injection robustness is improving independently from general capability.
- Monitor Codex, Claude Code, and OpenClaw-like products for identity, permission, sandboxing, and tool-call policy controls.
- Follow AI insurance vendors for a SOC 2-like framework or mandated third-party AI risk assessments.
- Compare Cygnal's enterprise positioning against open-source guardrails from OpenAI, Meta, and Google.
