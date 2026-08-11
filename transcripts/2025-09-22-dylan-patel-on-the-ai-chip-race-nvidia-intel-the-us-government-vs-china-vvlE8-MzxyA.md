# Dylan Patel on the AI Chip Race - NVIDIA, Intel & the US Government vs. China

- Date: 2025-09-22
- Channel: a16z
- Duration: 1:38:58
- URL: https://www.a16z.news/p/dylan-patel-on-the-ai-chip-race-nvidia
- Source: `a16z transcript page`
- Note: timestamps are preserved in the paired JSON file.

## Transcript

Erik Torenberg Dylan, welcome back to the podcast. Dylan Patel Thanks for having me.

NVIDIA’s Intel investment Erik It just so happens that there's some big news just as we're having
you, NVIDIA announcing a $5 billion investment in Intel and them teaming up to jointly develop
custom data centers and PC products. What do you think about the collaboration? Dylan I think it's
hilarious that like NVIDIA could invest, it gets announced, and their investment is already up 30%.
$5 billion investment to a billion dollar profit already. I think it's fun because they need their
customers to really have big buy-in. So when their potential customers buy in and commit to certain
types of products, it makes a lot of sense.

And it's kind of funny in a way because in the past, there was this whole thing around how Intel was
sued for being anti-competitive with their chip sets. And NVIDIA actually got a settlement from
Intel, way back when, when the graphics were separate from the GPU and the graphics were really put
on the chip set, which had like all this other I/O, like USB and all this stuff. So it's kind of a
funny turn of events that now Intel is going to make a chiplet and package it alongside a chiplet
from NVIDIA, and then that's like a PC product, right? So, you know, it's kind of poetic that
everything has gone full circle, and Intel is sort of crawling to NVIDIA, but actually it might just
be the best like device, right?

I don't want an ARM laptop because it can't do a lot of things. And so an x86 laptop with NVIDIA
graphics fully integrated would be probably the best product in the market. Erik So are you
optimistic? How do you think this will go? Dylan I mean, sure. I hope, right? I'm a perpetual
optimist on Intel because I have to be. I was thinking that the structure of the deal that at least
like a lot of the government folks and Intel were sort of trying to go for was big customers and the
biggest suppliers directly give capital to Intel. But this is sort of the other way around, where
they're buying some of the stock, having some ownership, but they're not really like diluting the
other shareholders. And then the other shareholders will get diluted/everyone will get diluted when
Intel finally does raise the capital from the capital markets. But because they've announced these
deals, and they're pretty small, right? 5 billion NVIDIA, 2 billion SoftBank, US government was 10.
These are still relatively small.

Guido Appanzeller Pretty small, yeah. Dylan On the nature of things, right? I mean, last time I
think I said Intel needs like $50 billion, right? Now when they go to the capital markets, it's
better, and hopefully they get another, you know, couple of these announcements. There's all sorts
of speculation that Trump is involved in getting these companies to invest. Now you know the
government as well of course. And now, you know, is Apple gonna come invest and also do something
with Intel? Or who else will come in? And that'll really boost investor confidence. Then they can
dilute/go get debt.

Sarah Wang Like a Warren Buffet coming into a stock. The Jensen is like the Buffet Effect for the
semiconductor world. Guido, you were the CTO of the Intel Data Center and AI BU. What are your
thoughts? Guido I think it's really good for customers and consumers in the short term, right?
Having, having both Intel… And like specifically with the laptop market, right? Having the two
collaborate is amazing. I wonder what's gonna happen with any of the internal graphics or AI
products at Intel, right? They might just push a reset and give up on that for now, right? They
currently don't have anything competitive, right? There was the Gaudi effort. That's more or less
done, right? There was the internal graphics chips, which never competed really at the high end,
right?

So from that perspective, it makes a lot of sense for both sides. For Intel, they needed a breath of
fresh air. They were sort of desperate. So I think it's a very good thing. I think AMD is fucked. If
your two archnemeses suddenly team up, it's the worst possible news you can have, right? They were
already struggling. Their cards are good. Their software stack is not right. They were getting very
limited traction. And they now have a bigger problem that side. I think ARM is a little bit screwed
as well because their biggest selling point was sort of like, “Look, we can partner with everybody
that doesn't want to partner with Intel.” NVIDIA is probably the most dangerous of the future CPU
competitors, right? And so they now suddenly have access to Intel technologies and might get in that
direction. It remixes the card, right? I did not see this coming. I think it's an amazing
development.

Sarah Yeah. It'll be very interesting to see this play out. To Erik's point, packed news week, the
other thing that we wanted to pick your brain on, since we have you here, Dylan, is the other news
dropping on Huawei unveiling their kind of AI roadmap. And you know, obviously they're hyping up the
capabilities. I think you guys have been sort of ahead of the curve of trying to gauge hey, what can
the 950 SuperCluster actually do? But would love your thoughts on everything that's going on from
the China front, right? And this is kind of coupled with DeepSeek saying their next models are gonna
be on domestically produced Chinese chips, the Chinese government kind of banning companies from
buying the produced specifically for China NVIDIA chips.

So there's just sort of a lot of dominoes falling right now in the semi market in China. But would
love your take overall and I mean, drill into some detail. Dylan Yeah, I think when you sort of zoom
out to even like, you know, let’s walk from 2020 because I think it's really important to recognize
how cracked Huawei is, or even just historically, like they've always been really good. Sure
initially they stole like Cisco source code and firmware and all this stuff, but then they rapidly
passed them up as well as every other telecom company. In 2020, they released an Ascend chip and
submitted it to impartial public benchmarks. And they were the first to bring 7 nanometer AI chips
to market. They were the first to have that. Now you could still say NVIDIA was ahead, but the gap
was like nothing, right? And this was when they could access the full foreign supply chain. This was
when they just passed Apple to be TSMC'S largest customer. They were clearly ahead of everyone on a
manufacturing supply chain sort of design standpoint on a total basis.

Now, of course, NVIDIA still had higher market share, but it was so nascent then, like they could
have really taken over the market. Huawei got banned by the Trump one administration from accessing,
and then it went into effect in 2020, the full ban. And so they were only able to make a small
volume of these chips, but they had trained significant models on these chips that they made then.
And then over the next couple years, NVIDIA continued to accelerate. Huawei, because they were
banned from TSMC, had to go and try and figure out how to manufacture at SMIC, the domestic TSMC.
And then they were also in parallel trying to go through shell companies to manufacture at TSMC and
acquire memory from Korea and so on and so forth.

So by the end of ‘24, they had this had gotten in full swing and it was caught, right? It was
caught, and they finally shut it down. But they were able to acquire 3 million chips, 2.9 million
chips from TSMC through these other entities. Roughly $500 million worth of orders, which ends up
being a billion dollar fine that the US government gave TSMC if I recall correctly. Or at least
there was a Reuters article. I don’t know if they actually issued it, which is important and
interesting to gauge because the number of Ascends floating out there is has not consumed this
entire capacity yet.

So now we get to 2025. The H20 got banned in the beginning of the year. NVIDIA had to write off, you
know, huge amounts of money. Our revenue estimate for NVIDIA and China for just H20 was north of 20
billion because that's what they were booking in capacity/had to write off. And then it got banned.
They cut the supply chain, like they just said, “No, we're not doing this anymore.” They had their
inventory, it gets reapproved, they resell the inventory, but now they're like, “Do we even restart
production?” is NVIDIA's question. And now you have China saying, “Hey, we don't need NVIDIA, we
have domestic alternatives.” Whether it be Huawei or Cambricon, these companies have capacity, but
most of this capacity is still foreign-produced, right? Whether it be wafers from TSMC, memory from
Korea, Samsung and SK hynix. So the question is sort of like, how much can they do domestically?

And there's sort of two fronts there. There's the logic, i.e., replacing TSMC, and there's the
memory, i.e., replacing hynix, Samsung, Micron. And on the logic side, they are behind, but they're
really ramping there, and I think they can sort of get to the production capacity estimates needed,
and the US is still allowing them to import all the equipment necessary, pretty much. The bans are
really for beyond the current generation of technology, beyond 7 nanometer. The bans are really for
5 nanometer and below, even though the government says they're for 14 nanometer, the actual
equipment that's banned is only for below 7 nanometer. And so they'll be able to make a lot of 7
nanometer AI chips and maybe even get to 5 using existing equipment for 5 nanometer rather than like
taking the new techniques.

And so like there's the logic side, and then there's the memory side. And the aspect of Huawei's
announcement that was surprising was that they're doing custom memory, right? That's, that's the
part that is sort of like, hey, this is really exciting. They announced, you know, two different
types of chips for next year, one that's focused on recommendation systems and prefill, and then one
that's focused on decode. Guido There's the trend these days.

Dylan Yeah. And NVIDIA, the same thing. They just announced a prefill specific chip recently.
There's numerous AI hardware startups that are really focusing on prefill versus decode. And so the
sort of split of inference into two workloads. You know, Huawei is doing the same thing for their
next year chip. And what's interesting is the decode one has, you know, custom HBM. What does that
mean? What is the manufacturing supply chain? That's the one that's tricky, right?

How much can they manufacture of that custom HBM? And NVIDIA and others are also adopting custom HBM
only starting next year. You know, yes, the manufacturing capacity is not there. It is gonna consume
a bit more power. It's gonna be slightly lower bandwidth. But the fact that they're able to do, you
know, some of the same things that NVIDIA plans to do, AMD plans to do in their memory is evidence
that they're catching up. But then, you know, the main question that remains is production capacity.
So as far as like, hey, NVIDIA is banned in China, right? Like they're saying don't buy NVIDIA
chips. I think for a period of time that's fine because—fine for China, right, from a perspective of
“Hey, I'm China,” that's fine because you have all this capacity that you shipped in in 2024, they
haven't turned into AI chips.

Now you're turning them into AI chips, you're running all that stockpile down. What about the
transition from running that stockpile down to ramping your new stuff? And that, that, that
transition is the one that's really tricky. China's either shooting itself in the foot by not
purchasing NVIDIA chips during that time period, or China is able to ramp. I think they'll be able
to ramp, I think it'll take a little bit longer. And there will be sort of a gap in between where
China probably backtracks and says it's fine. Like ByteDance is like begging for NVIDIA chips,
right? They use some Cambricon, they use some Huawei, but they really want to use NVIDIA because
it's way better.

