# Dylan Patel: NVIDIA's New Moat & Why China is "Semiconductor Pilled"

- Date: 2026-02-05
- Channel: The MAD Podcast with Matt Turck
- Duration: 1:16:51
- URL: https://www.youtube.com/watch?v=DqBMzuzxZog
- Source: `uv tool run youtube_transcript_api --languages en --format json DqBMzuzxZog`
- Note: timestamps are preserved in the paired JSON file.

## Transcript

This is the biggest change in human history maybe ever. What's about to happen with AI? This is the
biggest revolution bigger than industrial revolution. Jensen is very paranoid about losing. If he
just kept making his mainline chip, people crush him on cost and performance. Acquiring Grock is how
you get those resources to make more solutions for different parts of the market to stay king. At
the end of the day, this is an economic war. If the US and the West win in AI, China will not rise
to be the global hedgeimony. But without AI, China definitely will rise.

They're just going to outrun America. Hi, I'm Matt Turk. Welcome back to the Matt podcast. Today I'm
joined by the one person Wall Street and Silicon Valley turn to when they need to cut through the
hardware hype, Dylan Patel of Semi analysis. We dove into many of the most important topics [music]
of today. Nvidia's massive move to acquire Grock, the truth about the capex bubble, whether the US
power grid can actually handle the AI boom, and the geopolitical chess match [music] playing out
between the US and China. But I have to warn you, this conversation went off the rails in the best
possible way. And we ended up going into all sorts of fun tangents like the strange phenomenon of
Chinese romance dramas set inside semiconductor factories and what's really like when three AI
famous roommates live together in SF. Please enjoy this fantastic conversation with Dylan.

>> Hey Dylan, welcome.

>> Hello. How are you?

>> I'm great. I'd love to start with Grock and Nvidia since it's still fresh. So, not so long ago,
Nvidia was saying that uh one GPU could do it all, and now they're doing this acquisition non-
exclusive deal with Grock. What does that mean from your perspective?

>> It's very clear. We're not sure where AI models are headed in terms of, you know, over the next
few years, what happens to the architecture, but you know, the thing that I think everyone is sort
of like agreed on is models are pretty auto reggressive, right? Next token generation is like the
thing but beyond that right attention mechanisms changed the how how it works everything changes
right could could change and so what's interesting is the reason Nvidia one is because they just
took like the widest surface area bet and then people kept developing models on that and that kind
of shape worked but now the workload is so large that there is room for specialization that will
give you 10x increases in certain domains right in a general purpose workload grock doesn't work
right you know it can't train it can't you know it can't inference really really large models um
cost efficiently, right? You can't serve many many many users, but what it can do is it can go bl
screamingly fast, right? Same with the cerebrous open AI deal, but that's like one workload, right?
Uh very decode focused, right? Gener doing auto reggressive tokens in a in a single stream super
fast. Another direction AI models could head, right? We don't know are models going to think in one
token stream or is it actually they're constantly context switching, right? and they're going from
they have this humongous humongous context and they're generating in multiple parallel streams right
and so Google and openi have both released mechanisms of this with their pro models where the model
actually doesn't just have one single chain of thought for reasoning it has multiple right and then
I don't exactly like you know and and and how they choose which one and what the final answer to you
delivers is is an area of research um but there there is room for that kind of chip right something
that works on very parallel a lot lot of streams of chain of thought and maybe the latency
requirements are not as crazy, right?

Maybe you don't want to go blindingly fast, right? Maybe you're okay with it being, you know,
because I can spin up 100 parallel, you know, streams of thought or agents or whatever you want to
call them. Maybe I I care a lot about cost there. And because it's 100 in parallel instead of one
going super super fast, it's not as deep, right? The tree search or the depth of the inference is
not as deep, but it is much wider. You know, there's other parts of inference. Hey, process do
creating the KV cache. So, Nvidia has a chip for that, right? That's the CPX. So they they've made
the CPX, they bought Grock for decode, and then they still have their general purpose GPU. So
they've they're kind of trying to cover their bases because unlike the first wave of AI chip
companies where they sort of just made chips and then tried to figure out where it would work,
right? They had a thesis, Grock and Cerebrus, both as well as Samanova, right, which was put a lot
of memory on the chip and not necessarily in the case of Cerebrus and Grock, no memory off chip. And
in the case of Samanova, less memory offchip or slower memory offchip with higher capacity. You
know, they they sort of all made similar bets in that direction.

And it didn't work for a while until it kind of did, right? Um because there's a workload that now
necessitates it. Nvidia recognizes they're they're the leader. They're at the tent pole. Hey, in one
respect they can just run faster than everyone, but it's kind of hard to be 2x better than Google or
or OpenAI or whoever else's internal chip, right? To justify their, you know, 75% plus margins,
right? And then they have to be 2x to 4x better to justify 4x better to justify their margins
because that's what they're charging above COGS. You know, the question is what what architecture
will deliver that? Well, yes, keep the programmability of their GPUs is great for training and for a
lot of workloads, but you know, guess what?

I think I think a lot of people will just be downloading an open source model, downloading an
inference framework and pressing go, right? A little bit more complicated than that, but that's
that's going to be the consumption method for a lot of enterprises, a lot of uh startups, a lot of
tech companies is they're just going to do that or they're going to rent the G GPUs or or rent the
chips and then download an open source framework and model and go, right? And Nvidia recognizes this
and hey, there is room for products that aren't general purpose, right? The general purpose GPU will
still probably be the main line for training and for a lot of inference and for costefficient
inference, but maybe blindingly fast or workloads that have a ton of prefill, i.e. creating the the
KV cache. Maybe that those workloads could be different chips, right? And the CPX chip they
announced, right? They say it's for the context processing, creating the KV cache. It's also really
useful for video models because video models don't care about memory bandwidth and so you know why
pay for the expensive memory that the general purpose chip has or why do what Grock is doing which
is tying hundreds or thousands of chips together and not having memory but keeping the entire model
on chip. The trade-off for that of course is you need thousands of chips and you have less compute
per chip and so like Nvidia's trying to capture the whole surface area because again you don't know
where models are headed and it's hard to say where the research is headed.

>> And do you think it's a good thing for the market? Yet another one of those deals that's
structured as a as a license but really an acquisition.

>> I certainly think it's not good from an anti-competitive sense, right? I don't think people
should just be able to buy companies without like any antitrust like process at all. Now, in the
case of like a large company buying a startup, I'm completely fine with it. The flip side is like,
hey, we know the deal is happening, right? Uh this happened for a company I was an adviser for
Nvidia acquired in fabrica just maybe a few months before they did Grock and similar style of deal
right if someone wanted to strike it down that's the biggest limbo right we've seen this happen in
venture and you probably know more stories of this but like a company trying to get acquired they
get stuck in limbo for like a year

>> and then it falls apart

>> stories

>> yeah it falls apart the deal did because some regulatory BS and now the company was and the
founders were focused on getting the deal done instead of like making the product better for a year
and now they're like behind or you know they they they weren't focused on growth as much right you
know you only have so much time as a founder so in that sense I like the license deals right

>> so now is uh Nvidia also dominating the the inference market is there any world where Nvidia is
no longer the king or they seem to be getting stronger

>> I think the thing about Nvidia is they take the Andy Grove mentality like more serious than
anyone else right like okay fine Google like implemented OKRs because Intel did it but that's like
you know management stuff, right? Only the paranoid survive, right? This is like core to the Bay
Area, um core to Nvidia. Um Jensen is very paranoid about losing, right? These specializations, if
he just kept making his mainline chip, would mean people could, you know, point point solutions for
specific parts of the market would crush him on cost and performance. Then he can't justify his
margin. That's a threat to Nvidia's business model as a whole, especially if the best model only
changes every 3 months or the model you want to roll out. Okay, well then you're going to have three
months to figure out how to make a model work on one chip architecture for that point solution and
you know it's fine. Software software advantage of Nvidia is not that important. Then Jensen's super
paranoid about losing and frankly it's really hard to hire enough talented chip people. When you
look across the market, there is only a few companies who have successfully created a chip
architecture software to run the models accurately, run the run the models accurately, right? Like
cuz you can look at random APIs of say an Alibaba Quen model and different people are doing all
sorts of tricks like quantizing it, but also many other tricks which then end up like making the
model quality lower. You know, building a rack scale solution, networking thousands of chips
together and then deploying an API and Grock did the whole thing with frankly not that many people.
So now it's like okay well I'm Nvidia I want to make four different chip architectures and actually
four different point solutions maybe the general purpose and then one here one here one here and in
addition my general purpose thing is actually not just like a GPU chip it's like GPU chips CPU chips
networking chips NV switch nicks like you know there's many many chips and each of those chips has
many chiplets you don't have enough engineering resources right and so like acquiring gro is like
how you get those resources to make more solutions for different parts of the market as far as like
are they threatened like I think I think like obviously There's some cool startups out there, right,
that are raising a lot, right, currently or have raised such as Etched, Maddx, uh, positron, these
new age of AI companies.

There's also the prior age of like Cerebrris is is out there still, right? You know, Tenstor, etc.
And there's so there's a lot of AI chip companies on the startup side, but then there's also, you
know, Google's TPU, AMD GPUs, uh, Amazon Tranium, uh, who are all really credible competitors. And
then, you know, Meta's MTIA is somewhat credible. and then you know Microsoft Somaya is not credible
but like you know maybe it will be one day right so you sort of have like a lot of competition
they've got to hold the gates back and so I think

