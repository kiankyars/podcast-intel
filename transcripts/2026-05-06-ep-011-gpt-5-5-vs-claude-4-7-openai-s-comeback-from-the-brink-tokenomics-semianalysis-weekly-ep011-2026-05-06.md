# Ep. 011 - GPT 5.5 vs Claude 4.7: OpenAI's Comeback From the Brink (Tokenomics)

- Date: 2026-05-06
- Channel: SemiAnalysis Weekly
- Duration: 45:06
- URL: https://podcasters.spotify.com/pod/show/jordan-nanos/episodes/Ep--011---GPT-5-5-vs-Claude-4-7-OpenAIs-Comeback-From-the-Brink-Tokenomics--Jordan-Nanos--Dylan-Patel--Doug-OLaughlin--Max-Kan-e3iuqlr
- Source: `MLX Whisper large-v3-turbo audio transcription from downloaded episode audio`
- Note: timestamps are preserved in the paired JSON file.

## Transcript

Hello, everyone. Welcome back to SemiAnalysis Weekly. We've got a big show this week. We've got some
heavy hitters. Doug, Max, anybody else out there? Oh, yeah, of course, that's Dylan Patel calling in
nicely in a nice setup office with his headphones on and a SemiAnalysis logo water bottle. So, yeah,
we're going to talk about Claude Code, which is one of the only things we talk about on this podcast
now. We're going to talk about GPT 5.5, possibly, DeepSeek, and yeah, just get into it.

It's crazy. Today is May 5th. Yeah. GPT 5.5. It's Max's birthday. Happy birthday, Max. Max debuted
on the SemiAnalysis newsletter last week with his first lead author article, let's say, the coding
assistant breakdown. The funniest thing is he was like, he's like telling, he's asking like Doug and
Michelle, like, hey, like, you know, am I going to be approved on my work trial? It's like, bro,
obviously, like, what are you talking about? Also, also Max is now a full-time employee at
SemiAnalysis, not on a work trial.

Happy to be here. It's really exciting. Welcome to the team. Okay. So, let's run through this
article. Basically, when we pushed it out or when we were prepping to write it, it was effectively
just going to be a review of 5.5 Pro and, or just 5.5, whatever the new, I think we assumed it was
going to be called 5.5 when we were doing some testing of the- Potato patata. It's a spud, right?
Potato patata. Yeah, we're calling it spud. Tomato, tomato. I tried some different checkpoints, but
the, I guess the basis for the article was like, just going to be a review of that model.

And then quickly, Claude released, Anthropic released Claude Opus 4.7, which was a big change of
some, you know, pretty interesting features that we covered in the article. And then we also got
DeepSeq v4, the, whatever, four, five, possibly six months delayed release from DeepSeq. And so it
became this article just about all, all the latest releases. So Max, maybe you could give us like a
quick summary. What was your high level takeaway? And then we can dig into the details of, of the
changes for these models.

Yeah, happy to. I said the TLDR is that things were looking really dire for OpenAI for a while. You
know, start of the year, Anthropic was quickly encroaching in terms of revenue. I think the
information leaked like 19 billion ARR for Anthropic versus just like 24 for OpenAI. Anthropic then
sort of quickly surpassed them. Even with all the sort of accounting discrepancies related to like
derecognized net or gross from the hyperscalers aside, I think it's pretty clear they surpassed them
on a life-to-life basis.

And like early to mid-April. This is primarily because Opus 4.5 was just a real step change in
coding and overall agentic abilities. And so from like late November up until end of March, early
April, everyone was basically just spamming like Opus 4.5, 4.6 for all their workloads. OpenAI tried
to fire back with PPT 5.4, but that thing was honestly just an embarrassment. Like in the modern
release card, they didn't even compare it to the Opus models, just to the past like OpenAI models.

So that kind of tells you all you didn't know. But then finally with 5.5, they're like, they're back
on the frontier. Opus was re-included in the modern release card. I wouldn't say it's like
definitively better than 4.6 or 4.7, despite what the Twitter propaganda machine was trying to push
on release date. But I think it's definitely like in the conversation. I'm happy to use it and sort
of allow Opus 4.5 to come back in the game. You know, things were looking dire, but now I think they
got shot again.

Doug, what are you using daily driver? Are you using both or just one right now? I have tried so
many times to use codex, but the usage limits are, they raw dog me every day. Wait, what do you
mean? You use the API, bro? I use the API. Don't get me started. How do you get usage of it? How do
you get usage of it? I don't know, bro. And then after it takes me longer than 15 minutes. Just go
bitch in the OpenAI Slack. Just go bitch in the OpenAI Slack.

I have. I literally, dude. Okay, so but then after it takes me longer than 15 minutes. For what it's
worth, we're trying to get you started. It takes me longer than 15 minutes. I don't try essentially
to go actually fix it. X-High seems really expensive and blows out the context window. But I mean,
in my impression, it's like, you know, it's very neck and neck. They're pretty replaceable to me.
The thing that I really want is someone to give me fast mode and high uptime.