They don't care about the domestic supply chain. They wanna make the best models. They wanna deploy
their AI as efficiently as possible. And so this is like, you know, the government can mandate them
to like not do it, right? So it's not that NVIDIA is not competitive, it's that the government is
sort of trying to instigate it. And then like, I guess the last sort of thing is like, you know,
there's always the argument of like, hey, if banning NVIDIA chips to China is so good for China, why
didn't China do it for itself? And they're finally doing it for themselves. So again, like, it'll be
interesting to see.

Smuggling is still happening, right? Re-exportation of chips from, you know, other countries to
China, that is still happening, at some volume, low or medium volume, right? But then, you know, the
direct shipments of NVIDIA chips that are legally allowed to China are not necessarily happening
today, but may have to restart at some point because China won't have the production capacity to…
You know, they would just have so many fewer AI chips being deployed domestically versus the US. And
at some point you kind of have to pick like, am I all about the internal supply chain, or am I all
about chasing, you know, super powerful AI.

Guido So is there an angle here about a negotiation angle as well? Because currently there's still
discussions ongoing. What exactly are the boundaries? What can be exported to China? So these are
sort of well-timed announcements if you want to make the point that, you know, the US should allow
more exports. Do you think that's a factor or not? Dylan Yeah, so in the report we did a few weeks
ago about the production capacity of Huawei and the supply chain, there was a bit in there that we
wrote about how, you know, honestly, like if you were China and you do want NVIDIA chips, actually,
how do you play this? And it's by hyping up your domestic supply chain. It's like, yes, we can do
everything. It's Huawei, announce the most crazy shit possible, announce three years of roadmaps
that are… Guido So you think they read your report, basically.

Dylan No, no. I think they knew, I mean, they were already bid and then like, say we're banning
NVIDIA, right? Then the government official is gonna think, alongside sort of like lobbying from
domestic players, like “Of course we wanna ship them better AI chips, like, we're losing this
market. We can't lose this market.” And it's sort of like, it is 10,000 IQ, right? And we're here
playing checkers while they're playing chess.

Is Huawei just hype? Sarah Well, so I guess negotiating chip aside, in that report you talked about
HBM or high bandwidth memory being a bottleneck to Huawei. To your point on one of the surprising
aspects of the announcement, do you think it's credible that it's no longer a bottleneck based on
what they're saying? Or is it just hype? Dylan I think production-capacity-wise, it is still
absolutely a bottleneck. Certain types of equipment required for making HBM need to be imported.
They're working on domestic solutions, but as far as we know, they have not imported enough
equipment for this.

Although, if you look at Chinese import data for different types of equipment, right, there's sort
of like fabs spend, you know, roughly, it depends on the process technology, but fabs spend roughly
different amounts of money on lithography, etch, deposition, metrology, right? Like these different
steps. And historically lithography has hovered around, you know, 17, 18%. With EUV it grew to 25%,
right? But China, because they wanted to stockpile lithography, and they were worried about the
becoming banned, they were importing lithography at a much higher rate than that, right?

Like 30, 40% of their equipment imports were lithography. And they were just stockpiling lithography
equipment. This is sort of like reversed now in that like, if you look at the monthly import export
data both into provinces in China, but also out of countries, you can see that etch specifically is
skyrocketing. And the main thing about stacking HBM is that when you have each wafer, you have to
create like this thing called a through-silicon via so it can connect from the top to bottom, and
then you stack them on top of each other, right? 12 high, 16 high for HBM. That's how you make super
high bandwidth memory. And their import for etch is like skyrocketing now.

They don't have the production capacity yet. How fast can they ramp it as a function of how much
equipment can they get, A). And B), like the yields, right? Improving yields is really hard on
manufacturing. Intel and Samsung are really good, and TSMC is just amazing. Not that those companies
suck, like, I think is a better way to put it. And so, you know, it's those two things. I think
yield, they haven't even started production of HBM3. They've only done some sampling of HBM2. HBM3
came out a few years ago. So there's still quite a bit of ways to go on like going up the learning
curve. Obviously I expect them to catch up faster than it took, you know, the technology to be
developed because it exists in the world. We know how to do it. It's just a matter of actually doing
it versus inventing it. And then the other one is sort of the production capacity. You know, a
couple months of import-export data is not enough to set up for years’ worth of supply chain build
up, which is what we have today in Korea, for the Korean companies.

Now, hynix is also investing in the US in Illinois, and then Micron is primarily in Japan, the
American memory companies primarily in Japan and Taiwan, but they're also expanding in Singapore and
the US now. Like there's so much capital that's been invested, it would take some time for China to
build up that production capacity to actually match the West. And when I say, “the West,” I mean
non-China East Asia in production capacity. So it'll take some time to get there. And I think it's
like, “Hey, we can design this.” It's always a question of “Can we manufacture?” And then the thing
like that Jensen would say is like, you're betting on China not being able to manufacture, like… You
know, it's a matter of when not if. And that's the whole calculus that I think the US government has
to be aware of when they're like, “Hey, what level of AI chips do we sell? Do we sell everything?”
Probably not because AI is far more powerful, and the end market of AI is gonna be way larger than
the end market of semiconductors and equipment.

You know, what level do we sell at? Well, how much can China make at each specific, you know, sort
of performance tier. And then, you know, analyze that, and what's the volume, and then figure out
what is okay, which is like maybe a little bit above or around the same level.

Advice to Jensen Sarah Yeah, so, to your point on like playing chess versus checkers, if you're
Jensen, what would your next move be, given the situation at hand? Dylan It's both partially true
that he’s afraid of Huawei more than he is like an AMD, right? Sarah He called him “formidable.”
Dylan I mean… Like Huawei has beat Apple, right? They passed Apple up in TSMC orders. They passed
Apple up in phone market share, not in the US but like in many parts of the world, before the bans
came down. And then even now they're growing back again in market share without like western supply
chains. You know, they've done this to numerous other industries. I would say Apple's like a
formidable competitor, right?

They've beaten a lot of industries, and so it's reasonable that he is afraid of them. And he's not
afraid of AMD. I think like the best thing is like try sow as much like what Huawei announced is
reality rather than like their hope target. And sow away all doubt on manufacturing capacity, which
I think is not fair, right? Like I think manufacturing capacity is a real bottleneck for them. And
then the yield learnings, real bottleneck. Like temporary maybe. We’ll see how long, and we'll see
how fast the rest of the NVIDIA technology advances past what Huawei is capable of and how fast
Huawei is able to close the gap. But I think his main sort of pitch would be, Huawei is real.
They're a formidable competitor. They're going to take over not just the Chinese market, but also
foreign markets. Whether it be the Middle East or Southeast Asia or South Asia or Europe or LATAM,
right.

Everywhere besides America. Noah Smith has this analogy, right? This whole idea is that you should
Galapagos China, right? Make them have their own domestic industry that is so different from the
rest of the world, right? Kind of what happened with Japan in the ‘70s and ‘80s and ‘90s. Their PCs
were so specific and hyper-optimized to the Japanese market would like… I don’t know if you've seen
the weird scroll wheel on these Japanese PCs. It's like you go like this and it scrolls, right? And
then the touch pad is a circle, and then that's around it.

It's like things like that are so weird that the rest of the world doesn't care. But Japan market
likes it, right? And his whole idea is like, let's Galapagos them, i.e., keep their technology
within China, and then that's like dead weight loss and they never expand outside, versus, that we
serve the whole world. But the whole risk is that the opposite can also happen, right? Our
technology is hyper-optimized to running language models at this scale and RL. Hardware-software co-
design can take you down a path of the tree that like is a dead end. And then China, like, because
they're not allowed to access this tree, they're like, “Oh, okay.” Then they end up in the like
optimal spot, right? We hit a local maximum, they hit a global maximum. That sort of like
technological Galapagos-ing is sort of what Noah Smith's analogy is. I like it a lot. I don't know
if it's accurate, but it's an interesting one.

NVIDIA bull and bear cases Sarah Yeah. I love that. Well actually, maybe just taking a step back
from current events, even though there's so much to talk about right now, last time you appeared
with us, NVIDIA came up, obviously, and you talked about a couple of the potential paths forward for
NVIDIA. Erik Give us maybe the bull case, the bear case. Dylan There's a lot embedded in their
numbers now. But what's interesting is consensus for the banks is like for across the hyperscalers,
so, Microsoft, CoreWeave, Amazon, Google, and Oracle, Meta. So it's the six hyperscalers, right, who
I would consider hyperscalers.

The consensus for the banks is $360 billion of spend next year across all of them. And my number is
closer to like 450, 500. That's based on like, you know, all the research we do on like data centers
and like tracking each individual data center in the supply chains. Guido This is just NVIDIA spend,
right? Dylan This is CapEx for the hyperscalers. That CapEx gets split up across different
companies, but the vast, vast majority still goes to NVIDIA.

NVIDIA is where they can't take share, right. They grow with the market/defend share. And so the
question is like, how fast is the growth rate of CapEx for hyperscalers and other users? And the
reason I included Oracle and CoreWeave as hyperscalers, even though they're traditionally not called
hyperscalers, is because they're OpenAI’s hyperscaler. So, you know, when you look at the Oracle
announcement, right? First of all the Oracle announcement, I don't understand why people don't think
this is crazier. They did the most unprecedented thing in the history of like stocks and companies
ever. They gave a four year guidance.

And it made Larry the richest man in the world. You know, like all these things. Anyways, you know
the question is like, how fast does revenue grow? Do you think OpenAI, which signed a $300 billion
plus deal with Oracle, will actually be able to pay $300 billion across raising capital and revenue?
And it gets to a rate of like over $90 billion a year, in just a handful of years. So it's like, do
you believe the market will grow that fast? It's very possible. And it's very possible for like, you
know, OpenAI, what is their revenue gonna be exiting next year?

Some people think 35 billion, some people think 40 billion. Some people think 45 billion ARR by the
end of the year, next year. This year they hit 20 ARR, you know, so if that growth rate is
maintained, then all of that cost goes to compute plus all the capital they continue to raise. And
again, there are financials that they sort of like gave to investors for their last round was like,
“Hey, we're gonna burn like $15 billion next year. It's probably more likely gonna be like 20. And
you stack this on and they're not turning a cash flow, they're not gonna be profitable until 2029.

