# Dylan Patel: Is the "Low Hanging Fruit" in AI Gone?

- Date: 2026-01-15
- Channel: SAIL Media
- Duration: 14:01
- URL: https://www.youtube.com/watch?v=QHueG_5DvSw
- Source: `uv tool run youtube_transcript_api --languages en --format json QHueG_5DvSw`
- Note: timestamps are preserved in the paired JSON file.

## Transcript

Welcome to our booth. I remembered this morning that I am the name for sale. So I am also on this
and you're representing semi analysis and lambda is our amorphous bank. Bank of lambda. Thank you.
Thank thank you lambda. We appreciate it. Um what are you excited about this year? Try to recount
what you were feeling last year at nerds and how different that is.

>> So nerves comprises of like two things, right? One is like one is like parties which which are
actually more fun than you would expect. I think people are like, "Oh, AI researcher parties. It's
it's much better than San Francisco AI researcher parties." Then the other side of things is just
like walking around poster sessions. And so last year in Vancouver, the main thing I was doing, I
was just walking around looking for people with verifiable RL, anything RL and anything verifiable.
Right? Like I remember the first ner I went to it was like 21 or 22 and I was like I would walk
around I'd stop at only posters that said the word transformer like and anything that didn't say
transformer I just didn't read it. Um and then like you know that's evolved and last year like you
know obviously I stopped at a lot of random posters as I've learned more but last year was the first
time I like stopped at a bunch of like RL stuff and verifiable you know test time you know sort of
scaling stuff that you know verifiable RL stuff all that kind of stuff. This year I have no clue
what to stop at.

>> I know it's like what do we do now? There's gonna be so much RL stuff, it's like a wave. It's
hard to know. And I feel like last year's RL stuff was still like the early things. I would guess
though maybe like Vine PO was at Nerv or something. There was like a couple early things last year
that were relevant and um like the star work from Stanford.

>> Well, the the the whole reason to stop at the posters is not like that's the poster you want to
talk about. It's this is what they worked on six months ago.

>> Yeah. So

>> So what did you work on then and what what are you working on now? is like, you know, that's the
interesting thing to talk to them about because they're obviously on top of their field, whether
it's like, you know, RL or, you know, whatever whatever they're doing, they're on top of it. So,
like, it's it's more about like ga, you know, stopping at a poster with interesting keywords and
then not talking about the poster at all.

>> Yeah. I mean, it's good meta for people to have out there. It's like it's the way that you can

>> Wait, am I giving away too much alpha?

>> No, there's so many posters. It's so overwhelming. It's just like it's the nice way to figure out
how to corner people. It's like it's not too hard to figure out where I am on a few occasions giving
talks or whatever like okay I'm I'm screwed afterwards for 30 minutes. Back to the research thing
where we don't know what to look at is actually somewhat interesting cuz I feel like the path of
progress has been so obvious for a while and like academics could do stuff but it's like we are in
the age of research. I know it's like is this maybe a little bit true? Is that kind of bearish for
AI if it's like or is it good for AI that is just like

>> it's it's interesting

>> everything is like you know like there's no incremental thing that takes up the majority of the
head space anymore I guess is is one way to look at it the other way to look at it is like well
actually just every layer is innovating hugely right like there's tons of gains in pre-training
there's tons of gains in scaling there's tons of gains in quantization and systems but there's also
tons of gains in RL stuff and both the like you know infraight of things and non-infright of things
right so it's We took the low hanging fruit and now the low hanging fruit isn't as

>> No, but like it's, you know, when you talk to someone at a lab, they say there's a ton of low
hanging fruit, right? Like,

>> but it's not as obvious as turning on inference time scaling on top of everything,

>> I guess. But like you guys released a new model recently, and I'm sure there was, you know, if I
go ask you, hey, here's all the low hanging fruit we got. Go ask Dirk, here's all the low hanging
fruit we got. Like well the lore is like I made the SFT data set for reasoning in like a weekend cuz
we had like unlimited Azure credits for a certain period of time and I was just bombarding like
deepse points but I was like we haven't made our thinking SFT set. So I was like let's just get as
many tokens as possible.

>> Is this is this how you is this how you legally distill from open AI is by distilling from DC?

>> I'm trolling. Sorry.

>> We just we just dissolve from open AI directly. We do it for research purpose. Our model AI's
models are intended for research purposes and click to see our responsible use policy, but they're
still Apache 2 with no clickthrough and no terms of service, but there is low hanging fruit and it's
like it would take a meaningful amount of GPU hours on our scale to like do inference on DeepSeek
and a lot of the tooling to do batch inference on a model that needs to be served multi-node is just
not that good. And it's like we also used Frontier a bunch which is like the US AMD supercomputer
and we did a whole bunch of like Quen 32B because it works on a one node 8 by like MIX whatever rack
and we use millions of GPU hours on synthetic data because we have this frontier lying around. It's
like that's very much AIT's data vibe and there's a lot more