And that's, you know, no one is high uptime. Wasn't there, isn't OpenAI's fast mode like fake news?
Yeah, it's pretty fake. Well, they like reduce the reasoning depth and it's not that fast. Opus fast
mode is not that fast anymore either. It's not even two times faster. Sounds like we need more
compute. It started out at 2.5 times faster. Now it's less than two times faster. But OpenAI has
like three versions of fast mode. They have priority mode, fast mode, and the 5.3 codex Spark.

5.3 codex Spark is definitely fake. That's just a different model. But then fast mode, I feel like,
is comparable to Opus fast mode. You guys don't think it's actually faster or much faster. I've been
using it in codex and it feels pretty slow. I don't even notice it like really being faster than
with fast mode turned off. That's what you were showing me, Jordan, the other day is like the
distribution of like what's the peak tokens per second? What's the median?

What's the trough? I thought you showed me. Maybe it was someone else. But that like OpenAI's
priority mode doesn't like actually make it's not always faster. It can be faster, though. Yeah, so
priority mode is like guaranteed execution in an SLA, but not faster interactivity for people who
have like, you know, they need stuff done on the API and they'll pay a premium for that. But it's a
small premium. It's like two times. I think what I was showing you was the data that we have on 4.6
fast versus 4.6 base, which is it started out at, let's say, around 90 tokens per second per user on
fast mode and around 35 or 40 for base.

It's still 35 or 40 for base, but it's now at like 70 tokens per second fast mode consistently. So
it's like not even two times faster for six times the price. The guys internally are like, I mean,
Max, you made this point in the article, like, or we made this point in the article, I guess. This
is like the first time where any of the engineers at SemiAnalysis have made the trade of wanting
fast over higher quality tokens. And I'm not sure what drives that.

Definitely people want fast mode, definitely feels faster. But maybe the big thing is that 4.7 is
just not meaningfully better quality than 4.6 for people. Today. Yeah, I was actually thinking about
this earlier today. If you kind of treat in the context of the open eye, Cerebrus Steel Eye, because
if you assume that like Opus 4.5 with just this, like it passed some key threshold and intelligence
slash model capability, such that a lot of your sort of day to day tasks are now just like one shot
up all by the models.

Like you don't really have to supervise them at all. You're not even looking at the outputs. Maybe
it's just the case that like, even if you can never run anything larger than, let's say, like one or
20 billion parameters on Cerebrus. Well, you're going to have GPT 5.5 level intelligence in that
form factor in probably like less than a year. And it might just be that we've actually like passed
the inflection point where the majority of people do not need frontier level intelligence, like for
the day to day workload.

And this is probably like doubly true if the models keep getting more expensive. Like originally, I
thought same analysis, like maybe there's a chance where we'd be able to afford Mythos fast. I think
it's probably just not true anymore. A lot of people have already been priced out of the models. I
think we're on the cost of getting priced out. I don't think we can, right? Because like Mythos is
what? Six or seven. It's 25, 150, I think. 25, 150 or 25, 125.

25, one of the two. Versus 5, 15, right? 5, 25 for Opus. 5, 25. It's 5x. So it's five times more
expensive. And then fast mode 6x on top of that. If we were to take our current token spend, I can
justify that. But if you were to even double it, I'd be like, oh, fuck. Maybe we got to turn off
fast mode, guys. At this point, at this point. Like it is like margins, you know, like matter. Do
you think there's a possibility that we could define something so important in semi-analysis
research in the future that we would want to pay the premium just for one project or one task?

I think the flip side is Mythos is more token efficient. Mythos fast mode is probably cheaper than
like 4.6 fast mode for most tasks. I just imagine. At least that's the case with like Codex versus
5.4 versus 5.5. You know, even if they make the model more expensive, you know, that's like not a
huge jump in price for the model. I don't expect new models to be like more expensive to do the same
task. It's the problem of cost is like you're going to do new tasks.

Yeah. They call that Jevons, dude. Yeah. We're going to be coming up with new stuff to do with these
models based on the work that we do in the next few months with the models. We'll come up with new
things, new tasks that are harder and more complex and need to use the bigger models for them. At
least that's the problem, right? But I feel like right now, at least like I don't even think about
is this task like worthy for me to spend tokens on? I just like spend the tokens.

But if the models get much more expensive, you might have to think carefully like is this task
really worth Mythos fast token pricing, you know? I think that'd be really sad honestly when it
happens. The question, what is the trade-off? Because I have a personal anecdote where it's more
expensive to burn tokens than to do it. What are your examples of the cost is not worth it? Like
there are times where I was just setting up like some benchmark on a digital OS and drop with it.