So you sort of have like, they're gonna continue to be burn 15, 20, $25 billion of cash each year,
plus revenue growth. That's their compute spend. And you do this for Anthropic, you do this for
OpenAI you do this for all the labs. It's very possible that the pie does get to, you know, you
know, more than 500, you know, not 360 billion next year, 500 billion next year for total CapEx. And
the pie continues to grow for hyperscalers. NVIDIA says, actually it's gonna be multiple trillions a
year on AI infrastructure, and he's gonna capture a huge portion of it. That's his bull case, right?
That's the bull case is AI is actually so transformative, and the world just gets covered in data
centers, and the majority of your interactions are with AI, whether it's like, you know, business
productivity and telling an agent to do some code, or you're just talking to your AI girlfriend Ani,
right? Like, it doesn't matter. You know, all of this is running on NVIDIA for the most part. The
bear case is, you know, even if it does grow a lot… Guido Save the bear case for a second. I think
fundamentally the value creation, I think, personally, is there, right? I mean, to create trillions
of dollars of value with AI, I can totally see this happening. So assume it's true, where will
NVIDIA top out?

Dylan I guess, how much do you believe in takeoffs, right? So like, if there is like a takeoff
scenario, right, where like powerful AI builds more powerful AI builds more powerful AI, or, you
know, that creates more and more… Each level of intelligence enables more for the economy, right?
Like how many monkeys can you employ in your business versus how many humans, right? Or how many
dogs, right? There’s sort of like, what is the value creation of a human versus a dog? Sort of like
the same with AI.

In this case, the value creation could be hundreds of trillions, if not… Guido Do you need this? I
mean, if you take every white collar worker and make them twice as productive with AI, that's in the
hundreds of trillions, isn't it? Dylan Yeah but like, what is twice? You know, like, I mean like if
you talk to people at the labs, right? Like twice as productive, what does that even mean? It's
replace them, right? And it's be 10 times better than them. I mean I don’t know how soon… Guido If
white collar work is essentially useless without a constant stream of LLM tokens, that make them
productive, right? At that point, you basically can tax every single knowledge worker in the world,
right? Which is most workers in the world long term. I mean, what's your guess? Give us a number.
What's the cap for NVIDIA?

Dylan The cap? I mean why aren’t we making a Matrioshka brain? I don't know, at some point the
machine says humans don't need to live and I need even more compute. Guido One step before that.
Dylan Are we colonizing Mars yet? Guido TBD. Dylan I don't know, man. I find it completely
impossible to predict anything beyond five years given how much stuff is changing. I'll leave it to
economists, right? Honestly like, you know, supply chain stuff is like three, four years out and
that's it. And then fifth year is sort of yellow, right? I just try and ground myself with the
supply chain stuff, right?

Supply chain, and then like, what is the adoption of AI, and what's the value creation, what's the
usage? And you can see that in like a short horizon beyond that like, I don’t know, are we all gonna
be connected to computers, like BCIs and stuff? Like, I don't know, dude. Are humanoid robots, are
they gonna be… I mean you saw Elon's thing, right? He's like, yeah, humanoid robots are why Tesla is
worth more than 10 trillion. It’s like, okay, great. What is all that being trained on? Great,
NVIDIA. Okay. Awesome. So then that's worth also 10 trillion, right? Like, I don't know, like, it's
too out there for me. I don't like the out there discussions.

Sarah Very fair. Dylan Read some sci-fi books.

NVIDIA’s moat Sarah So just pulling out the thread where you talked about, I mean, this is kind of a
throwaway comment, but how market share can't really grow just because it's such a dominant market
share. And you guys talked about the moat of NVIDIA last time. And obviously this moat is tied to
maintaining that very high market share that they currently have. And I love this sort of historic
journey you took us through with Huawei just earlier. Can you kind of walk through what NVIDIA did
throughout history to build their moat?

Dylan It's super awesome because, you know, they failed multiple times in the beginning, and they
bet the whole company multiple times, right? Jensen is just crazy enough to bet the whole company.
Whether it was certain chips ordering volume before he knew it even worked, and it was all the money
he had left, or ordering volumes for projects he had not won yet. I heard a rumor that, or not a
rumor, but like a story from someone who's like a graybeard in the industry and I think would know
was like, “Yeah, no, no, no, like NVIDIA ordered the volume for the Xbox before Microsoft gave them
the order.” He was just like, “Fuck it. Yolo.” I'm sure there's more nuance there, like, you know,
verbal indication or whatever, but like the order was placed before he got the order, right, is what
he said. You know, there's cases like with the crypto bubbles, right? Like there was a couple of
them, but like NVIDIA did their damn best to convince everyone in the supply chain that it wasn't
crypto and that it was gaming. That it was durable real demand and it gaming and data center and
professional visualization and therefore you guys should ramp your production.

And they all ramped production and spent all this CapEx on increasing production and, and building
out new lines for them. And they pay per item. And then they bought them and sold them and made
shitloads of money. And then when it all fell apart, they just had to write down a quarter's worth
of inventory, whatever. Everyone else was like, “Well, crap, I have all these empty production
lines.” But like, what did AMD do then? Their chips were actually better for crypto mining on an
amount of silicon cost versus how much you hash. But like, they just didn't. AMD was like, “Ah,
we're gonna not really raise production.” Like, as a reasonable, you know, thing. So it's sort of
like, strike while the iron is hot. And so like, you know, the same has happened with NVIDIA, right?
In recent times, like sort of, they've ordered capacity that no one believes multiple times. They
see them in demand, obviously, but in many cases they're just like, their number for like Microsoft
was higher than Microsoft's internal planning, right?

And then Microsoft's internal planning went up, but like their number for Microsoft was way higher.
And it's like, “Ah, we just don't think Microsoft is gonna need this much, even though they tell us
this.” It's like, who the heck? It was like, no, no, no customer, you're gonna buy more like, and,
and orders. Right? And then when the orders come through the supply chain, it's like, I have to pay
NCNR, non-cancellable, non-returnable. I asked a question in Taiwan once, it was Colette, which is
the CFO, and Jensen, CEO. They were both there.

It was a room full of like mostly finance bros and they were asking stupid finance questions like
three days before earnings. So obviously they just could not answer anything because it's like, you
know, SEC regulations. But then my question to them was like, “Look Jensen, you're like, so vibes-
driven and like very gut feel, and like very visionary. And then Colette's, you know, CFO, like
she's amazing in her own right, but like, those personalities clash. How do you work together?” And
he's like, “I hate spreadsheets. I don't look at them. I just know.” Like that's his response. And
it's like, of course, you know, the best innovators in the world have really good gut instinct.

And so the gut instinct to order with non-cancellable when you don't know. And they've had to write
down, over their history, multiple times, many, many billions of dollars in total orders, whether it
be, you know, the H20, which is more regulatory, but like other cases they've ordered and had to
cancel. Guido Is it many billions? Dylan It's many billions. Guido Peanuts. Dylan Well it depends,
right? The crypto writedown was like multiple billion when their stock was like less than a hundred
billion.

Guido It’s peanuts compared to the upside, right? Dylan I think everything he did was right. And I
think everything AMD did was wrong. Like, you know, in that scenario. But like, it is crazy to,
especially in a cyclical industry like semiconductors where companies go bankrupt all the time,
which is why we have all this consolidation is, every down cycle companies go bankrupt. Guido I
mean, if you look from a risk-return perspective, right, these bets were totally worth taking. If
you look at it from “I'm a CEO, I want to have predictable quotas for Wall Street,” it's a very
different story, and I think that's sort of where part of the tension is from.

Dylan I don’t know if you've seen these like, Lee Kuan Yew edits where they're him saying some like
fiery speech,and then it's like some cool music at the end, and it's like showing different pictures
of him. And so we made one of Jensen recently and put it on social media, on like Instagram, TikTok,
XHS, red book, Twitter, of course, like all the different social media. And I really liked it
because he's like, you know, the goal of like playing is to win, and the reason you win is so you
can play again.

And he compared it to pinball where like actually you just play all day and you keep getting more
rounds. And it's like, his whole thing is like, I want to win so I can play the next game. And like
it's only about the next generation, right? It's only about now, next generation. It's not about
fifteen years from now because it's a whole new playing field every time. Or five years from now.
You're right. The risk-reward is correct. Few people take these kind of risks. It's the only
semiconductor company that's worth, I think, even north of $10 billion, that was founded as late as
it was. Like MediaTek was in the early ‘90s and then NVIDIA. And everyone else is like from the ‘70s
mostly.

Sarah I think you raised this great point on, bet the farm. And he's actually been wrong a couple
times, to your point. Dylan Mobile, right? Like what the hell happened with mobile? Sarah Exactly.
And he still takes them. And I think, Marc actually had this great conversation with Erik where he
talked about being founder-run, where you have this memory of the risks you took to get to where you
are today. And so in a lot of cases, if you're a CEO brought on later on, you're sort of like,
“Okay, continue to steer the ship as is.” But in this case, he remembers all the times they almost
went belly up and he’s like, “I’ve got to keep making bets like that.” How do you think he's
changed? I mean, he's been one of the longest running CEOs. He's kind of right up there with Larry
Ellison now. How do you think he's changed over the last 30 years or so?

Dylan I mean obviously like I'm 29. I don't freaking know what he was like. Sarah Fair. Dylan I've
watched a lot of old interviews. Sarah He’s been CEO longer than you’ve been alive. Dylan NVIDIA was
founded before I was born. I'm ‘96, right? Sarah Yeah, maybe anything over the last couple of years,
Dylan I think even like watching old interviews, right? Like, I watched a lot of old interviews, a
lot of old presentations he’s given. One thing is that he's just like sauced up and dripped up. Like
the charisma he's gotten has only gotten stronger, which is an interesting point. I don't know if
it's quite relevant.

Sarah Totally agree with that. Dylan But like the man has learned to be a rockstar more, even though
he was always charismatic. It was like he is a complete rockstar now. And he was a rockstar, you
know, a decade ago too. It's just people maybe didn't recognize it. I think the first live
presentation that I watched, it was extreme, it was CES, like 2014 or 2015 or whatever. It's
Consumer Electronics Show. I'm moderating like gaming hardware subreddits, right? At the time I'm a
teenager. And like the dude is talking only about AI. He's telling all these gamers about AlexNet
and self-driving cars.

