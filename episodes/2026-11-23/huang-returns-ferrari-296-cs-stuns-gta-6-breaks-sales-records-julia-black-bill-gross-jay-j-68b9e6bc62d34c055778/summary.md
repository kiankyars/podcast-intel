# Huang Returns, Ferrari 296 CS Stuns, GTA 6 Breaks Sales Records | Julia Black, Bill Gross, Jay Jandrain, Lincoln Murr, Thijs Simonian, Elliott Potter

- Podcast: TBPN
- Published: 2026-11-23
- Source: https://share.transistor.fm/s/ca7b9f75
- Relevance: 4/5

Thijs Simonian explains how he used coding agents to build Worldcraft's Minecraft map generator and what broke when players arrived. Linq CEO Elliott Potter describes the physical infrastructure behind voice agents. Supertake founder Lincoln Murr discusses the difficulty of translating an investment idea into a portfolio that actually tracks it.

**Why it matters:** These deployments expose costs a demo can hide. A generated world needs servers that survive launch, a voice agent needs a short network path to its users, and an investing agent needs access to instruments that reflect a user's idea.

## Signals

- **Worldcraft used about 250 agents to improve one shared generator against thousands of real locations.** [01:45:13; 01:45:38; 01:46:56; 01:47:23; 01:47:36; 01:48:53; 01:49:08] _agents_developer_tools; observation; medium confidence._ Simonian says the generator combines smaller models and rules. It uses OpenStreetMap building classifications to furnish interiors, so an office may get cubicles even when the real layout is unknown. Serving the world posed a separate problem. The server crashed almost immediately after launching with a 100-player cap. Simonian then worked with experienced Minecraft operators and estimates the rebuilt system can handle thousands of players. He gives no measured peak concurrency.
- **Linq is planning regional infrastructure expansion to cut latency for voice agents.** [01:56:16; 01:56:41; 01:56:57; 01:57:02; 01:57:11; 01:57:15; 01:57:26] _infrastructure_energy; observation; medium confidence._ Potter says Linq owns and operates hardware, started in Alabama and has about 90% of its customers on the West Coast. Its new wideband calling codec expands the audio frequencies available to an agent. Bringing infrastructure closer to customers addresses a different part of the conversation experience, the delay on each turn. The interview gives no before-and-after latency measurements. Linq also [announced a $90 million Series B](https://linqapp.com/blog/linq-raises-90m-welcomes-ben-horowitz-to-the-board).
- **Linq sees a checkout advantage for agents offered by businesses that already hold a customer's address, preferences and payment method.** [01:59:40; 01:59:59; 02:01:09; 02:01:27; 02:01:30; 02:01:56] _applications_business_models; opinion; medium confidence._ Potter names DoorDash as a customer and contrasts its stored information with the onboarding a general-purpose agent faces on a first purchase. He says a conversation carried over Linq can capture a user's request and identifies reliable verification that a human approved a particular charge as an open problem.
- **Supertake's AI can propose a portfolio for a thesis even when the available instruments offer a poor way to express it.** [01:38:03; 01:39:21; 01:40:54; 01:41:20; 01:41:42; 01:41:54; 01:42:35] _applications_business_models; inference; medium confidence._ Murr describes connecting brokerage accounts and building a portfolio conversationally. His US soccer example illustrates the limitation. A media-rights holder can make most of its money elsewhere, so its shares can rise even if soccer viewership falls. Supertake lacked short positions at interview time. Murr presents contracts tied to a specific sport's viewership as a possible future solution and says the business model is still undecided.

## Changed Views Or Tensions

- Worldcraft's builder distinguishes the workload used to create a reusable program from the cost of operating the resulting game for concurrent players.

## Follow-Ups

- Compare Worldcraft's measured peak concurrency, serving cost per player-hour and sponsor or in-game revenue after the rebuild.
- Track median and tail voice response times before and after Linq adds capacity nearer users.
- Look for cases where Supertake discloses how much of a portfolio's return came from the thesis and how much came from unrelated exposures.