And I was using Opus 4.6 fast and that was like $400 or something. And I was like, I don't know if
it's worth $400, you know? That wasn't worth 10 minutes of your time. Yeah. Yeah. Jordan, what's
yours? Yeah, I think stuff where you can very clearly do it from a script or writing. Like writing
docs, maybe the first pass with the model is good, but editing stuff is just annoying to use the
model sometimes instead of doing it yourself because it might screw it up or might, you know, edit
the wrong thing.

That's a quality versus cost conversation. What's this like? Wow, this is just a complete waste of
tokens. Like the tokens in were two times more expensive. I don't think I've had that experience
yet, to be honest. I had somebody give mine. Yeah, what's yours? Yeah. Okay, so scraping large data
sets, at some point, there's a diminishing return. You're like, hey, give me 10,000 employees from
this company. And you're like, great, I'm going to have a search API, various whatever, blah, blah,
blah.

Like I'll do a lot of variation to figure out a profile about every person who's worked at this
company. And then you like actually run the cost and there's like a data enhancement API. And like
the data enhancement API is like literally one tenth of the cost. You're like, oh, shit. Like I
think I burnt $800 in tokens to do what would take maybe $55 to $100 token of API calls. And one is
like, okay, it's probably slop. But the other one is, in theory, verified by another slop cannon.

And so like, I just, I think there's some value, like, and that's like probably one of the most
interesting places where the replacement cost of the tokens versus the actual information. You know,
it's still a lot cheaper to just like essentially serve data via an API. But like that cost, like
the pressure on the top will move that down, if that makes sense. Like just scraping the entire
internet is just not token efficient at all. So, yeah, that's a good example where I just tried to
boil the ocean using AI.

And I've been really curious about like, there's going to be a trade-off where the, like, you know,
it's just not worth this much intelligence. You know, like making me coffee. It's like the Rick and
Morty game. It's like, what's your purpose? Like pass me the butter. Like, this is, this is a waste,
man. Like, we've got to find a better, a better token efficiency. Yeah. You can actually hire some
people for cheaper to do some menial tasks than you can with tokens.

But some of the analysis that we've done recently is like, it kind of goes the opposite way so often
that you just get used to tokens being the cheaper approach or the faster approach in so many cases
that you don't even consider the alternative. In aggregate it is, for sure. No way. So what's the,
what's the takeaway, Dylan? Is, is OpenAI also back at this point? You think they're going to? I
don't know, man. New release in two weeks. New release in two weeks.

Everyone's releasing in two weeks. Google, OpenAI, maybe Anthropic. I don't know about Anthropic,
but Google and OpenAI definitely releasing in two weeks. So. What are they releasing? New pre-
trains? More RL? Same base model? More everything. More, more, more continued pre-training because
the spud, they kind of like didn't finish the pre-training and just released it. So finish the pre-
training, do more RL, drop model. Google mostly just going to be like multimodal swap.

We'll see. I guess my question is like, like the narrative is that, you know, for even the normies
who don't use fast mode, that 4.7 is worse than 4.6. Do you guys agree with this or no? I think the
instruction following has gone objectively worse. I think it keeps missing ClaudeMD instructions or
you pull a skill and you're like, dude, you didn't do exactly what was laid out in the skill. That
seems to be a consistent problem. I don't know. I feel like it's a compute problem more than
anything else.

It still has the like, we've done a lot for today, you know, go enjoy your weekend. I was like, it's
fucking Monday. Like, get back to work. Um, I annoys me so much. It tries to like enforce me to like
stop working. And I'm like, oh, clearly usage issue. Um, but I think, I think the 4.6 golden age
when it wasn't quantitized in the beginning, that's when it was, those were the days. Okay. Fast
mode 4.6 pre, pre the nerf. Oh, but I, I just think that there's this, this maturity of the models
as they become more inference optimized and more people use them, that it becomes a worse experience
as you 10 or a hundred X the users.

And I think that that's happened. Uh, yeah, I just think 4.7 is fine. I think 4.6, 4.7 is probably
the same. Uh, it's just that it's, oh my God, I saw that. Um, it's, it's kind of the same level of
experience. Yeah. It's just too many users, bro. I need a NIMBY. I need a NIMBY AI. I need a NIMBY
frontier model where no one else uses it except for, you know, except for me. So I can use it to get
it at a higher, a higher rate. Um, I mean, that's the appeal of codecs, uh, right now, I think, is
that in theory, you should be able to have higher rates, but.

Can we, can we talk benchmarks? Like Max, when, when you saw the 4.7 release, for example, and we
reviewed some of the benchmark scores, it was better on most, not better on all. And it led us to
talk about like where benchmarks are useful and where they're not. So Doug's given the vibes, like
obviously individual experience can be different across people and it just drives their preferences.
But like there should be some objective way to say 4.7 is better or is not better than 4.6.

Um, honestly, benchmarks obviously try to be that objective measure. I think they just like no
longer are today. I would say benchmarks, it's like you need to be close to, uh, the frontier
performance in order to have a shot at being like the true best model. Uh, but being like number one
on the benchmark rate theme does not necessarily imply that you actually are the best model. And so
I would say like, uh, benchmarks today are most useful as sort of just like a vibe check to make
sure that the model's not total trash.