>> is there a risk to them being I mean like there's there's risk from all of those companies that I
mentioned and and you know effectively California/ Seattle right only two two places there's there's
also chips from other parts of the world right obviously China has a number of different AI chip
companies that are doing cool things anyone would have told you Grock was you know their business
revenue their revenue was not like stellar right in fact they missed revenue last year significantly
and yet they got bought right because the value of the IP was there and the value of the team anyone
else would have been like well why the heck would I buy this right uh makes no sense there's
definitely a credible threat

>> yeah and do you think uh CUDA is going to remain that mode I guess a combination of CUDA and
whatever came out of the Melanox acquisition like do do those persist as long-lasting advantages

>> I think they do I think networking is super important I think uh the CUDA software mode is very
important but it's also like changing rapidly right It's an incredible amount of the software that
Nvidia GPUs run on is not from Nvidia. It's it's the developer ecosystem that's open sourcing it.
When you look at, for example, VLM and SGLANG, right? These support AMD GPUs almost as first class
citizens now. And VLM is getting significant support for TPUs for tranium and there will be other
chips coming out from startups that also support VLMs SGLang. Now like how difficult is it?

You know the the the reason why CUDA is so important is like okay I can do whatever I need to do
right programming a GPU.

>> I think most AI chips will not be consumed by people programming anything for it.

>> They will download an open source inference engine. and they will download an open source model
and then they will put it on the and it's really simple to download VLM and like make it work like
it's not that hard to set up uh you know a server and Nvidia's putting out a lot of open source
software like Triton inference server and and uh Dynamo and all these things to to make it easy
because that is the consumption model ultimately for the majority of AI right is and it might be
like oh it's my own inference engine but most servers will not run code besides the inference engine
and the model it's like not like people are actually like researchers are like writing code for GPUs
to see ideas if they'll work and train models and all these things or just mess around with them to
figure out you know infra performance or whatever it is but most of it won't be there and so CUDA as
a mode CUDA language is like you know like it's like fine right like you know no one actually writes
CUDA right like most people write PyTorch and then like torch compile and then they just run it on
the GPU they don't write CUDA but a lot of this CUDA mode is like how does PyTorch translate into
high performance GPUs and that surface area from when people were just writing like hardcore when
people are hardcore writing CUDA kernels to like hey they're writing PyTorch and then it's compiling
down to GPUs versus oh I'm just downloading VLM is it is a it is a curve of like not a ton of people
that can do CUDA kernels a whole lot more people can do PyTorch right random you know PhDs and
random people it's very simple right a crapload of people can do VLM download it run it on a server
well if it now supports other chips what is the CUDA mode's recognized this and they've been
building software that is not necessarily the CUDA remote and I I can give some examples All right.
So the name of the game is fast tokens and lowest cost tokens, right?

And lowest cost tokens happens by your chip being fast. But there's also tricks, right? One example,
right? Like I mentioned with, you know, the CPX versus Grock, right? Is processing your prefill
contacts, right? Super cheap CPX, right? If I'm if I'm care a lot about speed, then Grock. These are
optimizations on the hardware side. There's optimizations on the software side as well, right? And
so one example is when I'm doing for example if I look at a cloud code or a cursor type application
right the workload is like it takes your repo takes the relevant parts of your repo puts it in the
context of the LLM it prompts it generates right and if it's an agent mode it it it circulates the
context a couple times it'll collapse put things off to the side access different contexts but
what's you know especially when you think about an agent for software and you can see this in codeex
you know Codex Codex actually not as good as cloud code, but it can do work on time horizons of like
9 10 hours. Um, and do like a big refactor better than cloud code can, even though most of the times
cloud code is better. And and what's interesting about Codeex does is it'll like take your repo,
it'll identify parts if you're asking it to refactor it, identify parts, write stuff, you know, make
like these notes for itself everywhere, collapse the context, switch from this part of the repo to
that part of the repo to this part of the repo. But when you think about it, it's like, oh, if this
thing is just generating tokens all the time, plus it's switching what my context is constantly,
that's really expensive, right? If you think about like what's the cost of inference, um, I want to
say it's like it's it's $10 per million tokens of output and or and $3 for decode or 10 for decode
and three for prefill. Uh, and so if you think about, oh, it just worked for nine hours on one task,
one refactor, huge value. But if it changed context a ton of times and your context is like 30k
usually or 50k or you know heading to hundreds of thousands you know how long your how big your
repository is and how much context switch now you're spending all this money on on prefill right not
the decode tokens but actually why am I like regenerating the KV cache I can actually just like
store the KV cache elsewhere and then when I need it again I can pull it and and plop it into CPU
memory or into GPU memory. And so Nvidia's got this like KV cache manager and they've been working
really hard on like making it so they can interface SSDs and stick the KV cache on there and pull it
out whenever they want. So for this kind of workload and then if you do this and you look at like
coding as an application and you like look at these coding companies and how much they're paying for
prefill versus decode actually majority of their cost is pre-fill tokens not decode tokens because
their context is just so large and it's switching all the time even in agent modes. You know, if you
can now not have to do the pre-fill, your costs go down dramatically. But that's a very complicated
thing to do from a software perspective. You know, companies like Enthropic, Google, OpenAI have
already done it. But what about the wide world, right? And so Nvidia is trying to make the open
source software for this. And that's like CUDA mode, but it's like actually no, none of this is
CUDA, right? like it's like memory management and like you know storage management and when do you
call what and how do you transfer it and how do you like spread the KV cache across a bunch of
different storage nodes and what happens when you read it and the network congestion just like all
these things yeah it's like Nvidia's wheelhouse but it's not CUDA and I think like the easy way to
say it is it is the CUDA mode right and so things like this KV cache manager and many other things
they're trying to do to reduce the cost of inference like is how they build the new CUDA mode
because again today it's it's you know it is quite I mean AMD is like not fully there yet and TPU is
being added right now and tranium is being added soon as well to VLM but all of them will have a
very good UX for download model run model on VLM by the middle of the year I think right certainly
AMD is already there by the end of this quarter we have something that like tests this right it's
called inferencemaxa it's open source all the code is and the results are uh but we run across I
think $60 million of GPUs which are donated to us by companies like Nvidia AMD openai Microsoft
Amazon on Crusoe, Core Weave, Together AI, uh all these companies are sponsoring GPUs for us to run
this.

We're running VLM and SDG Lang every night on, you know, nine different kinds of GPUs on a variety
of different models and different work uh context lens and all these things, right? To see the
performance and you can see the performance moving every day or pretty often because the software
changes all the time. And so like the fact that this exists is the cuda boat, right? It's not that
like AMD you can do this on their chips, Nvidia can do this on their chips. It's oh when the new
model comes out, how fast does it get to peak performance? because you know it's it's a moving
target or hey can I implement this KV cache management thing how hard is it how many engineers do I
need oh just one great like or 10 great if I need a hundred people to develop it like Google and you
know so on and so forth did then that's much harder

>> do you think AMD can uh catch up

>> I think AMD will be caught up at times and very behind at other times like currently they're
super far behind right because Blackwell is just way better than MI355 um and then you know Rubin
comes out and they'll be way way behind but then AMD's new chip comes out and AMD will be caught up
or evenlight ly ahead on a hardware perspective. Software's behind, right? And you have this like
leaprogging and and AMD is a very credible second competitor. I don't think they'll go beyond like I
think they'll stay in single digits market share. Single digit percentage market share.

>> Single digit percentage market share is

>> still [laughter] pretty good.

>> Yeah. I mean, Nvidia's revenue this year is going to be like

>> it's a lot.

>> The three gajillion dollars.

>> I think it's actually four gajillion. [laughter] [gasps]

>> What about all the startups? You mentioned a few. So there's a cerebrus on the one end of the
spectrum and then newer ones edged and and others if if AMD has a you know uphill battle in front of
them like do you think those guys can take significant market share? you sort of the whole
specialization game, right? You you have to specialize because you're never going to beat Nvidia at
their own game, right? They're going to have the supply chain unlock.

They're going to get to the newest memory technology or process technology or whatever packaging
technology, whatever it is, sooner than you and they're just going to crush you, right? If you play
their game, you have to AMD is trying to play Nvidia's game, but AMD is like extremely good at
engineering silicon, right? Everyone else has to has to has to try something weird or different,
right? And so when you look at Etched or Maddx or Posatron or Cerebrris or Tenstor, you go to look
at all these companies, right? There are unique things about what they're doing and it's not clear
if AI models will still be within that realm when that comes out, right? Uh does oh now people use
like engrams and other sparse attention techniques. Is that like is does that change like some of
the specializations people are doing or hey people are now doing like you know models are now sparse
instead of being dense models does that change things there's so many optimizations and changes on
the model side and you can't predict what's going to happen with the ML research easily at least you
can't the thing you're optimizing for today has to be a vision of where AI will be in 2 years and
Nvidia's fully accepted they don't know where that's going to be that's why they have a portfolio of
chips now not just one GPU line, right?