>> but at least like from what you've put out from the most recent model um and I talked to Durk a
little bit. You guys both have indicated that there was like low hanging fruit on the most recent
models and I'm sure you feel that way about the next one. There always is. I think there's just like
I think part of AIT's balance especially in ports training is that we like bring in the best
students from Udub who are all like super excited top few PhD students in the world and they have
like their things to that they want to work on a lot of it is just like building a platform where
they can run with it

>> and like there's like one student like like Scott and Victoria are two people that are doing all
the DPO stuff and he had this one DPO paper and it's like we just got massive gains from doing DPO
and this is this guy that's just like I have my chance to prove my paper on the almost scale and
just goes like crazy hours and he does it and I was like like that's not really that like it's not
like I'm giving an engineering plan to some full-time employee. It's just like doing it between the
hours of 10 and 2 a.m. for the week training the 32B model. And I'm like, "Okay, I've got to go to
bed." Like, "Good luck. It's not broken right now." Right.

>> Well, so Elon RZ is paying people to do this, but I think you have another level of RZ that's
above that. You're not even paying the UDub.

>> We pay them a little bit. They're student collaborators.

>> Okay. Let me go Let me go look up what the

>> They need to be paid more. They're underpaid. I I agree. They are underpaid. The students are fun
to work with, but it's a very different dynamic of everybody.

>> Has Has any lab started just like, "Oh, they work at AI2. Maybe I should like interview them."

>> Probably.

>> Is this like a thing?

>> Probably not as much as they should because AI2 is out in this like Seattle bubble and people
kind of ignore it. But I'm always one of the most prominent worriers about poaching with like with a
small team, it's just like you lose three people and you're back a few months realistically and it's
just so hard. There's like a couple labs at Stanford where I know just got pilered by, you know,
even Meta most recently, right? So, it's like, you know, they'll just like, well, we need people.
Where should we go? Okay, here's the like active players, but what if we want to pay people only a
million or two, right?

Instead of paying them 10 million, well, let me go find the PhD students and offer them that, right?

>> I'm surprised it doesn't happen more.

>> Yeah. Yeah. I mean, that's the next level of the talent drain is like

>> maybe semi analysis when we when we when we do maybe we should we should go to we should start
trying to poach from AI too.

>> No comment.

>> I'm just kidding. I'm just kidding.

>> Um person from Momo or one of the two leads. It was like Chris C and then Matt Duchka. He like
had left AI2 for a bit and then there's a New York Times article where he famously like turned down
100 million from Meta and then Zuck offered him 200 million. So it's like people are looking. He
would probably be like up there with the best possible super intell like if I was going to just
throw money at a researcher that hasn't really been brought into the scene yet, he's like up there.
He's so good. So, it's like

>> I don't know. We we screwed by. But also,

>> what's it like here, right? Cuz like a lot of people um you guys have the most open source stack
here, whether it be on your data, on your recipe, all the checkpoints, all your RL stuff. You guys
have so much open source stuff here. is OMO like disproportionately represented by you know building
upon OMO here or I don't want to say disproportionately but like you know it's it's

>> we've we've done analysis for like what do people use OLO for and I think there's a lot of
interpretability research that's done by releasing intermediate checkpoints and then especially post
training data is really heavily used but that post training data is not just academic because it's
like people like thinking machines one of their examples loads one of our data sets but it's also
just like a lot of startups and small companies will pull it in or like when we did reward bench
which like a tiny academic project it's like tons of companies are also just like h yeah we should
have this around and or use this infrastructure as an early thing so I think that definitely gets
adopted and then whatever is the best pre-training data I think gets used a lot at the time and that
kind of oscillates between like like AI2's dolma was it and then like hugging face with fine web has
been it and it kind of goes back and forth and then like um DCLM whatever is clearly the best at the
time gets used a lot in research but I I think that there's Like we would like to see if people can
do continued pre-training on specific domains to see if that could work cuz our intuition is that
you need the pre-training data and the checkpoints because you have to like mix the domain in with
the web otherwise you're going to have instability which is something we would like to see but I
think that it's still hard to get a new pre-training code base set up on a cluster unless you have
really good talent. Like it it seems like you can take Megatron off the shelf and use it and like
Megatron's a bit better but it's still really hard. And the same thing for Mo Core. So we have had a
few collaborations where somebody from like astrophysics is like I want to train this model and use
mo to

>> all this special data and it's like

>> hasn't there hasn't been like really cool examples but there's a lot of inbound on it. So
hopefully it can make it a bit easier to use and do this and like obviously having bigger and better
better models helps to do that.