Um, we kind of talked about this in the newsletter article, but it's, it's surprising to me sort of
how few people actually look into the details of the benchmarks to understand how unrepresentative
they are of like real, uh, like LLM use cases. I think a lot of people just hear a name like
humanity's last exam and they assume like, oh my God, you know, if early, if a model can solve
humanity's last exam, that implies that it's, it's like smarter than all of humanity, right?

We've like passed AGI or something. Um, in reality, you just like, you look at the individual
questions and they're just the most like esoteric multiple choice questions you've ever seen. Uh,
they're not at all representative of anything you've like ever asked an LLM to do. Uh, it's very
intentionally multiple choice to make a verification easy, even though like, obviously when you,
when you like use a LLM in real life, it's, it's open-ended. Um, and this like even applies to
benchmarks that on the surface you might think would be better like sweet bench too, where it's
like, oh, you know, coding is this verifiable task.

Surely you can just come up with some coding problem for the model and then write some like tests
and verify if it's successful or not. Um, but then you dig into the details and it's like, oh, it's,
it's actually really hard to write a coding problem that is both naturally worded, uh, yet still
like perfectly unambiguous with exactly one correct solution. Um, and the sweet bench problems, uh,
at least for the original version, they, they do not at all like fit those criteria.

Uh, they just scrape GitHub issues. And for all the developers listening know that like GitHub issue
descriptions are not meant to be like well-scoped tasks, uh, that you just copy paste and give a
model. Uh, similarly for the verifiers, like they, they often include lots of unit tasks that are
scoped, like particular implementation details, uh, going as far to like ask the AI to output a
specific like 20 word error message. That's not at all mentioned in the task description.

Um, and obviously like later versions of sweet bench tried to solve these issues, but, uh, it's
still not perfect. I think really just underscores a lot of the issues with benchmarks. Makes sense.
So let's, uh, let's talk about 4.7 specifically. Like there was a few things that improved, um, or
changed, let's say, uh, in terms of like features as opposed to just the benchmark itself. And I
think you, you made the point in the article that like the, the people don't necessarily care as
much about the quality of the model anymore.

It's the model plus the harness, which is the product that should be tested as opposed to the model
on a generic, you know, bash only harness or something like that. Harness meaning, uh, Claude code
is the thing you're testing, not Opus 4.7. Uh, so it's Claude code versus codex. It's not Opus
versus GPT. Um, so to that end, like during the release for 4.7, uh, they announced a, uh, extra
high reasoning effort option that slots between high and max.

They announced high resolution image support, which people can use to, um, like use for screenshots
and styling and front end applications. Um, they're omitting thinking content by default. So people
won't see when the model's thinking, um, they're, they've got this task budget concepts that you can
tell the model how much it should think or work before it can actually like run out of context in
the context window. And then maybe most importantly, they updated their tokenizer.

So it, it potentially costing people 35% more for the exact same output from the model as a previous
model, just because they're counting tokens differently. And they're, you know, using it now that of
course, like implies that there's, uh, there's, there's something, um, sorry, I'm just laughing at
Dylan right now. I literally put him to sleep with that monologue. Holy shit. Oh my God. Okay. Well,
man, come on. Hold me over. Well, what are you talking about, man?

Tokenizer. The tokenizer is so boring. Then it puts Dylan to sleep. That's the takeaway. It's not
like the pod was like compelling or great at this point, but it is now I'm compelled. Now we can
talk about all the shit we want. The tokenizer. What's the Michelangelo painting or sculpture where
the guy is like, um, Oh, the thinker. Yeah. He's back. He's back. Could you actually not hear us
through your headphones? I mean, he's been, he's been asleep.

I was just thinking, man. You've been gone for a few hours. Call me, call me, call me GPT 5.5 X
high. I was just thinking right now. Okay. Tokenizer, Opus 4.7, Opus 4.6. We've been dancing around
the fact that GPT 5.5 is fine. Not goaded. Definitely good enough. Lots of capacity. They'll catch
up on the margin. Sounds good. Great. Anything else? Benchmarks suck. That's a really good thing.
Anything else? What's the tokenizer thing? What's the tokenizer difference?

They changed tokenizer between 4.6 and 4.7. The exact same output could have 35% more tokens with
the new one. Oh, they made the tokenizer, they made the vocab smaller. They made the vocab bigger
for 4.7 compared to 4.6. There's 35% more tokens in the tokenizer, like more vocab. So wouldn't that
make the average output smaller? No, it doesn't have to be smaller. Because you can represent
longer, you can represent longer things with fewer tokens? No, more tokens.

