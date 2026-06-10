# Why Video Agent models are next — Ethan He, xAI Grok Imagine

- Podcast: Latent Space
- Published: 2026-06-01
- Source: https://www.latent.space/p/video-agents
- Relevance: 5/5

Ethan He gives a technical account of frontier video generation from NVIDIA Cosmos to xAI Grok Imagine, with unusually concrete details on synthetic captions, VAEs, temporal compression, iteration speed, and why image models bootstrap video models. His main thesis is that video generation is becoming a video-agent problem: LLMs plan, rewrite prompts, call diffusion and editing tools, and iterate toward production-quality media.

**Why it matters:** This changes the competitive lens for generative media. The winner may not simply be the lab with the best standalone video diffusion model, but the lab or product that combines strong language reasoning, cheap iteration, media tools, and workflow integration into an agentic creative system.

## Signals

- **He says a small xAI team built Grok Imagine 0.9 from no video infra, data, or model in three months.** [00:02:30] _frontier_labs_models; observation; high confidence._ He attributes the speed to prior Cosmos experience, a small high-talent team, strong data and inference foundations, heavy compute, and high iteration rate.
- **He says coding-model improvements are making compute the bottleneck for model iteration again.** [00:07:05] _semiconductors_compute; inference; high confidence._ He argues ideas that previously took weeks to implement can now be built in hours, so teams need enough compute to immediately test many more model and data experiments.
- **He says video models usually start from image models because video has too few dense language-video pairs.** [00:10:28] _frontier_labs_models; observation; high confidence._ He explains that internet videos lack reliable captions, so labs generate synthetic descriptions, train image models first for denser language grounding, then bootstrap video models from them.
- **He says temporal compression trades off context length against real-time interactivity.** [00:20:52] _frontier_labs_models; observation; high confidence._ He describes 8x8x4 VAE compression that saves context by compressing four temporal frames into one token, while frame-by-frame compression is more responsive but about four times larger.
- **He says video agents turn LLMs into planners that call diffusion, editing, and deterministic media tools.** [01:20:34] _agents_developer_tools; inference; high confidence._ He says prompt rewriting has become agentic, with language models fetching context, planning layouts, calling generative models or FFmpeg, and iteratively refining longer videos.
- **He predicts video agents become a major category by the end of 2026 if they reach production-grade ad quality.** [01:29:37] _applications_business_models; forecast; medium confidence._ He says enterprise budgets expand once video agents can produce distributable ads, even though agents cost more because they generate many variations through iterative workflows.
- **He says the current bottleneck for video models is increasingly the language-model and agent side.** [01:33:33] _frontier_labs_models; opinion; high confidence._ After leaving xAI, he says he wants to work on LLMs because most video-model gains now come from language intelligence rather than diffusion technology alone.

## Changed Views Or Tensions

- Near-term video generation progress may come more from LLM planning and tool use than from isolated diffusion-model improvements.
- Video-agent economics could be materially more expensive than one-shot video generation because production quality requires iterative variation and editing.

## Follow-Ups

- Watch whether Grok Imagine Agent or comparable systems reach ad-quality production workflows by late 2026.
- Track whether frontier labs converge on separate LLM-plus-diffusion tool systems or jointly trained omni models.
