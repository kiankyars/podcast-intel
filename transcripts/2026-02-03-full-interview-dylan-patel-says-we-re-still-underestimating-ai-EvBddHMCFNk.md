# FULL INTERVIEW: Dylan Patel Says We're Still Underestimating AI

- Date: 2026-02-03
- Channel: TBPN
- Duration: 43:42
- URL: https://www.youtube.com/watch?v=EvBddHMCFNk
- Source: `uv tool run youtube_transcript_api --languages en --format json EvBddHMCFNk`
- Note: timestamps are preserved in the paired JSON file.

## Transcript

Good to see you again. Good to have you. Data centers in space. What you got? [laughter]

>> When are we going?

>> Me, you, the International Space Station. Let's break it down.

>> You know, the space tourism industry is quite a quite a fun one, right? Um

>> would you go? Would you do the Blue Origin thing where they blast you out past the Carman line?

>> Good enough for Katy Perry? It's not good enough for you. What's going on?

>> It's It's like, you know, like you're in freef fall. You're not actually countdown. I want to be
like going around for days, you know? I want my bone density to start to atrophy, [laughter] right?
Like I I truly want to feel the negative effects of space.

>> Yeah. Yeah. It's not enough just to go back. I I think I would do it. It's even

>> It's like 90 seconds, right?

>> Yeah. But it's better than being hanging out at on

>> all the cool stuff that astronauts do, right? Like, you know, put water and then like they're
bubbling and then you like try and drink the water or like

>> So they'll be unplugging the GPU, [laughter] plugging it back.

>> Oh, yeah. Yeah. Yeah. Yeah. Yeah. That's how you pay for your space tourism. You got to go unseen
[laughter] ship

>> 90 seconds of service one 90 second trip at a time uh no but uh people were wondering uh you know
TPUs Nvidia going on the on the on the Starlink V5 or what whatever something gets up there uh it
feels like this will be uh something more like a Tesla silicon chip an AI chip like do you have any
insight into like what the process if you wind up figuring out how to heat dissipate if you wind up
figuring out the costs what might the chip look like?

>> So, I think I think you know everyone freaks out. Oh my god, putting stuff in space is expensive.

>> Uh but if you look at like Starship launch cost and you know they keep falling, you're you're
like fine, right? Like I think that's not you know by the end of the decade the cost of space launch
will be fine. The heat dissipation I mean it's a challenge but you just put a massive massive
effectively radiator

>> and it's it's fine, right? By the end of the decade like you'll be good. I think I think the big
challenge is that chips are just really unreliable, right? Um and so so how do you deal with like a
couple things, right? Satellites can only be so large before they like you need start needing a lot
of support and structure before they tear themselves apart. So when you look at like the the
launches, right, these these things are shooting out sat like tiny satellites and many of them.
Okay, so you can't have like a big fully connected

>> cluster of chips.

>> Um and then and then like on top of that, right, how do how do you deal with any random error? Um
on on Earth you have techs running around the data center unplugging stuff, putting in spares,
things like that. Um what [clears throat] do you do in space?

>> Um you RMA it to the factory where they like might unsolder it and resolder it and then like test
it and it works and go back out. Sometimes it is just trashed. But like you know that's the
challenge to me. Is that is that I I I feel like maybe the the pattern we should be looking at is
like how often do the Tesla self-driving chips need to get serviced because that's like the the team
that would probably be building or like bridging the gap there. Like the Starling satellites, sure,
they go down, but like the service works like you're you're just relying on some sort of like, you
know, 90% uptime stuff's coming down, but most people that are in a Whimo, like the chip keeps
working, right? Most people that are in a Tesla self-driving, like they're not like you don't hear
about Tesla owners being like, "I love FSD, but I'm constantly in the shop getting my my custom
silicon chip unseated and receated," right?

>> Well, I mean, it's it's also a function of like the complexity of a chip, right? Um, you know, if
if a chip is twice as fast and let's say the bit error rate, right? Like how often a bit flips

>> is the same, then it's erroring out twice as often.

>> Um, but let's say the chip is 10x as big, right? So when you look at like a Tesla FSD chip, very
very good, very very efficient, very

>> still like relatively inexpensive and cheap compared to, you know, a big old GPU or TPU or
whatever, right? Those things are extremely large. And, you know, again, like if if the error rates
are the same, then it it fails 10x more, but in fact, the error rates are a bit harder, higher
because they're pushing these things to the absolute limit. Yeah. Um whereas you know Tesla does
have some level of like well first of all the Tesla car has two chips sort of redundancy already
built in right um

>> maybe you do that on the satellite but then that's more power more

>> yeah right so the whole allure right of it is is

>> you know effectively power is free right and solar panels you look at the cost curve of solar
panels you look at the cost curve of uh satellite launches you're you're like this is this is free
this is great um

>> but power is less than 10% of the cost of the cluster

>> sure right so so like

>> it's that 90% you're not saving anything on.

>> Yeah. Yeah.

>> Um and in so far as much as

>> for potentially a hundred times the hassle.

>> Yes. Yes.

>> Yeah.

>> Um there's this whole like you know like if you look at Nvidia GPUs right when you first turn on
the cluster

>> about 10 to 15% of them

>> fail RMA

>> in the first two weeks.

>> Wow.

>> And and that's fine. Like you have to receat them whatever.

>> And like the industry knows how to deal with this right. And and over time like Hopper is now at
5% but Blackwell's still 10 to 15%. Right. actually started out higher than that. Um, and when a new
generation comes out, it's going to be higher than 10 15%. It'll it'll have its curve gradually
decline down. But, you know, who who's going to are you going to test it and burn it in on the
ground,

