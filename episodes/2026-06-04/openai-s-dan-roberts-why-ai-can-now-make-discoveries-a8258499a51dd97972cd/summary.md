# OpenAI's Dan Roberts: Why AI Can Now Make Discoveries

- Podcast: The MAD Podcast with Matt Turck
- Published: 2026-06-04
- Source: https://podcasters.spotify.com/pod/show/firstmark/episodes/OpenAIs-Dan-Roberts-Why-AI-Can-Now-Make-Discoveries-e3ka0se
- Relevance: 5/5

OpenAI’s foundations-of-RL lead says the lab is treating reinforcement learning and test-time compute as a primary scaling axis alongside pre-training. He describes a recent informal-mathematics result as genuine exploration: a model spent hours pursuing a contrarian hypothesis, connected disparate fields, and refuted a conjecture. The interview also identifies the remaining frontier: moving from well-defined, verifiable problems toward selecting worthwhile research questions and exercising scientific taste.

**Why it matters:** This is a first-party account of OpenAI’s technical direction beyond the next model generation. It suggests future capability gains will depend materially on scaling RL and inference-time computation, not merely larger pre-training runs. It also provides a concrete mechanism for AI-assisted discovery while defining the unresolved bottleneck to broader scientific autonomy.

## Signals

- **Roberts says OpenAI is studying scaling laws for reinforcement learning versus pre-training and working on systems beyond the immediately forthcoming model generation.** [01:31] _frontier_labs_models; observation; high confidence._ His team investigates what RL teaches, where it fails, and how OpenAI can convert its expanding compute base into more capable reasoning models, including work aimed at the next and next-next model generations.
- **Roberts argues that RL has become a principal way to convert additional compute into intelligence, rather than a small post-training enhancement.** [24:50] _frontier_labs_models; observation; high confidence._ He says OpenAI had only begun scaling this approach roughly a year and a half earlier and intends to apply substantially more RL, treating it as a major scaling axis beside pre-training.
- **Roberts says sufficiently capable pre-trained models were the prerequisite that made reasoning-oriented RL effective.** [25:46] _frontier_labs_models; inference; medium confidence._ His proposed mechanism is that a strong language prior lets a model use RL to learn productive token-space reasoning and spend test-time compute on problems it could not solve with an immediate response.
- **Roberts characterizes OpenAI’s recent unit-distance mathematics result as genuine exploratory discovery rather than routine retrieval or exploitation.** [22:35] _frontier_labs_models; observation; medium confidence._ He says the model spent hours testing alternatives, rejected a conjecture widely assumed true, and used expertise from another mathematical field to construct a counterexample.
- **Roberts distinguishes OpenAI’s informal mathematical reasoning strategy from DeepMind’s formal proof-search approach.** [10:25] _frontier_labs_models; observation; high confidence._ He says DeepMind translates problems into Lean for mechanically checked proofs, while OpenAI generally reasons from informal English and mathematical notation, producing human-style arguments that require harder external verification.
- **Roberts rejects a scale-only interpretation of the Bitter Lesson, arguing that algorithmic ideas and empirical scaling must advance together.** [31:47] _frontier_labs_models; opinion; high confidence._ He says pre-training alone would have produced materially weaker models than scaling RL on top of it, and describes a cycle in which large runs reveal phenomena that researchers study and turn into new methods.
- **Roberts expects AI research automation to progress gradually and forecasts more AI-driven mathematics, science, and AI-engineering advances over the next six months.** [45:51] _agents_developer_tools; forecast; medium confidence._ He says models already complete some coding work that previously took weeks, but humans remain useful for choosing research questions and applying scientific taste, which are difficult to reward automatically.

## Changed Views Or Tensions

- RL should be modeled as a major compute-scaling regime alongside pre-training, not merely a finishing layer for alignment or style.
- The latest mathematical results offer evidence that long-running language-model reasoning can perform meaningful exploration across fields, although informal outputs retain a significant verification burden.
- Scientific autonomy is unlikely to arrive simply by extending solution length; question selection, research taste, and rewards for non-verifiable work remain distinct technical bottlenecks.
- OpenAI appears to view capability development as an iterative interaction between scale and new algorithms, rather than scale alone.

## Follow-Ups

- Examine OpenAI’s published unit-distance result and independent mathematician verification of the claimed counterexample.
- Compare compute usage, verification burden, and success rates of OpenAI’s informal approach with DeepMind’s Lean-based systems.
- Track evidence for RL scaling laws and whether gains continue outside mathematics and coding.
- Watch for concrete OpenAI products or evaluations addressing legal, consulting, and other domains without deterministic rewards.
