# Scott Wu on Cybersecurity, Compute, and the Future of Engineering - [Invest Like the Best, EP.502]

- Podcast: Invest Like the Best
- Published: 2026-11-24
- Source: https://www.youtube.com/watch?v=efoZj_7oVJs
- Relevance: 4/5

Cognition CEO Scott Wu describes how customers and his own engineers use Devin, what drives the company's compute commitments, and how Cognition evaluates changes to production code. The clearest operating figures are internal. Wu estimates that automated triggers account for about 90% of Cognition's Devin usage and reports roughly ten times as many merged pull requests per engineer as a year earlier. He also reports crossing a $1 billion revenue run rate on September 16, 2026. His references to October activity place those observations before the November 24 episode release. Timestamps follow the official video edition.

**Why it matters:** An agent can keep generating paid work between human interactions. Wu's internal adoption figures give a reason to track workload triggers, usage per customer and reserved compute alongside seats. Customers still have to determine whether the additional merges deliver working features and reduce time to production. Cognition's own benchmark illustrates how even a passing change can create costly review or maintenance work.

## Signals

- **Wu estimates that about 90% of Cognition's internal Devin usage starts automatically, including jobs triggered by software events.** [40:38; 40:42; 40:50; 40:53; 40:59] _agents_developer_tools; observation; medium confidence._ He distinguishes scheduled jobs from API calls that start work when an incident appears. In the latter case, Devin can begin investigating before an engineer opens a session. This creates demand between human interactions. Wu describes the share as internal usage and leaves the unit unspecified, so the figure cannot be applied to billed tokens, autonomous completions or customer accounts.
- **Wu says Cognition doubled its engineering staff while its rate of merging pull requests rose about twentyfold over roughly a year.** [35:08; 35:13; 36:17; 36:24; 36:32; 36:54; 37:04] _applications_business_models; observation; medium confidence._ That implies about ten times as many merges per engineer. Wu also saw some new hires work entirely through Devin's hosted repositories and test environments while continuing to review and test changes themselves. At an unnamed bank he projected 250,000 Devin-assisted merges in October against a prior organization-wide monthly baseline of 400,000. The projection gives no subsequent total or breakdown of displaced manual work. Neither comparison measures the size, quality or customer value of a change.
- **Wu says compute reservations expose an agent vendor to financing risk even when its revenue grows severalfold.** [27:32; 27:44; 27:55; 28:20; 29:11] _companies_capital_allocation; inference; medium confidence._ He illustrates the mismatch with a company reserving capacity for eightfold growth and achieving fivefold growth instead. Cognition has explored building infrastructure and working with partners. Wu discusses equity, secured or investment-grade borrowing, and customer prepayments as possible ways to bridge the timing gap. He gives no signed commitment, minimum payment or utilization figure for Cognition. The growth multiples illustrate a downside case rather than company guidance.
- **Cognition grades coding agents on whether a fix stays in scope and respects a repository's dependency rules, even when the test suite passes.** [48:58; 49:19; 49:36; 49:45; 51:40] _agents_developer_tools; observation; medium confidence._ Wu describes how extra features or a change that crosses an architectural boundary can make an otherwise functional patch unacceptable. He identifies two harder evaluation problems: making historical design decisions available to the agent and grading a debugging conversation in which the human and agent discover the specification together. He gives no measured gain from these evaluation choices.
- **Wu reports that Cognition crossed a $1 billion revenue run rate on September 16 and had begun rolling Devin out to about 14,000 Citi engineers.** [01:10; 01:14; 01:24; 02:29; 34:11] _applications_business_models; observation; medium confidence._ He dates the first revenue to September 20, 2024, and reports use across more than 100 Fortune 500 companies at interview time. He describes enterprise onboarding team by team, with explicit workflows, playbooks and return measurements. The run rate is an annualization. The Citi figure describes the rollout population, and Wu gives no active-use or retention figure. He separately cites Citi's broader projected savings on bringing work in-house, with no Devin-specific attribution.

## Changed Views Or Tensions

- An account's use of coding agents can grow through incident and workflow triggers even with stable headcount. Cognition's own deployment offers a specific case for measuring that usage separately.
- Merged pull requests are an informative activity measure when paired with engineer counts. Measuring the economic result also requires review effort, production outcomes and change quality.

## Follow-Ups

- Ask for the denominator behind the 90% automation estimate and a split between scheduled runs, API-triggered sessions and sessions started by other agents.
- For the enterprise rollout, track weekly active engineers, net added throughput, time to production, reversions and any consultant spending the customer directly attributes to Devin.
- Compare minimum compute commitments and customer prepayments by maturity to assess the cash exposure if realized usage falls short of plan.
- Wu expects large-company and government breaches within six to twelve months of the interview. Track disclosed incidents and remediation outcomes against that forecast.