Well, sorry. Each token is more granular. If you had 20, if you wanted to make English with only 28
tokens, then you would have to do every letter. But if you wanted to do English with 500 tokens,
sure, you'd have every letter, but then you'd also have like of and the as tokens. Wouldn't it make
the output smaller with fewer tokens? This is a good take. In practice, no. But conceptually, yeah,
you could train the model with full words as tokens. But I think what people have seen is that the
model currently is less token efficient with a larger vocab.

Oh, interesting. But that's a good point. Yeah. Man, the guy came back in with a heater here. So,
yeah. Wow. He was thinking all this time.

Okay. Yeah. Well, the whole concept of being more token efficient is that you can solve total tasks
with less tokens because the more granular breakup of the tokens or the larger breakup in the token
size or just having a larger vocabulary would mean that you would have more information represented.
in latent space. Like the concept of semi-analysis might be a token instead of semi-and analysis,
right? Yeah. But then, yeah, it creates more context, right?

Versus maybe even four tokens in semi-analysis. I get it, right? Like there's choices. It's richer
information. Like the embedding for semi-analysis might be close to the embedding for Dillon in the
latent space, right? Yeah, that makes sense. Which is, you know, the embedding for semi or the
embedding for analysis is probably not close to it. So, whatever. It's probably like, I think it's
unclear whether this is significantly improving performance because everybody still thinks it's a
toss-up between 4.7 and 4.6 of what's better.

But then I also think it's a toss-up about whether this is more token efficient or worse. Because it
seems like people are saying, if it's not a significantly better model, then why are we doing this
new tokenizer thing? So, maybe it's just an early checkpoint. They got to do more RL and improve 4.7
and then have a 4.8 drop that really improves things. I don't think Anthropic really does half-baked
models. Like OpenAI clearly does. Like 5.3 codex is like RL only on code.

Is this the most half-baked of any model? Previously, we've seen Sonnet before Opus, right? 4.5
Sonnet, then 4.5 Opus, 4.6, then, right? This is the first new one of just Opus. It's because Opus
4.7 is actually Sonnet, dude. Are you not a truther? Yeah, yeah. And then Opus 4.7 is mythos. There
you go. Yeah, there you go. This is truther, bro. It's time for truthers, bro. Opus 4.6 is actually
Sonnet all along. Does everyone know? Do you not remember that?

Like, that was like a big model spell. Yeah, removing the mask. Yeah, yeah. Exactly. Yeah, yeah.
This model spell is small. Actually, I wanted to maybe actually pull this back to the DeepSeq
portion of the article because I don't think we talked about DeepSeq. Yeah, the DeepSeq version of
the article. We didn't talk about DeepSeq in depth, but I think we have a lot more internal takes
than what we put in the article. And I guess my question is, do you think the gap between open
source and China and the United States is now widening again?

Because it feels like it is now. And it's because of compute constraints. I would like to have some
takes on that. Just my take is the take. Yeah, I'll give a quick one. I think one thing that's been
overlooked with DeepSeq is the fact that this is a 1 million token context window model, which many
of the leading open source models that perform great on benchmarks that people use for coding don't
have million token context. And then I think that the reasoning in visual space paper that they
posted and then took down as a Git repo makes me think that they're going to release a multimodal
version of this as well, or that they're like in the process of developing it.

And there's going to be new waits for that. Both of those things are, I think are fascinating for
making China caught up on a product basis. If we're comparing cloud code to codex to DeepSeq in open
code or DeepSeq in some other harness, it'll be able to support all the same features in addition to
being pretty good at like all the other stuff. With that said, at the time of the first DeepSeq
release, I used it all the time for random stuff. And I don't use this one for anything really.

So. Isn't Kimi 2.6 better anyways? Yeah. And I don't use that either. Yeah. No, I'm just saying
like, it wasn't like, you know, DeepSeq, I mean, the DeepSeq moment was that it was like so cooked
and it was like from the ether. Right. Or it cooks so hard rather. And it's from the ether, not
cooked. Right. But this round, it's like, it comes out, it's just state of the art or it's state of
the open source art, if it makes sense. It's not exactly better than Kimi 2.6.

I think the other drops in it clearly is just inference optimization. Right. They talked about the
Ascend, the Ascend kernel being partially able to inference it, which would like really, really
unlock more compute for China for the first time. And then also, if you look at the weight size, it
looks very like conveniently, it looks like it can, like, I feel like the China, the soft max for
China is effectively the size of H200 8X pod. Like all the models that you're looking at essentially
are able to be inferenced within that memory domain space.

And there's nothing bigger that is served in state of the art. And like, clearly that seems to be
like, that's the cap, right? Maybe they can do that, but they won't release it on, you know, there'd
be 200 pods to the public. But it just, it just clearly feels like they are starting to hit some
kind of wall. Agree or disagree. Do you think that will like keep or cap the Chinese progress
because they can't inference this at all? I'd like to hear some hot takes here.