It's not just Hopper, Blackwell, Reuben. Now, it's going to be, you know, it's not Ampure, Hopper,
you know, you know, it's not that line. It's like there's a variety of chips to serve the different
markets um and different possible scenarios. They think each of them has this vision today, but oh,
it might turn out the general purpose one sucks and and actually AI models have developed in a way
where CPX or Grock style chips are the best, right? Well, okay, now we have a solution for that
market. And so, I think that's the challenge with the startups. With that said, I think they're all
taking very interesting bets. I think it's I think it's much more exciting than the first wave of AI
hardware uh bets graph course rebringing the memory on the chip they sort of just made a bet and
they optimized for a certain kind of model all similar kinds of model and it didn't end up working
out for a long time right they had to pivot and they had to work on a lot of things and it took a
long time I think these companies have like a really clear vision of what they think models will
look like right like Etch does Maddx does, Posatron does, and that's what's really cool about it
between the three of them, uh, these new age. So, I mean, I'm I'm excited for them. I'm very very
skeptical. I don't know what uh what a venture capitalist views as likely chances of succeeding, but
I think all of them are less than 1%. Right?

>> But, you know, that's that's that's a

>> but the world where they win is a multi-silicon kind of world where any given customer uses a
range of different GPUs. It could it could or it could be any given customer has like one workload
they care a lot about. Anthropic clearly does not give a crap about videogen image gen right they
just don't care. Um on the flip side, company like midjourney cares a lot about image and videogen,
right? Image and videogen is very very like like I mentioned like it's a very like it's not very
memory bandwidth heavy. It loves loves loves compute, right? Whereas inference of large language
models in the style of like you know this these you know say for example coding agents cares a lot
about decoding for long streams of time.

Um and that's very memory bandwidth heavy right? And so there's like that's like a simple example,
but there's a lot more nuance there in terms of like even like the size of like the matrix multiply,
you know, the tensor cores that you you know the systolic arrays that you use or the ratios of
networking and memory memory and like what's that memory hierarchy look like and you know what are
you doing for different kinds of attention and like oh like all these sorts of things like there's a
lot of specialization here and so some people are betting big on on different types of
specialization and I I think like you could clearly see a world where companies do care about
different stuff right like like if for example a chip optimized for video and image generation
existed today and it was better than Nvidia or Nvidia made it. I think Midjourney would absolutely
only use that for inference. I think for training they'd still use the general purpose thing and as
would like Meta and Google would like they should do that, right?

And hey, Meta actually has two lines of AI chips there. MTIA there's a line that's focused on
recommendation systems and then there's a line that's focused on Gen AI. The GI one is a new line,
but that recommendation systems ch line is still continuing, right? It's not sexy. No one cares
because there's no and bite dance also has a recommendation system line of chips and it's not really
focused on Jedi which is fine because you know this is a $200 billion business or something which is
just deciding what ad to serve me right and what order to put my friends stories and you know things
like this so so I think like it's perfectly fine for there to be specialized AI chips given the
target market is big enough and you have to have vision to know what that target market is unless
you're hyperscaler then you can like just like you can just use general purpose until you've like
it's clearly there and then you can make your asich right

>> fascinating turning to the geopolitical aspect of of uh all of this which is always fun. Huawei
and Nvidia in China last year that was like 10 or 12% of their overall revenue and this year they
they were saying that their market share but has basically dropped to not very much. Is that Huawei
chips? Is that restrictions? Is that tariffs? Uh what's happening?

>> It's a variety of things actually in in some in some quarters last year. uh it was even north of
20 I think but I don't remember exactly but anyways you know if you look at 2022 China was almost
the size of the US in terms of buying server hardware right almost not quite but getting there um
and it looked like they were going to be the same size as America in like a year or two after that
right and if you look at like global data center capacity global cloud capacity etc etc etc it's
American companies and Chinese companies right that dominate the world American companies obviously
doing a lot better here but both of those dominate the world and if you look at like every industry
right you know it's It's it's very clear that like China wants to insource stuff, right? So in 2015,
they made these 5-year plans for two 2020 and 2020 uh five where they set the percentage of
semiconductors they wanted uh domestically produced and they've missed the goal both times which is
fine, right? They set really aggressive goals and even you know shoot for the uh moon even if you
miss you hit the stars, right? And that's sort of what's happened, right? Like look, China is not
caught up on, you know, leading edge semiconductors, but microcontrollers from China are almost as
good as the microcontrollers are as good and cheaper than the ones from Texas Instruments or ST
Micro or, you know, etc., right? Or like this power random power chip is better than or the same as
the one from like another company, right? And so they've really built up a semiconductor industry
and started insourcing a lot more. I don't see why China wouldn't be buying you know 30 40% of the
world's AI chips and the US like 50 60% and then the rest of the world like you know and when I say
US I mean US origin companies that seems like a more natural state for the world but there are
restrictions and and hey this is the biggest change in human history maybe ever knowledge work and
you know everything that's going to happen there and and then eventually like robotics and all these
things like you know obviously there's there's a lot of geopolitical stuff and so there are
restrictions Nvidia's been handcapped hand handicapped from selling their best chips to China. And
so that's obviously impacted the sales a lot because like why would you do that? And so when you
look at who rents the most GPUs in the world, it's three companies, right? So one of them is
obviously OpenAI. Second one, actually they were bigger than OpenAI. They are bigger than OpenAI
today or no, they were bigger than OpenAI than OpenI. Eclipsed them recently is Bite Dance. Bite
Dance runs rents tons of chips from Oracle and Google and and you know many other cloud companies
because they couldn't get the chips they need in in China. They're mostly just serving Tik Tok,
right?

Okay. Well, they they're not allowed to buy them and that sucks, but you know, they're they're
allowed to rent them. And so, okay, if I'm not allowed to get the best ones, I'm going to rent
externally. And if Bite Dance is the second biggest renter of GPUs in the world, that's substituting
demand that would have been built in China in many cases. It's instead being built in Malaysia. And
Oracle has over a gigawatt of capacity in Malaysia that Bite Dance is going to take, right? So,
things like this are, you know, you know, hundreds of thousands, if not millions of chips, tens of
billions of dollars of cap capacity that would go to China, but it's not. that it's going to
Malaysia instead as an example. Another sort of point around this is China's like you know they've
had these 5-year plans. So and and you know the way these initiatives work from China is there is
like some top down ordering but then they just kind of whip the whole like everyone just kind of
gets into it and it's really cool like I don't think it's as top down as many people think. Like I
think the entire country is like semiconductor pill right there are dramas where people fall in love
in the fab or dramas where people fall in love and they're photovoltaic like solar cell researchers
and engineers and it's like it's like this is just the backdrop and it's like actually this is it's
like super cool for your like significant other to be that semiconductor engineer or to be that
photovoltaic you know uh solar panel researcher

>> as opposed to an influencer

>> as opposed to an influencer. Right. Like I'm sorry. Love Island is I I I watched like for 10
minutes cuz I was forced to. I was like this is freaking terrible. [laughter] Um but you know like
um

>> we are so cooked.

>> No, you know [laughter] seriously we're cooked. We're cooked. And I think I think like when you
think about like this happens it's like it's diffused into drama even people like like there's
multiple dramas like taking place about semiconductor industry and and they're like romance comedy
like the entire spectrum, right? Drama like it's like it's like what the heck is going on? Anyways,
you have all these provinces, you have all these local cities studying out ordinances and giving out
subsidies and all sorts of stuff, right? It's truly like crazy. Like there's some national level
stuff like, "Oh, no taxes on uh this. Oh, we're going to ban a few things." But as far as I
understand, the national government has not banned Nvidia's H20 or H200. But the local ones have,
right? A lot of local ones have said, "No, you know, you must use China manufactured chips." And
it's like, who told you that, you know, you're here to uphold this? It's like, does it matter,
right? I mean, like, it's it's it's cool because then you have this like survival of the fittest,
all these all these provinces and cities are trying to attract different companies with different
types of subsidies and grants and industrial parks and like all these different things

>> and then like the ones who succeed actually develop an industry and they take over.

>> This how one thinks of of China, right? It almost sounds like more like the US or like with the
federal government and states where the provinces have authority over their purchasing. It's It's
actually like uh great. There's this one um Tik Tok or not Tik Tok, Tik Tok and Instagram like uh
person and they're like they they like sing it. They're like if you want to if you want to buy
things in China, make sure you go to the right place. And then they just say the most random [ __ ]
and name the city. And then you look into it and you're like wow this city has the entire supply
chain for this. Um and it's like lampshades and then it names the city.

It's like what the [ __ ] There's a city that specializes in lampshades. Like it's like and it's
like microphone arms like microphones. It's like it's like literally there's a city in China that
specializes in

>> guitars as well, right? This one one city that became the guitar capital of the world.

>> It's literally everything.

>> Literally everything. There's a city and it's not like hey specifically for uh camera arms for
example, there's ball bearings in this and the ball bearings are like there's ball bearings. There's
multiple manufacturers of ball bearings for camera arms

>> and then like most of the camera arms in the world come from that one city. It's like what the
hell is going on? Um and and so like the semiconductor industry I think people don't realize is
absurdly specialized. I'm not answering your question. I'm just going a little bit of a rant because
I think people don't understand China semiconductors. It's really sick or semiconductors in general.
But like you know like in Japan they like focus on a few different types of chemicals and they're
the best at it and it's like almost a cultural thing, right? Japanese people were so precise like
with sushi and like it's all about the trade and the craft and like you know the French food in
Japan is better than the French food in France because the f the Japanese chefs went there and then
come back and they perfected it in Japan and like cuz they're so precise and and there's so many
different like things that like Japan is so good at because they're so precise and like dedicated to
the craft and it comes out of like I don't know like samurai culture or something I don't know right
like I don't exactly know how that culture came up and so when you look at like and it's like across
the world there's different places where things like this happen right like Oh, like the Netherlands
makes EUV tools. Cool. I guess so. And you look across the semiconductor industry. There's a famous
economic essay called I pencil or something like that. Or talking about how the pencil like a simple
pencil comes from like oh the rubber comes from like Indonesia for the eraser and the graphite comes
from this mine here and and the wood comes from these aspen trees in Canada and like you actually
can't make a pencil without aggregating this entire supply chain. semiconductor industry is like way
crazier because like I would say there's like 15 or 20 countries that could shut down the entire
semiconductor industry, right?