>> or are you going to say 5% of my chips or 10 15% of my chips are trashed because someone can't go
up there and like do these things or am I saying, "Oh, I need robots who can do all this stuff in
space and now that's like an additional engineering problem." When sacks of meat are actually very
cheap.

>> Sacks of [laughter] meat. Yeah. Uh, speaking of Nvidia, uh, we haven't talked since the Grock
acquisition. uh what does that look like in the bull case? Like if it's if it's a good if the next
version of Grock is a great chip, is it sitting next to the you know H200 H100s in the in the rack
GB200? Like how does it fit into the actual like what Nvidia deploys? Is it just a separate chip on
the side?

>> I think it's a big vibe shift from Nvidia, right? Before they were like, "All right, I got this
big GPU. Everyone's going to use this GPU. Software ecosystem of the GPU is so good. It's one
sizefits-all. everyone try, you know, like everyone's trying to make all these like specific point
solutions, but we've got the thing that's good good at everything. Okay. Um, and then they had a
vibe shift, right? They launched this thing called CPX, okay, which is a chip made for prefill.
Okay.

>> Um, you know, prompt processing, creating a KV cache, and also good at like video generation and
image generation. Um, and that's coming out later this year.

>> Press release. They were really talking about video generation as well. So, so yeah, you've got
like CPX, you've got like the standard GPU, now you've got the Grock chips, and they all fill a
different niche, but really it screams, "Oh crap, we don't really know exactly where AI is going,"
which I don't think anyone does, right? I mean, it's it's moving so fast, the software is um the
model architectures, etc. So, we're just going to like engineer solutions that are along multiple
points of the prao optimal curve and then, you know, if

>> one of them will win, right? And I think I think it's like sort of like a big vibe shift from
Nvidia. Also, they just knew Open was going to do this serious deal, so they freaked out, but

>> Got it. Okay. Yeah. Yeah. Get me up to speed on what makes Cerebras important in the ecosystem
right now.

>> Um so so you know you have people thinking like oh latency matters in terms of where our data
center is. It doesn't matter at all. What matters is you know as we've moved from you know chat
applications which were like or search response immediately chat applications let's say response
takes 10 20 30 seconds. you've got agents, you know, I don't know, my cloud codes are working in the
background for for a long time, right? Doesn't matter where the data center is, but what does matter
is that these streams of inference take, you know, 30 minutes versus 10 minutes versus 5 minutes.
And for a lot of people, I'm fine to spend 10x the price

>> on something that completes 10x faster. Yeah.

>> Um, and so, so Cerebras sort of just makes a ton of sense there. So, OpenAI, you know, they've
got these like long horizon. There's there's like codeex 5.2 uh extra high thinking or whatever.
It's terrible. Can you guys teach them how to market? [laughter]

>> You have to sponsor this podcast.

>> Yeah. Yeah.

>> Yesterday and I did actually ask him like I I I had the Codeex app pulled up on my desktop and I
was like there are six different models and then there's a there's another button that I can pick.

>> Well, how many different products are called Codeex now?

>> There's a lot and now there's an app. Yeah.

>> We actually [laughter] on just to do branding. Lexagon branding came on the show yesterday
talking about the all the naming

>> naming architectures

>> naming architectures. It is complicated but uh hopefully

>> you could tell he's just bloods boiling [laughter] because like all the AI companies just have
the most chaotic like anthropic claude code but also you can use cloud code for other stuff and

>> yeah but yeah I mean uh with with suras it seems like there is a value to it but are they
constrained on the supply side like can they actually scale up to you know a colossus style data
center that could actually speed up codecs not just for like one user but all the users So, so I
mean servers can speed up multiple users for sure. The question is sort of like where you use it and
that's where they have to like

>> figure out where within codeex right because there are times where codeex is running for like 10
hours and sometimes you don't mind right like screw it I've put out this nice prompt gone work on it
refactor my code do this thing do this task other times I want this iteration feedback loop so how
do you expose it to the user without saying hey actually there's another toggle

>> so your permutation is is 18 times

>> well hopefully like a really robust model router but it feels like that's been a process Yeah.
So, so the open eye deal is like for 750 megawatt. It's it's not that much capacity on the order of
like what open talked about. You know, by the end of 2018, they'll be at like 16 gawatt

>> um of that.

>> So, it's like the absolute cutting edge, the most price insensitive customers in that specific
use case of this is the type of prompt that you need to return fast, then you'll get the speed up
potentially.

>> Right. Right. And and they've got to figure out how to do it from a product exposing to the user
etc. But it it's it's clearly

>> something where there is demand, right? like I don't know like Andre Kpathy doesn't care if he's
spending a thousand bucks per agent per second or whatever right like you know whoever it is this
these like super cracked engineers don't care at all and then obviously there's like a long tale of
like actually cost does matter for most people um and so so all along that curve they've got to have
solutions right

>> uh when did you first think that XAI might end up at another Elon company

>> I mean this has been rumored for a long time right like people are saying Tesla Tesla Tesla for
the longest And it's harder with a public company.

>> Yeah. Yeah. And then and then a few a bit ago people were like, "Oh, SpaceX." I'm like, "Wait,
this makes no sense."

>> But there was a very coordinated like narrative pump. Oh, yeah. Like data center at the end of
last year and it was like almost like perfectly telegraphed.

>> Well, there's there's a bet right between um basically the head of compute of XAI and the head of
comput of Anthropic. And the bet is what percentage of worldwide data center capacity is in space by
the end of 28. And the bar is 1%.

