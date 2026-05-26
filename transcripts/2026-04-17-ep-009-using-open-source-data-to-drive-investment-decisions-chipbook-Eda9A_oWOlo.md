# Ep. 009 - Using Open Source Data To Drive Investment Decisions (ChipBook)

- Date: 2026-04-17
- Channel: SemiAnalysis Weekly
- Duration: 53:22
- URL: https://www.youtube.com/watch?v=Eda9A_oWOlo
- Source: `uv tool run youtube_transcript_api --languages en --format json Eda9A_oWOlo`
- Note: timestamps are preserved in the paired JSON file.

## Transcript

Hello everyone, welcome back to SemiAnalysis Weekly. I'm here today with the guys from the Chip Book
team. We're going to talk all about what is Chip Book, uh what's open-source data, some of the use
cases that people are using it for, and some of the nice viral tweets that the guys have put out in
the last couple of weeks. Guys, welcome to the show. Great to have you on. Good to be here, Jordan.
Thanks for having me. Thank you, Jordan, for having us.

All right, let's jump in. So, um Chip Book, Chips and Wafers, can you give us a little bit bit about
what you guys do at SemiAnalysis, what it is? Yeah, sure. Um yeah, so first, Jordan, great to be
here. Longtime listener, first-time caller. Um I'll try.

>> say let me give you a little bit of a background of what Chips and Wafers is and and uh what the
Chip Book is. Uh essentially, Haim and I both came from the buy-side. We worked at a hedge fund
where we covered semis. Um Not exclusively semis, but one thing is true of any sector you cover on
the investment side of things is that you're constantly looking for data. Data is valuable um to
generate investment ideas. You're looking to validate ideas.

Let's say you have some idea and you want to know does it make sense or not. You're looking for some
sort of alt data platform or some information you could use to validate an idea. Um and sometimes
you want to track an idea. Like let's say you have a great thesis. It seems to check out. But like
how do you time that position? How long do you hold it? When do you size it? When do you get out?
So, you have to track the idea. And everybody in the hedge fund world is looking for alternative
data. In fact, just a a funny anecdote, uh a few weeks ago we attended a conference for alt data,
which was um alt data providers came to this one conference center and they had dozens of hedge
funds and they were all looking to buy some sort of alternative data platform.

Of I think maybe 60 vendors at the platform, we were the only guys who were selling semiconductor-
related data. And the reason I'm pointing that out is just to say that we recognized it on the buy-
side as well is that there is a dearth of data of information that's out there. So, uh semiconductor
investors are thirsty. They're hungry for some kind of data. And what we sort of developed an
expertise in is being able to identify open-source data which can help inform your investment
decisions, your view of the industry.

It's all open-source. It's all public, but it's messy. And it's distributed all over the world. It's
in different languages. It's coded. Um Often times, most of the time you don't even know what you're
looking for and how to use it. So, there's all this data out there. And what we do is we say, that
data is interesting information. But information is interesting. What we want to do is turn that
interesting information into actionable intelligence. And the way we do that is we kind of learned
how to gather all of this data, put it together in a package that can help inform your idea
generation, your tracking and monitoring, your investment thesis validation.

So, the Chips and Wafers Chip Book platform is a way for the investment community and for
semiconductor companies themselves to have insight into big picture where the industry is going. And
on a more granular level, how that impacts individual companies, trends, themes, inflections within
the space. Um just to give sort of an idea of what the data is, most of it is open-source import
data, export data, production statistics, inventory. All that stuff is out there, but it's a pain in
the neck to find and we try to bring that to our to our uh Chip Book customers. And if I if I could
if I can interject here, maybe just to add a little bit on what Semi's saying.

So, you know, Semi used Semi used the word intelligence. And like a like a helpful parable that I
like to think about, and Semi mentioned that we we both came from the buy-side. Before the buy-side,
I was in the military for a few years. Like an interesting parable to think about in this context is
this concept of what people like to call open-source intelligence or OSINT for short. So, you know,
for years that any respectable military operation, you know, had obviously their entire intelligence
director working across organizations and they and they have their intelligence signals, right? And
they have signals intelligence and they have visual intelligence, they have human intelligence. And
then about like at the in the beginning of the 21st century, like this whole new theme of open-
source intelligence comes out. And at first, it's kind of like only reserved for like the nerds on
the internet that are scraping IP addresses and random YouTube videos. And like within the
intelligence community, it was totally disregarded at first cuz like like, bro, what's interesting
about open-source intelligence, right? If it's open-source and anyone can access it, why is that
valuable? Why do I need that? And all the intelligence agencies just say like, I don't need this. If
I If everyone can access it, what what use do I have for it? But what everyone has come to
understand over time is that one thing that open-source intel has a lot of times over all these
other sources of intel is that it's real-time. And yes, it's messy, but it provides super valuable
signals super early and a lot of times in places that it's really hard to get to with all the other
forms of intelligence, right? If you obviously if you can have a human asset inside somewhere that's
super valuable, you'd want to get that, but it's not easy to do that. However, if there's a guy on
the street corner with, you know, recording a video that he then uploads, you know, to YouTube and
then you're able to see that video. So, like yes, it's open-source, but you actually have, you know,
you have access to that. Uh where in the past that would have been super hard. So, again, like just
to bring this full circle, like when people say like, wait, like open-source data, like is that
valuable? So, like the the like the obvious answer is that like, yes, it's super valuable, but you
need to know how to find it, you need to know where to find it, you need to know how to sift through
it, you need to you need to be able to distinguish between what's noise and what's a true signal. Um
so, that's like a like a a helpful parable how to think about, you know, this whole this whole idea
and this whole concept of open-source data to help inform decision-making, especially in the semi
industry. Yeah.

