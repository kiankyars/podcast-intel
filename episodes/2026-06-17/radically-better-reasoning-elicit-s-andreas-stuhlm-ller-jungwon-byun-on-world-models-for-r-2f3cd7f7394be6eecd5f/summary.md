# Radically Better Reasoning: Elicit's Andreas Stuhlmüller & Jungwon Byun on World Models for Research

- Podcast: The Cognitive Revolution
- Published: 2026-06-17
- Source: https://www.cognitiverevolution.ai/radically-better-reasoning-elicit-s-andreas-stuhlmuller-jungwon-byun-on-world-models-for-research/
- Relevance: 4/5

Elicit's founders describe a product strategy built around trusted reasoning workflows for scientific and commercial evidence synthesis. The episode includes concrete customer traction in life sciences, a domain-specific workflow language for applying the same reasoning process across thousands of objects, an internal automated software-engineering system merging 30-50 issues per week, and a token-spend strategy based on model routing rather than all-frontier-model execution.

**Why it matters:** The episode is a useful counterweight to generic deep-research enthusiasm: Elicit's thesis is that high-stakes work still needs process guarantees, evidence quality controls, and explicit external representations. It also offers a real operating example of agentic software automation inside a serious AI company.

## Signals

- **Stuhlmuller says generic research agents can produce plausible outputs without actually completing the requested process.** [08:48] _agents_developer_tools; observation; medium confidence._ He describes an experiment where Claude and ChatGPT were asked to analyze about 100 toxicology papers and then admitted they had not actually analyzed all 100, which he treats as a process failure.
- **Elicit built a domain-specific workflow language so frontier models can orchestrate deterministic reasoning primitives at scale.** [11:30] _agents_developer_tools; observation; high confidence._ Byun says Elicit rebuilt on more agentic infrastructure starting around March or April 2025 and designed a programming language to apply the same process over 10,000 documents, drugs, targets, genes, or other objects.
- **Byun says Elicit now works formally with several of the top 20 life sciences companies across research, clinical, commercial, and medical workflows.** [15:21] _applications_business_models; observation; medium confidence._ She describes pull from discovery biologists, toxicologists, late/post-clinical researchers, and teams supporting launch, pricing, regulator, and payer decisions.
- **Elicit is moving beyond citation metadata toward claim-level confidence and domain-specific evidence-quality judgments.** [22:25] _applications_business_models; observation; high confidence._ Byun says the system should evaluate methodology and content, let researchers specify appropriate evidence levels, ingest non-paper sources such as filings, and express how well individual claims are supported.
- **Stuhlmuller says Elicit is exploring external world models as inspectable continual-learning representations for hard-to-verify research questions.** [47:59] _agents_developer_tools; observation; medium confidence._ He describes turning thousands of papers into representations that can answer prediction, intervention, and counterfactual questions with internal consistency, instead of relying only on model weights or million-token context stuffing.
- **Elicit's internal automated software-engineering system, The Line, is already merging roughly 30-50 issues per week fully automatically.** [1:11:54] _agents_developer_tools; observation; high confidence._ Stuhlmuller says a Slack emoji or support-system trigger can start a pipeline from spec through implementation, video testing, review, dev merge, and production merge for simple features and bug fixes.
- **Stuhlmuller says Elicit's economics favor one smart orchestrator that dispatches simpler subtasks to cheaper models rather than multiplying all work through the largest model.** [1:20:32] _frontier_labs_models; opinion; medium confidence._ He says he personally spends about $2,000 per week on tokens, would not easily spend many more multiples, and expects model-size routing to become increasingly important.

## Changed Views Or Tensions

- For high-stakes research, process guarantees may remain differentiated even as general deep-research agents improve.
- Agentic coding automation is already operational enough at Elicit to handle a material volume of simple issues, but reliability calibration remains the main limiter.
- Token-cost pressure may push serious agent systems toward orchestrator-and-worker model routing rather than uniform frontier-model usage.

## Follow-Ups

- Look at Elicit's API and MCP docs to understand which workflows are externally callable today.
- Track whether The Line's 30-50 fully automated merges per week grows into more complex product work or remains small bug/admin work.
- Compare Elicit's workflow-language guarantees with Anthropic workflows and other deep-research process-control systems.