Even like Austria could, right? And and it's like what? And it's like well yeah, there's two
different companies there who have like 90% share in like some random niche stuff.

>> And it's like okay, cool. I guess Austria can and oh yeah, those two companies only like have
less than a billion of revenue, but they just happen to have lynchpin critical things. And there's
lynch pin critical things everywhere because the process is so complicated. And so China's been
trying to replicate this. Um,

>> is there one thing they're missing that they don't have yet?

>> I think there's a lot of things. I think if you were to close your eyes and say or if you were to
cut off every country and say there's no more globalism, China has the most vertical stack in
semiconductors today and they're the best at semiconductors in the world because their fabs could
still run somewhat on a lot of things because they have built some of these chemical supply chains,
right? Like TSMC for certain kinds of chemicals 100% share from Japan, right? Or Intel same thing,
right? or you know for certain kinds of tools 100% share from Netherlands or 100% share from you
know this American company or that you know Austrian company or this or that right like there's just
all these like you know this Swiss company like there's just all these different places have 100%
share it might be one company might be three companies but geographically or in the same area and
China's built that up right because they've created this made in China initiatives which just plowed
money into it and they've got this culture of like the diffused like you know these provinces like
yeah I just decided I'm going to [ __ ] focus on or might not even be might not even be the Right.
It may be the like, you know, someone brought it there and decided and then people were like, "Oh,
wow. You're doing that?" Me, too. Like, I'm a Patel and I grew up in a motel and guess what?

We like almost all the Patels I know grew up in a motel and it's because some random Patel
immigrated to America and like worked at a hotel motel and then bought a motel and then like it just
started happening, right? Like you sort of like these things are serendipitous of sorts and like I
don't know like and it's like I I view it as the same kind of specialization, right? Chinese cities
are like starting to do the these things. China's missing a lot of things, right? I would say like
if you say minus 10 years tech, China's complete and no one else is complete, right? Taiwan is not
complete. Their the fabs would shut down without foreign supply, you know, and you go down or you go
across the stack. Uh but if you go to 10ear tech, maybe maybe more like 20-year tech, you could get
a fully vertical supply chain in China, which I do not think any country could do. Like America
could not build a fully vertical fab without stuff from elsewhere, even if it's 20-y old tech.

>> Um probably not even 40-y old tech. And so, so that's interesting. But then when the flip side is
like well like you kind of do need specialization. That's how that chemical gets the purest best,
you know, most engineered, you know, or that that slurry of chemicals or that, you know, that gas or
like that tool because every smart person or a lot of them in that country grew up around that
culture and like every the supply chain is there and like everyone kind of knows and like it's like
a a driveaway and like sort of like this is what makes supply chains work is that there is this
specialization and the best of the best only comes when you have that hyper specialization. So,
China doesn't have lithography. their lithography is like 10 years behind and I think it'll be 5
years behind in a couple years, right?

They're catching up fast. I don't think they'll be as good as ASML for a long time. You know, maybe
I don't know, maybe they will be, you know, China. You shouldn't ever underestimate China, but like
and Chinese engineers or, you know, but like for a while, right? Or like, you know, I don't think
they'll be able to make leading edge chemicals like many chi uh Japanese companies or many American
companies and their tools and like you just go across the supply chain. They're not hey forefront on
really anything in the manufacturing supply chain on the design supply chain.

There's some things that they're starting to be similar par but like cheaper or like a year or two
behind but cheaper and that's like fine for a lot of stuff. An example of that is Huawei, right?
Huawei in mobile phones was on par with Apple like entirely. Yeah. And they had become Apple TSMC's
biggest customer and they were designing the best thing and they are number one in telecom and their
tech is just literally better. And so when you think what happens, you know, is is is China missing
anything? It's like they're they don't they don't they don't have the best of much, you know, today
in the AI supply chain. they have a complete package and a couple years behind and they'll figure
out how to make it cheaper slash do more slashcatch up and and create a robust industry. But there's
a reason like I don't think that like Jensen is scared of AMD really.

He's paranoid. I mentioned he's paranoid. I'm sure he's a little bit scared of them, right? Like I
think some of the things that they've done are reactions and competitive dynamics with AMD or
Google's TPUs or whatever. Right. There was a Core Weave deal today and I think that's directly the
result of what Google's been doing.

>> Yeah. the two billion pipe that Nvidia announced into

>> Nvidia invested two billion in core but what's more important is that that's like sort of just
like the sticker what's really relevant is Nvidia is going to work with core reef to uh acquire um
and and back stop and all these things the the land the power the energy the transmission that help
build the data center all this capital side stuff that because Nvidia has so much money they can
backs stop corore weave doing it because corore reweave then can be the one who generates demand
anyways there's like because Google was doing And they did that with like a couple companies such as
Fluid Stack and Terowolf and Cipher. These are some public deals that have been announced.

And so Google is doing that with TPUs and Nvidia reacted, right? Um, and so in the same way, I think
Nvidia's reacted to AMD. And in the same way, I think the thing is Nvidia is like deathly terrified
of Huawei

>> because Huawei has caught up to Apple and actually surpassed them as TSMC's biggest customer
before they got banned, right? They did just crush Nokia, Sony, Sony, Ericson, etc., right? Like the
entire telecom supply chain. they just like completely destroyed them. And there's so many other
areas like they straight up made a folding phone, right? You know, I have a Samsung folding phone.
They have a folding phone that's better than Samsung's folding phone.

>> And it's like, bro, what? Like, you know, you know, Huawei's really really cracked. And so, of
course, they're terrified of uh and and Huawei is the most vertical company in the world. No company
is more verticalized than Huawei, which then leads to huge innovations. It's something that we don't
fully appreciate in the US, but like when you travel in Europe, you see everybody who's like honors
honor phones and it's like the the footprint of Huawei is huge in in phones in a way that people

>> not just phones um you know security cameras actually they think they have like you know

>> a lot of training on the [laughter] that a captive group of testers.

>> Exactly. Exactly. Um I think I think Huawei is terrifying right and and so like yes their chips
are not as good today

>> and is that is is that already happening? I mean obviously the US and China are the two biggest
markets but like for other markets I don't know UAE, Middle East, Europe are Nvidia and Huawei
already uh headto-head in

>> well they shipped a little bit but like mostly just like sticker capacity like there's nothing
like no no like I would say like a little bit as in like a few servers not like a billion dollars
worth of stuff right the thing is China's supply chain has to ramp up right um China China's express
goal is to have all inter internalized but then like a company like Alibaba's like I I don't want to
use Huawei, right? Like I want to make I want to use Nvidia and just make the best freaking models,
right?

Because that's my business. My business is not, you know, using a Huawei thing, but it's like, okay,
it's being pushed upon me. There's other companies too, like Cameron Con and so on and so forth. And
so the sort of like supply chain, you know, companies in China don't want to use they're kind of
encouraged obviously and pushed, you know, you must some local provincial government be like, well,
you're doing this much business here. You got to do this, right? Like there's all sorts of like
crazy stuff that, you know, pushing of of companies to use Huawei. Um the challenge is probably
can't manufacture enough, right? We've like done a lot of work on this. Um and we've just put it for
free, you know, instead of like to our customers because it's like something that's like national
security, which is how was Huawei actually building chips? Well, actually they were uh using shell
companies to get chips from TSMC and using different methods of like sneaking HBM, which is memory,
from you know, Korea through Taiwan to China, right? Like all sorts of crazy stuff we've reported on
and and people it's like a whack-a-ole, right? they shut it down or like tools that get shipped to
China and they shouldn't be for you know making leading edge chips but they actually are um and all
these sorts of things are happening because they can't make everything and if they want to make the
leading edge stuff they do need to rely on the foreign supply chain quite a bit in terms of the
upstream supply chain right uh memory logic chips uh tools for fabs chemicals for fabs etc Huawei
cannot satisfy the market um because there's not enough advanced leading edge capacity in memory
logic you know and all all these other things uh domestically in and they're trying to build it as
fast as they can, but that means there's just not enough to satisfy the market. So, Nvidia has a
market. I think they'll figure out how to sell chips to China. And Jensen's in China, I think, like
right now or was yesterday.