And I I think this can it So, this is obviously about trends. If you look back at historical data
and then you try and um inform the the current day. You need to stay up to date, needs to be
current. Um so, more so, it's like establishing a process to get access to this data and then
actually making sure it's current, up to date. You have you know, monthly or quarterly updates. Can
you give me some examples of like real data in the Chips and Wafers uh context, you know, uh we like
we've seen you guys put out some uh interesting teasers uh on the SemiAnalysis account or the Chips
and Wafers account. Maybe we can run through some of those as examples.

Yeah. Let me um let me sort of take one step back and sort of give a sort of the value proposition
so I can explain like where the the examples come in. Ev- Everybody knows there's available open-
source data. People are aware it's out there and you have a lot of banks that put out, you know, a a
generic statistic as an indication that, you know, WFE is up or WFE is down, for example. You know,
people are looking a lot of the the WFE equipment type imports, exports, things like that.

Um I think where the secret to using it properly is to have the ability to get as granular as
possible. So, like just looking at the WFE side, for example, WFE has a category and I've seen
statistics. WFE is up 10%. So, let's assume ASML's going up or Maybank's going up or wha- whatever
equipment manufacturer you're you're invested in. Um the problem is that WFE is like the broadest
category in the world. It includes wafer manufacturing equipment, like tools to make ingots and to
slice uh wafers. It includes um deposition tools, etch tools, lithography tools, ion implanters.

It even includes um it even includes packaging equipment, like flip chip tools and wire bonders. Um
often times, it even includes inspection tools and metrology tools. So, if you're tracking like KLA
metrology and you're looking broadly at WFE as a metric to monitor your investment, you're looking
at a metric which is far too broad to at all be meaningful for your investment. And you can make
mistakes. Like I one thing I I like to say a lot is the only thing worse than having no map at all
is having the wrong map.

Right? Investing based on the wrong bit of information is very, very dangerous. So, the value comes
in trying to be as granular and targeted as possible. And that comes out in WFE, that comes out in
the AI supply chain, using the AI supply chain um supporting companies as a tracker both for the big
guys, but also as investment opportunities on their own. When you look at uh chip shipments and
production and inventory levels around the world, being able to distinguish between logic and
memory, within memory being able to look at flash, DRAM, HBM from different countries and knowing
who's making what and for what customers. So, I think the granularity is the way that we try as best
as possible to have our information targeted.

Um Maybe I'm I'm trying to think, Haim, maybe you want to do uh one example or or talk a little bit
about, you know, uh some use cases from the data. We we could do some use cases. The the only thing
I would just add on what you were saying up till now that like I think is important to expand on is
really this idea that uh at like a lot of the investors that we talk to, like I everyone knows
semiconductors is huge, especially over the past, you know, 3 years since AI has entered everybody's
lives. Like everyone knows that semiconductors is a is a is a super hot, you know, market right now,
right?

Really, most people do not understand just how massive the supply chain is. Like they do not
understand where it starts and they like really can't even understand where it ends. Like right
where like you're thinking about a token output on the chatbot that you're using, whether, you know,
it's a you know, OpenAI or Cloud, it doesn't matter. Like that that's what the consumer's seeing
like at the end right now with AI. Like that started 4,000 steps earlier when some random Japanese
chemicals company, you know, was making a polysilicon boule, you know, that from the like and then
like the everything flows from there, right? So, this is it's this massive supply chain that it's
like super duper hard to comprehend. And like a a really like another good value proposition. Again,
we we do open-source data and we track the entire supply chain. We start all the way like I said
from the Japanese company and try to go as far as we can to where the where the where the data
allows us to go. And so like the ability to see that entire value chain, to see what's moving up,
what's moving down, is super valuable because you know, obviously they all they also always impact
each other, right? Like you know, Semi mentioned WFE. Like if WFE is an input, then obviously the
output of that is chips that the fabs and foundries are doing after that. And then it's chips that
goes to the server DRAMs. And from the server DRAMs it's going to the hyperscale data centers. From
the data centers that's token outputs. So, just to be able to like to see that, you know, that whole
wave of that whole supply chain move and like noticing where the different signals hit to understand
how, you know, where that's happening upstream then how that how that impacts the downstream is
something super valuable.

Yeah, let me let me give an example. Let me give one example of memory. Maybe we can talk more about
um you know, early signals. But one example is like memory. So, obviously we're in this memory
supercycle and everybody in the world wants to know about that memory. It was probably a year ago we
called out the memory cycle. How did we see it early? So, obviously you can look at, you know,
memory uh memory sales numbers once Samsung reports and Hynix reports, but then you're already like
looking backwards.

What we were looking at for example was Taiwanese DRAM inventory levels. And we had seen that
inventory levels of Taiwanese DRAM were rising for months. They were building, building, building.
And all of a sudden

>> DRAM here by the way, not not HBM. Like just like conventional DRAM, non-HBM, non-AI related uh
at least at the time. Non-AI related DRAM. Sorry, Semi, go. Yeah, and we and we're watching the
Taiwan DRAM levels going up and they were hitting like historic highs. And then all of a sudden, it
must have been about a year ago, probably was the summer of 2025, we see the first month, for the
first time in a in a year, the inventory levels drop. And then we and we called it out. We said,
"Something's happening, but let's let's wait to see.

It's only been 1 month." The next month we see we see the inventory levels drop again. And then a
third month. And then we realize we're starting a trend. And sure enough, I think we've now been at
11 or 12 months in a row with Taiwanese DRAM inventory levels have dropped. And what that told us as
the inventory levels started to drop is we're beginning to see a demand-supply imbalance where the
demand is now outstripping the supply. Um that was a very very early call we were able to make by
tracking a relatively obscure um specific data point that was available.