Okay. I think. What the hell is that, Jordan? You're like. He's getting hot. He's getting hot and
sweaty over deep-handed, bro. He's getting hot and sweaty over deep-handed. Deep-seeks and
engineering release. It's fascinating. All the new attention variants and the compression on the KB
cache is fascinating stuff. They do so good on the infrastructure stuff. I think that the, again,
the fact that Kimmy's 256k context and Deep-seeks 1 million is like a significant difference for
long horizon egenic cats.

Is it, is it, isn't like the context from 256k to 1 million dog shit anyways, even on like Opus?
Yes. That's garbage. I mean, it's okay. It's not, it's not okay. So it's not like true garbage. It's
probably a step off of the state of the art, like in theory. But the problem is you don't want to
just be clearing your context. Like if you're doing a big task, like seeing the whole context window
is really nice. Compaction sucks. Compaction blows. To not be able to use a million token context on
this stuff sucks.

It's better to clear. It's better to clear, actually. That's my hot take. I would rather just start
over. I would literally be like, make a summary of what we've done, copy paste that and just start
over. Like fuck the task. No, that's what Deep-seek saw in their 3.2 paper is that it's better to,
for their benchmarks, which I think are probably bad, but they published this, is that if you go
beyond the context window for a given task, it's better performance on the tasks they were testing
on to completely clear the context, not even make a summary.

Isn't making a summary like just what compaction is underneath the hood? So to be clear, when I say
make a summary, I say I want literally like, okay, yeah, you can do the entire context window versus
like what the last thing I was doing. I'm trying like, you know, I'm trying to memorize. I was like,
dude, I'm not going to read the million context of slop. It's like, okay, what was I doing here?
Read this. And then I like, well, control C, like a very small part.

So I'm not even, I'm not summarizing the entire thing. I'm just doing the task. I'm like passing off
tasks. Yeah. There's different ways to do compaction, but compaction, I believe is different than
summarization because compaction is, is removing the thinking traces initially. It's not actually
having the model write its own summary of the full context. I thought they're literally just taking
your entire context and being like, yo, please summarize this.

That is an approach and they've done multiple of them. But the, I've got, I've got a hot take. I've
got a hot take. Anthropic with Cloud Code, they, they did well with the CLI. And so they just kept
making the CLI experience amazing. But the CLI experience is not the end all be all of agent
orchestration. And therefore they've really cooked themselves into sort of like an innovator's
dilemma, but they keep making the CLI better. But open AI, they have the, they have the true vision
of where, what the true agent orchestration platform of the future is, where you'll be able to
integrate voice and you'll be able to integrate, you know, multimodality and you'll be able to
integrate all these other things into the app.

And the app is so much better than the CLI. And the real point where you should develop and, and,
and users should be using it in the use case should be on the app, not on the CLI. Because the CLI
is a dead end and it's a foregone relic of H126 and H225. Do you mean the, the, the app forever? Or
do you mean their device? Cause they're, they're talking about releasing a consumer device next
year. No, no, no, no, no, no, no, no, no. Like the laptop app, the codex app.

I have a question. Then why does the codex app suck? So, so, so like, look, I think, Dylan, I think
you had to do the great leap forward. Okay. Dylan, in my opinion, I think you are thinking too small
because in the perfect true maxi world, the operating system doesn't need to exist. You will just
get a piece of hardware. You will plug in your, your, your thing. It will pull up the terminal and
you will connect your cloud API and it will build the OS for you.

Like thinking. So, so, so codex app, they're at, they're adding generative UI stuff too, which is
pretty interesting. Things. I'm just saying, I think, I think if you're a code, if you're coding
purists, generative UI is downstream of CLI. I think I, I, I am a CLI. I do. I don't know. This is
just a slow, this is a slot preference thing. I just love the CLI. Like, like codex, the, the cloud
code usage is clearly just a CLI wrapper and you can tell.

And then codex is, codex CLI is clearly just an app wrapper. Like, I feel like they forced it over.
I think there are two opinion, opinions in the future. Who knows who went out in the very long run.
I'm going to, I'm going to definitely like keep it open for competition. But at this beautiful
moment, a true maxi's vision in dream is, uh, it's all downstream of the CLI. It's just tokens. It's
the most efficient version of everything. Got an Elon max.

Okay. All you need is just an API and then inputs. That's it. Your app and your, all that stuff.
That's all, that's all obfuscation. Mythos would know better than, than, uh, than open AI. Who are
we little brains to know what, what UI we want? No, dude. It's CLI all the way down. Pure maxi
vision. I'm a VS code plugin guy. I literally tested this yesterday. I was bothering Max who told me
to go away about using ghosty for the CLI stuff. It just doesn't work.

Well, no, I still think having like today, having six ghosty terminals open, like cloud code CLI is
a superior experience to having like six different chats going in the codex app. For sure. I just, I
feel more productive. Yeah. I'm, I'm comparing to the VS code plugin, six different windows in VS
code also with a file browser on the left side. So I can, you know, write. Well, I think the
difference is that like, you're still writing real code and you kind of care about like the output,
whereas I just don't even look at it.