It's like, know your audience, first of all, but also, like… It has nothing to do with consumer
electronics and gaming. At the time, I was half like, “Holy crap, this is amazing.” But I also was
half like, “I want you to announce new gaming GPU.” On the forums, quickly, everyone was like, you
know, screw this. I want to hear about the gaming GPUs, NVIDIA is price gouging. You know, of course
NVIDIA has always had the like “We priced to value plus a little bit because we were just smart
enough to know…” You know, I am guessing Jensen just has the gut feel of how to price things. At
least on gaming launches, he'll change the price up until right before the presentation. It really
is like a gut feel thing, probably. And anyways, so he had that charisma to know what was right.

But I think a lot of people were like, “Oh, no,” whatever, “Jensen is wrong. He doesn't know what
he's talking about.” But now, he talks, people are like, “Oh, very…” So it might just be that he's
been right enough. Sarah Yeah. There was a post on X recently that said he had moved up into Godmode
with a select group of CEOs. Dylan Who's the other gods? Sarah It was Zuck. Who was the other God?
Erik Elon? Sarah Elon! Elon, Zuck, and Jensen. Good crew to be in.

Dylan So when we pray to Silicon Valley… Guido The cult now, is it?

Potential successors to Jensen Sarah Exactly. Just one last thing on people. You mentioned Colette,
his CFO, and you know, there's sort of a famously loyal crew at NVIDIA, even though all of the OGs
could retire at this point. Is there anyone akin to a Gwynne Shotwell at SpaceX or previously a Tim
Cook to Steve Jobs at Apple that is at NVIDIA today? Dylan I mean, he had two co-founders, right?
Let's not overlook that. One of them is like, you know, not involved and hasn't been for a long
time, but the other one was involved up until just a few years ago. So it's not just Jensen running
the show. Although he was running the show. There's quite a few people on the hardware side. There's
someone at at NVIDIA that's like mythical to me. Like when you talk to the engineering teams, he
leads a lot of the engineering teams. He is a private person, so I don't wanna say his name
actually.

Sarah Okay, fair enough. Dylan But you know, he’s effectively like Chief Engineering Officer, is
like his role. And people within his org will know who he is. I think there are people like that.
But you know, he's intensely loyal and there's a number of these types of people. There's another
fella who's like, you know… Like there's all these like innovative ideas at NVIDIA, and he's the guy
who literally is like, “We need to get this silicon out now. We're cutting features.” And that's
what he's famously known for. And all the technologists in NVIDIA hate him. This is like a second
guy. This is a second guy. Also intensely loyal to NVIDIA has been around for a long time, but when
you have such a visionary company and forward, one problem is that you get lost in the sauce, right?
“Oh, I want to make this, it's gotta be perfect, amazing.” And these people are like, you know,
obviously they're close to Jensen for a reason because Jensen also believes like these things,
right? Have the visionary future looking, but also like, screw it, cut it, we'll put it in the next
one, ship. Ship now, ship faster, in a space like silicon, which is really hard to do so. The thing
about Nvidia that's always been, you know, super impressive, and it's from the beginning days, where
he's talked about this before, is their first chip, their first successful chip, they were gonna run
outta money, and he had to go get money from other people, to even finish the development. And even
then he just had enough money, because he'd already had a failed chip before this, was the chip came
back and it had to work, otherwise it would not, you know… Because they could only pay for, it's
called a mask set, right?

Basically you put these, like, I'll call them “stencils” into the lithography tool, and then it like
says where the patterns are, and you put the stencil in, you deposit stuff, you etch stuff, you
deposit materials on the wafer, etch it away. And you put the stencil in and like you like tell it
where to put stuff, right? And then the deposition and etch keeps happening in those spots, and you
stack dozens of layers on top of each other. And then you make up a chip. These stencils are custom
to each chip, right? And they cost today in the orders of tens and tens of millions of dollars. But
even back then, it was still a lot of money.

It wasn't that much then, of course. They could only pay for one set. But the typical thing with
semiconductor manufacturing is, you know, as good as you can simulate it, as good as you can do all
the verification, you'll send a design in, and you have to change it. There's gonna be something.
It's so hard to simulate everything perfectly. And the thing about Nvidia is they tend to just get
it right the first time. Even great executing companies like AMD or Broadcom or whoever, they often
have to ship, you know… They're denoted in like “A” and then a number, or “B” and then a number.

So it's like two different parts of the masks. So like, NVIDIA always ships A0, almost always. They
sometimes ship A1. The A is basically the transistor layer. Then the number is like the wiring that
connects all the transistors together. So NVIDIA will start production of the A and ramp it really
high and then just hold it right before you transition to the metal, just in case they do need to
change the metal layers. And so like the moment they're ready, and they've confirmed that it works,
they can just, you know, blast through a lot of production.

Whereas everyone else is like, “Oh, let's get the chip back. Oh, okay, A0 doesn't work. We gotta
make this tweak. Make this tweak.” It’s called a stepping, right? Guido At Intel we were very
jealous of NVIDIA at that time, right? They consistently delivered in the first one. We did not.
Dylan The data center CPU group, there was one product where, you know, I said “A0,” “A1,” or you go
to B if you have to change the transistor layer as well. So it's like “B…” Intel got to like “E2”
once. E2, that's like a 15 revision. This is like the peak of AMD's, like when they went
skyrocketing on market share versus Intel was when Intel was at E2. Like 15 steppings.

Guido It causes quarters of delay. I mean it's catastrophic for a go-to-market. Dylan Yeah. Each
time is a quarter of delay or something. It's absurd. So I think that's the other thing about NVIDIA
is, like, you know, screw it, let's ship it. Let's get the volume ASAP. And so anyways, they have
some of the best simulation, verification, etc, that lets them sort of go from design, you know,
from idea to shipment as fast as possible. You know, cutting out any unnecessary features that could
delay it. Making sure they don't have to do revisions so that they can respond to the market ASAP.
There's a story about how Volta, which was the first NVIDIA chip with tensor cores… You know, they
saw all the AI stuff on the prior generation P100, Pascal, and they decided “We should go all in on
AI.” And they added the tensor cores to Volta, like only a handful of months before they sent it to
the fab. Like they said, “Screw it, let's change it.” And it's like if they hadn't done that, maybe
someone else would've taken the AI chip market, right? So there's all these times where they just…
And those are major changes, but there's often like minor things that you have to tweak, Number
formats or like some architectural detail. NVIDIA is just so fast.

Guido And the other crazy thing is they have a software division that can't keep up with that,
right? I mean if you come out with a chip, and basically no stepping required, it's immediately in
the market, then being ready with drivers and, you know, all the infrastructure in total. That's
just super impressive. NVIDIA’s business in 10 years (00:46:23) Sarah Yeah, I love that point
because you think of NVIDIA benefiting from tailwind after tailwind, but I think both of you are
saying you have to move fast enough and execute well enough to take advantage of those tailwinds.
And by the way, I loved your CES story. I'm just envisioning him more than 10 years ago, talking
about self-driving cars. But you know, if you think about nailing the videogame tailwind, VR,
Bitcoin mining, obviously AI now, you know, one of the things that Jensen talks about today is
robotics, AI factories. Maybe my last question on NVIDIA, what do you think about the next 10 to 15
years?

I know calling beyond five is hard. But like, what does NVIDIA's business look like? Dylan It's
really a question of, and this is like… I think every time I've talked to, you know, some executives
at NVIDIA I’ve asked this question because I really wanna know, and, you know, they won't answer it
obviously, but it's like, what are you gonna do with your balance sheet? Like you are the most high
cash flow company. Like you have so much cash flow. Now the hyperscalers are all taking their cash
flow like way down, right? Because they're spending on GPUs. What are you gonna do with all this
cash flow? Even before this whole takeoff, he wasn't allowed to buy art, right?

So what can he do with all this capital and all this cash, right? Even this $5 billion investment in
Intel is, there's regulatory scrutiny there, right? It's in the announcement, like, yeah, this is
subject to review, right? I imagine that'll get passed, but he can't buy anything big. He's gonna
have hundreds of billions of dollars of cash on his balance sheet. What do you do? Is it start to
build AI infrastructure and data centers? Maybe? But like, why would you do that if you can just get
other people to do it and just take the cash?

Guido Well, he's investing in those, right? Dylan Investing peanuts. You know, he gave recently like
CoreWeave a backstop because today it's really hard to find a large number of GPUs for burst
capacity. Like, hey, I want to train a model for three months. I have my base capacity where I’m
doing all my experiments, but I want to train a big model 3 months down. Guido We know from our
portfolio. Dylan NVIDIA sees this issue, they think it's a real problem with startups. It's why the
labs have such an advantage. You know, right now, most companies in the Valley spend, what, 75% of
their round on GPUs, right?

Sarah At least. Dylan What if you could do 75% in three months on one model run, right? And really
scale and have some sort of like, competitive product, and then you have the model. And then you
raise more capital, or start deploying. What do you do with it? Is it start buying a crapload of
humanoid robots and deploying them, but like, they don't make really that amazing software for them,
in terms of the models, right? The layer below is great. Where they deploy their capital is a
question.

Guido He has been investing up and down the supply chain a little bit though, right? Investing in
the neoclouds, investing in some of the model training companies. Dylan Yeah. But again, small
fries. He could have just done the entire Anthropic round if he wanted to. Of course he didn't.
Right. And like really gotten them to use GPUs. Or like he could've done the entire, you know,
OpenAI round. He could have done the entire, like any xAI round. Erik Do you think these are things
he should be doing?

Dylan I mean like, I don’t know, right? Guido We’ll quote you for the next round… Dylan He could
make venture a dead industry. Take all of the best rounds. Sarah Put us all out of business, yeah.
Dylan You know, you can do the seeds and then have Jensen mark you up. I think picking winners is
obviously really tough for him because he has customers all across the ecosystem. If he starts
picking winners, then his customers will be even more anxious to leave and give even more effort to,
whether it's AMD or you know, some startup or their internal efforts, etc, etc, right? Buying TPUs,
whatever it is. He can't just like invest in these, like, you know, he can do a little bit, right?