It was open-source, but you had to know how to find it. And you have to know, more importantly, what
is it telling you about the memory cycle? And then we started to track, okay, everyone's going to be
looking at like Korean memory exports. But what are we seeing when it comes to Chinese memory
exports or Taiwanese memory exports? Because that gives you a better sense of the broader market
demand beyond the specific HBM chips, which we're also tracking as well. But those were all ways
that we were able to have early identification of a trend within memory. And number two, to continue
to foster that tracker going forward. Now, what do we do today? So, now everybody's made huge
investments in memory companies and you're sitting on huge positions. So, if you're a hedge fund
right now sitting on a huge position on a memory company, what you're really nervous about is when
does the cycle end? And I need to know before Hynix reports on a company call, "Oh, by the way, the
demand is now uh is is falling off and supply outstrips demand or somebody comes online with huge
capacity that's no longer um uh we're no longer in a supply-constrained environment." So, what now
what we're doing as a tracker is not to generate the investment idea cuz that we did a year ago. Now
we're tracking and monitoring your investments for you by making sure we're following memory uh
shipments globally both from Korea, Taiwan, China. We're following DRAM, we're following flash,
we're following HBM. All of those are invaluable trackers because the size of the position you're
sitting on is huge.

And the the the risk of not getting out of those positions or maybe or selling too early. But those
positions are worth a tremendous amount of money to a hedge fund. So, staying on top of that data on
a monthly basis for our customers, I think is a is a huge value proposition.

>> Yeah, makes perfect sense. I mean, we we had Sravan on a few weeks ago. He was talking about the
allocation of TSMC 3 nanometer between Nvidia, Apple, and then some of the small smaller smartphone
players. And I think just this morning we saw uh Xiaomi uh smartphones from China, you know, they're
they're 35% down on shipments or something like that. So, it can I mean, some of these calls can
happen in weeks, but they can also happen in like months of uh you know, it can take months or or
even like a year plus for for some of this stuff to play out when it comes to inventories or stuff
shipping and moving around. Um do you have any stuff currently that you're tracking? Uh like what
what is this uh cuz I mean, to some extent looking at historical data is is different than
forecasting the future, but historical data on something so far back in the supply chain is like
predicting the future on things that are downstream of it in the supply chain.

Yeah, maybe if I'm going to talk about WFE because WFE is a great example of that because you know,
WFE equipment is shipped 6, 12, 18 months before production even starts. Yeah, right.

>> Yeah, totally. Uh and I'll speak to that in a minute, but just to address kind of like what Semi
was talking about beforehand just like with the examples that we were giving about memory is like,
you know, the odds are in investing in general like it's it's going to be rare that you're going to
have that like silver bullet piece of information, just one thing that gives you everything you need
to know, right? This is the time to go long this company. So, like you're like the odds of that
happening with one piece of information is you know, highly unlikely to basically zero. And so like
going on the examples that Semi was giving like for example like that we were able to call out like
we were seeing in the Taiwan DRAM inventory or, you know, memory exports coming from non-HBM
geographies like South Korea. Like those were those were signals. Again, going back to what I was
saying beforehand.

Like you get these signals and you just you need to be paying attention to these signals and you
need to be aware of them before they kind of hit the market because, you know, if it's already on
the print of the company when, you know, results come out, it's too late. Right? So, this this idea
to be able to track those signals. And again, you know, sometimes you know, going back to the
intelligence parable that I gave, you know, sometimes sometimes it's noise, sometimes it's signal,
but you need to be aware of the signal so that you could then have that on your radar to understand,
wait a second, like does this translate into actual intelligence?

And suddenly gives you, you know, even a heightened awareness of the questions you need to be asking
or the the areas that you need to be focusing on. So, that's just to to speak to what Semi was
talking about. But you you you know, then you were talking about what are certain examples of
upstream things that you could look at that then impact the downstream. We talked about WFE. So,
again, like WFE is massively important because again, going back to what I was saying beforehand,
WFE moves from the equipment manufacturer into the fab.

Once it's installed in the fab, that's what allows you to output wafers and to output chips, which
ultimately ends up in the data centers, which you know, it ends up in the memory modules that go,
you know, into the into the packages. So, like and again, you have lead times on the So, like if you
order it today, it's only showing up in your fab 6 to 12 months from now, then you have an
installation period, and then you have time until it ramps. So, like being able to track the WFE
movements, again, that's that's giving you like a good 12 to 24 month uh you know, preview into what
wafer capacity is going to look like down the road. And again, once the company says it, once once
you already know that it's coming, it's already too late. And so like I think like a really good
example to this of like something that we track super duper closely because we understand just what
an impact it has on the market is specifically on China WFE, not the Chinese manufacturing of WFE,
although I'll touch on that in a second also, but primarily the amount of WFE flowing into China,
right? Because first of all, when AI and memory was down, like everyone's you know, everyone's
talking right now about, you know, how much South Korea you know, the the revenue composition of
South Korea of the ASML prints earlier today.

Um kind of what that was, but like memory was like really muted for 2 years. And you know, you had
TSMC, but everyone else kind of like wasn't putting in orders. And like really what was like, you
know, propping up all of these WFE companies was just the China demand. Like, you know, companies
were getting to 25, 35, 45, even 50% of quarterly revenue was coming from China. All right, this is
this is companies like SMIC or YMTC importing equipment.

Cuz yeah, so that's the example that I'm giving right now. That's one of the things that we track
super closely. So, what like we we track WFE imports into China at the provincial level, right? Cuz
you have you know, you have YMTC, you have SMIC, you have Huahong, you have CXMT. Um and they're all
operating in different, you know, in different provinces. And we're tracking the WFE inflow into all
of those. Cuz this this has like two massive consequences, right? The number one is what does that
mean for the WFE company revenues, right? If we're thinking about KLA, if we're thinking about Tokyo
Electron, if we're thinking about ASML, like obviously it impacts them because the the their China
revenue and you know, how that fits in is like obviously super material to how people are going to
be looking at are going to be looking at their results. But then also, right, once Chinese capacity
comes online at all these companies, right? Everyone wants to know like when is there going to be
this massive adoption of Chinese memory, right? When are you going to be when are you going to be
SMIC being adopted by 10 people? When does this capacity going to be come on Yeah, when is the when
is the memory capacity going to come online?