And so, like he's clearly like wheeling and dealing to try and get his chips into China because, you
know, I think Nvidia's argument is if we sell them chips, then they won't, you know, there won't be
enough of as much of a domestic market. The feedback loop for software and everything else won't be
there. That will sort of like really challenge it, right? Like most of the open source software for
AI has a lot of Chinese contributors, right? VLM and PyTorch, SG Lang and like all of these other
like libraries and things that are just like you know and and and it goes to low-level software
especially right like a lot of the best open source stuff is actually just from like a Chinese
company who decided to open source it and same with models right and so like it's like okay well if
they can't use Nvidia chips anymore then this open source stuff won't be designed for Nvidia chips
it'll be designed for Huawei chips and now does that like weaken the CUDA mode and now like not only
is China domestic now they have like a feedback loop internally and then they can externalize across
the rest of the world right so This is the like argument Nvidia makes. I'm not sure if I am like I'm
like you know I think I think my AI timelines are so fast. I'm not that fast like not in terms of
like AGI but like hey AI is hundred billion dollars of revenue uh across the industry. I think the
industry could hit 100 billion ARR by the end of this year like 4550 for open AI like 3540 for
anthropic and then you know vertex deep minds uh models at Google Gemini right um and then vertex
API for anthropic models and uh bedrock APIs and Azure foundry APIs like I think hundred billion
dollars like end of this year

>> that's a lot and then what's the economic value of that hundred billion dollars now how much of
that is in China right like China's number is probably 10x lower right? Because they just haven't
been able to pervasively push AI, right? Chat GPT has a billion users roughly and you know, then you
add on Gemini and Meta claims they have 500 million users. I don't know. I think people just
accidentally click like generative sticker or something. Um, [laughter] but like anyways, like
there's like there's like a lot of usage of AI in the west already and it's going to climb. It's
going to keep climbing and like you kind of have to get used to it and so like the question is like
do you you know what's what's the economic benefit to the world, right? And at the end of the day,
this is an economic war, right? If the US and the West win in AI and control, you know, more
powerful AI systems that have this feedback loop that improved economic growth and weapons systems
and whatever else, right? Engineering of grids and cyber attacks and all these sorts of things.

They have this like advantage over China, then China will not rise to be the global hedgeimony. But
without AI, China definitely will rise to be the global hedgeimony. They're just going to outrun
America. And so the question is like you know that's I think like the other view right and how fast
are super powerful AI systems versus you know China building a domestic ecosystem for chips and
models and everything that is a few years behind like what's what's actually the value right like
that's sort of like

>> around restrictions and regulations

>> where where do the uh US onshoring efforts fall in that category what do you make of them from
the chipsack to like all the thing that is being built everything looks like it's massively delayed
by the way which perhaps is not surprising

>> I think TSM MC's manufacturing wafers and they're like building real wafers and there's real fabs
and like you know there's some other fabs that have been announced and like they're doing well and
there's like a bunch of like different kinds of plants like a Korean company making a random gas
plant in Texas for you know their chips right like uh for chips and all these like sort of things
are happening. Um I think the chips act did really well with its $50 billion. It's just I don't
think people understand the scale of the semiconductor industry. is the most complicated supply
chain in the world, right? It's much bigger than, you know, say manufacturing airplanes. It's much
bigger than like, you know, really anything else, right? If you look at the top 10 companies like of
the world, I think eight of them designed semiconductors, right? Now, obviously like Google designed
semiconductors, but it's like, oh wait, no, but their cost of search would be like 10x higher if
they didn't have TPUs and TPUs were super optimized for search, right? Or like, you know, you you
you go down the list, right? Like Meta serves recommendation systems with their chips, right? Like
you go down the list, it's everyone is making their own chips.

Apple devices would be materially worse if they didn't have their own chips, right? Um and you just
go down the list, it's like it's the most complicated supply chain and they they're spending
something on the order of like $150 billion roughly in subsidies a year to the chip industry.

>> We are doing 50 over like a decade.

>> Yeah,

>> there's a difference in scale here, right? The collective total amount of like capex that has
been spent in Taiwan is like 500 billion plus, right? across the industry, across all the companies
that are making semiconductors in Taiwan and Taiwan doesn't have a domestic industry. How is $50
billion of subsidies going to change America's needle? Right? It does move it a little bit, right? I
I want to be clear like the chips act is awesome. I don't understand why like EVs or like solar was
given this massive massive like trillion dollar package. Semiconductors were only given 50. Like
semiconductors need a lot bigger package to actually incentivize onoring. I think what's happened so
far has proven that it's working well. TSMC is literally making chips for Nvidia and Apple and AMD
and others in Arizona today, right? And I think that's really great.

>> Is is your sense that the broad American government is just uh aware of of all of this that it's
uh I wouldn't say only passed because the automotive like prices went up because car manufacturers
are like the worst because they do just in time inventory, right? Or not worse, but like this is
just like a thing, right? Just in time inventory systems. COVID happens, sales plummet fabs that
were making, you know, random power IC's or random microcontrollers for engines got repurposed to
the boom from COVID, which is which was data centers and PCs and smartphones. So, that stuff was
booming. And then when people were like, "Oh, wait. Actually, like, you know, I have some money. I
stayed at home. I didn't go out. I didn't drink. I have a lot of I have some cash, right? Let me buy
a car." They went out and bought cars and cars started skyrocketing in prices. Oh, let's restart and
let's let's Oh, yeah. Can I can you sell me that microcontroller for the engine again? It's like,
"No, I I'm making a slightly different microcontroller that works for, you know, uh, let's say a
keyboard or a mouse, right, or whatever." And it's like, and and and they actually didn't just leave
me flatfooted and they were like a partner through co, right? You know, versus you just left me.
Screw you Ford or whoever, Toyota, um, or automotive OEM, you know, you up that supply chain. And
so, Chips Act did not get passed, only got passed because that happened. And people are like, "Oh my
god, the semiconductors are why cars can't be made." If that didn't happen, we wouldn't even have
the chips act. It's like it's like silly. So like I don't know like I think you know whereas like
and and even though that's what was pitched to all the senators like I know people who were running
around Capitol Hill just pushing that narrative and story and that's why it finally got passed in
reality it was all for advanced leading edge chips, right?

Nothing that goes in a car, right? And so it's like this like funny thing. So, in other words, do
you think my words my words not yours, but is it is it hopeless that the US is going to I'm very
optimistic. Okay. I mean, do you think there's a world where the US just decides to invest in
semiconductor at the scale that

>> you know, I thought we just needed a bigger chips act, but

>> look, Trump's kind of gotten TSMC to promise to invest a fuckload more [laughter] and they're
moving on it, right? They're like actually like just building it. It's like, I'm going to tariff the
[ __ ] out of you unless you build a fab. But it's like we'll build a fab [laughter] and they're
building it right now. The timelines for fabs just takes forever cuz again it's the most complicated
thing in the world. The cleanest space in the place in the world is not like a hospital or a biotech
lab or whatever. It's a semiconductor fab.

And the most expensive tools in the world are not you know any of these medical tools or whatever.
It's it's semiconductor tools or it's not a rocket. It's a semiconductor tool, right? Like
everything you know I describe it as um I remember when I was a kid I was like I want to be a rocket
scientist and then I was like oh I want to be a surgeon. And I'm like wait chips are like rocket
surgery but even cooler right? Like I think anyways like sort of like there there are fabs being
built in America.

>> They won't take America to self-sufficiency. I don't think that's a relevant. I don't think
that's a goal relevant like that's relevant, right? Like globalism is generally just good. Hot take
[laughter] like in terms of economics.

>> We'll turn this into a short a YouTube short.

>> Globalism.

>> Globalism is good. [laughter]

>> Dude, you're gonna get me like cancelled.

>> [gasps]

>> I tweeted about ice and it was a complete joke, but so many people got mad at me because I can't
be, you know, I'm too I'm too much of a joker. You know, these are serious things.

>> Yeah. Yeah. No, I know the I know the feeling. Yes. [laughter]

>> Anyways, um I think I think you know I think we are building fabs and I think it's like going to
move and now even Elon's talking about building fabs now because he sees the shortages in the world,
right? Uh there's a lot of semiconductor related shortages for building out AI and and so I don't
think it's hopeless. I think I'm like very optimistic that we're going to do more and more and more.
And maybe this administration threatens tariffs and they get the deals and the next administration
comes back with the carrot. If it is the Democrats, whatever happens, I don't know. Like I was at a
comedy club on Sunday night and like he's like, "Oh, I'm I use Chad GPT." And then like there were a
couple people who booed and he's like, "Yeah, I'm one of those guys. I know." And like it's like,
"Wow, people hate AI."

>> And that has has not even started, right? Like the actual impact of AI

>> or like New Jersey power prices are up, right? Uh is it because of a data center? New Jersey, the
governor's election like I think literally fl like there's like an election that changed recently in
New Jersey because power prices were up and people blamed a Microsoft Nebius data center in New
Jersey for that reason. But in reality that data center has nothing to do with power prices going
up. It's super storm standy like five years ago knocking or whatever how many years ago knocking
down the state's electrical infrastructure and then the then improving all these improvements and
then those improvements have to be paid by someone and it turns out the consumer has to pay for them
with higher power prices, right? And so like you know like there's like there's a lot like going on
in that regard, right? Um that kind of is uh

>> sad. Um, and and people hate AI and they're blaming AI on it and artists hate AI and like you
know you see all this deep fake stuff and like I think I think it'll be the hottest button issue
especially as like we're really getting into like I think last year Google spent $3 billion on Whimo
and we're waiting for their guide for this year $3 billion on Whimo taxis but their t their Whimos
went from like 300k to like 100k or 90k the new Whimo car and they're going to spend more than three
because they've just launched in like four cities now right or five cities and and they're testing
it a lot and the same a robo taxi like people are going to hate AI for that reason people are going
to hate AI because the slop on the internet people are going to hate AI because you know the
perceived job replacement people are going to hate AI for all these reasons and so yeah it's going
to be a hot button political issue don't you think