You know, I just, I'm not looking at the code. I'm not looking at the code. I'm making, I'm copying
in images or like Excel files or, um, don't you accuse me of reading the code. I'm sorry. Fucking
up, Hudson. My favorite, my favorite is, uh, I mean, I actually agree. I actually agree that the,
the API CLI, whatever is the new compiler. No one is reading the compiler. No one cares. They don't,
you know, they don't need to touch. They don't need to touch.

This is, um, this will be true in the future, but it is currently for any code you actually care
about. This is currently not true. It is currently still producing a bunch of stuff that is bad and
should be fixed with coaxing to tell the model to fix it. I don't, I'm not saying I type code
anymore, but I do read some code. One of my, one of my group chats, uh, I was reading it this
morning and it's, it's like a group chat, like with all the most cracked kernel programmers in the
world.

And it turns out what they do, what they've found is the best work list. Because they're my boys,
bro. You look, look, Max, come on. I'm a, I'm a, I'm a, I'm a master networker. Okay. Um, so, so
anyways, um, I think it was true now. True now. It's like, yeah, dude, codex is like so dumb, but I
always just have it created and then it works and it's smarter, but the code is slop and then I have
Opus rewrite it, but you can't go the other way around.

You can't have Opus write the thing and then have codex fix this, fix it. You know, it's funny.
Really? I go the other way around. Everyone else at the firm prefers the other way around. The
entire firm's preference is the other way around actually. Yeah, but we're not writing fucking
kernels, right? We're not writing fucking tree now kernels. That's probably fair. We're doing
benchmarks of kernels, but yeah, uh, we wrote some kernels. Oh, come on.

Yeah, they're not tree now kernels. No, they're not tree now kernels. They're just, uh, GPU mode
kernel competition. Because apparently like, if you like, if you like talk about like niche and
micro architecture details, Claude will um and ah and waffle on about like shit instead of actually
just doing it. Whereas if you describe it to codex, it'll just try and implement it all and then
it'll be slop. But then you tell Opus to fix it. Opus will um and ah, it'll just fix it.

Yeah. And Doug, this is the context window stuff, which is like when you were pumping in so many
docs about the ISA of a given GPU to write a kernel or something like you need performance at a
million context. Like you just run out of space on the smaller stuff. Um, so I don't know. Do you
want to go back to DeepSeek and any, any hot takes on DeepSeek, Dylan? Why didn't it crash the
market this time if KV cash is reduced by 90%? Dude, you know, it's been a while since I've been in
Asia, but every time I go to Asia, they reference some fucking new paper that reduces KV cash every
fucking time for the last three years.

Some paper that reduces KV cash and no researcher in America has even heard of this paper. It's the
fucking best thing ever. Um, DeepSeek and TurboQuant were the like most precipitous ones that popped
up the most and, uh, TurboQuant was obviously fake news. Um, but yeah, I think it's, I think it's
very funny. Um, I don't know. I don't know. I guess like they're tired of being rugged. Um, I have
a, okay. Well, cause look, I think the real, yeah, I think that's fair.

It just doesn't matter. Jevons is working, uh, clearly with the price of the GPU going up. Like
that's all you got to know. Now, if we're going to talk about real fake news, let's talk about sub
queue. Cause let's do some, I mean, we're not going to write an article about it. We're not going to
write a post about it. This is free, free alpha. Did anyone else read the sub queue thing today?
It's pretty sus. It's actually extremely ultra mega sus. Yeah.

Um, it seems, yeah, it seems like people are, uh, launching their startup, right? You know, they're
going to get, I honestly, they should close funding and then they'd be like, wow, it was just opus
with 10, 10, uh, context windows stapled together. I mean, you think the market is hot enough for
them to close like, uh, you know, 200 at 1 billion round the next month or something. If they did, I
don't think it'd be 200. I don't think it'd be 200, but I think they could do 50 at a bill, a trail.

What? Sorry, bill. No, are you familiar with what we're even talking about? Dylan? No, sorry. I just
thought you guys were talking about Anthropic. No, we're not talking about Anthropic. He's talking
about model sparsity. I'm talking, I'm talking about like the worst. Did you not? It's like this
fake news Twitter thing today called sub queue. Oh, yeah, yeah, yeah, yeah, yeah. Yeah, yeah. Dude,
don't worry. Don't, don't worry. Don't worry. We, we requested for API access.

We, we, we made sure to use our semi-analysis email to, you know, improve dogs. Yeah, we're like,
please give us this API for this very real model, bro. Who knows? Maybe it's a state space model.
Maybe it's a, maybe Mamba cooks. No, it's not SSM. I don't think it's SSM. I, I think it's, I don't
know. It's just really funny because, because, okay, we're talking about like the deep seek people
freaking out. If this was real, like stock, memory stock should be down, like whatever, a
quadrillion percent today.