>> Oh wow.

>> And the XAI guy is like really bullish and the Anthropia guys is like

>> a little far. [laughter]

>> Yeah. Yeah. So but but it's it's a really interesting bet. Um I I [clears throat] take the under
on 1% by 28 because that's a gigawatt in space.

>> Yeah.

>> But it's actually not that crazy, right?

>> Um it's roughly 150 Starship ship launches. We'll get them to get them to a gigawatt in space.
Yeah.

>> So

>> you know Starship hasn't worked yet.

>> Yeah.

>> Fully. I was looking at the energy draw of the current Star Starlink fleet and I think they're at
like what is it uh 200 kilowatts or something like that. So you you get a thousand of those 200
megawatts and like you're starting to be in the territory something like that.

>> Yeah. So the V2 star uh satellites I think are the only ones they've launched. Maybe they've
launched a few V3s but the V3s are coming soon and those are those are like 100x more bandwidth
each. Right. And more power

>> and just more power. And so when I'm just thinking of like can you scale this thing up at all?
It's like are they two orders of magnitude off? Are they three orders magnitude off being one
something that looks like an H100?

>> I think the metric is like 50. It's either 50 kilowatts a ton or something like this per
satellite for V3.

>> Um if they let's say from V3 to whatever the compute thing is, they double it again, get to 100.
I think the V2s are like 25. Um so if you get to 100 kilowatts per ton for launch, it's it's only
150 or so Starship launches. I think that's so reasonable. um maybe not 28, maybe it takes 29, but
like

>> you know it's it's so reasonable. The question is cost and reliability and uh you know what
happens when the chip fails? How do you service it? That kind of stuff. How do you how do you deal
with having clusters be much smaller instead of like you know these big clusters even for inference
big clusters are useful.

>> Yeah. Uh yeah. Uh how do you think about uh Google's response to Grois? uh TPUs obviously very
successful but uh are they forking that project to eat more of the paro curve.

>> Yeah. So so for the longest time Google's had uh one main line of TPUs right um all made by
Broadcom and then sort of next year they've diverged it right where Broadcom makes a TPU uh and
MediaTek makes a TPU. These two TPUs are focused at different things

>> and they're fabbed at

>> they're both fabbed at TSM. Everything at the end of the day goes to Rakus, right?

>> I I want to I want to go there next, but [laughter]

>> goes to Araus.

>> So So Fab by TSMC regardless, but both of these TPUs are focused on different things and they've
actually got a third project for another kind of TPU. They're they also see this need to proliferate
uh along the curve of like, hey, do I care a lot about super high amounts of flops, not that much
memory? Do I care a lot about super fast onchip memory only? Do I care about 3D stacking memory? Do
I care about, you know, this sort of general purpose middle ground AI chip, which is what, you know,
an H100, a Blackwell, a TPU looks like today? Um, you know, there's sort of like, oh, we need to hit
the entire predo optimal curve and it's like, okay, within this there's training versus inference
differences and like what numeric you want and all these other things. There's so much complexity
there. Um, everyone everyone sort of is diverging their road maps um

>> once they're at a sufficient scale, I think.

>> Yeah. Are is Google still way ahead on cross data center training? Yes.

>> And are the other labs like is that is that important to the other labs to catch up there or is
it something that will just naturally happen because everything sort of commoditizes or do the other
labs need to sort of marshall some herculan effort to like crack the code on what it takes and what
Google's doing?

>> Yeah. So, so it's a couple of things, right? In 2023, everyone thought that scaling was pre-
training. Yeah. Right. Um, you know, more parameters, more data. And that's very difficult to split
across data centers.

>> And has Google been able to do that?

>> And Google's been able to do that to an extent, right? So what they've done is they've got, you
know, they don't have the largest individual data center campus, but what they do is they do these
like uh regions where it's like, hey, each data center is roughly 40 miles apart from each other. So
in Nebraska and Iowa and then in Ohio, they've got like these complexes. And now they're building
one in Oklahoma, Texas. You know, these complexes where there's all these data centers pretty close
to each other.

>> So it's not really cross data center across across the world, right? It's just across like
region.

>> Yeah. And then that that makes a lot of the difficulties a lot easier. Um flip side is we've also
moved to RL, right? Um and majority of the time of the chips is spent generating data, right? Only
doing forward passes through the model. Um and then you only send the final tokens that you verified
sort of back to train on to the training to the train to train, right? So then you end up with like
oh instead of in pre-training scaling you need to like synchronize all the weights every 10 20
whatever seconds. um when you're doing these rollouts and especially as things get more and more
agentic in training, you might not only need to send not the entire weights but just the tokens that
are relevant. So way smaller amount of data and way less frequently, right?

Minutes at a time instead of uh seconds at a time. Yeah. Um and so you've got this like now now it's
become like reasonable where oh actually multi data center training is completely reasonable and
people do this people do multi data center multi-chip training. Sure. Right. You know you do your
inference on one set of chips and you do your training on another set of chips. So like Anthropic
does this. Um

>> I don't know if Google does this, but Google's kind of already uh got the cards. Yeah.

>> Okay, got it. Let's go to this. But

>> talk about just there's this debate TSMC risk. Is that the bottleneck or is energy the
bottleneck? I was doing back of the envelope calculations. seems like we're using maybe like 1% of
global energy production or western energy production on on AI specifically workloads and then we're
using like 50% of leading edge fab capacity on AI workloads. Um and so that feels like okay well
even if we all agree and we say as a society we're going all in on AI we can only double the AI chip
capacity before we need to build more fabs. that takes years. Whereas we could say everyone turn off
your air conditioning. We're sending the electricity to the data centers, right?