>> yeah talking about that so um capex is there a capex bubble are we u investing too much or
actually are we investing not enough given what you were saying earlier about uh the the the rate of
revenue increase and and therefore implied demand that you expect for this year.

>> I'm obviously a maxi. I think we're going to need a lot of infra and I think I'm literally paid
to like analyze the supply chain and do consulting. Like that's what my company does. So like
obviously I'm very [laughter] biased. I think I think we're pretty good at calling when when things
go down though, right? Before like a part of the supply chain reb. Anyways, you know, again, going
back to the economics of it, it's north of hundred billion dollars of revenue exiting this year for
AI from a base of, you know, sub1 billion gen AI from a base because ads and stuff is like already a
multiundred billion dollar AI industry, right? You know, go back to 2023 it was like less than a
billion, right? And 2024, I don't know exactly what number, maybe let's call it 10 and 25 was maybe
like 30 40. It'll be north of 100 easily. If you're talking about hundred billion of revenue, let's
say at a 50% gross margin. So that's $50 billion of gross profit um and $50 billion of COGS. That
$50 billion of COGS needs to run on infra, which cost roughly if a five, if you're talking about
fiveyear depreciation, call it $250 billion, right, of infra

>> for hundred billion of revenue.

>> Mhm.

>> Okay. What is what is the actual spend on AI infra this year? It's going to be like it's I mean
it depends on what layer. If you're talking about energy, those are longer lived assets and all
these other things, right? Um data centers are longer lived assets. The chips are not as much.
People are putting capex down. Um and the hyperscalers capex is going to be like $500 billion this
year or something like this. And then besides them, there's also a lot more hyp uh capex elsewhere.

Um and so, you know, is it a bubble? I mean theoretically like you know it's twice as much as it
should be but it's also like well no there's an R&D component to this and the excess spent that
wasn't revenue generating last year is what led to models being so good this year um and led to like
everyone who can using cloud code and like that changing their life. This is like it's not a bubble,
right? I don't think it's a bubble yet. Um I think if AI model progress stops and that's the main
thing, right? The moment model progress stops all the spending is for not. But so far we've had
consistent improvement.

As you put in more compute, you get more performance and better models.

>> Yeah. Model performance being the lagging indicator of hardware progress or data center.

>> Yeah. of of capex, right? Yeah.

>> Ultimately, the capex that Microsoft spent in 2024 for OpenAI is what results in in 2025 for
OpenAI Cory or whoever is what results in their models being so good this year. Same with Enthropic
and Amazon Google and their models now being so good now is is that capex and actually they still
haven't paid for those chips yet because those chips are still have a useful life for another few
years right I think model progress is very clear um the moment that stops happening right if we hit
a wall there's no new research directions um then then it's cooked yeah right

>> and that assumes that better model leads to more demand which is a reasonable assumption

>> yeah for sure

>> but um yeah I mean there scale the adoption curve regardless of how good the model is uh in the
enterprise

>> like 2% of GitHub commits today are cloud code

>> as in committed by cloud code you can disable that where it's not automatically committed but 2%
of GitHub commits today are cloud code $2 trillion of software wages paid in the world

>> if it was 2% then you like you're like wait a second

>> this is this is an insane amount um AI is under earning the value that it's producing in the
world right by a significant margin already today

>> Bor's journey from Cloud code who had who we had on the pod was saying that what he's written all
of Claude what is it called co-work like the new product entirely with cloud code yet so we're very
much in that world. Yes.

>> Yeah. My uh one of my roommates I was asking him because he's like always been a really low-level
good programmer and he started you know I was like he's like he had this um holiday obsession right
I mean he was using cloud code for work already right like whatever. Um but he had this holiday
obsession. We got into playing Age of Empires 2. Myself, you know, my roommate, a handful of people
from like Open Eye, GDM, Anthropic. We just would do land parties of AoE 2 over the holidays a bit.
Not not like Christmas, but like a little bit before, a little bit after, you know, cuz most of us
went home for Christmas. Um, but like we'd do these lands. My roommate got so obsessed with like the
game that during Christmas week, cuz he didn't go home, he just stayed in San Francisco.

Um, he just worked on an RTS game and he built an entire RTS game. And I think I kid you not, I
think he he used like $10,000 of Claude in one week and built an entire RTS from scratch uh about a
like but instead of like being a standard RTS where it's like oh Age of Empires for advance through
ages or Starcraft, it is it is an RTS where it's China versus the US and you're in the AI race and
you go from the start of the information age all the way through to you know AGI and like robots and
humanoids and and and like all like space fairing civil like it's crazy. He built it in a week

>> and he didn't type a single line of code, right? He can only dictate it to the model. And he told
me, yeah, like we have an indicator internally at Enthropic where you see how many people actually
write code now. There's only a few hold outs left.

>> But I guess the question to the bubble is is really a question of uh timing as well, right? Uh
it's it's whether the build which is supply side and the demand side are going to land sort of at
the same time. Is that is that fair?

>> Yeah. But also the economics of like say you you spend let's say you spend you build a gigawatt
you put down roughly $50 billion across you know the data center the chips the networking blah blah
blah blah blah right let's say it has a 5year useful life so it's $10 billion a year is it a bubble
if the first year you have you didn't make any money it's zero the second year it's zero and then
third fourth fifth year you're at 50% gross margins and so you make 20 2020 now you've made $60
billion off of this $50 billion investment it's not the best return on invested capital, but it did
pay for itself.

>> Yeah.

>> Um, is that is that a bubble? Well, that's what's happening today is that people are spending all
this infra money on infra and there's no return for a lot of it, right? A lot of it is just doing
research and like trying to get adoption and is free users and like what does that mean?

>> Yeah.

>> Um,

>> depends a bit on

>> the timing. That's the timing though. Yeah. But oh, that $50 billion capex was spent in year one.

>> What about energy? In the in the data center world, you had this fun post about the gas
replacement for for energy. So, is uh is AI basically uh uh destroying the grid?

>> It would if the utilities were willing to let it, but I think the utilities are so slow and dumb
that they don't want to. Not destroy, but like expanding the grid. Yeah.

>> Um I think the US could have a way better grid, but we just don't want to. Like, no one's made
the effort or initiative. You know, there's not enough power. America's not built power for 50 years
really, right? It's like converted from coal to gas and like things like this but like really just
have not built wholesale new power on a large scale and there have been a lot of times where the
industry blew up right independent power producers IPs have blown up multiple times in the 2010s
when uh Korean and Japanese investors like flooded the market with because they saw such a good
return there or before in the early 2000s power was growing a little bit for a little bit and so
people overbuilt on power so power industry has been burned a couple times but no one really built
power and then you've got data centers now all of a sudden coming online and going from 2% to 10% of
the US grid in just a handful of years. And so you've got this humongous humongous change in the
industry. We don't have the labor, right? I think ultimately that's the biggest problem is the
equipment and the labor and equipment is basically you know again labor and time takes time to build
a factory so you can build the things. I think the equipment side of things will be solved like more
reasonably. And one one example was like gas, right? People initially thought, oh, you can only use
like the two vendors, right? Uh Seammens or G Vernova for gas turbines, but they have the they have
the best ones, the most efficient ones. It's like, okay, well, like, okay, also Mitsubishi exists
and they're ramping up production fast. Oh, Ducson and Korea exist and they're ramping up production
fast. Oh, actually, I can just take Cumins engines, right? Like, you know, if you've ever like
ridden a pickup truck or like you know, like diesel trucks, like everyone loves Cumins, right? You
know, you see the Ram on the street and has the Cumins like badge. It's like it's like a that's like
an aura symbol for a certain kind of redneck from South Georgia, which I have a little bit of.
Anyways, I I don't have a I don't have a truck. [laughter] I have though. Um but anyways, like the
there's like all these engines like people are figuring out how to make the equipment. You know,
solar sucks. It's too intermittent. Wind sucks. It's too intermittent. Nuclear sucks. It takes
forever to build. Coal sucks. It's way too dirty. How do you make power for data centers besides
gas? And like, okay, the grid's not willing to put the gas on your site, right? That's what Elon
did. Now everyone's doing it, right?

>> This other cool post just uh last week or two weeks ago that was about water consumption. Uh did
you want to talk to that?

>> Yeah. Yeah. So there's this annoying thing where everyone's like, "Oh, AI is using all the water.
Oh wow, AI and data centers are going to like use up all the water and now we don't have any water."
And it's like that's so silly. Uh water is a distribution problem, not a like we don't have enough
problem, right? Like you look at California. So California has shitloads of water. But people decide
to make oat milk which consumes like 1,000x the water of like anything else like regular milk even
and and cows obviously eat a you know consume a lot of water. Um but anyways like you know data
centers consume very little water actually right. So the US grid will get to like 10% of power by
like 28 27 is data centers. For water consumption it's not even going to crack 1%.

>> Yeah.

>> By the end of the decade.

>> And what was the metric? Um and so so the the comparison we made is because like you know it was
a bit of a [ __ ] post but it was like serious research. Yeah. Basically like we were doing serious
research because we keep getting this like question and debunking it and we would do it seriously
but then I was like no no no this is like too like complicated like let's make it very simple. So I
was like, "Guys, why don't we just compare it to like hamburgers, right? Cuz cuz you know, I've
heard that argument from some like vegetarian people before or some Hindus or like I'm Hindu myself,
although you know, and I I I do eat beef sometimes, but you know, like I I'm Hindu, but like you
know, so so we made this comparison to hamburgers, right? Hamburgers require a shitload of water cuz
cows, you know, when to for them they require a ton of water and when a cow's taking a lot of water,
it's not the cow itself, it's all the feed you're feeding them, right?