But obviously it's not real because if you look at the found, like, no offense, maybe the founder is
super legit, but you like, look at these guys and you're like, yeah, man, I just don't think these
guys are going to be the guys to crack the single hardest problem in all of it. So, okay. Maybe one
thing that this reminded me of was the fact that Llama 4 Scout or Maverick, I think Scout, the
smallest one, was released with a 10 million token context window or announced with it, but not
supporting it officially in the released weights or something.

And I'm just, I'm just really surprised that we haven't seen anybody with, you know, effectively
unlimited compute budget, give it a go for a more expensive model with a larger context window.
Like, where are you going to get the data, right? Like you pre, most people pre-train with like 16K
context or four, you know, something like that, 32K context. And then they post-train it so that
they can add and hack in the rest of the context. But it's like, what data do I have?

That's why my 250K to one mil context is trash anyways, is because there's no data on this stuff.
And so the model doesn't generalize the context really well. And then if you stick it to 10 million,
it's like, what fucking data do I have from that is useful for the next token generation that exists
from 1 million context to 10 million context? It's so little. Yeah. I mean, it makes sense. Possibly
synthetic stuff. Possibly. I mean, why'd they do it in the first place?

Like, it seems obvious that people would be working on it. We haven't even seen anybody announce 2
million. So there's some argument. Google serves 2 million. Google serves 2 million on 3.1 Pro? They
did on 2.5, 2 million. Well, maybe that's the answer. That's the answer to me. It's 1 million today.
It's 1 million today? On 3.1 Pro. One of their announcements, they announced 10 million. They
started at 1 and then they updated it to 2 at some point.

One of the models. Makes sense. Yeah. I mean, they've got a big scale up domain. Why not give it a
go with the TPUs? Yeah. Maybe another thing that was a little bit missed in the article. And you
kind of talked about when you brought up DeepSeq. Max, I want your take on this. Because Doug asked
the bait question about, is China catching up or are they still behind? And kind of depends on how
you look at it. But I was bugging you the other day. Like, is DeepSeq or Kimi currently ahead or
behind Meta?

And are they ahead or behind Grok slash Cursor slash SpaceX XAI? I would say that today, they're
probably ahead of all those companies. But the thing that really matters is, like, slope from here.
This is a pretty basic take at this point. But I do think, like, the amount of compute you have is
actually just one of the key inputs to how good your mall is going to be. And obviously, Meta is,
like, signing all these monster deals. It seems like they've overcome the overhang of, like, having
to fire and then rehire their entire AI team.

And they're, like, you know, in the process of making some good malls now. So I would expect Meta to
pull away from all the Chinese guys. If not, so I could have this year, like, first half of 27. And
Meta's not distilling. I thought they were. I don't think they're distilling from Anthropic. I
thought everyone's. I thought they were distilling from the Chinese guys. They were just running to
open source. I mean, that's what Mistral does. They don't distill from Anthropic.

They distill from the Chinese guys. That's fair. Why are we talking about the leading French
frontier model company, Mistral? Dude, you know their revenue is, like, fucking really strong. Yeah,
I do, actually. You know what they've broed down on? Also, dude, the bottles. Because they're a
Neopod. You pick up the bottle on the bike. Every frontier model is in a company. They don't find a
Neocloud. No, yeah, they're trying to become a Neocloud. Or I believe they're doing fine things.

Cerebrus is becoming a Neocloud. NVIDIA is launching Neoclouds. The ultimate business model for any
company in the world is to become a Neocloud. Semi-analysis will become a Neocloud. And then we will
be ClusterMax Platinum. Diamond. No, dude, we gotta introduce a new tier. Yeah, diamond. Tungstick.
Yeah. Yeah, yeah. Semi-analysis. Lithium. I don't know. Germanium? I don't know. I'm just making up
shit. What's the worst? What's your favorite? What's your favorite semiconductor, Doug?

We should make the tiers semiconducting materials only. Oh, yeah? You like semiconductors? Name all
of them. Name them all. Yeah. Name your top five. We should be rhodium. Rhodium. The rarest and most
expensive precious metal. Vanadium? All right, Blaise. This is getting off track. We gotta get out
of here. Yeah, okay. Any other hard-taking takes? No, I think the hot takes have run out. Claude
Code was the inflection point in February of 2026. Doug, your victory lap today in May is complete.

Appreciate all the hot takes today on, yeah, Claude versus... I hope it's not the next inflection
point. I hope it's more exciting than that. And for anybody who didn't enjoy the format today and
would prefer a different one, I just want to shout out one of our listeners, Anna, who said you
should do a format like this, which we did today. So you can give the feedback there or to us in the
comments if you want us to do something different. We're judging.

We're like back and forth between whether we do weekly news or review of the newsletter article we
did, you know, the last week or two weeks ago or something like that. So anyway, feedback's
appreciated if people are listening and making it all the way through this one. ROHF. That's really
appreciated. I bet it better than Dylan.