A few hundred million in an OpenAI round is fine, or a few hundred million in an xAI round is fine.
CoreWeave, right, like, yeah, everyone's like throwing a fuss about it, but it's like he invested a
couple hundred million early on plus, rented a cluster from them for internal development purposes
instead of renting it from hyperscaler, which is cheaper for NVIDIA to do, right? It's better for
them to do it from them than the hyperscalers. It's like, is he really backstopping CoreWeave that
much? Right. Or, you know, any of the other customers or neo clouds, like there's some investment.
But it's more like this is a google cloud, you know, we'll throw like 5 or 10% of the round. It's
not he’s taking 50% plus of the round.

Guido Is he also reshaping his market? I mean, look, a couple of years ago there were four big
purchases of these cards. You just listed six. To what extent is that… Is that a strategy? Dylan It
is. I think it absolutely is. But he didn't have to put much capital down to do this. Guido Just
chip one earlier than the other? I don't know. Dylan No, but it's like, if you look at the grand
amount of capital that he spent investing in the neo clouds, it’s a few billion dollars.

Guido But he has lots of other levers if he wants to. Dylan Right, right. Allocations, as you
mentioned. What's nice is, you know, historically, you gave volume discounts to hyperscalers. But
because he can use the argument of antitrust, he's like, everyone gets the same price. Guido So
fair. Dylan It’s very fair. It's very fair. You know.

What NVIDIA should do with their cash Erik So what should he do with the cash? Or what to guide his…
Dylan I mean, I think, there's the argument that he should invest in data centers. Only the data
center layer, not what goes in the data center so that more people build data centers, and then if
the market demand continues to grow up, data centers in power are not the issue. Invest in data
centers and power. I've said that to them. They should invest in data centers and power, not in the
cloud layer. Because the cloud layer is, not commoditized, but it's… Commoditize your compliment
right? Is the whole phrase. And I won't say being a cloud is commoditized, but it's certainly like
you have a lot of competitors who are decent now.

And you've educated the commercial real estate and other, you know, infrastructure investment firms
going into AI infra as well. So like, I don't think it's the cloud layer that you invest in. Do you
invest in data centers and energy? Yeah because that's the bottleneck for you in growth really. Is
A), well, how much people wanna spend and can't spend, and B), the ability to actually put them in
data centers. And then like robotics. And like, I think there's like areas he could invest in, but
nothing requires $300 billion of capital. So what do you do with the capital? Like, I really don't
know, and I like feel like Jensen has to have some idea, there's some visionary plan here because
that's what shapes the company, right?

I mean they could just continue to, you know, I mentioned $200 billion of free cash flow, $250
billion of free cash flow a year. What do they do with it? Like, do they just buy back stock
forever? Like, do they go Apple route? And the reason why Apple hasn't done anything interesting in
like, you know, nearly a decade is, you know, they've got, they've got a not visionary at the head.
Tim Cook is great at supply chain. And they're just plowing the money into buybacks. You know,
automotive. The self-driving car thing failed. We'll see what happens with AR/VR. We'll see what
happens with wearables, right? But like, Meta and OpenAI might be even better than them. We'll see.

Like and others, right? So what does he invest in? I have no clue. What requires so much capital, is
the tough question, and actually gets a return. Because the easy thing is like my cost of equity,
right, I just buy back stock. Guido And doesn't completely change the company culture. I think
that's another thing, right? There are probably areas he could invest it in, but you suddenly end up
with the company doing two completely different things, which are very difficult to keep… Dylan But
they do like 10 completely different things, right? I mean, one way to look at it is, “We build AI
infrastructure.” And in the guise of, “We build AI infrastructure,” robots, humanoids around the
world are AI infrastructure. Or data centers and energy as AI infrastructure, Guido So the humanoids
would totally work, right? If you are suddenly pouring concrete and building power plants, it has
completely different cultures, completely different set of people, and getting much, much harder.

Dylan Agree, agree. But there's different ways to do it, like invest in the various companies or
like, backstop the building of power plants, right? Because no one wants to build power plants
because they're 30-year underwriting things. You know, there's all these different areas where could
it use capital to, you know, allow something to happen, right? Not necessarily owning it himself.
Guido And look, looking back on my time at Intel, one of the biggest problems we had was that our
customer base sucked, right?

I mean, we were selling to… Most of the chips went to the large hyperscalers, you know, which
they're way too concentrated and they build their own chips. And so you can push down your prices.
Honestly spending it on diversifying the cloud. Dylan Well the problem was in 2014, you guys should
have just charged so much that your margins were 80%. What would the world have done? Nothing. Guido
The margins were pretty good back then. That wasn't the problem. That was the primary problem.

Dylan They were 60, 65. They weren’t 80s. Guido PTSD is kicking in here.

Amazon’s cloud crisis Sarah Well, wait. I think Guido's comment is actually a really good segue into
something else we wanted to talk to you about, which is the hyperscalers. And one of the reasons
that I love reading SemiAnalysis is you guys make these out-of-consensus calls that you're often
right about. Dylan Only often? Sarah You have a Jensen hit rate. It's very high. Dylan Where’s my
billion-dollar EV-positive bet? Sarah The one that caught my eye was Amazon's AI resurgence. So I
wanted to talk to you a little bit about that just because, you know, I think we found it pretty
interesting being on the ground, helping our portfolio companies pick who their partners are.

And so we have some micro data on this, but can you sort of walk through why they're behind? Dylan
Yeah. So in Q1 2023, I wrote an article called “Amazon's Cloud Crisis.” And it was about all these
neoclouds are gonna commoditize Amazon. It was about how Amazon's entire infrastructure was really
good for the last era of computing, right? What they do with their elastic fabric. ENA and EFA,
right, their NICs, and the whole protocol and everything behind them, what they do for custom CPUs,
etc, right? Like it was really good for the last era of scale-out computing and not this era of sort
of scale-up AI infra, and how neoclouds working commoditizes them and how their silicon teams were
focused on, you know, cost optimization.

Whereas the name of the game today is max performance per cost, right? But like that often means you
just drive up performance like crazy. Even if cost doubles, you drive up performance more, triples,
because then the cost per performance falls still. That's sort of the name of the game today with
NVIDIA's hardware. And it ended up being a really good call. Everyone was calling us out like, “No,
you're wrong because…” And this was when Amazon was like the best stock. And Microsoft really hadn't
started ticking off yet. Nor had like all these other, you know, Oracle and so on and so forth.

And since then Amazon has been the worst performing hyperscaler. And the call here is that, you
know, they still have structural issues, right? They still use, elastic fabric, although that's
getting better, still behind NVIDIA's networking, still behind Broadcom's/Arista’s, like type
networking NICs. Their internal AI chip is okay, but the main thing is that they're now waking up
and being able to actually capture business, right? So the main call here is that, since that
report, AWS has been decelerating revenue. Year-on-year, revenue has been falling consistently. And
our big call is that it's actually going to start reaccelerating. And that's because of, Anthropic.
it's because of all the work we do on data centers, right? Tracking every single data center, when
that goes online and what's in there, the flow through on costs, right? If you know how much the
chips cost, the networking costs, the power costs, you know how much, you know, generally margins
are for these things, then you can sort of start estimating revenue.

So when we build all that up, it's very clear to us that they trough on, AWS revenue growth this
quarter. This is the lowest AWS revenue growth will be, on a year-on-year basis for at least the
next year. And it's reaccelerating to north of 20% again because of all these massive data centers
they have online with, Trainium and GPUs, right? It depends on which one. It depends on which
customer. The experience is not as good as, you know, say a CoreWeave or wherever, but the name of
the game is capacity today. CoreWeave can only deploy so much. They only can get so much data center
capacity, and they're really fast at building.

But the company with the most data center capacity in the world, then, and still today, although
they may get passed up in the next two years, is Amazon. Actually they will get passed up based on
what we see is Amazon. But incrementally, Amazon still has the most spare data center capacity that
is going to ramp into AI revenue over the next year.

Building data centers Guido Let me ask one question. Is that the right type of data center capacity?
Like for the high-density AI buildouts today, you need, you know, massively more cooling. You need
to have enough water close by, you need to have enough power close by. Is it the right place or is
it the wrong type of thing? Dylan So data center capacity, in this sense, I mean all the way from
power secure to substations built to transformers, to, you can provide the power whips to the racks.

Now obviously the data center capacity will differ, right? Historically, actually Amazon has had the
highest density data centers in the world. They went to like 40 kilowatt racks when everyone was
still at 12. And if you've ever stepped foot inside of… Most data centers, they're like pretty cool
and dry-ish. If you step inside of an Amazon data center, they feel like a swamp. It feels like
where I grew up. It's like humid and hot. Because they're like optimizing every percentage. And so
your point in here is that like Amazon's data centers aren't equipped for the new type of
infrastructure, but when you compare them to the cost of the GPU, like having a complex cooling
arrangement is fine.

You know, we made a call on Astera Labs a few months ago, a couple months ago when they were like at
90, and it's gone to 250 the month after because of what orders Amazon is placing with them. But
there's certain things with Amazon's infrastructure, I won't get too much into it, but the rack
infrastructure requires them using a lot more of like Astera Labs’ connectivity products. And the
same applies to cooling, right? So on the networking and cooling side. They just have to use a lot
more of this stuff. But again, this stuff is inconsequential on cost compared to the GPU, Guido You
can build, right? My question was more like, look, I may need a major river close by for cooling at
this point, right?

In many areas they just can't get enough water and, you know, there's probably power in the same
region. Dylan There's two-gigawatt-scale sites that have power all secured, wet chillers and dry
chillers, all secured. Like, everything, everything's fine. It's just not as efficient, but that's
fine. Like, you know, they're, they're gonna ramp the revenue. They're gonna add the revenue. Not
that I necessarily think Amazon's internal models are gonna be great, or, hey, their internal chip
is better than NVIDIA's or competitive with TPU, or their hardware architecture is the best.

I don't necessarily think that's the case. But they can build a lot of data centers, and they can
fill them up with stuff that will be rented out. It's a pretty simple thesis.

Anthropic’s role in Trainium Sarah How, how important has Anthropic been to the co-design for
Trainium? Because I remember we had a portfolio company, this was summer 2023. They invited them to
AWS, they spent, man, I think eight hours with them over the course of a week trying to figure out
Trainium. Back then it was just impossible to work through. Obviously that portfolio company hasn't
gone back and tried it now, but how different is it now based on what you're hearing and… Dylan Oh,
it's still bad. It's tough to use. This is sort of the argument that every inference company offers,
right? Including the AI hardware startups is because I'm only running like three different models at
most, I can just hand optimize everything and write kernels for everything and even like, go down to
like an assembly level, right?