Because no one grass feeds their cows, you know, and just lets the rain take care of the grass. They
like either rain the the grass or most likely they do mass industrial farming of corn, soybean,
alalfa, etc., which uses shitloads of water, right? Like, you know, or like almond milk like uses
tons and tons of water. Like produce is like the main user of water. I think the uh metric was the
entirety of Elon Musk's Colossus data center, right? Uses as much water as two and a half in-n-outs.

Um because that's, you know, you do the calculation on how many how many b what's the average
revenue per in-n-out and how many hamburgers does that translate to, right? If everyone's ordering
like a combo, right? Okay, let's ignore the drink, let's ignore the fries, let's just talk about the
hamburger, let's ignore the bread, which does use have grain, let's just do the meat

>> and the cheese. And all of a sudden all this water is there's so much water, right? Like a single
query like all of your AI usage from chat GBT of the average user is like a hamburger, right? Like
it's like okay, this is nothing, right? You know, because these things are the data centers actually
are like they're mostly closed loops and like sure they evaporate some water for like cooling
reasons, but like by doing evaporative cooling, they're using less power, right? And that's actually
better for the environment than uh than not using evaporative cool. There's all all these reasons
why this myth or hoax of AI of AI using all the water is just nonsense, right? Like Meta's data
center in Louisiana is getting protested because the water it's it's going to be the largest data
center in the world.

It's going to be like four or five gigawatts at least announced so far. We're tracking some other
ones that are that may be as big or bigger. Uh but Meta is getting protested because the local
population around that area is like, "Oh, the water's dirty. It's because of this meta data center."
And like there's these trucks on these big trucks on these back roads that used to be empty
completely. They're just like mad and annoyed about that, right? But at the end of the day, what
actually made the water dirty is that that's an area where you go fracking. Like

>> fracking is absurdly worse and almost all of that gas is being shipped to an LG terminal and
being shipped to Asia. Like you know, you know, like Japan or Taiwan or China or Korea and some
Europe as well, right? Like like actually all of this water is dirty because of regulation fracking.
Like I support fracking by the way, but you know that's that's an insane take too maybe. Um but like
water usage is is is like not a relevant argument.

>> Are you bullish on the sort of energy uh companies I'm thinking constellation for nuclear or
Vistra I guess is an independent power producer.

>> I think IPS will do well. I think IPS can secure contracts at premiums to what they've previously
been able to for new power plants that are either uh dedicated or grid connected but come with a
pairing of a grid load right for example utilities won't let you just do data centers now but if you
come with a a pair right you're like hey I'm going to build this massive data center but we're also
going to have this massive uh power generating asset right say you know whatever it is right some IP
they're going to partner with and they'll build the load and the uh consumption even if it's
connected through the grid for better stability and more reliability. Um or it's not it's behind the
meter i.e. not connected to the grid at all. Um like some part some data centers like partially like
Colossus from Elon uh the original one or part of Abene's Texas OpenAI right like Cruso there's a
lot of room for power producers to get outsized returns.

I'm not necessarily bullish nuclear. Um existing nuclear fine yeah it'll it'll it can find a higher
buyer higher priced buyer but majority of it will be gas but like you can do like renewables backed
by gas and then just turn off the gas and like it's cost more but whatever right or you can do wind
backed by gas

>> and why not nuclear

>> takes too long

>> takes too long

>> no one can build nuclear fast

>> even China takes like 5 years to build nuclear right like it's it's complicated it's unsafe right
you know I love nuclear I wish it would work it's just not relevant in the time scale that like AI's
power is going crazy. Um, but yeah, there's a lot of interesting stuff like have clients would like
had a client buy a coal plant and we were advising them on the transaction based on they just like
showed up and they're like, "Yeah, we want to buy we want to buy power assets. We believe in this
power story." It's like, "Okay, great." So, yeah. So, here's all of the like power plants that we
know of like you can get some of it from EIA blah blah blah. um which are these like and then we
like worked through the economics and we looked at the new data centers being built in the region
and all this and then they decided to buy a coal plant and they restarted it and they're like making
tons of money now because now someone a certain hyperscaler wants to buy the entire pipeline of
power and put a load load near it right instead of just being a grid connected asset. So it's like a
super awesome investment. So like you know power is power is going to do great.

>> Yeah. I was going to talk about peace dividends of the whole AI boom. Uh generally yes right like
hyperscalers are paying for uh transmission grid upgrades which people will benefit from right or
like you know investors are obviously going to benefit people who work in the industry electricians
wages are skyrocketing you know etc right like plumbers wages are skyrocketing so there's like a lot
of trades that are doing really well too I think that's definitely also um part of it yeah

>> I wanted to come back quickly to uh that um Nvidian core wave deal that you mentioned as we sort
of close the discussion on uh on capex and a and a bubble. It seems like there is circular deals but
also a lot of debt kind of like flushing around. So I don't know the specifics of of that deal but
like I did hear variations of this where effectively you have a large player guaranteeing the debt
being the last recourse uh for a lot of infrastructure build is sort of uh this plus the whole like
oracle commitment.

there there is a fragility into this whole thing that can be a little unnerving. What do you make of
it?

>> I think it's like completely fine and I think like people are like freaking out and making
narratives where there really is shouldn't be one. It's like well okay Google doesn't have enough
data center capacity. They need people to build data centers, but no one can build a data center
because they don't have the capital. Like don't have, you know, many cases capital is not the, you
know, they don't have capital, right? Or like no one will give them a loan because they don't trust
some random [ __ ] company.

And it's like, but then Google's like, well, no, we've due diligence to them. We think they can
build it here. We'll like even guarantee we'll buy the thing or start using it once they build it.
You know, just having a customer alone spoken for it was enough, right? Um, in the case of
Cororewave, they were actually able to no backs stop, right? Right? They were able to just say,
"Hey, hey look, here's our Microsoft contract for this many GPUs. I want to put in that data center,
that data center, that data center. Here's the contract for renting those GPUs. I want to hire these
people. I want to do this." No one will like they don't have any money, but then they were able to
like have it work out because they were able to get people to lend to them. I think like Cororeweave
did that and there was no circular financing. But that was when there was like the scale of
investment was like single digit billions or less than a billion. Right? Now the scale of investment
is hundreds of billions.

>> Yeah.

>> Um and so the question is like, oh well, if I want data center capacity, how do I how do I get
data center capacity? I just go to everyone who's going to build it looks smart is smart enough to
do it but can't afford to do it and tell them I'll I'll take it and in fact I won't just take it.
I'll go to your debtor and be like, I'll guarantee you. Yeah.

>> Because, you know, obviously you're a new company. I've vetted you, but the debtor hasn't. And
so, you know, like, you know, you know, they don't want me to just be able to walk away because like
in the Microsoft Corwave deals, Microsoft could have walked away if Corwe [ __ ] it up,

>> right?

>> Yeah.

>> There's no I mean, yeah, there's there's always like uh sort of like cancellation or whatever
possibilities. And so, this is just a further form of guarantee um as far as on like a lot of these
back stops as far as on like Oracle getting the money and then OpenAI getting money and Nvidia, you
know, paying and it's a whole circular. It's kind of nonsense because it's like Nvidia's getting
equity in OpenAI. They're basically saying, "Hey, every gigawatt you buy, we'll also buy some
equity."

>> Yeah.

>> Right. Okay. Well, cool. Now, Nvidia owns an asset which they think is valuable. OpenAI, right?
Open AAI is turning around and is like trying to rent those uh use the equity they buy. What do they
what was their use of equity? People's cash pay isn't that great, right? It's mostly just 99 plus%
of their spend at the company is probably just compute.

>> Yeah.

>> Uh so so sort of like it's like, okay, well then I I raise this money. I'm going to do the the
whole thing I explained earlier, right? Year one and two I lose money. Year three, four, five, I
hope to make money on it, right? Um, and open has been doing that, right? So, I'm going to Okay, I'm
going to go out there. I've raised $50 billion. I've raised $10 billion. I'm going to raise it. I'm
going to rent a cluster for five years for $65 billion. And I've rented that contract and now I only
have enough to pay for the first year to be clear.

But I think, you know, you trust me, Oracle, you think I'm going to grow and you think I'll be able
to pay for it. Oracle's like, "Yeah, or if you're not, I think I'll be able to sell it to someone
else." So like, okay, cool. I'm going to spend $50 billion this year.

>> Yep.

>> To build that data center. And and and this these this is like for a gigawatt. Um and so is it
like circular that OpenAI is every amount of GPUs they consume and gives an investment that
investment is turned around to pay for the first year of the rent to the cluster. Um or second year
then first two years go, you know, it's sort of like it's fine.

>> Yeah. Yeah.

>> Like it's like it's like it is a little bit funky, but like I don't think it's a big deal.

>> Yeah. Love it. Contrary intake. Maybe let's finish with the models and the software side of
things. We talked extensively about hardware and supply chain and all the things. I get a sense that
you are super super bullish on uh what's happening next in in AI. Your roommate Schulto I assume was
the roommate that you were talking about earlier on this pod effectively making the point that we're
just starting to scratch the surface and there was so much low hanging fruit around you know RL and
all the things you were in Silicon Valley circles. Is that is that your sense as well and what are
you tracking on the model side?