And then suddenly we'll start seeing more of a supply-demand balance if like, you know, unlike what
we're going through right now. Um so, like that's like a really good example where we're tracking
this like super upstream thing because again, it's like also informing you how you need to be
thinking about about what WFE revenue is going to look like for these companies that are selling
into China, but then also what this is going to mean for Chinese capacity moving forward because
that like, you know, that's something else to just keep in mind for the Chinese companies but also
that always impact right if you know, if if people are adopting more you know, smick then like maybe
that's coming out of UMC right maybe that's coming out of you know, Texas Instruments. So it's just
another thing to it's just another thing to keep in mind and and like just to give Yeah, maybe can
you look backwards and and and give an example there of like the impact of um tariffs or the impact
of some of the uh regulations or or stuff that the US has explored in terms of China restrict
companies actually selling equipment into China? Yeah, so so that that was the example I was going
to give so like we had observed now again like this is this you know, this is a while ago but like
anyone who looked at the China WFE revenue like the massive massive brand happened in 2024 cuz
that's when you know, we're still talking Biden admin time and people are talking about all these
restrictions that were going to come online. So like you basically saw this massive massive massive
um lithography build up happening inside of China. Like people were like oh my god We saw I mean
deposition at everything.

We saw everything. There was definitely lithography was definitely more I think that they were
probably thinking that lithography like meaning that there's going to be a lot more focused on ASML
and like they'll probably be able to get like you know, deposition and even with some of the
restrictions in place. So like there was a lot more focus on lithography but again yes, we saw we
saw this happening that like so like 2024 was a ridiculous year in terms of Chinese WFE demand
right? And then if you look back at all of the WFE companies transcripts at the end of 2024 when
they were guiding into 2025 they were all like we realized that that was just you know, this that
was the stockpiling ahead of you know, tariffs ahead of regulation ahead of you know, what whatever
the administration was going to do we're guiding that 2025 is going to be somewhere between 20 25%
down. Everyone was saying that and we were tracking the status super closely and like month after
month it is on par at the same levels with what 2024 was like. Now again like you know, and this is
our when you're starting to see you know, TSMC is ramping a little bit so you're starting to have
all these other orders at the same time Chinese demand is like literally remaining the exact same
thing and and like we're going month after month and we're you know, we're we're we're tracking all
this and like year at year's end if you look at China revenue from these WFE you know, WFE players
but they were not down 25% year over year.

It it it was even it was slightly I can remember it was slightly up or slightly down but it was
basically flat year over year and like 2024 was massive like absolutely massive and now when you
look at all what all the WFE company you know, company commentary going into 2026 is what are they
all saying? China's going to be down 2025% in 2026 right? And it's so like that's what they're
guiding and like maybe it's true but like for example ASMI was saying that you know, they're
actually seeing China go up in 2026 a little bit. So like now like something that's on our radar is
like wait a second okay so we already saw this play out in 2025 where people said it was going to be
down and we tracked it was actually the same and that obviously impacts what 2026 going to look like
and that's obviously something that we're tracking super duper closely and kind of stuff.

>> sort of but that sort of speaks to the to the importance of having like a granular tracker. So
you know, I do think that to some degree we're going to see a slow down in China WFE imports but the
degree of slow down may not be consistent across the supply chain. So certain tools you may see a
slow down certain tools you may not. Um I don't know exactly how this is going to play out but we
did see that um the inspection equipment into China was holding on a little bit longer than some of
the front end tools.

Um I don't know if it's holding on anymore we're going to find out more in the next week or so but
um when more data comes out and and that will be included in our chip book coming out next week but
our chip book comes out once a month. So next week we're going to put out the new one. I think
there's going to be some really important data in there about that split which tools are slowing in
China which ones are not. Um because that also creates a huge opportunity because if everybody is
assuming something about WFE writ large but there are exceptions within that being able to identify
those exceptions that are going to be hit by the macro noise but ultimately will on an earnings
level continue to perform that's a huge buying opportunity.

Um so that's something we'll probably have more insight into next week but uh to Khayyam's point
there's there's a lot of value in tracking each one of those things on a granular level. Yeah, I'm
I'm thinking in the back of my mind I'm thinking about how it all connects from high level like when
you were walking through that it's the diffusion regulation that Biden was exploring that people
were saying Trump was going to repeal and then he did how that actually flows through to shipments
and to earnings and you know, uh A lot a lot of it is kind of also trying to figure out like what's
the normal run rate.

Meaning I think like Biden comes out with these rules so that everybody in the world rushes to pull
forward orders cuz people want to get things in before the restrictions kick in. Um and so you see a
huge like Khayyam was saying you see a huge ramp in in imports let's say China WFE equipment. Um
well looking forward is there now an elevated capacity expansion in China which you know, will be at
an elevated level albeit maybe not as high as 24 25 but is there a new norm or do we have to look
back at historic run rate levels to get a sense of how far can it drop? I think people sometimes
have a hard time with visualizing how far something can drop after it's already down. You know, so
you'll say oh well listen shipments already down 10%. So I guess we've you know, we've bottomed out
and companies love to say that. Every single company you know, call will talk about now we've hit
the bottom. They've always hit the bottom. They're constantly hitting the bottom.

So like what is the bottom? Well look historically at norms

>> 180% historic high is the bottom or something like that?

>> Yeah, exactly. I remember when um when wire bonders like a very you know, obscure packaging tool
I not not obscure but you know, unexciting unsexy uh packaging tool wire bonder orders were flying
into China uh during COVID. Um and it was just so out of whack with the historic norm which we've
now kind of returned to. And the order levels dropped off 10 15 20%. So you see Khayyam looking at
sofa's like okay now we've kind of hit the bottom again.

But if you looked at it at historical data it was clear that we were far from the bottom and having
that perspective even though it's like outdated data can certainly inform your investment decision
going forward. Um and I and I love what Khayyam said about that is it's like the mosaic theory. Like
sophisticated hedge fund investors are very very smart. They're not looking for somebody to like you
know, feed them the answer. They need pieces to the puzzle. They're going to put the puzzle together
but every single puzzle piece you offer them they will incorporate that into their mental model when
they develop their thought about the business.