Like like we have the ability to to generate without creating new uh did I just get something
turning off the AC [laughter]

>> turn needs to eat strokes for all the grandmothers.

>> Yes. [laughter]

>> I need my cat dancing videos.

>> You need to feed Claude, right? Um but but but seriously, like there's this debate over, you
know, is TSMC the main bottleneck or energy the bottleneck? How are you feeling about that?

>> Yeah. Yeah. So, so sidebar before I answer the question because I think it's fun. Um, you know,
in the US it's insane to say turn off your AC for AI, right? And the general public hates AI
already. [laughter] Um, but in Taiwan they've had droughts before and they've turned off water to
entire cities. They're like, oh, you get to you get water three days of the week

>> and then the fab still gets supplied water. It's [laughter] like this is, you know, you've got to
understand the mindset. We are not ready as weak Americans to do this. Um no but um at the end of
the day right like um water water water water water water and power are certainly less big of
constraints now now you've got to imagine like you know semiconductor industry is used to hey
doubling the amount of transistors made every year or two um part of that is more slow part of that
is more more capacity um whereas the energy industry in America wasn't and and so like initially
people were like not creative they're like let's do let's do these kinds of gas plants it's like
well no now we've realized you know yes there's three main uh manufacturers of turbines and then
you've for a dual combine cycle. Then you've got like IGTS, but you've also got like medium speed
reciprocating engines, right? Like turns out Cumins can make like a million diesel engines a year
and like those can make electricity. Like if I don't give a and I put it in West Texas

>> easy. Um so now it's more of like a regulation thing, a supply chain thing. Power is not a
constraint in in so far like that much, right? I think it certainly is a constraint still today. Um
it was the biggest constraint in 2425 data center capacity power uh because the industry was not
ready. people have woken up. They've like sort of been shocked to the system. Now you've got, you
know, tens of gigawatts being deployed. Um, you know, next year 30 gawatts are being added and we
think the power is there for it. Um,

>> what was it this year?

>> Uh, it's it's or this year is like I think it's like 18ish 10ish. 15 to 18ish, sorry.

>> So, so almost a doubling.

>> Yeah. Almost a doubling. Yeah. Wow. Um and when you look at when you look at um TSMC and the crew
right there is not really oh this random you know there's 12 people making medium speed
reciprocating engines that you can now convert to make uh power at some random data center. No, no,
no. There's like there is rackus, right? There is one set of spice like, you know, there's, you
know, that's it, right? And so, um,

>> and then and then the flip side is like, okay, when you have 12 vendors, everyone's got a little
bit of slack capacity, you know, there's more likelihood, you know, you can people are like, oh,
turbines, you can't get you can call a broker and you can get a turbine. You might be paying 50%
more, 2x more, but you can get a turbine. Yeah. Right. Like it's

>> you can't get a 3 nmter fab.

>> You cannot get a 3 nometer fab. Exactly. Um and so when you talk about what's the you know the
the baton got passed from semiconductor shortages in 23 to power and and data centers in 2425. Um 26
we're still we're swinging the pendulum but it will fully beat semiconductors again in 27 right and
so we see this across the entire space of the ecosystem. It's not just TSMC it's also memory both

>> because both of them have built at a certain pace. Now TSMC has been expanding at some rate. Mhm.

>> Uh the memory makers in fact have just not expanded capacity basically. They've not built new fab
since 2022 cuz their their cycle is so undulating.

>> Yeah. And and so when you look at it, it's like, oh, even if they wanted to double capacity, they
need to build the fabs. Yeah. Right. And building the fabs, it is the most complex building humans
make, right? Um it's it's it's it's the entire air of a clean room circulates itself every 1.5
seconds.

>> What?

>> And you don't even feel it when you're inside. Really?

>> It's like that. And and it's like parts per billion of particles, right? Like it's it's actually
insane how um you could you could get coughed in the face by someone who has COVID um and not get CO

>> because it gets circulated so fast it doesn't even hit you.

>> It's like that meme of like the spraying when someone's talking and then it [laughter] just gets
circulated.

>> So another another sidebar is um everyone knows CO like really popped off in Wuhan, right? Wuhan
also is home to uh China's uh largest memory company YMTC. And so when they were like welding people
into their homes, the people who worked in the fab still went to work. [laughter]

>> Wow.

>> It was because it's, you know, one, it's a national like it's national importance, but two, like
these people aren't getting sick. This fab is like way too clean.

>> Crazy.

>> Sorry, Jordy.

>> I I want to talk about Oracle. They put out a post this morning [laughter] that said, "Our
partners financing for the Dona Anna County, New Mexico, Shackleford County, Texas, and Port
Washington, Wisconsin data centers are secured at market standard rates, progressing through final
syndication on schedule and consistent with investment grade deals. Obviously, they were fast
following their posts from yesterday where they said the Nvidia OpenAI deal has zero impact on our
financial relationship with OpenAI. We remain highly confident in OpenAI's ability to raise funds
and meet its commitments." And obviously everyone was looking at this being like, "Give me a
cigarette." They're like [laughter] smoking. Like it's like bankr run language. I haven't seen posts
like this since like the FTX coms or is there something worse?

>> Um it's it's terrible coms. Yeah. Like like uh I I I I told my Oracle context like who the hell
is in charge of the Twitter? Like what are [laughter] you doing? Um Nvidia did something similar
last year when the whole TPU mania was going on.