Guido How hard can it be? Dylan It is pretty hard. It is pretty hard. But you tend to do this for
production inference anyways. Like, you aren't using cuDNN, which is NVIDIA's like library that's
like super easy to generate kernels and stuff, right—or not generate kernels. But anyways, you're
not using these like ease of use libraries. You know, when you're running inference, you're either,
you know, using CUTLASS or stamping out your own PTX, or, you know, in some cases people are even
going down to the SaaS level, right? And like when you look at, like, say an OpenAI or like, you
know, an Anthropic, when they run inference on GPUs, they're doing this.

And the ecosystem is not that amazing, once you get all the way down to that level. It's not like
using NVIDIA GPUs is easy now. I mean, you have an intuitive understanding of the hardware
architecture because you work on it so much, and everyone has worked on it, and you can talk to
other people, but at the end of the day, it's not like easy. Whereas with Anthropic, Trainium, more
TPUs… Actually the hardware architecture is a little bit more simple than a GPU. Larger, more simple
cores rather than having all this functionality. You know, less general. So it's a little bit easier
to code on. There's tweets from Anthropic people saying when they're doing that low level, actually
they prefer working on Trainium and TPU because of the simplicity.

Sarah Really? Interesting. Dylan Now, to be clear Trainium and TPU, I mean, Trainium especially, is
very hard to use. Like, not for the faint of heart. It's very difficult, but you can do it if you're
just running like… If I'm Anthropic, and I must only run Claude 4.1 Opus, 4 Sonnet, and screw it, I
won't even run Haiku. I'll just run Haiku on GPUs or whatever. I'm just gonna run two models, and
actually screw it. I'm just gonna run Opus on GPUs too and TPUs. Sonnet is the majority of my
traffic anyways. I could spend the time. And how often am I changing that architecture? Every four,
six months.

Like how much… Guido It's nothing changing that much, honestly. Dylan I think from 3 to 4 it
definitely did change. Guido I mean, define architectural change. You know, at a high level, like
the primitives are more or less the same across the last couple of generations. Dylan I don't know
enough about Anthropic’s model architecture to be honest, but I think from what I've seen at other
places, there have been enough changes that it takes time to program this and really get… The main
thing is like, you know, if I'm Anthropic and I have, what, 7 billion ARR now or whatever, by the
end of next year, north of 20 ARR, maybe even 30 is like, and my margins are 50%, 70%. That's $15
billion of Trainium that I need, right? That I can run on Sonnet. And most of that's gonna be Sonnet
4 or 5, whatever it is, right? It's gonna be one model serving most of the use cases. So I could
spend the time, and it'll work on this hardware.

Oracle’s success Sarah Yeah, totally. Maybe on the topic of non-consensus calls you've made, and
maybe I'll move to another cloud. In June, you guys said that Oracle is winning the AI compute
market. And then in this pod we've already referenced the big jump obviously that Oracle had, I
think it was the single largest gain that a company with over 500 billion in market cap has ever
had. Dylan Was the 2023 Q1 NVIDIA not bigger? It might've been smaller, okay.

Sarah I think it was maybe close. We’ll fact check ourselves, but you know, obviously this is the
massive commitment that was announced. Can you walk us through why you made that call then? And just
sort of why Oracle is poised to do so well at such a competitive space. Dylan Yeah, so Oracle
they’re the largest balance sheet in the industry that is not dogmatic to any type of hardware.
They're not dogmatic to any type of networking. They will deploy ethernet with Arista. They'll
deploy ethernet through their own white boxes.

They'll deploy NVIDIA networking, InfiniBand, or Spectrum-X. And they have really good network
engineers. They have really great software across the board, right, again, like ClusterMAX, they
were ClusterMAX Gold because their software is great. There's a couple things that they needed to
add that would take them higher, and they're adding those to Platinum, right? Which was where
CoreWeave was. And so you couple two things, right? Like OpenAI has got insane compute demand.
Microsoft is quite pansy. They don't believe OpenAI can actually pay the amount of money, right, I
mentioned earlier, right? $300 billion deal. OpenAI, you don't have $300 billion, and Oracle is
willing to take the bet. Now, of course, the bet is a bit like, there's a bit more security in the
bet in that, Oracle really only needs to secure the data center capacity, right? So this is sort of
like how we came across the bet, right, is, and we've been telling our institutional clients,
especially in like a super detailed way, whether it be the hyperscalers or AI labs or semiconductor
companies or investors, in our data center model because we're tracking every single data center in
the world, Oracle doesn't build their own data centers either, right, by the way. They get them from
other companies. They co-engineer, but they don't physically build them themselves. And so they're
quite nimble in terms of like being able to assess new data centers, engineer them. So we saw all
these different data centers Oracle was snatching up, in deep discussion, snatching up, signing,
etc.

And so we have, you know, hey, gigawatt here, you go out there, gigawatt there, right? Abilene, you
know, two gigawatts, right? You have all these different sites that they're signing up and
discussions with, and we're noting them. And then we have the timeline because we're tracking the
entire supply chain. We're tracking all the permits, regulatory filings, you know, through, you
know, language models, using satellite photos constantly. And then supply chain of like chillers,
transformer equipment, generators, etc. We were able to make a pretty strong estimate in our data
center model, quarter by quarter, how much power there is for each of these sites.

So some of these sites that we know of aren't even ramping until 2027. But we know Oracle signed it.
And we have this sort of ramp path. So then it's this question of like, okay, let's say you have a
megawatt for simplicity’s sake, which is a ton of power, but now it doesn't feel like much because,
you know, we're in the gigawatt railroad. But you know, if you talk about a megawatt, right? You
fill it up with GPUs, how much do the GPUs for a megawatt cost, right? Or actually it's even simpler
to do the math, right? If I'm talking about a GB200, right? Each individual GPU is 1200 watts.

But when you talk about the CPU, the whole system, it's roughly 2000 watts. At the same time, you
know, all in, everything, simplicity's sake, $50,000 per GPU, right? The GPU doesn't cost them.
There's all the peripheries, right? So $50,000 CapEx for 2000 watts. So $25,000 for 1000 watts. And
then what's the rental price for a GPU? If you're on a really long-term deal, volume, 270, 260, in
that range. Then you end up with, oh, it costs like $12 million per megawatt, to rent a megawatt.
And then each chip is different. So we track each chip, what the CapEx is, what the networking is.
So you know what each chip is, you can predict what chips they're putting in which data centers,
when those data centers go online, how many megawatts by quarter.

And then you end up with, oh, well, Stargate goes online in this time period. They're gonna start
renting at this time. It's this many chips. Each Stargate site, right? And so therefore this is how
much OpenAI would have to spend to rent it. And then you prick that out, and we were able to predict
Oracle's revenue with pretty high certainty. And we matched pretty dead on what they announced for
‘25, ‘26, ‘27. And we were pretty close on ‘28. The surprise for us was that, you know, they
announced some stuff that ‘28, ‘29, data centers that we haven't found yet, but we'll find them, of
course.

And sort of like this methodology lets you see, sort of, hey, what data centers are you getting? How
much power? what are they signing? How much incremental revenue that is when that comes online. And
so that's sort of the basis of our Oracle bet. Obviously in the newsletter we included a lot less
detail. Bit it was that thesis, right? That like, hey, they have all this capacity, they're gonna
sign these deals. And in our newsletter, we talked about two main things. We talked about the OpenAI
business, and then we talked about the ByteDance business. And presumably tomorrow, on Friday
there's gonna be an announcement about TikTok and all this, but like the ByteDance business, you
know, huge amounts of data center capacity that Oracle is also gonna lease out to ByteDance.

And so we did the same methodology there. You know, with ByteDance it's pretty certain they'll pay
because they're a profitable company. With OpenAI, it's not. And so there's gotta be some like error
bars as you go further out in terms of like, will OpenAI exist in ‘28, ‘29, ‘30. And will they be
able to pay the $80+ billion a year that they've signed up to Oracle with? That's the only like risk
here. And if that happens, then Oracle's downside is also somewhat protected because they only sign
the data center, which is a minority of the cost. The GPUs are everything. And the GPUs they
purchase one to two quarters before they start renting them. So the downside risk is pretty low for
them in terms of, if they don't get the deal, well they don't get the revenue, they're stuck with a
bunch of assets they bought that are worthless.

Guido Is there another angle here? I mean, OpenAI and Microsoft were the BFFs, and now they've filed
divorce papers, and they just wanna diversify, and then that's pushing them away towards other
providers. Dylan Yeah. So Microsoft was exclusive compute provider. It got reorged to right of first
refusal. And then Microsoft… Guido Is it not the last choice or something like that? Dylan No, it's
still right of first refusal. But it's like Microsoft… Guido Those two are not mutually exclusive.

Dylan Well, if OpenAI is like, “We're gonna sign a $80 billion contract or a $300 billion contract
for the next five years, do you guys want it?” And they're like, “No, what?” “Okay, cool.” And then
they go to Oracle, right? OpenAI needs someone with a balance sheet to actually be able to pay for
it. And then they'll make tons of money off of OpenAI on the margins, on the compute and the infra
and all these things. But someone's gotta have a balance sheet. And OpenAI doesn't have a balance
sheet. Oracle does, although, given the scale of what they signed… We had also had another source of
information, which was that they were talking to debt markets, right? Because Oracle actually just
needs to raise debt to pay for this many GPUs over time.

Now they won't do it like immediately, like they can pay for everything this year and next year from
their own cash. But like in ‘27, ‘28, ‘29, they'll start to have to use debt to pay for these GPUs,
which is what, you know, CoreWeave has done. And many of the neoclouds, most of it's debt-financed.
Even Meta went and got debt for their Louisiana mega data center. Just because it's cheaper than…
It's literally better on a financial basis to do buybacks with your cash and get debt because the
debt is cheaper than the return on your stock. Like, it's like a financial engineering thing, but
like… You know who's out there, right? It could be Amazon, it could be Google. It could be
Microsoft.