So every one of these data points it's not the answer but it's a puzzle piece and when you know how
to put those together um I'll give you I'll give you an example. Yeah, I'm itching for more puzzle
pieces here. What? I'm itching for more puzzle pieces here man. Give me give me some more pieces.
[laughter] I'll give you this is like an obscure one but it's interesting. One of the things we were
looking at was um photomask writers going into China.

Two years ago there was a big build up China was building up their own mask shops. And we were
watching photomask go into China and all of a sudden they started to slow down which kind of made
sense because they had built up more capacity than they needed. But watching the slow down of
photomask writer imports into China made us start asking questions. Why aren't they going into China
anymore? What's happening? And what what we found is actually counterintuitive. First I thought okay
they're not going into China because they already are not utilizing the capacity that they have
available.

But then it's like why aren't they utilizing that capacity if they're able to create photomasks at a
cheaper price than the western suppliers why don't they just do it? And what we discovered is that a
lot of the chip makers weren't comfortable uh buying masks from China because in order to get a mask
made for you in China you need to share your chip designs with the Chinese companies and they didn't
want to do that. So that made us realize that photomasks were a huge huge onshore motivation.

Like of all things you don't want your photomask to be made in China and that's why even though
China had built up huge capacity in mask writers the customers weren't comfortable buying the
photomask from China. And so we said okay well who are the photomask makers um in the western world?
Well, Photronics P Lab is an American company even with the Chinese subsidiary which is like a win-
win on both sides and then we realized like P Lab is a huge long.

And sure enough like once they came out with that story the stock like doubled. So that's like a
nobody was handing you that story but by tracking the data you begin to know what questions to ask
and then it leads you down the road of discovery and you figure out you know, winners and losers
that way. Makes sense. Yeah, great story. Can you um can you run me through how that actually gets
incorporated in a chip book release right? Like what does it actually look like?

Um what if when people subscribe what do they actually get access to? How how clearly are you
spelling out these uh long and short positions that you're recommending to people or just providing
data? What format does that data come in? Okay, it's a great question. Uh Khayyam jump in if I'm
missing anything but um basically the chip book looks like this. It's basically there I'll like make
it very simple. It's basically a PDF with 35 pages of charts.

The first 10 charts are the same charts every single month. It comes out on a monthly basis. The
first 10 are like fundamental building blocks of the semiconductor industry. Things that every
semiconductor analyst every investor every company needs to keep their eye on. Basic things. What
are the hyperscalers spending? What do the main silicon content product shipments look like, whether
that's PCs, smartphones, auto, wafer shipments, PCBs. Right, we're not just looking like end market,
we're also looking very early in the supply chain, but basic semiconductor building blocks.

Those are 10 slides that appear every single month. The next 25 slides rotate on a monthly basis. We
track probably two to 300 different data sets. But not every month are those 200 data sets
interesting, actionable, are there any inflection? Sometimes they're just boring and nothing happens
that month. So as opposed to sending our customers a 250-page chipbook that would just like
completely overwhelm any analyst, nobody would even look at it, what we do is we say, "Let's
identify." We don't have a specific number. It could be 15, it could be 25, whatever we think is
actually interesting, we pick out another 25 or so slides and we amend those, we append, amend,
append those to the first 10.

So now we have 35 pages. We have the 10 and then we have the 25 that vary every month. Every single
page of the chipbook has the chart and it has a on the bottom three things. It says number one, what
is this data? Number two, it says, "What are the stocks?" Not all of them, but what public companies
are connected to this data? And number three, it gives an update every month of what we're seeing in
the data. So you can scroll through the chipbook, you can flip through it and you can say, "Here are
the companies that are connected, here's what happened this month, here's my update." Um that's how
you read it. What we what we now add to the chipbook as well, which I think is a super valuable
tool, is we write an executive summary at the beginning of every chipbook. So the front page of the
chipbook is the executive summary. In the executive summary, Khai and I tell you the two, three,
four, five most important implications of the chipbook. We say, "These are the trends that we're
seeing this month, these are actionable ideas, these are either investment ideas, um there are ways
of tracking very important components, there are ways of tracking the overall industry." And we call
out in the executive summary what page in the trek chipbook you can find that data. So we'll say,
you know, "This is what we're seeing in PCs, page seven, which relates to our view on China exports,
page 13, which has implications for silicon content from this company, page 15." So you could just
read that one-page executive summary and it's a very, very valuable piece of research um that allows
the customers to then go flip through in in depth the 35 pages of the chipbook. That's kind of the
overview of what it looks like. That's yeah, super super good summary. It It begs the question for
me of where people go from there. Let's say they've got some chart, some theme that they really are
interested in that they got kind of focused on from that review of the chipbook. How do you guys
have been doing this for a long time before you were part of SemiAnalysis, right?

Where's the connection to the rest of the SemiAnalysis organization? Maybe you could tell me a
little bit about what it's like working with you know, other teams at SemiAnalysis, other data,
other research that we do beyond the the 35 pages that a lot of people treat as maybe the entry
point to this industry even if they they end up wanting to go bigger, deeper, whatever it is. Uh
I'll start off here and I'll say I um Rave, our memory analyst, Rave Wang, but I think was here how
many weeks he was here? Jordan was here I think Brian I think I think he did the podcast a few weeks
ago, right?