>> It was Yeah. It was it was it was like we're we're thrilled with Google's progress with the TPU.
That said, [laughter] Nvidia chips are the only, you know,

>> it's like no one asked you to comment. I mean, like I'm sure a handful of people in your DMs and
and random, but that doesn't mean

>> doesn't project confidence.

>> It's it's sort of the lion shouldn't concern themselves with the sheep and like okay, Nvidia is a
line. Maybe maybe Oracle is a little bit more bumpy, but I think Oracle is like fine. Um, people are
just freaking out because, you know, OpenAI is is peak, you know, people are peak negative on OpenAI
right now because of how good Anthropic's been killing it. Um, yeah, I think it's just like kind of
silly like they need to they need to hire someone to do comms like a Lulu or something, right? Uh,
both Nvidia and Oracle cuz what are you doing? [laughter]

>> Yeah.

>> Uh, how did you process yesterday in general? Jensen was clip farming. Uh, he was like I don't
know why he does these street interviews, right? No other CEO does those where they just stick 25
microphones in your face and the paparazzi's flashing. It's a great vibe.

>> It's it's you know Jensen's not been as famous as other CEOs for as long and yet he's so
important now. Um and if you've like if you know Jensen how he is in meetings there I feel like
there's two Jensen, right? There is like PR like good at PR just good at talking good at like making
people hyped up and believe what he's doing. He's great at standing on stage holding up the chip,
delivering like a sermon.

>> And then there's the real Jensen, which is like a business killer and like actually just knows
about every like aspect of the supply chain, right? Um all the way from like niche semiconductor,
you know, design and and manufacturing stuff all the way to like energy, power, data center, like
and and and then doing the business deals too, right? And so like you've got this whole paro like of
a whole thing whole range of things that he's good at and he's a killer in. And clearly he's like he
was in a meeting where he was being a killer and like negotiating like supply contracts or
something.

>> Oh, he walks out and then he walks I mean that's hilarious. Yeah theory, but I like it. Yeah,
that's awesome.

>> And and that's why he was like, you know, like he was like still killer. Like no, we never said
we committed to hundred billion, you know, like. And it's like

>> I don't know where did you even get the hundred billion dollar number from.

>> And it's like well you did go on CNBC and like you make a big deal out of it. I think people
would assume that it was but but they did say in the press release and remember these are early
talks but they just kind of jumped the gun. This was the height of the press release economy.

>> Yeah. Yeah. What's funny is um Oracle stock peaked like just like a week after they announced the
open eye deal. And so like the press release of like hey open do this humongous deal stock peaks.
Um, same happened with a couple other vendors who uh announced deals with OpenAI or Nvidia like sort
of a lot of these like like they all peaked then and then it's sort of been like Nvidia OpenAI trade
has been going poorly and sort of like the TPU anthropic Google Amazon complex has been doing well.
Um, it's quite interesting good energy back at home with the roommates. [laughter]

>> What what's going on?

>> I wanted to uh uh Yeah, I got one more thing. I uh so yes, over the weekend it was sort of
drowned out by all the Justice Department stuff, but

>> wait, have you guys talked about Elon saying he can smoke a cigar in the fab?

>> No.

>> Yeah. Yeah. Yeah. Okay. I was going to say this is this is this is part of the whole thing.

>> I didn't realize that was related. Yeah, that makes a lot of sense.

>> Yeah. Indoor heaters. We have indoor heater technology. No one's taking advantage.

>> Yeah. What what does the fab look like if you have no humans inside? Like that's probably
[snorts] his long-term thing is like Yeah. There there will be an optimist. No one. No. Like the
number of people work in a fab is like irrelevant. Like

>> Yeah. But but is it is it irrelevant because there's all these things you have to do when a
human's in there because they sweat and they breathe. And if you don't have to do that because it's
a robot walking down even if it's puppeteered or teleoperated. You you might be able to have
different considerations. I don't know if that actually affects

>> Well, it's like a nesting of like it's a nesting [clears throat] of like cleanliness, right? For
example, you've got this wafer you've put like down let's say you put down copper and now you're
moving it from one area to another. Well, it needs to be stored in a vacuum, but easiest way to
store a vacuum like or or an inert gas. Um, and that's like the thing that's being transported in,
but then around that you want it to be super clean as well. Um,

>> you you you if you don't, then the copper starts getting oxidized, it affects your yields, all
this sort of stuff happens. And so, like, you kind of want it to be a need layer, nested layer of
like, well, this ch this thing inside the EV tool is super clean and then the thing feeding it is
super clean and then the thing it sits in is super clean cuz cuz that's how you get to like there's
zero particles. Well, because like you know in the in the in the foop in the transportation devices
like parts per you know trillion and maybe FOP it's called F O P front operated uh front opening I
don't know something pod

>> but it's called a FOP it's like the thing that moves and it carries the wafers sure um and then
and then the fab is like parts per billion and you know sort of like you know you you've got to like
got this nesting relationship so everything is super clean. Um, you know, I'm I'm bullish on robots,
like super bullish on robots, but only for like not for tests that have like TSMC's, Arizona fabs or
okay, let's say TSMC Tynon, which I think produces like,

>> you know, indirectly hundreds of billions of dollars of global GDP. Even directly, it's like
still tens of billions of dollars, has like 5 10,000 people in it. Like it's like irrelevant in
terms of the number of people who work there

>> in terms of the overall economic value that's created,

>> right? It's like it's like it's like how many people fold laundry or how many people wash dishes
or how many people like do construction work. Like these are way bigger markets