Guido It's a very short list. Dylan Or it could be Oracle or Meta, right? Meta is obviously not.
Microsoft has chickened out. Amazon, Google, and Oracle. That's all that's left. Guido Google would
be an awkward fit. Dylan Yeah, Google would be an awkward fit. Amazon would be a fine fit, but you
know… Exactly,

Datacenter buildouts Sarah Well I guess maybe, you know, on the topic of these giant data center
buildouts, you guys just released a piece on xAI and Colossus 2. Are you getting less impressed by
these feats of building something this massive in six months or is it still very impressive to you
guys? Dylan You know, this is the thing I've said about AI researchers was that they're like the
first class of humans to think about things on an order of magnitude scale. Whereas people have
always thought about things in terms of percentage growth, like ever since industrialization. And
before that it was just like absolute numbers.

You know, sort of like humanity is evolving in terms of how we think because things are changing
faster. Guido Everything is log scale. Dylan And so, it was like really impressive when GPT-2 was
trained on so many chips. And then GPT-4 was trained on 20k H100s. It's like “Holy crap.” And then
it was like, 100k GPU clusters, right? And we did some reports around 100k GPU clusters. But now
there's like 10 100K GPU clusters in the world. It's like, okay, this is kind of boring, but it's
like a 100K GPUs is over a hundred megawatts now.

Literally, we, in our Slack and some of these channels like, “Oh, we found another 200 megawatt data
center.” There's someone who puts the yawning emoji every time, and I'm like, “Dude, what?” Like,
now it's only exciting if you do gigawatt-scale data centers. And I’m sure—I'm not sure—maybe we'll
start yawning to that too, but the log scale of this is like, the capital numbers are crazy. It was
crazy enough that OpenAI did like a $100 million trading run.

Then they did a $1 billion training run. Now we're talking about $10 billion training runs. It's
crazy that we think in log scale, but yes. Things are only impressive when they do it. Like what
Elon's doing. So what Elon's doing in Tennessee, in Memphis, the first time was crazy. 100K GPUs in
six months. He bought a factory in like February of ‘24 and had models training within six months.
And he did liquid cooling, you know, first large scale data center at this scale for AI doing liquid
cooling, like all these sorts of crazy firsts.

Putting generators outside, like Cat turbines, all these different things to get the power, you
know, mobile substations, all these different crazy things. Tapping the natural gas line that's like
running alongside the factory. So he does this, it's like “Holy crap.” And he did it for 100K GPUs.
You know, 200, 300 megawatts. Now he's doing it for a gigawatt scale, and he’s doing it just as
fast. You would think like, this is obviously way more impressive that he did it again. Maybe I'm
desensitized, but like, you've given the child too much candy.

Yeah, right. Exactly. And now like the child doesn't like apples, right? So, like yeah, a gigawatt
data center. There was all these protests around his Memphis facility, people like, “Oh, you're
destroying the air.” And it's like, have you looked around that area of Memphis? Like there is a
gigawatt gas turbine plant that's just powering generally that area. There's a sewage plant that's
servicing the entire city of Memphis. And there's like open air pits of like… There's open air
mining. Like there's all sorts of disgusting shit around there, which is needed, right?

We need that stuff to have a country run, like to be clear. It's like people were complaining about
like a couple hundred megawatts of generation. So he got protests from all sorts of people. You
know, you got super into the politics side of things. NAACP even protested him. He really got like
some local municipalities to be like, “Oh, I don't like, you know, like this.” And so he couldn't do
as much as he wanted to in Memphis. But he still needed the data center to be close because he
wanted to connect these data centers.

Super high-bandwidth, super close. And he obviously already had a lot of infrastructure set up
there. So he bought another distribution center at this time. And it's still in Memphis, but the
cool thing about Memphis is it's right across the border from Mississippi. It's like 10 miles away
from his original one, but his facility is like a mile away from Mississippi, and he bought a power
plant in Mississippi, and he's putting turbines there because the regulation is completely
different. And if the question is really like, galvanize resources, and build it really fast. Maybe,
Elon is ahead of everyone. You know, he hasn't made the best model yet, or he doesn't have the best
model, at least today, I think. You know, you could argue Grok4 was the best for a little period of
time, but it’s truly amazing how fast he's able to build these things.

And for first principles, it's like most people are like, “Fuck. We can't build the power. We can't
do power here anymore. I guess we have to find a new site.” And it’s like no, no, just go across the
border Sarah Go to Mississippi. Dylan And my favorite thing is like, Arkansas is right there. So
Mississippi gets mad. Guido Future data centers built in places where multiple states meet. Is that
the… Sarah Four quarters, yeah. Dylan Is there a point in the US with five? I know there's a point
with four states intersecting.

Hardware recommendations for startups Sarah I'm gonna buy real estate in that area. Front run it.
Well I guess on the topic of just maybe new hardware, you had this piece analyzing TCO for GB200s.
And I'm kinda gonna ask this question on behalf of our portfolio companies, which it sounds like
you're helping them already. But one of the findings that I thought was really interesting was TCO
was sort of 1.6x H100s for GB200s. And so obviously, you know, there's this point on, okay, that's
sort of the benchmark for the performance boosts that you're gonna need to at least make the sort of
performance-cost ratio benefit, from switching over.

Maybe just talk about what you've seen, from a performance standpoint and what do you recommend to
portfolio companies, maybe in a smaller scale than xAI who are, you know, thinking about new
hardware, try to get it. There's capacity constraints, obviously. Dylan Yeah. I mean, that's the
challenge, right? Is with each generation of GPU it gets so much faster, that you end up, like, you
want the new one. And you know, in some metrics you could say GB200 is three times faster than, or
two times faster than the prior generation. Other metrics, you can say it's way more than that. So
if you're doing pre-training versus inference, right?

Guido They can run everything at 4-bit, right? Dylan Yeah. If you can run it at 4-bit or just
inference and take advantage of the huge NVLink, NVL 72, you know, there's ways you could squint and
say, GB200 is only 2x faster than H100, in which case, 1.6x TCL. It's worthwhile, right? It's worth
going to the next gen. Sarah But more marginal. Dylan It's more marginal. It's not a big deal. Then
there's other cases where it's like, well on, if you're running DeepSeek inference, the performance
difference per GPU is north of like 6, 7x, and it continues to optimize, you know, for DeepSeek
inference. Then it’s like, well, I'm only paying 60% more for 6x. It's a 4x or 3x performance per
dollar gain, like absolutely. And if you're running inference of DeepSeek, that can also include RL.
And then the other question is like, well, the GPU is new, you know, there's also B200.

There's GB200, there's B200. B200 is much more simple from a hardware perspective. It's just eight
GPUs in a box. So then it's not as much of a performance gain, especially in inference. But you have
all the stability, right? It's an eight GPU box. It's not gonna be unreliable. The GB200s are still
having some reliability challenges. Those are being worked through. It's getting better and better
by the day. But it's still a challenge. When you have an H200 box, 8 GPUs, one of them fails. You
take the entire server offline, you have to fix it. So usually if your cloud is good, they'll swap
it in.

But if it's GB200, what do you now do with 72 GPUs if one fails to break the whole thing and you get
a new 72? The blast radius of a failure. Note GPU failure rates at best are the same and likely
worse gen on gen because thing, everything is getting hotter, faster, etc. So at best, the failure
rates are the same. Even if you model the failure rates as the exact same because you go from 1 out
of eight to 1 out of 72, it's a huge problem. So now what a lot of people are doing is they run a
high priority workload on 64 of them, and then the other eight, you run low priority workloads,
which is then like, okay, there's this whole like infrastructure challenge. I have to have high
priority workloads, I have to have low priority workloads. When a high priority workload has a
failure, instead of taking the whole rack offline, you just take some of the GPUs from the low
priority one, put it in the high priority one, then like you just let the dead GPUs sit there until
you service the rack at a later date.

And it's like there's all these complicated infrastructure things that make it so, “Oh, wait,
actually that 3x or 2x performance increase in pre-training is lower because the downtime is
higher.”/“I'm not using all the GPUs always.”/“I'm not smart enough” or “I don't have the infra to
have low-priority and high-priority workloads.” It's not impossible. The labs are doing it, right.
It’s just… Guido I mean, if I'm running a cloud, it's actually really hard, right? Because I
probably have to rent the spot one, the spares or the spot instance or something?

Dylan No, no. Because it's a coherent domain. It's NVLink, you don't want anyone touching that. So
it has to be the end customer. Guido It doesn't have to leave them with the empty spares. So it’s
even worse. Dylan No, the end customer usually will just be like, “I want them and I will…” And the
SLAs and the pricing, everything is like accounting for that, right? So like, generally when you
have a cloud, you have an SLA, right? That is, hey, uptime is gonna be 99% for this period. With
GB200, it's 99% for 64 GPUs, not 72, and then it's like 95% for 72. Now it differs across every
account. Every account is a different SLA.

But like, they've adjusted for this because they're like, “Look, this hardware is just finicky. Do
you still want it? We will credit you in that 64 of them will always work, not 72.” And so like,
there's this whole like finicky nature, and the end customer has to be capable of dealing with the
unreliability. And it's like, and the end customer can just continue to use B200. Performance gains
not as much. The whole reason you want this 72 domain is so you can have, you know, some of these
gains. But you have to be smart enough to be able to do it. And that's challenging for small
companies.

Understanding prefill and CPX Guido NVIDIA has announced the Rubin prefill cards like CPX. What's
your take on that? Does it cannibalize? Dylan Dude, and by the way, I don't know if this is like
brainrot or, I don't know, but I can't remember what I had for lunch yesterday, but I know the model
number of every fucking chip like… Sarah Haunts you in your dreams, Dylan We're broken. We're
broken. Guido Living the dream. Why do you pre-announce a product that's 5x faster for certain use
cases? Is it that much?

Dylan Historically, AI chips were AI chips, right? And then we started getting a lot of people
saying, “This is a training chip. This is an inference chip.” Actually training and inference are
switching so fast in terms what they require that like, now it's still one chip. Actually, there are
still workload-level dynamics that differ, but the main workload is inference even in training. It's
because of RL. Most of that is, you know, generating stuff in an environment and trying to, you
know, achieve a reward, right? So it's inference still. Right? Training is now becoming mostly
dominated by inference as well, but inference has like two main operations, right? There is
calculating the KV cache, for prefill, right?