Yeah, yeah. Like three, four weeks ago. So he put out a tweet, I can't remember if it was earlier
this week or last week. Um and I'm going I'm going to botch up exactly what he said, but it was
something along these lines. He's like, "Every single day I am amazed at the quality of people and
research that are at SemiAnalysis." And I just got to echo that because, you know, those who are
fortunate enough to be inside our, you know, chaotic Slack channels know just like and and chaotic
is like a massive understatement, but um like anyone who's inside that knows just like these are all
people who are in it for love of the game and like, you know, everyone's always, you know, sharing
ideas, sharing data, share sharing what they're seeing and it's obviously, you know, uh massively
encouraged, you know, to be you know, talk about what it is that you're you know, what is it that
you're seeing. And so like and again, SemiAnalysis, you know, we talked about the entire supply
chain like the SemiAnalysis product portfolio spans that, you know, the the entire semi value chain,
right? You have end fields, you have energy, you have data center, you have accelerator, you have,
you know, the core research team doing a great job. Everyone's doing a great job.

And you know, we in our, you know, small part of the chipbook team might have had like the great
fortune of being able to feed that into like the different people that we talked to. Like like we
talked a lot, you know, we talked a lot about WFE in this conversation. Like yeah, obviously, you
know, we're talking to, you know, Jeff of the great WFE team about like what we're seeing in the,
you know, the diff- different WFE arenas to help inform them in you know, in their research process.
And if we see something interesting that we think is like, you know, a good output to put into, you
know, a core research piece, like we'll we'll put it there. Like I'll like I'll give an example on
that, you know, we like one of the data sets that we were tracking was this whole idea of ABF
substrates, which has like exploded over the past two weeks. Like we put a piece out through core
Like we put it in the chipbooks and then in addition we also put out a core research piece cuz we
thought that that was a good platform to put it out talking about like really these massive
tailwinds that were coming to the ABF substrate space. You basically had um you had GPUs that were
increasing in size and in layer count and like that was driving demand and like, you know, suddenly
the CPU shortages coming up and everyone's talking about CPU substrates also. And like this was all
leading towards the fact that like we knew and we were seeing really interesting uh data on like
what was happening to, you know, in ABF production and um like you know, both production value and
production volume at like, you know, Japan and Taiwan which are like the two biggest uh ABF
suppliers and it's just like, you know, we we put that out there. So it's just like, you know,
having our hands in all these different data sets that, you know, across the value chain has been
really fun in the sense we've been able to, you know, to contribute into into cross-pollinate across
you know, other teams.

Um Yeah, that's that's like what the integration looks like. Yeah, I mean, like Khai said, this is
like the smartest group of semi analysts anywhere assembled in the world. Like we worked on the buy
side, covered semis, we thought we were really smart. You show up here and you're just surrounded by
people who get it on a very deep level. Um I think what we maybe add to the team and what we all
add, like Khai said, we're contributing to core research, we're talking to Rave, we're talking to
Shravan, like all of us are sharing information that helps build up what we're able to provide our
customers. But I think very broadly or very quickly is ours is a objective, quantitative set of data
which complements other qualitative research.

So like for example, to me it's like a no-brainer. You're subscribing to core research and chipbook.
That's like the basic building blocks, that's table stakes in order to understand what's going on in
the industry. You have core research which is a brilliant um research tool that every hedge fund
should have their hands on. And then you want to have the complementary data set that helps inform,
that helps dep- depth, gives more depth, more granularity, more color, more whatever, you know,
finance word you want to use.

It makes it like more meaningful. So you have the qualitative and the quantitative uh before you
even get to the models, right? Then you're in a different world entirely, but I think that we
complement each other on that qualitative-quantitative basis. I'm going to I'm going to jump back
now a few topics um because I think that we wanted to say something about this and then forgot
because we got into something else. But uh Jordan, you you asked about like, you know, about the
diffusion rules and where you kind of see geopolitics play into the supply chain and like how we
were able to catch up on that. So like one of our tweets that we put out earlier this week that that
kind of went viral um was talking about this idea. One of the things that we're tracking is
smartphone imports into the US.

And since the Trump nomination in November, for sure November, November 2025, um you we saw this
like yeah, thanks for putting it up. We saw this massive drop when looking at the import side, you
know, US imports of smartphone, a massive drop of smartphones that were coming in that were coming
in from China. Um it was like, "Hmm, like that's interesting." And it was, you know, it's
interesting because like again, we talked about the supply chain. Like how do supply chains move and
how do they react when there's geopolitical instability? Right?

Like what how what what is changing? What's happening? How could you track that? How could you know?
Right? So like obviously, you know, it would be nice if you had, you know, a guy who went to the
Foxconn assembly and test uh facility in China who would then report back and be like, "Yep, you
know, it's still here." Or nope, they moved it out of here, but the reality is you don't have it all
the time. So, you know, we try to supplement that vacuum of information with the sources that we tap
into. Like this is something interesting. Now again, like it's it's important to just like highlight
specifically for this data set. So this exploded I I can't even It's yeah, it's almost at 600,000
views.

It's like important for me to highlight that like this specifically like obviously the smartphone
supply chain is is also massive, right? Like obviously every single processor that goes into an
Apple iPhone is coming is coming from TSMC in Taiwan and then it's going to then it's going to
China. So like when you when you look at a smartphone that was imported into the US um and the
country where it came from, like obviously that's not representing, you know, the entire phone and
everything that's there. You know, there's there's different rules about the percentages of
component that need to be in there, but like the fact is um and and maybe if you want to bring back
the the tweet, you could see in the second chart that um in the second tweet that we put there, you
could see through the chart that actually talks about this.

Um like it's unmistakable that, you know, it used to always be coming from China even though there
were the different components that came from the different countries, but then like that basically
dropped to, you know, 25% and some leads coming from other countries like Vietnam and India. So like
clearly the supply chain made a shift and realized that even if it's the last, you know, step, uh
you know, FATP, you know, final assembly, test, and package, needs to move out of China so that
we're able to respond to whatever's going to be happening in the, you know, in the political
landscape in the US. There was a very, very clear response to that and that was something that we
tracked here.

Um and then Semi, maybe maybe you want to talk about cuz there Qatari helium right everyone's
talking about the war in the Middle East and how it impacts the semi supply chain we put out
something about that yeah there it is maybe you maybe you want to respond about you know what what
this is why it's important and why like this didn't exist until we put it out and that's why it blew
up. Yeah let me add one more thing just what Heim was saying about the the smartphones because um
the the the shift that Heim was describing is actually even more pronounced by PCs.