>> for robotics. Yeah, makes sense. Uh speaking of China, um what what are you making of the the the
Daario essay or I guess his comments at Davos about uh you know selling chips to China is equivalent
to you know nuclear weapons these days. the the Ben Thompson line was something like uh he's he's
okay selling chips because he wants dependency on the Nvidia ecosystem cuda but he would ban uh
lithography tools from going to China and I'm always I've I've been wrestling with this idea of like
I don't know if China would accept this but wouldn't there be a different world where you want them
dependent on American LLM APIs and you don't even send them the chips and you say yeah you're you
can have as much AI as you want as long as you're paying you know open AI and anthropic API Yeah, I
think it's I think it's like a curve of like

>> what they will accept.

>> It's it's it's you know, one you you you push someone into the corner, they're going to start
swinging, right? And and I'm I'm like very concerned that China does this, right? Do they do you do
you push them too far into the corner? Do they say screw this, we're going to start being a lot more
aggressive. We're going to we're going to do more military actions or or even just invest twice as
much in

>> in global supply chain take over Africa more than they already have latam like etc. there's
there's or or just take over Taiwan, right? Because if I can't have the chips, what value is there
in Taiwan existing in its current state, right? So there's like there's this like game theory
aspect. Um at the same time, you don't want China to be able to like, you know, if you believe AI is
going to be do what I think many at least in San Francisco think it's going to do, which is like
completely revolutionize humanity and cause GDP growth to accelerate. Um do you want to have China
also own that technology? um and the and all you know their ability to integrate that into their
military and all these other things much faster you know so there there is like these competing like
you know interests where where is the like right line and some people think it's like hey yeah sell
them AI model well I think Dario would say don't even sell them AI model access

>> don't even sell them tokens

>> yeah I think so I think like I think anropic does not sell AI access to China they they loop it
through and you can see this in the traffic data they go through Korea and Japan other places but
like and so they get it um

>> and then the other other side is like sort of like I think the Ben Thompson view which is like um
and I think I'm more sympathetic to that although I think I'm not exactly in aligned with that which
is like and we've been saying like don't sell them equipment don't sell them equipment don't sell
them equipment um and my view my argument is like more economic in the sense of like if you sell
them like tens of billions of dollars of equipment they can make hundreds of billions of dollars of
AI value or chips with that equipment whereas if you sell them AI model access and it costs them
this much to get the economic you know they're not able to

>> so you're capturing more of the value west yeah

>> um and so that's sort of the question that is is at foot here right do We want them to capture
all this value of the of the supply chain in equipment or by buying the chips or using the models
right and services. Um and we've seen you know across many you know stacks China refuses to accept
uh you know using American ecosystem and they'll wait many years before they develop their own
whether it was like hey they didn't use Windows they figured out a bootlegging economy or they
didn't use Visa and eventually they came out with like Alipay and WeChat pay or whatever it's called
on and and like these things are way better than Visa in fact right lower transaction cost and
higher volume.

>> Have you ever used Red Star Linux? It's North Korea's Linux distribution. Really? Yeah.

>> If you if you don't uh if you put it on a network, it'll immediately call home. So, you have to
put it on a on a on a firewall network or else it just like steals everything immediately.

>> I'm a fan of Temple OS, you know. [laughter]

>> Yeah. There you go. Uh uh is Doug Olaflin suffering from a case of cloud code psychosis?

>> Okay. Yes. Yes. So, I think I think everyone's like cloud code is for coders and it's like no.
No.

>> Cloud code is for people who don't code now. Yes.

>> Right. And that's the big realization this year. Um,

>> you know, we've got we've got a couple folks now in the firm who have psychosis, but Douglas
Olaflin, who is like, you know, semi analysis number two. He's president, you know, he's my boy. Um,
he's the one, in fact, he's the one who encouraged me to make a Substack a long time in the long
time ago.

>> What were you doing before?

>> Uh, I I had a WordPress blog and I was like consulting on the side, but I was like, okay, let me
do a Substack now. Um, because I saw him making money off it. I was like, this is Like, why are
[laughter] WHY ARE YOU GETTING PAID FOR THIS? Like there were multiple times where he wrote
something was like I could do way better. [laughter]

>> I'll show you.

>> And like obviously like it was good because we both taught each other a lot of things and we
we've been great friends and eventually he joined semi analysis but like

>> you know he he his background is he was a hedge fun analyst and then he decided to do a Substack
walk hike the Continental Divide Trail for like six months walking from Mexico to you know and then
and then you know came back to doing Substack and tried to do a fun

>> six months of touching grass and then he was like I'm ready to lock it on clock.

>> Yeah. Yeah. and and and so now he's, you know, like he's he's never been a software developer,
right? But he's been on a generational run like he's he's he's not coding anything, right? He's just
telling Claude to do stuff and like it's to the point where it's like our our our like head of data,
head of it is like, "Oh, can you send me that?" And he's like, "Uh, how do I do that?" And then he
like he zips the whole thing and sends it to him. It's like local host.

He sends him a leak once. It's like local host like

>> it's like, [laughter] "Bro, that's not how this works."

>> But but yeah, no, I I I've talked to some folks at Vibe Code and they'll be like and I'll be
like, "Why did you choose no.js?" And they're like, "What's no jazz?" [laughter] That's a very
specific

>> someone. Yeah.

>> No, but like [laughter] it's um we went on we went on a little tour of a lot of our clients like
you know roughly like half our business is or 40% of our business is like hedge funds. So, we went
to New York 2 weeks ago and we went to all of our clients and like part of it like them asking me is
opening I and I'm answering like no I think they're fine and and then like some actual ideas and
then like a lot of Doug just telling them cloud code is like they they're like you don't have to
hire any junior hedge fun analysts anymore and they're like the junior hedge fun like and then he's
explaining you know what what can you do it's like well like you can just do like financial models
and perform a financial models and like everything in cloud code without ever opening Excel and you
can generate charts and like you don't need