Here's all these documents. Do the attention between all of them, between all the tokens, whatever
type of attention you use. And then there's decode, which is autoregressively generate each token.
These are very, very different workloads. And so initially the ideas or infrastructure techniques,
the ML systems techniques were, oh, okay, I will just make the batch size every single, you know,
forward pass this big. Let's call it, I'll make it 1000 big. And maybe I'll run 32 users
concurrently. That way, you know, now I still have, you know, 900-something left, 960 left, right?
That 960 is actually doing the prefill for, you know, if a request comes in, it chunks it, it's
called chunk prefill, you prefill chunks of it.

Now, you get really good utilization on GPUs. But then that, that ends up like impacting the decode
workers, right? The people who are autoregressively generating each token end up having slower TPS,
and tokens per second is really important for user experience and all these other things, right? So
then the idea is like, okay, these two workloads are so different, and they are literally different,
right? You prefill and then you decode. It's not like you're interleaving them. So why don't we
split them entirely? And this was done on the same type of chip, right? OpenAI, Anthropic, Google.

Guido Pretty much everybody does that. Dylan Everyone good. Together, Fireworks. All these guys do
prefill, decode, disaggregated prefill decode. So they run prefill on a set of GPUs, decode on a
certain set of GPUs. Why is this beneficial? Because you can auto scale them, right? You can, hey,
all of a sudden I have a lot more long context workers. I allocate more resources to prefill. All of
a sudden I have… not all of a sudden, but like, you know, over time, my traffic mix is not long-
input short-output, it's short-input, long-output. I have more decode workers.

And so now I can autoscale the resources differently, and I can also guarantee that my prefill time
is… What's really important in search is how fast you get the page to start loading. Not “When does
the resource happen?” What do people do in games? Like the loading screen often has some sort of
interactive environment, or it blends in over time, or whatever it is. It has tips and tricks, ways
to distract you. The same thing is, there's like studies and papers out there that users prefer a
faster time to first token, first token gets streamed to me sooner, even if the total time to get
all my tokens is a little bit longer.

Guido They can't read that fast anyways, right? Dylan I mean, I like to skim. Guido I mean, most
models return about speedreading speed. Dylan But you need that, right? The idea is that you want to
guarantee time to first token is a certain level for user experience reasons, otherwise people are
like, screw this, not using AI. The decode speed matters a lot too, but not as much as time to first
token. And so by having separate prefill decode you, you do this. And this is all in the same
infrastructure, you've already done this. So now it's like what's the next logical step? These
workloads are so different. Decode, you have to load all the parameters in and the KV caches to
generate a single token. You batch a couple users together, but very quickly you run out of memory
capacity or memory bandwidth because everyone's KV cache is different. The attention of all the
tokens, right. Whereas on prefill, I could even just serve like one or two users at a time because
if they send me a 64,000 context request, that is a lot of flops, right? 64,000 context request.
I'll use LLaMA 70B because it's simple to do math on, like 70 billion parameters.

That's 140 giga flops per token, times 64,000, that's many, many teraflops. You can use the entire
GPU for like a second, right? Like potentially, depending on the GPU, to just do the prefill. And
that's just one forward pass. So I don't necessarily care about, you know, loading all the
parameters in KV cache in fast. All I care about is all the flops. And so that leads us to sort of
like, you know, I had to, I give this long-winded explanation because it's hard for people to
understand what CPX is. I've had a lot of, like, even my own clients, like, we send like multiple
notes, like explaining and they're like, “I still don't understand.” I'm like, “Shit, okay.” Guido
Send the “Attention is All You Need” paper.

Dylan I mean think about like a networking person. They're like, “I don't need to know about this
‘Attention is All You Need,’” Or think about an investor, right? Data center operator, like, they're
like, “Oh, there's two chips. Why should I build my data center differently?” I gotta explain
everything. Or just like, no, you don't have to build differently. Guido In Stanford, there’s 25% of
all students, not CS students, of all students read that paper. “Attention is All You Need.” Dylan
That's low.

Guido The literature majors, and like the philosophy guys, I think that’s amazing. Dylan The Middle
East, I can't remember what country it is, has AI education starting at like age, like eight, and in
high school they have to read “Attention is All You Need.” Someone told me that their kid had to
read “Attention is All You Need.” Look, top-down mandates for education, you know, maybe they work,
maybe they don't like, maybe people like homeschooling their kids. I don't know. I went to public
school, but like, back to your readers.

Sorry, I didn’t actually explain what CPX is. So CPX is a very like, compute-optimized chip, for
prefill and then, and then decode is, just to succinctly say it, is like the rest is the normal
chips with HBM. HBM is more than half the cost of the GPU. If you strip that out, you end up having
a much cheaper chip passed on to the customer. Or like, you know, if NVIDIA takes the same margin,
then the cost of this prefilled chip is much, much lower, and now the whole process is way cheaper,
more efficient. Now long context can be adopted.

The state of GPU purchasing Sarah Yeah. I love that we're actually going into all this detail
because I had a more 10,000-foot view question for you, which is, I haven't been following the semi
market as closely as you have. I probably started with the A100, and I remember helping Noam at
Character, this is summer of June, 2023, chase down GPUs, and the only thing that mattered at that
time was delivery date because there was a huge capacity crunch. And then to see that over the last
two years evolve, where, you know, let's say 6 to 12 months ago people were doing these RFPs to 20
neoclouds, right? And the only thing that mattered to some degree was price.

Dylan Do people actually do RFPs for GPUs? Sarah Yes. Dylan So just to be clear, my opinion on how
you buy GPUs is that it's like buying cocaine, or any other drug. This is described to me. Not me. I
don't buy cocaine. Someone tells me this, someone tells me this, I'm like, “Holy shit. That’s
right.” You call up a couple people, you text a couple people, you ask, you know, “How much you got?
What's the price?” This is like fucking like buying drugs. Sorry, sorry.

Sarah No, I mean, like accurate. Dylan To this day, it's the same way. You just send, like we have
Slack connects with like 30 neoclouds, as well as like some of the major ones. And we just send them
a message like, “Hey, customer wants this much, you know, this is what they're looking for.” And
then they send quotes. Guido I know this guy. Sarah I know a guy. Well, so I think that's actually a
very accurate description. And I've sent countless portcos your ClusterMAX original post because I
thought it did a really good job breaking them down. But maybe one question to end on for me is just
what era are we in now with Blackwells coming online?

Are we sort of back to the summer 2023 era, and that's kind of the cycle that we've just entered? Or
what, what's sort of your view on where we are? So Guido That’s a very good question. Dylan For one
of your portcos, we were like, you know, after their difficulties with Amazon, we were like, okay,
let's actually like get you GPUs, the original deals we got you were gone, but like, here's some
other deals. It turned out that multiple major neoclouds had sold out of Hopper capacity. And, their
Blackwell capacity comes online in a few months. So it's a bit of a challenge, right?

Sarah Due to inference? Dylan Inference demand has been skyrocketing this year, right? Guido
Reasoning models, yeah. Dylan These reasoning models, the revenue. It's been skyrocketing this year.
And then also, like, there's a bit of like the, you know, Blackwell comes online, but it's hard to
deploy. There's a learning curve to deploying it. So whereas like you got down to, like, you buy the
Hopper, you install the data center, it's running within like, you know, a month or two, right?

For Blackwell it was like, it's a longer timeframe because of reliability challenges. It's a new
GPU, I mean, it's just growing pains. So there was this gap of like how many GPUs are coming onto
the market as revenue is starting to inflect. And so a lot of capacity got sucked up. And actually
prices for Hopper bottomed like three or four months ago, or like five or six months ago. Yeah. And
actually they've crept up a little bit now. I don't think we're quite 2023, 2024 era of, GPUs are
tight. If you want like just a few GPUs, it's easy. But if you want a lot, it’s hard. You can't get
capacity that instantly.

Sarah Wow. What a time. Erik Shall we wrap on that? Dylan, this was another instant classic. Thank
you so much for coming to the podcast. Dylan It was like two hours, bro, like what the hell. Guido
We couldn’t stop. Erik Thanks so much. This was great. Dylan Thank you so much for having me.
Resources: Find Dylan on X: https://x.com/dylan522p Find Sarah on X: https://x.com/sarahdingwang
Find Guido on X: https://x.com/appenz Learn more about SemiAnalysis: https://semianalysis.com/dylan-
patel/ Stay Updated: If you enjoyed this episode, be sure to like, subscribe, and share with your
friends!

Find a16z on X: https://x.com/a16z Find a16z on LinkedIn: https://www.linkedin.com/company/a16z
Listen to the a16z Podcast on Apple Podcasts: Listen to the a16z Podcast on Spotify: Follow our
host: https://x.com/eriktorenberg Please note that the content here is for informational purposes
only; should NOT be taken as legal, business, tax, or investment advice or be used to evaluate any
investment or security; and is not directed at any investors or potential investors in any a16z
fund. a16z and its affiliates may maintain investments in the companies discussed. For more details,
please see a16z.com/disclosures.

Discussion about this video Comments Restacks Podcast a16z Podcast a16z Podcast Subscribe Authors
a16z Dylan Patel Writes SemiAnalysis Subscribe Erik Torenberg Writes Erik Torenberg Subscribe Sarah
Wang Writes Wang Gang Subscribe Recent Posts Sam Altman on Sora, Energy, and Building an AI Empire
Oct 8, 2025 • a16z and Erik Torenberg The Death of Search: How Shopping Will Work In The Age of AI
Sep 20, 2025 • a16z Faster Science, Better Drugs Sep 16, 2025 • a16z and Erik Torenberg Mark Cuban
on the NBA, Cost Plus Drugs, and How to Fix Politics Sep 10, 2025 • a16z , Erik Torenberg , and Mark
Cuban The Little Tech Agenda for AI Sep 8, 2025 • a16z Is Non-Consensus Investing Overrated?

Sep 5, 2025 • a16z , Leo Polovets , Erik Torenberg , and Martin Casado a16z is Moving to Substack!
Sep 4, 2025 • a16z Ready for more? Subscribe © 2026 Andreessen Horowitz · Privacy ∙ Terms ∙
Collection notice Start your Substack Get the app Substack is the home for great culture This site
requires JavaScript to run correctly. Please turn on JavaScript or unblock scripts