Um but what I think I like best about the tweet was in addition to the you know hundreds of
thousands of people there was like almost a lively debate that we started because of that tweet
basically is it real or not some people are like you know it's not real it's just final assembly
it's just putting a sticker made in Vietnam so it won't be made in China. Some people are like this
shows that we're moving in a direction once the ball gets rolling who knows what's going to happen
next. The point is and maybe the whole thing is a shenanigan like maybe it's not even real they're
just like you know making it look good that way so it's not coming from China. I don't know for sure
I don't think any of us really know for sure right now but I think that the data opens up a
conversation that forces the world to look at this and say what's happening like is this real or
not. Can a supply chain shift that quickly and I and I wish we don't have it in front of us but I
wish I could show you like the PC one is just like opposite directions. Um you know it was like 90%
coming out of China now it's like 6% in terms of PC imports to the US.

So the question is is like not only does this data allow us to give answers but it provides us with
a direction in terms of asking questions and that's also to what you're saying Jordan is like that's
how we work at SemiAnalysis. Like we're going to put that data out there and then we're going to say
Doug Sravan Ray Dylan Dan like what do you guys think? And then as a result the conversation is a
lot more meaningful within the company and within the entire ecosystem. So I just wanted to add
that.

Um Heim said about the Qatari helium. Oh that was an interesting one. So as soon as the Iran war
started so one of the implications that was recognized by the industry is that Qatar who was getting
bombed by Iran provides a large portion of the semiconductor industry's helium which is used in chip
manufacturing. So like what happens when the Qataris either the facilities are blown up or they're
shut down or shipping lanes are closed what happens to all the helium that's coming from Qatar?

So there was one camp that was like who cares don't worry the supply chain will be replaced
elsewhere. And there was another camp that was like oh we're in big trouble because a lot of the
helium comes from Qatar and we need that. And I think what bothered us is like where's the data? W-
what what is the actual number? How much of the helium for semiconductor manufacturing comes from
Qatar? And what first thing we did is we figured out okay when it comes to Korea and and Taiwan and
China what's the answer?

What percentage comes from Qatar? And what we found is that well over 50% in all three countries
meaning the major manufacturing facilities over 50% of their helium is coming from Qatar. So it's a
problem. But then the question becomes how quickly can that supply chain reinvent itself and start
getting helium from the US or from Russia. And what the chart over here shows is that very quickly
the supply chain was able to make a about-face and whereas really the Taiwanese had stopped
importing helium from the US and were had relied almost entirely on Qatar all of a sudden now they
were able to shift their supply chains over to the US which is a good sign. Now can they go all the
way to 100% from the US? I think so but that's something we're definitely going to want to track.

And the other thing the next question I would ask is what does the pricing look like? Meaning there
was some reason why the Taiwanese decided to stop importing their helium from the US and start
importing it from Qatar. Is that a pricing question? And if they have to now shift back to the US
facilities what does that do to the pricing? Now it could be all the total bomb helium is so low
that it won't have a huge impact. Um but that's definitely something to ask. So I thought this was a
great example and and and like Heim said for some reason nobody else in the world had gone through
the trouble to actually look at the data. Everybody was talking vaguely they have six months of
supply they have eight months of they have two months of inventory does it really come from Qatar
does it come from Russia?

Our question always is show us the data. Let's just look at the facts and then we at least know what
we're talking about to have an intelligent conversation. And then we can begin to ask the next
questions. So that's what was gratifying to in some ways in in some ways what's jumping to mind is
is the fact that this is a process you guys have a system you have the access to the data you know
where to look you have the software built to be able to build these charts on a effectively a
moment's notice when something happens in the world and so it's jumping to me that like this Qatar
helium chart for those maybe just listening is from April 12th 3 days before we're recording this
conversation and the the tweets about the Foxconn China assembly network stuff was from April 13th.
So you guys had a big week of viral tweets talking about this stuff but I think it goes to show
again like the fact that um we don't know what's coming we don't know what geopolitical trends are
coming we don't know what um kind of macro big picture stuff is coming in terms of like demand of
tokens or or constraints in the supply chain and having the process established to be able to build
a chart and get some insight from that data is is in some ways more valuable than actually having
one individual data point. You need to be able to like adapt to whatever area of the market is in
focus.

I don't think a lot of people forecast helium being a big focus 3 months ago 6 months ago right? If
you told us we'd go viral on a helium post last week I don't think we would have called that one.
Yeah it's Right?

>> Yeah yeah there there's the I'm I'm thinking I'm thinking of that guy I can't like there's the
meme template of the guy who's like wait you're talking about this like you know like that like
today it came out because of this this like all birds thing and their transition to now being an AI
company so he's like you know it's like the guy in the podcast like wait is it all birds like you
know the AI company? So like when I hear when I hear helium for the first time I'm like like helium
you know like the inflatable balloon and stuff you know gas but like now apparently it's for
semiconductors and and like to go back like to go back to like what Semi started with with this
whole thing like we were from the buy side like the reason that like you were talking about the
process like how we do this like when you're on the buy side you're looking for data like you're
looking for things in order to inform you right like how much of an impact is is this actually
right? Like the reason I love that that helium tweet was because I don't know if if this is true
about like your Twitter timeline my Twitter timeline was dominated by helium. It was like it like
and and it was literally it was like it was that it was that chaotic in the sense cuz there were
those who were saying like guys calm down this is totally totally negligible like stop getting
worked up on it and then there was the other side that was like you know TSMC is going to zero
tomorrow like it's over like it's so over. And and then like Semi and I looked at each other we're
just like like where is the data like can someone please give me an intelligent answer as to like
what has it been up till now?