>> to know how to code.

>> You just need to know how like how this stuff generally works and you can just do it.

>> Are how how many hedge funds are just trying to copy trade situational awareness?

>> Yeah.

>> Um I mean I think everyone who's I think I think a lot of hedge funds obviously believe in AI. I
think there's a lot of them who don't believe in it, right? To be clear, but a lot of them that have
done the best believe it.

>> Believe in it. Why are they selling software everywhere?

>> Oh, you mean selling software stocks?

>> Yeah. Yeah.

>> Yeah. Why the selloff then?

>> Yeah. I mean I mean of course it's like an incremental thing right um and but anyway so so these
hedge funds like and then then the question is like okay if you believe in it how do you manifest
that trade um and and so when you look across the like ecosystem um I would say almost all my
clients sometimes think are two years out numbers are too high

>> um but like there's there's like Leopold's like your numbers are too low [laughter] and so it's
like it's like it's like uh in general right and I think I think like if you think about how much do
you believe in AI and what's your access to information of AI um you know there's not many hedge
funds who

>> live in San Francisco and like fully breathe and live and understand it then and then depending
on how much you believe in AI how do you manifest that trait right

>> are you surprised that more hedge funds wouldn't like even just smaller shops wouldn't say like
hey this AI thing seems like it's going to be big maybe we should set up in San Francisco

>> or hire

>> there's there's a number of people right um so we're we're you know we're getting an office uh
together Leo pulled myself and then a client of mine another hedge fund and they have one analyst
here and it's And there's like a number of other hedge funds that are like hiring analysts here.
But, you know, being plugged into the AI ecosystem does not mean you're just in San Francisco
because you can just walk around and talk to like doofus like startups and VCs and like not
actually, you know, see what's coming down the pipeline. Um,

>> and you have to comi com combine it with all sorts of information, right? You have to have a good
tune with like what's going on in Asia supply chains. You have to have a good tune with what's going
on in New York. Um, you have to good tune with like what's going on like in the in the financial
markets, right? and then like what's going on in credit markets and what's going on in all you know
the data center energy blah blah blah all these different industries and so it's it's it's actually
not like so simple to like be in tune with what's going on in AI you can easily get like head faked
right um

>> you know for the longest time people were thinking you know Adobe is an AI company and like and
it's like

>> for for a bit like Adobe was going down on AI and then they like launched a few AI features and
the stock skyrocketed and then now it's going back down again because people realized oh wait no
actually it's not an AI company like um I I think It's it's the manifestation and thought of like
what is actually going to the world going to look like if Anthropic 3xes its revenue again this
year, OpenAI 2xes its revenue again this year or you know by the end of the year do how many people
even believe by the end of the year AI startup revenue is over hundred billion dollars. I think
that's an insane statement for a lot of people, but that's what it's going to be, right? And who
believes that number, right? It's like very few people. And then you you you draw the continuation.

It's like, who believes, you know, and when Anthropic says in their funding like, hey, we're going
to have $300 billion of revenue by the end of the decade, and it's like actually um I think that
number's too low [laughter] because because the economic value of what they're going to create is
going to be insane. Um and and you tell people, oh X, you know, OpenAI is going to have 18 gawatts
or 16 gigawatts by the end of 28 and they're going to be able to pay for it and that's like, well,
that's $300 billion to spend. How are they going to pay for it? It's like you you sweet summer
child. Don't worry, Sam can raise. They're going to blow up on revenue. They're fine, right? Like it
is like a bit of a vibe thing. It's a bit of like,

>> you know, irrational exuberance almost, right? Like um Lip Hold's in his, you know, mid 20s. Like
I'm 29. Like we we are irrational, right? because we have not lived through, you know, you get these

>> these PMs who like

>> you've never been you've never been that humbled. I

>> I don't know like we almost my family almost went bankrupt in 2008 like you know cuz we lived in
a motel and we almost forclosed and we actually did forclose on one motel like pretty bad but like
yeah I mean I was still a kid right like it was like yeah I've never been

>> humbled. It's good I mean it's good to live through that and understand how things can go wrong.
Uh what are you expecting out of Zach and Meta this year? We've been big Zuck defenders especially I
mean there's this pressure of like oh Meta is spending so much and yet they haven't created you know
any any AI product that's super compelling or that's really working and our stance has has generally
been Meta's making more money from AI than almost any company in the world outside of Nvidia.

So it's like of course Zuck should be justified in saying hey this is real it's big like I'm going
to like back the truck up and and go all in.

>> Yeah. I mean, it's it's clear if you look at the most recent earnings, I think their CPM went up
9% when the consumer is weak, which means like if you were to like try and strip out like what is
consumer spending increasing for CPM of ads versus what is the effectiveness of their algorithms,
their algorithm got better by double digits in one quarter,

>> right? It's like actually insane how good

>> the ALGO is getting, right? Um at serving you the slop and the ads, right? Um, so, so, so in that
sense, like [laughter] the pig sound, the trough. I love

>> I got [laughter] so slop for the slop.

>> We're going all in on that on that [laughter] slop.

>> So, I love it.

>> Uh, so, so, you know, if you if you think about it, right, like, okay, Meta, where are they going
to like win, right? Um, you know, I think if you have the Galaxy brain take, it's like, well,
they've got the best like wearables coming down the pipeline. They're going to put AI on it. Apple
won't be able to put good AI on their wearables or they'll seat it all to like Micros Google or

