# Ep. 14 - Finding Miscompiles For Fun, Not Profit (AI Infrastructure) | Justin Lebar & Jordan Nanos

- Podcast: SemiAnalysis Weekly
- Published: 2026-06-04
- Source: https://podcasters.spotify.com/pod/show/jordan-nanos/episodes/Ep--14---Finding-Miscompiles-For-Fun--Not-Profit-AI-Infrastructure--Justin-Lebar--Jordan-Nanos-e3kbp3d
- Relevance: 3/5

The available episode metadata describes Justin Lebar using fuzzing plus LLM-assisted review to find critical miscompiles in NVIDIA PTXAS, LLVM AMD GPU, and x86 compiler backends. The cached transcript appears unrelated, so this analysis is conservative and relies on the description rather than transcript evidence.

**Why it matters:** If accurate, low-cost discovery of severe compiler correctness bugs in GPU and CPU backends is directly relevant to AI infrastructure reliability, security, and the usefulness of agents for deep systems verification.

## Signals

- **Lebar reportedly found critical compiler miscompiles with about $10,000 of LLM-assisted effort.** [00:00] _agents_developer_tools; observation; medium confidence._ The episode description says he spent $10,000 in an afternoon and combined traditional fuzzing with LLM-assisted bug finding across multiple compiler backends.
- **The episode frames ML and GPU compiler backends as less-tested surfaces with latent high-severity bugs.** [02:48] _agents_developer_tools; inference; medium confidence._ The description contrasts mature CPU environments with less-tested ML compilers and says the discussion covers NVIDIA PTXAS and LLVM's AMD GPU backend.
- **One x86 finding reportedly split an atomic operation into two non-atomic operations.** [04:13] _policy_geopolitics_security; observation; medium confidence._ The metadata calls this a high-severity x86 bug, implying a correctness or security failure in a primitive that software relies on for synchronization.

## Changed Views Or Tensions

- Compiler verification may become an agent-assisted security workflow sooner than many AI infrastructure teams expect.

## Follow-Ups

- Refresh the transcript: cached captions are for an unrelated SemiAnalysis silicon-shortage discussion.
- Read the linked SemiAnalysis article before using these claims as high-confidence evidence.