>> Makes sense. scaling. I think scaling will help the scale that all these Chinese labs are doing
and then like cursor is obviously built on some Chinese large of some sort.

>> I was wondering because like when I look around at the models a lot of it is built on top of the
Chinese models as well, right? A lot of the researches. So I was curious like how much of

>> how much of the industry like cares I guess like about hey here's just the best open weights
model versus like actually I want it to be open source across all these dimensions for my work. Are
there certain areas where it matters more versus not interpretability? You gave that example.

>> I think there's like healthare stuff. So like AI2 has some early collaborations on like cancer
research and other thing that needs patient data and they want to try building on this open
research. I think that's all a lot earlier.

>> Why does why does healthcare care about whether it's I guess just like consciousness of not using
a Chinese?

>> I think you like can't release the data. This is might be more on like the flexible mo side,
which is like being able to train part of a model with like specialized data, but it's just
operationally easier for them to onboard.

>> I guess I guess I more so meant like not collaboration, but like hey, we dropped all this like
they're just taking the code and going or taking the weights and going.

>> Not a ton. I mean like we got inbound from like data bricks are like we're going to try it. So I
think it's like we're constantly in and out of this boundary of performance where it's relevant
which is like the thing that I say internally all the time is like we have to bet more like the you
need to put more of the company on this in order to get to this next scale because then there's just
way more interesting things that you can do like the actual like fully open coding assistant or
whatever.

I think it just becomes far more interesting at that level of performance where the 32B model if
it's solid you can do automation tasks with it and a lot of information processing and they might
like do different retrain different stages of our post training to do that but like it's not the
like sexy stuff

>> Nathan Nathan today new open source model

>> not from an American company not from a Chinese company from mistrol them seems good I'm happy
they released base models I think that that like that's coming back around because everybody like it
seems like there's real demand and for base models and because people want to post train their own
thing. I mean see cursor and composer that very likely is a post train that they did because they
have a ton of data and they can do a lot more

>> didn't yeah one one sort of like I guess like last question I'll answer it too and I have my I've
thought of my answer for like the last like couple minutes

>> and I'm going to jump it on you. We've had these leaps, right? Um, in various domains um and
depending on how much you specialize in the domain, you can, you know, people can point out like if
you're in pre-training, you people can point out like 5 to 10 leaps over the last few years, right?
If you're an RL, there's 5 to 10 leaps. What what do you think the next area of like like leap uh
growth? Like what what is something that you think will come and probably will be heavily discussed
here, right?

>> I don't have a huge leap thing, but I think token efficiency is underrated. So it's like we
didn't release these plots but we did a lot of like Pareto plots which is like a val performance and
number of tokens per val and that's the thing that we want to be like if we're like

>> number of tokens generated for the eval number of tokens used to trade

>> for at inference time because it's like if we're reasonably close to Quen and Nvidia on
performance

>> that's what that's what opus was right 4.5

>> Opus slam down the token

>> it just makes it's cheaper and faster

>> 5.1 as well right GPD 5.1 codecs really slam

>> so I think there'll be a lot of interesting research on my uh my gigab brain thing and I just I
only thought about about it because you got you're uh you're kind of against it was uh you know the
continual learning stuff.

>> I know I know you're like oh shut up.

>> Um it's a long time longterm continual learning is definitely a thing. I just think that when
industry is building we're we're building the mega computer for the first time and they're going to
build it for sure. I'm like focusing on the thing that is for sure and the research it is an it is
good research problem.

>> Yeah. Yeah. Yeah. I guess that's interesting. You guys despite being a research or don't go for
the moonshot silly right? You guys actually just go for like open sourcing like the paro op like
paro frontier of what we have today mostly. Is that is that a fair statement or is that is that
fair?

>> It's cuz it's hard to get all the setups right. I think there's famously these numbers and how
much compute goes to different parts of the org where it's like you'll say like pre-training gets
40%, post training like 20%, long-term research gets 5% and like AI2 we've talked about this and
it's like if you break these down like AI2's long-term research percentage should be much higher.
should be or used to be

>> should be and it like kind of is it's just like the distribution of projects a lot of things you
won't hear about because it's like just hard to have impact in that space as well. So I do think AI
does

>> that's the interesting thing about labs as well right open has over 500,000 GPUs working on uh
R&D right let's call it R&D but then when you look at like frontier scale models their pre-training
is not even 100k GPU scale yet right like GBD5 like not even 100k GPU pre-training scale so it's
like that actually goes huge amount of stuff working on now I don't know if it's RL or long-term
stuff but it's it's interesting the the mix is quite different

>> yeah I would like know more about that but it's like I hard to know what they actually share hair
too.