>> the other people people have had this narrative, oh, uh, as AI gets better, the the value of real
world experiences will increase. And I think that's a cool theory, but if you actually play it out,
AI getting better means more content that's more uh like effectively crafted for you, more
personalized, a hundred times more con thousand a million times more content. That would imply to me
that people will just use digital products more, which means more time on site, more time in the app
for meta. So I don't know.

>> I I mean I I'm I'm with you entirely. Um, but I think I think like the galaxy of bra intake is
that you're just going to have a wearable and that's going to have AI assistant. Open is trying to
make it wearables, you know. Um, you know, there's there's, you know, everyone's trying to make
wearables, Google is, etc., etc. I think metal will actually execute and then they'll have

>> a good AI. Um, and then you you stack on like a few things, right? How do they get users? Well,
we've seen at least if you look at the user metric charts, Google's use, you know, Open Eyes users
were growing, growing, growing. They were going to hit a trillion by the end of the year. They 800
billion. Why did they not keep growing in the last quarter? It's because Nana Banana came out and
they took all the incremental users, right? Um and and likewise, if you go look at like, you know,
Gemini 3 didn't actually make Google grow that much. It was Nana Banana and then Pro or two or
whatever it's called, right?

Those were the ones that made them really grow.

>> Uh Meta's licensed all of Midjourney's uh code, data models, right? One, two, they were like
actually just like focusing hardcore on.

>> Was that was that a a billion dollar plus deal? The number is undisclosed. Mjourney still exists
as a company. Um,

>> no, it felt it looked to me like effectively a massive exit, but the best case scenario where
they can just keep kind of being artists.

>> I I think I think if you had me guess, I would bet it's a over a billion, right?

>> Every deal that Meta did was over a billion. [laughter] They basically like whether it's an
employment contract, a licensing deal, an acquisition, everything had a B after it.

>> Well, so so [laughter] the interesting thing is

>> that is you're missing a zero again. Don't never miss the zero again.

>> Yeah. Every discussion was how many billions are we spending on hiring this person, buying this
company.

>> Well, you know, Meta interestingly um has gone down market for compute because they there's not
enough compute in the big size deals. So, they've actually gone and like bought like small clusters.

>> Oh.

>> Because it's like well I want more comput

>> from like from like longtail neoclouds or

>> Yeah. Just like Yeah. From a longer tale.

>> Okay.

>> Um because that's the only place they can get the compute they need. Interesting. because you
know they've already like went out and signed big deals with Google and coreweave and so on and so
forth.

>> Is cluster max 3 going to be a smaller chart because of consolidation in the industry?

>> No, it's there's more.

>> It's going to be bigger. It's going to be bigger bigger. Um but but you know so so Meta

>> some thunder [laughter]

>> that's ominous. It's ominous. Um so so I think meta will you know capture consumers through
generative. Um if there's more content people are just going to go to the content marketplace,
right? um the creator of the content captures less value as there are more content creators and more
diversification of content, right? Um and so I think Meta just wins by being a platform, right?
Google does too and Bite Dance does too, right? But like those three win by having the platform and
then the real question is can they get in the assistant uh productivity game, right? And I think
this is

>> and through that effectively search like if you're an assistant it means that you can like
there's some commerce happening.

>> Well, they span out and poached a bunch of people from Google. So, this wasn't in the media much,
but like they actually poached Google search people with similar sized deals as like these crazy.

>> Yeah. And I always I always I you know demoing demoing any of the the the wearables, you can
imagine like Meta wants you to walk around in the world and see like, oh, what are those headphones?
And like while we're talking, I just hit my little thing and buy it, right? And it's like you didn't
even necessarily know that it happened. Uh but like of course Meta is going to want to

>> knows those are the Sony MDRX272s 462. Dude, I've been I've been screaming about them like doing
some proper marketing

>> branding. So,

>> it's it's literally like their over here is like WHX 1000XM5 and then their inear is like WF100
XXM1000. It's like [laughter] dude just call them like Bravia buds and Bravia like headphones or
some

>> Well, China just just bought Sony, right?

>> Yeah. Yeah. The Bravia brand is actually a Chinese company now. Sony sold their TV and

>> PlayStation buds.

>> Yeah. Yeah. Yeah. PlayStation Walkman.

>> Oh yeah. Walkman

>> something something

>> for sure.

>> Anyway, uh anything else, Jordy?

>> No. Great. I'm excited for this weekend.

>> Yeah. Yeah. Super excited. You guys

>> What are some plays? We don't watch a lot of sports. What [laughter] are some football guy,
right?

>> Yeah. Yeah. Yeah. Grew up. Yeah. Rural Georgia, so I like football. High school football was the
thing. College football was the thing. I think NFL is a little less

>> soulful. Sure. But, you know, now now college football has has has the NIL and so it's also
soulless to some extent. It's fine. We we enjoy it, you know, um primal desire of seeing heads
clash, you know, and and and and sometimes that manifests in like, you know, Twitter drama and
sometimes that manifests in real football.

>> Yeah.

>> Um all I can say is the Patriots.

>> Okay.

>> Whoa. Okay. Okay. Uh I'm kind of bummed. We're we're going to we're going to since we're going to
be at the game, we're not going to really get the great experience seeing the ads. I'm going to be
like glued to I'm going to be like glued to my phone. I I want to see all the AI uh the different

>> Well, don't worry. I got some more ads for you. Thank you so much for coming.

>> Thank you so much.

