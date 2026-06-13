# AI in the AM — Week 2 Highlights (June 2026)

- Podcast: The Cognitive Revolution
- Published: 2026-06-13
- Source: https://www.cognitiverevolution.ai/ai-in-the-am-week-2-highlights-june-2026/
- Relevance: 5/5

This Cognitive Revolution highlights episode is a dense update on Fable's first week in real workflows, Anthropic's safety gating, early signs of model-driven post-training, and the state of alignment theory. The most important thread is that frontier capability is moving into long-running agentic work while the control story still leans on gates, monitoring, character training, and theory work that participants say is not yet adequate.

**Why it matters:** The episode connects operational deployment facts, model economics, recursive-self-improvement timelines, and safety mechanisms in one current snapshot. Several claims come from practitioners testing Fable, alignment researchers launching Sequent, Julius, Goodfire, and Lovelace operators describing concrete deployment bottlenecks.

## Signals

- **Prakash says Fable often refused or silently downgraded when asked to touch production systems, suggesting early access is gated around operationally sensitive workflows.** [03:16] _agents_developer_tools; observation; high confidence._ He says Fable repeatedly dropped to Opus 4.8 when asked to work with production databases, security keys, or direct production review, and he interprets this as a constrained research-style release whose gates may loosen over weeks.
- **Rahul Sonwalkar says Julius sees API-level Fable failures for advanced coding or safety-triggering data tasks, but without the Claude-app fallback behavior.** [07:05] _agents_developer_tools; observation; high confidence._ He reports failures on tasks like training models and on borderline personal-data lead prospecting, while noting that Julius API calls appear to fail rather than falling back to Opus.
- **Shlok Khemani says Fable showed unusually high agency on a vague 3D-world task by independently sourcing satellite imagery, NASA elevation data, and pixel-derived vegetation placement.** [08:37] _frontier_labs_models; observation; medium confidence._ Khemani says Fable rebuilt Yosemite as a navigable world by choosing data sources and implementation details that exceeded the original vague instruction, including adding trees and snow based on image analysis.
- **Labenz says Fable produced a more than 10x improvement when training small specialist models on a puzzle task, making post-training automation a concrete near-term capability to watch.** [10:53] _frontier_labs_models; observation; medium confidence._ He describes Thoughtful's frog-game setup where earlier big models failed to improve small models much, but Fable substantially increased small-model task performance.
- **Prinz argues Anthropic's own Fable/Mythos materials show strong engineering acceleration but not yet research judgment, making true research automation the key RSI warning sign.** [14:05] _frontier_labs_models; inference; medium confidence._ He points to Anthropic's distinction between engineering execution and research judgment, and says the claimed biology example appears more like a useful engineering result than a novel-research breakthrough.
- **Geoffrey Irving and Daniel Murfet frame Sequent around a short, uncertain RSI timeline and a gap between current empirical alignment and formal guarantees.** [33:50] _policy_geopolitics_security; forecast; medium confidence._ Irving gives a modal two-to-three-year superintelligence timeline, says labs are focusing on acceleration tasks, and Murfet argues alignment lacks the precise definitions that make automated math-style progress straightforward.
- **Andrew Moore's Lovelace thesis is that serious enterprise AI should pre-cache context and rely on redundant data streams, reducing query-time compute by more than 100x while improving recall.** [1:03:56] _agents_developer_tools; observation; high confidence._ Moore says Lovelace can show comparable results to deep-research models at less than 1% of compute cost by moving work to ingestion time, then stresses redundant information streams for high-recall decisions.

## Changed Views Or Tensions

- Fable's first-week deployment looks less like unrestricted frontier access and more like a gated preview where production, security, ML, and sensitive-data tasks can be blocked or downgraded.
- The live RSI discussion is shifting from generic model capability to whether models can automate research judgment, post-training, and alignment theory before current monitoring methods fail.
- Enterprise-agent cost structure may hinge on context architecture: pre-cached, redundant context systems can be dramatically cheaper than repeated just-in-time deep research.

## Follow-Ups

- Track whether Anthropic changes Fable's refusal and downgrade behavior for production, ML, finance, and data workflows over the next few weeks.
- Compare Thoughtful's post-training result with other small-model training benchmarks to see whether Fable's improvement generalizes beyond the frog task.
- Watch Sequent and Goodfire for concrete outputs: formal definitions, scalable oversight theory, and training-data debugging tools that labs actually adopt.
