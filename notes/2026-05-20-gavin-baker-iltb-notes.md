# Gavin Baker on *Invest Like the Best* — "Watts, Wafers, and the Future of AI Infra"

- **Episode:** Invest Like the Best (Patrick O'Shaughnessy × Gavin Baker)
- **Published:** 2026-05-20
- **Duration:** 1:22:11
- **YouTube ID:** `Mmj_G9RlW-I` — https://www.youtube.com/watch?v=Mmj_G9RlW-I
- **Local transcript:**
  - `transcripts/2026-05-20-watts-wafers-and-the-future-of-ai-infra-gavin-baker-Mmj_G9RlW-I.md`
  - `transcripts/2026-05-20-watts-wafers-and-the-future-of-ai-infra-gavin-baker-Mmj_G9RlW-I.json`

This document walks through each of your raw notes in order, points to the exact place in the transcript, quotes the relevant lines, and adds light commentary or fact-checks where requested.

---

## 1. "SpaceX compounding 30"
**Where:** ~[11:34] – [12:06]

Gavin's friend Antonio pointed out that **SpaceX has compounded at "low 30% per year" for roughly a decade**, and Baker frames that as a *deliberate* Elon strategy:

> "Elon has always made investors money. He treats it like a sacred covenant. … He can essentially raise as much capital as he wants whenever he wants."
> "My friend Antonio pointed out SpaceX compounded … low 30% per year for whatever that was, a decade. And that was just cuz Elon was … focused on preserving the superpower and … trying to strike a fair balance between investors and employees."

**Takeaway:** Baker's argument is that systematically *under*-pricing primary rounds — never being greedy on valuation — is what gives Elon (and, by extension, Anthropic if they imitate it) a 20-to-30-year fundraising superpower. The 30% isn't a forecast; it's an empirical compounding rate showing that leaving money on the table at each round still produces an enormous CAGR.

---

## 2. "Boom Aerospace"  →  **Boom Aerospace + orbital compute**
**Where:** [16:07] – [21:21]

Two threads collided in this note:

- **Orbital compute (racks in space):** Baker reframes "data centers in space" as **single Blackwell-sized racks (≈8 ft × 4 ft × 3 ft, 3,000 lb) in sun-synchronous orbit**, cooled by radiators that extend hundreds of feet behind the rack and linked by lasers through vacuum (the same physics as Starlink V3 inter-satellite links). A Starlink V3 is already a 20 kW satellite; a Blackwell rack is 100 kW. He thinks **inference, not training, is the right workload** to push to orbit.
- **Boom Aerospace:** mentioned in the context of bridging the watts gap — _"we're getting really good at repurposing jet engines, you know, there's that Boom Aerospace that is doing this"_ ([21:21]). It's one of several stopgap energy plays alongside turbines while orbital compute matures.

---

## 3. "South Sea — valuable"  →  **Carlotta Perez / historical-bubble framing**
**Where:** [22:50] – [24:53]

You almost certainly meant the **Carlotta Perez "every new general-purpose technology gets a bubble"** thesis. Baker doesn't say "South Sea" by name, but he lists the historical analogs:

> "Carlotta Perez wrote this great book about this. … Markets are efficient. They correctly understand that this is a foundational new technology. … Forget the internet bubble. We had a railroad bubble. A canal bubble. We should expect a bubble."

Key differences he flags between *this* build-out and 2000:
1. Funded out of **operating cash flow**, not debt.
2. **Every GPU runs at ~100% utilization**, vs. ~1% of dot-com fiber.
3. Valuations are **not extended** at the leaders.

He cites **George Vanderheiden** at Fidelity — _"being early is the same thing as being wrong"_ — as the cautionary tale of how painful it is to be a valuation-sensitive PM in a bubble even when you're ultimately right.

(If you specifically want a *South Sea* analogy, the Perez framework explicitly includes 1720 South Sea / Mississippi as the canonical pre-industrial example — worth a Perez re-read.)

---

## 4. "Jensen Huang handshakes"
**Where:** [22:50]

> "I do think it's wild that Jensen has never had a contract with Taiwan Semi. They do business on what seems fair, in handshakes. … No contract. It's going to be fair over time. We're partners. We're going to be fair to each other."

**Why it matters:** Baker treats this as evidence that the *Morris Chang → Jensen* trust covenant is the real moat — neither side wants to vertically encroach because the relationship compounds. It also rhymes with his Elon "sacred covenant" frame in §1.

---

## 5. "Lam, KLA, Lam, Tencor, monopsony"  →  **The semicap monopsony point**
**Where:** [27:50] – [28:36]

You captured Baker's argument that **the wafer-fab equipment vendors actively *want* a second leading-edge foundry** so they don't have to live as a monopsony supplier to TSMC.

> "One big reason Taiwan Semi caught up is ASML and KLA Tencor and Lam Research and Applied Materials. They wanted them to catch up. They didn't like having a monopsony. And so the A teams were in Taiwan working … And so the A teams will be here [at the Terra Fab] cuz of Elon's reputation in hardware engineering."

So your shorthand maps to: **Lam Research, KLA-Tencor, Applied Materials → monopsony**. Baker's prediction is that the same dynamic will route the **A-teams from ASML / KLA / Lam / AMAT to the Terra Fab** for the same reason — they don't want TSMC to remain the only customer for their best machines.

---

## 6. "It's sad but he's a deity"  →  **"Elon is a living deity in Asia"**
**Where:** [29:42] – [30:26]

> "It's sad, but he is a living deity in China, Taiwan, South Korea, and Japan."

Context: U.S. politics has obscured how Elon is perceived in Asia, and Baker thinks that perception advantage is what will let Tesla/SpaceX **recruit the very best hardware engineers** to the Terra Fab in Texas — including literally relocating Taiwanese restaurants ("Taiwan town", "Japan town", "Korea town") to keep those engineers happy. He frames it as a structural recruiting moat that Intel and Samsung organizationally cannot replicate.

---

## 7. "TSMC production is the bubble indicator"
**Where:** [25:31] – [27:02]

> "If Taiwan Semi did what Jensen wanted, I think Nvidia could sell $2 trillion of GPUs in 26 or 27. Maybe 2 and 1/2 trillion. Maybe 3 trillion."
> "If we don't get a bubble, like we need to throw a party for [TSMC] because they will have single-handedly prevented a bubble."
> "If I were to watch one thing to understand where there's a bubble, it's Taiwan Semi's capacity decisions."

**Operational read:** Baker thinks **TSMC's leading-node capex pace is the single best leading indicator of whether the AI build-out tips into bubble territory.** The "Goldilocks zone" is when TSMC expands enough to prevent Intel/Samsung from grabbing >30% share, but not so much that supply outruns demand.

---

## 8. "TPU v8"
**Where:** [33:01] – [34:33]

> "Google losing their per-cost-token leadership as a result of making very conservative design decisions with TPU v8 to try and take it away partially from Broadcom and Nvidia…"

The argument:
- 9 months ago **Google dominated the Pareto frontier** (intelligence vs. cost). Every other lab sat *inside* their curve.
- Today the Pareto frontier is **Anthropic + OpenAI**, with **Grok 4.3** as the best low-cost ~500B model and **Gemini 3.1** only "hanging on" (he suspects subsidized out of pride).
- He attributes the regression to **conservative TPU v8 design tradeoffs** that were partly motivated by wanting to take *more* of the chip stack away from Broadcom and Nvidia internally — and that cost them their cost-per-token edge.

This is one of the most important investment claims in the episode for the Google / Broadcom / Nvidia triangle.

---

## 9. "Usage pricing is better than Max plans!!!"
**Where:** [36:41] – [39:00]

> "These AI models just shifted to usage-based pricing. And if you're on that $250 or $300 or $280-a-month plan …, you're getting severely rate-limited. You're getting a lobotomized version of the AI."

Why it matters per Baker:
- **Token quality ≈ answer quality**, and Claude is producing **~70% fewer tokens** per question on a flat plan, materially degrading reasoning.
- To experience the frontier you **need Claude Code or Codex on an *enterprise / usage-based* plan**, not the $200-ish "Max" tier.
- Historical analog: telecom shifted from per-minute → unlimited and growth died. **AI is going in the *opposite* direction** — fixed → pay-by-the-drink — and that's why he expects OpenAI and Anthropic to each blow past **$200B ARR** this year.

(Direct practical implication for *your* tooling: usage-based >> Max.)

---

## 10. "Disaggregation of prefill and inference"
**Where:** [44:40] – [45:31], and again [49:22] – [50:48]

Best one-line definition in the transcript (from Baker's colleague Andrew Fox):

> "Picture a British naval ship from the 18th century. **Prefill is loading the cannon, decode is firing it.**"

More precisely:
- **Prefill** = ingest the prompt/context and build KV state → **memory-capacity bound**.
- **Decode** = generate tokens one-by-one → **memory-bandwidth bound**.

Two big consequences Baker draws out:
1. **The chip canvas opens up.** Startups can now make very different chips for prefill vs. decode, instead of trying to build a "better GPU."
2. **GPU useful life extends to 10–15 years.** You can put a Cerebras system or **Groq LPUs (which Nvidia acquired)** in front of older Hopper or even Ampere GPUs and reuse them for prefill until they melt. This is the *quiet* reason he thinks **private credit on GPUs will survive** — refinanceable at 5–6% instead of CoreWeave's ~low-7s.

---

## 11. "Cerebras's limitations in terms of compute"
**Where:** [46:40] – [48:12]

Baker is *long* Cerebras (his firm was a venture investor) and frames it as "doing something different *and* hard" — wafer-scale computing. The honest limitation he names is:

> "One of the problems Cerebras has, once you start needing to glue a lot of chips together and scale-up networks or scale-out networks, you need a lot of IO. And **IO is bound by what's called the shoreline, the sides of the chip**. And so Cerebras has an overwhelming ratio of on-chip compute and memory relative to shoreline IO."

How they're trying to solve it:
- **Optical wafer stacked on top** of the compute wafer (to escape shoreline IO).
- Likely **hybrid bonding of DRAM** to address the "alleged" memory-capacity ceiling.
- It took **three chip generations** to make wafer-scale work; that's the bar for any "hard + different" startup.

So your note maps directly to: *Cerebras's shoreline-IO bottleneck and the optical-wafer fix.*

---

## 12. "Energy 2027"
**Where:** [14:15] – [16:07]

> "The watts shortage will probably begin to alleviate **'27, '28**."

Drivers:
- Turbines: capacity ramps have been announced, but giant cast-blade tooling has atrophied in the West for 80 years.
- The big-PE-infra-investor quote (paraphrased from Blackstone/Apollo/KKR): _"It used to be energy and chips were our biggest gating factors. Now it's **zoning and approval**."_
- Beyond '27–'28, **orbital compute** takes over the marginal-watt problem for inference.

So your "Energy 2027" note = Baker's specific call that **wattage stops being the binding constraint somewhere in 2027–2028**, with regulatory/zoning risk as the new bottleneck.

---

## 13. "I don't get the point on Nvidia"  →  **Why Nvidia would release its own open-source frontier model**
**Where:** [55:29] – [57:26]

What Baker actually said:

> "I have a belief that whenever he wants, Jensen can probably get pretty close to the frontier — with his own model. … to monetize your complement, as Sklansky would say. … He's a very logical thinker. This is the logical counter-move. And I think you will see that, like, open-source frontier — which today consists of, you know, Chinese models with stolen American tokens…"

### The strategic logic, plainly

This is the classic **"commoditize your complement"** play (Joel Spolsky's framing, which Baker attributes to David Sklansky). The rule is simple: if you sell **product A**, you want **everything that gets used alongside A (its complement)** to be **as cheap and abundant as possible**, because that drives more demand for A.

Apply it to Nvidia:
- **Nvidia's product = GPUs.**
- **The complement to a GPU = the AI model that runs on it.**
- If models stay expensive and concentrated in two private hands (OpenAI, Anthropic), those two labs **capture the AI profit pool and squeeze Nvidia's margin** — exactly what they're trying to do by building/funding custom silicon (OpenAI's Broadcom chip, Anthropic's Trainium relationship with AWS).
- So Jensen's logical counter-punch is to **release a near-frontier model as open source**. That:
  1. **Collapses the price of intelligence** — nobody pays $20/M tokens to Anthropic if a Nvidia-released open model is 90% as good and free.
  2. **Destroys OpenAI's and Anthropic's pricing power**, which is the cash flow funding their custom-silicon programs.
  3. **Maximizes GPU demand**, because every startup, enterprise, and dev can now self-host frontier-class intelligence — and every one of those deployments needs to be bought from… Nvidia.
  4. **Makes the Chinese open-source threat redundant** — the current open-source frontier is, in Baker's words, "Chinese models with stolen American tokens." Nvidia releasing its own model means American teams stop being forced onto DeepSeek / Qwen.

Baker's nuance ([57:26]): Jensen probably wants the open-source frontier to **trail the closed frontier by a controlled lag** — close enough to crush OpenAI/Anthropic's pricing power, but not so close that he eliminates the reason hyperscalers keep buying his top SKUs to run the *true* frontier. It's a knob, not an on/off switch.

The deeper point: this is **the same prisoner's dilemma as Taiwan Semi / Samsung / Intel**. Everyone at the frontier *would* prefer to keep their model closed, but if one labs defects and releases at the frontier, that defector grabs the revenue and pulls ahead — so eventually somebody defects, and Baker thinks Jensen has both the means and the structural incentive to be that defector.

---

## 14. "5 layers of cake"  →  **Jensen's five-layer AI cake**
**Where:** [52:41]

> "In **Jensen's five-layer cake of AI**, the profits — they're accruing to **energy, … data centers, … chips, … models, not really accruing to the applications.**"

Layer by layer (as named in the transcript):
1. **Energy**
2. **Data centers**
3. **Chips**
4. **Models**
5. **Applications** ← Baker explicitly says profits are *not* accruing here today.

He pairs this with **Jamin Ball's "token path" test**: if you're a software / AI app and you're *not* on the token path (Databricks-style) or in a defensible niche, life is hard.

---

## 15. "RSUs vs PSUs — go through all the podcasts"
**Where:** [01:01:05] – [01:02:18]

This is Baker describing his **most useful AI agent** — one that ingests podcasts and surfaces specific signals he cares about, prominently:

> "I'm very sensitive to management compensation. … Do they have **stupid RSUs**? Or do they have **PSUs**? And if they have PSUs, what are those PSUs incentivized to do? … pulling the PSU thing, looking at how it's changed versus all the proxies, cuz there's signal in that."

**Why he prefers PSUs:** RSUs vest with time regardless of performance → "stupid." PSUs vest only when specific operating or stock-performance targets are hit → comp aligns with shareholder outcomes. Tracking *changes* in PSU design across proxies is the real alpha — companies loosen vesting targets when management has lost confidence and tighten them when they think they can deliver.

**Action item for your reading list / agent:** build (or have your podcast-summary agent build) a recurring scan that flags **proxy diffs in PSU targets** for the names you follow (NVDA, AVGO, GOOG, AMZN, MSFT, GE Vernova, ALAB, etc.).

---

## 16. "Cross-sectional valuations"
**Where:** [01:02:37] – [01:03:40]

> "**Cross-sectionally the valuations do not make sense.** They just flat-out do not make sense. They cannot all be true. You have semi-cap equipment companies trading at 40x next quarter's annualized earnings and DRAM companies trading at mid-single digits. At the peak of the last cycle, that was like 5 vs 12. At one point it was like 3 vs 45. **Those can't both be true.**"

Baker's framing: in shortage regimes the **lowest-quality names rip the most** because they go from on-the-brink to gushing cash. So the cross-section is being distorted by *quality of buyer*, not by *quality of business*. See §18.

### Side-explainer (you asked for this concisely): *"Yes, they have some element of recurring revenue with parts and maintenance, but it's not worth a thousand percent multiple gap."*

He's comparing **semi-cap equipment makers** (ASML, Lam, KLA, Applied Materials — the companies whose machines *build* the chips) to **memory/DRAM makers** (Micron, Hynix, Samsung's memory arm). Right now the equipment guys trade around **40× earnings**; memory trades around **mid-single digits**. That's roughly a **10× (1000%) multiple gap**.

The standard bull justification for paying so much more for the equipment guys is that they earn **recurring service revenue** — once their machines are installed in a fab, they get paid year after year for spare parts, maintenance contracts, and software/process upgrades, which smooths the cycle. Baker's response: yes, that recurring revenue stream is *real* and worth a premium — but **it's worth a small premium, not a 10× premium**. Both groups are still fundamentally cyclical hardware businesses tied to wafer starts. A modest service-annuity layer cannot, mathematically, justify pricing one as if it were SaaS and the other as if it were going bankrupt.

In other words: the market is using "recurring revenue" as a *narrative* to justify a multiple gap that the actual cash-flow math doesn't support.

---

## 17. "GE Vernova vs Nvidia"
**Where:** [01:03:40]

The cleanest pair-trade observation in the episode:

> "It's very hard to square that valuation with something like **GE Vernova**'s valuation, cuz it builds in like unfathomable amount of share loss for Nvidia."

### What GE Vernova actually is
GE Vernova (ticker `GEV`, spun out of GE in 2024) makes the **physical power-generation kit** that AI data centers run on: gas turbines, steam turbines, generators, grid equipment, and wind/nuclear gear. It is one of only a handful of companies in the world that can supply heavy-frame gas turbines on the timelines hyperscalers need. So the market treats it as **the purest "picks-and-shovels" play on AI electricity demand.**

### The logical inconsistency Baker is pointing at
Both stocks are AI-derivative bets, but the same demand forecast cannot justify both prices simultaneously:

- **GE Vernova trades like an AI super-cycle is certain.** Its premium multiple is only rational if you believe data-center buildout is enormous, sustained, and accelerating — i.e., that *gigawatts of new compute get installed* through 2030.
- **Nvidia trades like the AI super-cycle is uncertain.** Its multiple was, in early April, "as cheap as it gets relative to the market" in 10–12 years.
- **But every gigawatt of new compute GEV powers has to be filled with accelerators.** Today, Nvidia has roughly 90% share of merchant AI accelerators. So if the market truly believes GEV's volume story, by arithmetic it has to also believe Nvidia ships a *correspondingly enormous* amount of GPUs.
- The only way both multiples are internally consistent is if **all those new data centers get filled with non-Nvidia silicon** — Trainium, TPU, MI450, custom ASICs — i.e., the market is implicitly pricing Nvidia's accelerator share collapsing from ~90% to something dramatically lower.

Baker calls that implied share loss **"unfathomable."** He thinks it isn't going to happen (see §8 on TPU v8 missing, §10 on disaggregation extending GPU life, §13 on Jensen's open-source counter-move). The trade that falls out of this:
- If you agree with him → **Nvidia is the mispriced leg; GEV is priced for perfection.**
- If you disagree → you have to articulate a coherent thesis for who actually wins the accelerator share GEV's multiple is implicitly handing away.

Either way, the **NVDA / GEV spread is the cleanest single chart** for tracking whether the market is being internally consistent about AI infra.

---

## 18. "Look into retail-driven low quality"
**Where:** [01:03:40] – [01:06:04]

Baker is uneasy about the **retail-driven low-quality bid**:

> "The lowest-quality players … hated and detested by the hyperscalers … high costs, unreliable, parts fail at a high rate … they're sold out and raising prices. And then that activity gets the interest of these retail accounts on X, and these stocks get bid to the moon."
> "You have this **nuclear bubble** and this **quantum bubble** right here, right in front of you."

Where he sees the froth concentrated:
- Nuclear small-caps
- Quantum small-caps
- "Speculative, lower-quality, smaller-cap names where if you have a big presence on X or Reddit, it's easy to move them."

He explicitly contrasts those with **high-quality compounders that are *not* extended** — that's where he wants to be long.

**Action item:** when you "look into retail low quality," scan the X-popular nuclear and quantum names for the "high-cost / unreliable / parts-fail" profile Baker describes.

---

## 19. "Astera copper"
**Where:** [01:05:07] – [01:08:37]

> "Astera was in a lot of **copper-loser baskets**. Astera's biggest product is going to be a **switch**. You use both copper and optics to connect switches to accelerators. … Definitionally, if you're a switch company or an accelerator company, you cannot be a copper loser because you're going to be on the other side of that connection."

The structural claim:
- Quant baskets miscategorized Astera Labs (ALAB) as a *copper loser* (a victim of the optical transition).
- But Astera's flagship next product is a **switch**, and switches sit *between* copper and optical — so they win on *both* sides.
- Baker calls out **basket / factor mispricing** as the biggest 2026 opportunity now that AI sub-sector correlations broke down in January (DRAM diverged from NAND/HDD, scale-up vs scale-out networking decorrelated, etc.).

This dovetails with §16 — the same mispricing that breaks the cross-section also creates Astera-style names that are caught in the wrong factor basket.

---

## 20. "Fact-check this guy's slavery quote"
**Where:** [01:18:02] – [01:18:54]

The exact claim:

> "**Slavery was endemic to essentially almost every civilization, and slavery was really ended by the British Empire.**"

### Your contention, addressed first

> *"My main contention is that the British Empire created slavery on a global scale. Is that not correct? You can't claim that you saved something if you started it."*

You're substantively right, with one precision fix on the word "created." Slavery as an *institution* predates the British Empire by thousands of years — Mesopotamia, Egypt, Greece, Rome, the Arab and Ottoman trades, the Aztec and Inca empires, multiple African kingdoms, etc. So the British did not *invent* slavery in any literal sense.

**However, what they did do is essentially what your sentence is pointing at:** Britain — alongside Portugal, Spain, France, and the Dutch — **industrialized, racialized, and globalized chattel slavery on a scale the world had never seen.** Specifically:

- Britain became the **single largest carrier in the trans-Atlantic slave trade** during the 18th century, dominating the volume of forced shipments out of West Africa.
- British capital, ports (Liverpool, Bristol, London), and credit networks built the financial machinery that scaled the trade.
- The plantation economy in the British Caribbean (Jamaica, Barbados) and the American colonies was the *demand* engine the British state defended militarily and politically for ~200 years.
- The legal innovation of **race-based, hereditary, chattel slavery** — slavery as a permanent racial caste passed to the next generation — was an Atlantic-system creation that the British helped codify and propagate globally through colonial law.

So a sharper version of your sentence is:
> *"The British Empire didn't invent slavery, but it scaled the trans-Atlantic slave trade to global, industrial, race-based proportions for two centuries before turning around and abolishing the very system it had built."*

That framing is historically defensible and, to your moral point, **it is not credible to take sole credit for ending a global institution that you spent 200 years engineering at industrial scale.** Britain's 1807 Slave Trade Act, the 1833 Abolition Act, and the Royal Navy's West Africa Squadron did all happen — and they did materially suppress the Atlantic trade — but framing that as Britain "really ending slavery" erases:

- **Haiti (1791–1804)** — enslaved people abolished slavery themselves by revolution, before any British Act.
- **Northern U.S. states** — progressive abolition from 1780.
- **France (1794 / 1848)**, **Denmark (1803)**, **Mexico (1829)**.
- **The U.S. Civil War (1861–65)** — emancipated ~4 million people, by far the largest single emancipation event, and not a British action.
- **Brazil — 1888** (Lei Áurea), the largest receiver of trans-Atlantic enslaved people in the entire trade.
- **Slavery in the Islamic and Arabian worlds persisting into the 20th century** (Saudi Arabia: officially 1962; Mauritania criminalized only in 2007).
- **Modern slavery today** — ILO/Walk Free 2023 estimate: ~50 million people. Not "ended."

### Net call
Baker's first clause ("endemic to almost every civilization") is **broadly correct.** His second clause ("really ended by the British Empire") is **the part you're right to push back on** — it's both an *overclaim* (many other actors abolished slavery independently or earlier) and a *moral sleight of hand* (Britain spent two centuries building the very trans-Atlantic system it then dismantled). The cleanest one-line correction is:

> *Britain led the 19th-century abolition movement and its navy materially suppressed the Atlantic trade — but only after spending two centuries building that trade into the largest industrialized slave system in history, and abolition globally was a multi-actor process including Haiti, the U.S. Civil War, Brazil 1888, and slavery in parts of the Islamic world persisting into the 20th century.*

---

## Quick portfolio / reading-list residue from this episode

These items aren't in your raw notes but fall out naturally from the above and are worth a follow-up note:

- **Watch TSMC leading-node capex** as the bubble dashboard (§7).
- **Track Astera Labs basket assignment** in quant factor data; the re-rate happens when it's pulled out of "copper loser." (§19)
- **Track the NVDA vs GE Vernova spread** as a single chart — the cross-section is incoherent. (§13, §17)
- **Build a PSU-proxy-diff agent** for your covered names. (§15)
- **Re-read Carlotta Perez** — *Technological Revolutions and Financial Capital* — given the bubble framing he keeps returning to. (§3)
- **Move off Max plans** for Claude/Codex; usage-based or enterprise only. (§9)
- **Watch for the Trainium 3 ramp** and the **MI450** as the only ASICs Baker thinks have any chance of "tugging on Superman's cape" (TPU v8 made aggressive tradeoffs that hurt Google).
- **Orbital compute timeline:** inference moves first; training stays on Earth "for a long time." (§2)

---

*Generated from `transcripts/2026-05-20-watts-wafers-and-the-future-of-ai-infra-gavin-baker-Mmj_G9RlW-I.md`.*