>> One thing is like you know simple stuff like uh GitHub commits other things are like what's the
amount of usage how much are people using like all these sorts of things. I think there's so many
different alternative data sources for tracking AI model progress area tokconomics uh token
economics tokconomics and so that's like an entire practice for us.

>> Are you rebranding the term from crypto?

>> I yeah I don't believe in crypto people like I've always hated them. [laughter] Um,

>> so now you're taking the term.

>> Yeah. Yeah. And Jensen's used it now. So I've like I've convinced him to use the word. He's used
it as sovereigns and so I think I think we've won.

>> That's awesome. Congratulations.

>> I've said it to him. We've written it in articles. It's an entire practice of consulting that I
just I started in like 23 2023 uh was token economics and we've been trying to build out these like
you know but basically I think the main things are like people who don't code can use cloud code now
right? I think people don't understand that like even if you don't code you've never had any
training in software development, you've never take had a job as a software developer you can code.
Let's take an an example of what one of the one of the analysts at my company did right comes from a
engineering background but on like semiconductor systems right uh like worked on mechanical systems
worked on these sorts of things and they coded this thing which was they wanted to do an analysis of
area of clean rooms right clean rooms are the building that you the fab has all the tools in the
most complicated kind of building in the world has every all sorts of chemical systems and all this
area of that a company who builds systems builds these systems and revenue of that company, right?
And so it was like, okay, uh we have this fab data set. Pointed it at it was like, hey, here's this
fab data set. What's the square footage of all of them? And we have this like thing that we built
which uh just pulls with cloud code separately which for data centers and and and fabs and
everything else just calculates the area of something from a from a satellite image, right? Very
simple. So we have the square footage of all these things. Points at that. Here's the company name.
Okay, go find the filings. So it dig dug through all these filings. It it pulled the data, right?

Okay, great. now told it to um compare these two. Make a chart. Great. Oh, wait. There's this like
weird inflection. Oh, that's because they bought a company five years ago. Can you do a proform of
this analysis without those financials of that of that company they acquired? Okay, great. And then
like we were able to like like figure out an investment case for our clients as well as like you
know some other interesting details from someone who's never really coded just using clawed code and
it like doing this all and this is like not even their and it wrote the note and they just like they
didn't even like work on this full-time for like 3 hours right they just told the model and would go
work on other things and told the model and worked on other things they just did this people don't
understand that like the skill sets that like I think like if you go talk to an analyst right a very
junior analyst at any right? Whether it's venture or especially growth venture or public markets or
private equity, their their job is like finding data, cleaning it, making charts. It's like this is
cloud code now. You don't need junior analysts. Just like a lot of companies have stopped hiring L4
engineers because it's useless. Why would I hire an L4 engineer? I just tell Claude to do it.

You you sort of like have this has happened and this is a really big like shift I guess like is that
like low-level knowledge work just doesn't matter, right? Why would I why would I use Excel when I
can just tell Claude to manipulate CSVs? Why would I use Word when Claude will just generate the
markdown and I can copy and paste the markdown directly into our WordPress and then you know and
that WordPress is fully formatted now and it's like oh my god like what's the point of Word, right?
Um and what's the point of doing all sorts of stuff? I think when we look at model progress that's
just for Opus 4.5. Open's new model I think will be better than Opus 4.5 and it's coming like
somewhat soon in Marchish um time frame. I maybe February, Marchish, but yeah. Um because OpenAI has
a better RL stack than Enthropic today. It's just their pre-trained models suck compared to
Enthropic's pre-training, right? And so like if they catch up a lot on pre-training and keep their
better RL stack, they would actually have a model that's much better, right? Flip side, Google has a
better pre-trained model than Anthropic or OpenAI, but their RL stack sucks. So if they catch up on
RL, like these models are going to get ridiculously and then Anthropic is obviously advancing as
well, right? And so and then and then you look across the ecosystem, everyone's advancing really
fast progress. These moments are happening, right? You know, chat GPT was a moment. Gibbly was a
moment. Those were more consumer. Those were less like I mean there chat GBT is everyone using it
for work too. But like I think cloud code is like a new moment right 4.5 on cloud code is a new
moment where the way you work has forever changed. And so now we're trying to force everyone in my
company. There's 54 people here. I think like half of them have coded. The other half we're trying
to force them to use like cloud code. And it could be like oh well actually you come from a consult
a semiconductor consulting background. Oh, you come from like a semiconductor like engineering of
like package. Oh, you worked in a fab, right? Like these kind of people, they're using cloud code
now, right? And and their productivity is being boosted.

>> And it's like,

>> you know, workspace, cloud workspace is new. It sucks compared to cloud code, but it'll get
there, right? He he he said he coded it entirely in cloud code. You know that, right? Or that was on
your pod, right? Yeah. Yeah. So, like um you I've heard that and I think maybe that might have been
from your pod uh original uh disclosure.

>> My pod was before that, but yes. Oh, okay. Okay. It was

>> I had as the guy on my pod subsequently said that.

>> Okay. I think it's like a brand new age and and like there's so much low hanging fruit as Shto
said on the episode when he was here. There's so much low hanging fruit. Yeah. I mean for for the
models progressing and I think model progress will translate to revenue. Adoption is difficult but
like actually the UX of cloud code sucks but like give it 6 months the models will be good enough
that the UX can be like talking to it. Yep.

>> And you don't even have to have like you know CLI integration, right? It's something even easier.
or like cloud for XL was released recently and it's like not bad you know building models and like
all these sorts of things are just going to be like tell someone right like why tell a junior
analyst right when you can just do it yourself I think it's a whole new world and it's a $2 trillion
of software work but also of wages but it's also we have more north of 2% 2% is claw and then you
know there's codeex and cursor and all these other guys so probably like 5% of code committed today
is AI generated if not higher marked as AI generated what's going to happen when normal workers who
do spreadsheets and office processing start automating their workflows. I think it's a whole new
world.

>> And speaking of Schultoe, we both agreed that he was a a perfect specimen.

>> Dude, [laughter] I' I've been I'm straight, but I've been accused of being uh homosexual, which
is perfectly fine for for how much I like praise this man because like, think about it, right? He's
like 6'4. He's like really good-looking. He's like Australian accent. Sounds amazing. Like you've
heard his I I have like a annoying voice probably. His voice sounds amazing. He's absurdly good at
coding. He was an Olympian level fencer. Like like he picks up any sport, he's really good at it,
right? Because he's athletic. It's like, "Holy crap, you're a specimen."

>> Yeah. Yeah.

>> This clip and sent him [laughter] for sure.

>> Yeah. It must be uh you know I guess uh may maybe some people don't follow the playbyplay on on
Twitter and like don't haven't haven't heard of like the fact that all of you guys are roommates or
you roommate with Scholto and then with Dwarish and Darkish is like the podcasters podcaster. So it
must be absolutely

>> What's a podcasters podcaster mean?

>> Uh the podcaster that other podcasters uh aspire to to to become or learn from.

>> Yeah. Yeah. his his when he's preparing, you know, it's like he's he's he's he's so locked in and
he prepares so hard for interviews. It's great.

>> No, he's he's just uh incredible.

>> And then and then he might only say like a hundred words on the episode,

>> but he's prepared so hard and then like I think people just realized, oh wow, he's not just like,
you know, it's like, oh, he just has good guests. No, no, no. Like he's preparing really hard, but
you can't tell if you're not like realizing that. And then once he started writing more and he
started writing more, people like, oh wow, he's actually really really smart. It's like, yeah, cuz
he's studying like crazy. Like it's like, "Oh, I'm interviewing an AI researcher who worked on this.
I'm gonna try and train a freaking model." Yeah.

>> Right. It's like that's the level of like commitment he goes to when he records this stuff.

>> What do you guys talk about when you bump into each other? Is that is that AI non-stop or you
talk about everything but AI

>> with Shoto? It's like the Age of Empires game, you know, because we we got super into it for a
bit. We talked only about that in his RTS that he made. Uh with with with Dwarash, it's I mean, it's
all sorts. It's like normal roommate stuff. It's like, [laughter] "How's your dating life?" "Oh,
okay. You went on a date. It wasn't well. It didn't go well." "Okay, well, okay." Yeah. you know,
like, oh, you know, like that's me. That's me. You know, my days don't go [laughter] well.

No, I'm just kidding. Um, or like it's like, oh, you want to like have dinner? We can invite a few
friends. Like, yeah, great. Or like, you know, it's like all sorts of like normal stuff, too. Um, al
obviously we also do talk about a lot about tech, right? Like we are like this is our lives. Um, and
tech is the most fun thing.

>> Awesome. Well, great. Great San Francisco lore. Uh, Dylan, thank you so much. Uh, that was
absolutely fabulous. Really enjoyed it. Learned a lot. So, really appreciate uh your coming on the
pub.

>> Thank you so much. Hi, it's Matt Turk again. Thanks for listening to this episode of the Mad
Podcast. If you enjoyed it, we'd be very grateful if you would consider subscribing if you haven't
already or leaving a positive review or comment on whichever platform you're watching this or
listening to this episode from. This really helps us build a podcast and get great guests. Thanks,
and see you at the next episode.