Are there other suppliers who can get in there? And then of course like Semi said there's there's
the questions after that like how does it impact pricing you know um who are those other suppliers
who could benefit from but like let's answer the question like is this a big deal or not? And that
and you know and we've we've developed you know this process of like you know okay let's answer the
question like who's impacted from this you know where are these different sources coming from? And
can we get an answer to this that's like in the data I mean the data is objective like we don't we
don't manipulate the data we don't change the data like the data is what the data is.

The um so that's what that's why I particularly like that um that's why I particularly like that
chart cuz like there was so much noise like about helium as like let's cut through the noise and
just find the numbers that could either back this up or not back this up. Uh and again it would be
nice if you got the procurement manager at TSMC on the phone to just tell you like oh like this is
the amount that we get in we are or are not able to get it from other suppliers but like you don't
have access to that like you can't like it would be nice if you could but you don't. Um so like
where can you find alternatives to that in order to inform your decision-making process your
investment process and you know and that's where that's where Semi and I and and the Chapek product
try to be try to be handy. Awesome guys. Well I think this is a great place to wrap. Um SemiAnalysis
in pursuit of truth.

Yeah I like that.

>> [laughter]

>> Well I I got I I got I got to add one more thing though cuz I need cuz right right now I'm going
to be in armchair geopolitical strategist cuz I think that you know Semi talked about the war in the
Middle East right now and I think if there's one thing that we need to be talking about that people
aren't thinking about and that is that I think it's important to realize and again like there's
there's obviously a lot in the air right now with with this war and what it means but I think the
one thing that people are not realizing is that the largest winner or loser of this war funnily
enough I think in my from my perspective is actually TSMC and nobody's talking about that. I'm going
to give I'm going to give my like wacko perspective as to why I think that this is. Okay. But just
yeah yeah you're going to be like what what's he talking about but like let's let's try to frame
this war right now then I'll and then I'll say how this ties into TSMC. So if you think about the
war right now you have the US fighting with a partner nation in this case Israel who is a
technological ally to the US and you know provides a lot of tech that goes into the US who are
fighting for what the US is an adversary and what for Israel is an existential threat and they're
they're managing a campaign together in order to try to take out to take out this enemy. And how
this war is going to play out is going to massively impact the new theater the next theater cuz you
always need to be thinking from the US perspective there's obviously a very big reason why Israel
want to be in this war but the US need to be thinking about what the US perspective is and I think
that the US perspective has been and always will be you know what's happening on the Pacific front
in China.

Now, how does this relate to TSMC? Now, I you know, we framed what the situation is like right now
in the Middle East. Now, let's move that to the Pacific theater. So, you have China, which is an
adversary to the US, who isn't you know, in a way an existential threat to a small island there,
Taiwan, which is a technological ally to the US because they're providing basically a lot of the
backbone to you know, to the you know, the largest US companies like the we you know, we put out
that the semi analysis put out that table that like you know, eight out of the largest 10 companies
by market cap all rely on TSMC.

So, again, like putting it putting this into the framing. So, you have China, you have the
technological partner, which is Taiwan, and and the US, right? And if there were to ever to be a
future campaign in the Pacific theater, right? If the US is able to effectively execute this
campaign and show that they were actually able to fight with a partner nation in the theater against
an adversary, that could be seen as a massive deterrent in other theaters also, right? In this case,
moving to the Pacific theater, if really the US is able to come out of this war as the proclaimed
winner, and I think that that's you know, that's still up people still don't know, but if they
basically are able to create that effective deterrent against the Chinese adversary, that obviously
means that you know, that there's a big deterrent there from the Chinese making a move on Taiwan or
whatever they talk about 2027. And the biggest winner from that is obviously TSMC. Now again, it
could also be the biggest loser because if the if the deterrent is not effective and it doesn't end
up propelling you know, the you know, the big the big big China, so then that's going to be an
issue. But I think that like when you when you think about what the outcome of this war in the
Middle East is going to be, like yes, obviously there's massive implications for what the Middle
East is going to look like, but if you're thinking two steps ahead, one of the big companies that
are going to have probably the biggest impact from this is going to be TSMC. And that's something
that you know, people need to be thinking about. And when you see the outcome of this war because
again, this this entire conversation has been about signals, right? How this outcome of the war is
going to be is going to have some downstream effect on what's going to happen to TSMC. So, that's me
taking off my semi analysis nerdy semi analyst hat and suddenly I'm I'm a you know, geopolitical
analyst, but whatever. Just a just a random tangent that came to my mind that I was

>> uh Yeah, geopolitical analyst moving the focus from the Strait of Hormuz to the Strait of Malacca
going forward or something like that. Yeah.

>> [laughter]

>> Chips and wafers in war. Okay.

>> [sighs and gasps]

>> I don't know if we want to coin that one on this podcast, but uh

>> [laughter]

>> All right, guys. Well, look, I I learned a lot. I appreciate the overview of of chips and wafers.
Uh I definitely appreciate the uh the walk-through of some of these um examples. Uh and we got to
yeah, we got to we got to do this again soon because uh I think some of some people need to need to
listen to this. Uh check out some of the data and then watch to see how things play out in the next
few months to see if we uh we have the same track record while they're paying attention that we
claim to do as we look back at some of the the previous tweets or the previous calls that we've
made.

Anyway, thanks so much for for taking

>> Appreciate it. And and people are interested, you can find the Chip Book on the Semi Analysis
website. You can even download a sample there. Um maybe we'll put that in the show notes, but uh
it's there. It exists. And yeah, thanks for the time, Jordan. This was awesome.

>> Uh we have a transcript, yeah. Um but we can definitely Put it in the show notes. We can
definitely put links to uh semianalysis.com email address sales@semianalysis.com uh
semianalysis.com/chipbook or /institutional/chipbook. That's probably the place to go.

>> /chipbook Yeah, we'll we'll put it on the We'll put the links in the show notes and the
description on YouTube and Spotify and wherever everybody else is listening to this. So. Yeah, cool.
Thanks, guys.

