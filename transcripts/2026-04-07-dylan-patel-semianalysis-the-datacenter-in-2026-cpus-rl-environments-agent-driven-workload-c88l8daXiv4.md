# Dylan Patel (SemiAnalysis): The Datacenter in 2026: CPUs, RL Environments & Agent-Driven Workloads

- Date: 2026-04-07
- Channel: Daytona
- Duration: 25:04
- URL: https://www.youtube.com/watch?v=c88l8daXiv4
- Source: `uv tool run youtube_transcript_api --languages en --format json c88l8daXiv4`
- Note: timestamps are preserved in the paired JSON file.

## Transcript

everyone I'm happy to have Dylan here. The first time I saw one of his videos was an interview when
he talked about all the way up to CPUs to talk about like neo clouds and why they have the right to
exist and that was super interesting for me because the theme of today is all like what are the new
infrastructure primitives now that agents are here and so you are tricking at that really well at
that point why neo clouds are different from hyper scalers and why they should exist. So can you
share any of that with us?

Sure. I mean um in the age of AI the hyper scalers were a little bit slow to move right Google
Amazon Microsoft bit slow to move into AI and so a whole new crop of companies popped up and there
was a new low bar right there's no need for a lot of the complex software that Amazon Microsoft
Google had built up and a lot of this in fact slowed down AI right they had custom networks that
were actually not that great for AI they were more focused around reliability and storage traffic
rather than you know doing an all reducer across the network or something like this so so there was
a lot of things that these large cloud companies these hyper scalers had that neo clouds could just
skip right and and then build focused optimized solutions and deliver much lower cost because they
have much lower overhead right there's not 20,000 Google PMs sitting in a meeting at these neo
clouds right although some of them have started hiring Google PMs and slowed down the the the neo
clouds they they they just moved fast on energy they moved fast on bringing up GPU clusters and so
they were able to carve out a market right and then you know those are the early ones and then since
then there have been a lot more copycats or followers many who haven't succeeded many who are
succeeding right it really is like a a battle of like who's the most competent And so are all the
cuz there's like I think you said there's like an order there's like a 200 of these neo clouds or
give or take right and so are there differentiations between them that you see like are are some of
them just copying the the sort of software stack that these first ones did or they doing something
else like anything that you've seen that have been successful and less successful across these neo
clouds? Yeah so there's a variety of things that separate them right so we have something called
cluster max that ranks all the neo clouds but we test for various things such as observability
reliability networking security um orchestration all these sorts of things are different right like
does does someone test for their GPUs to be working properly in when the GPUs are idle for a user
right that's active health check or a passive health check hey are the fans spinning at the right
speed or are the you know is it drawing the right power is there something wrong with the node is
the is the network flapping or is anything problem problem with the network is the performance there
right like there's all these sorts of checks and tests because GPUs are unreliable um there's all
sorts of stuff around um the types of software you run on top of the GPU right many people started
off doing just bare metal right so when you go look at like hey Microsoft's first contracts with
Coreweave they were all bare metal right you just SSH in and Microsoft would set up their own stuff
but as we've stepped forward there's a lot more people want right people wanted Slurm installed okay
that's simple people wanted Kubernetes installed that's a little bit more difficult but still pretty
simple people wanted Slurm on Kubernetes installed cuz it's easier to push out jobs and things like
that right and now you're starting to see people do things like managed ray services and all these
things for RL and so there is a class of neo clouds that are building these things and there's a
class of neo clouds that are like I don't care about that I'm just going to build GPUs and rent them
out at bare metal and and there is a difference in cost right like the the clouds that have the good
software also tend to charge more and and sort of returns back to the old school model where Google
Microsoft Amazon had good software and they charged right and so you know and and you see a lot of
these cloud companies start trying to launch inference services and all these other things yeah So
like that similarly in that vein I'll just get to the CPU ones where historically we have customers
that ask for this with like open cloud that happened so that there's a bunch of people that are like
oh I need my sandbox or CPU box running for a very very long time can you give me like a $5 Hetzner
type you know offering and I'm like well no because like that is a bare metal machine that has no
incurs very little cost but when you have something that's larger software offering then there is
more cost so it's hard to to compete with that so I would assume also on the neo clouds that like
the ones that are bare metal as you mentioned have a lower cost of sale than the the software ones
um that moving just I was just curious about that like why the right to exist they had because it's
sort of analogized with what we do but the real question is you brought this up which is
directionally what we're thinking about is that CPUs are the new bottleneck like every investor
partner everyone that I talked to historically was just like GPU GPU GPU and now you had this big
report about like CPUs and I'm like okay yes thank you and so you reported like this year will be a
bottleneck so just give us a high level TLDR why is CPU now bottleneck and what do you see? Yeah I
mean for the first few years of AI CPU was a real big lagger right sure you used it for some storage
used it for some checkpointing used it for pre-processing your data and pre-training but it was
pretty light and then inference was also like the models just weren't good enough to be agentic you
couldn't you know go step by step by step so there was no there was no capability for a model to go
and do actions and string them together so then it wasn't really it was like it was like you would
send a string and it send a string back right simple inference and so there was not much need for
CPUs but then over the last few years or last couple years it's not even like last couple years
right you know Q star open I had that and they had all that drama but then finally 01 preview
launched I want to say like 15 16 months ago feels like much longer ago

>> a long time ago Yeah ages yeah but 01 was the first model sort of there and and we we sort of had
a entire flood of models right like before people would do simple things like check the output of
the model with regex or something simple just to see if it was doing structured properly doing
structured outputs you know for function calling and things like this right but as we've stepped
forward the the the checks on the model are much much larger integrated fully into training right
with reinforcement learning right instead of just doing regex you're doing like various classifiers
instead of doing classifiers you're doing like code unit test and compilation instead of doing that
you're running you know agentic flows where it's actually calling databases and stuff or you're
interfacing with some environment that is heavy on CPU like a physics simulation or or biology
simulation you just kept stepping into more and more complicated things where the model outputs to
checks it right this environment reinforcement learning environment and then goes back and trains on
it and and this loop has gotten tighter and tighter and tighter over the last couple years and then
more recently over the let's call it really the last 6 months you know code agent revenue has gone
from a couple billion to north of 10 billion in like a very short amount of time and and these the
horizon of these has also increased dramatically right like 54 codex can work for like 67 hours and
it's like fine right and so you know it's it's in that time frame it's doing all sorts of calls to
databases it's doing calls to you know at least we we use a lot of cron servers but you know like
whatever whatever it is right there's anything and everything it can go ping check it out scrape and
just work agentically on its own and that's also requiring a lot of CPUs so over the last 6 months
that's ballooned as well in addition to the reinforcement learning training loop getting tighter and
tighter and so over the last 6 months we've seen um the entire cloud market run out of CPUs right I
don't know if you folks have interacted with GitHub a lot recently but it's really unstable

>> I think you're the third person to mention that today Okay

>> Yeah Yeah yeah so we've we've been we've been like checking GitHub's like stats on like how often
is it down how often does it fail to commit like you know whatever right it's it's terrible and
that's because Microsoft sold all their CPUs that they had spare to other people right either
internal use for their lab but you know not really more so like external labs they signed deals with
Anthropic and OpenAI and so they just have like no CPUs left right and we've seen you know the same
at many other firms right so whereas before you'd have like you know have many GPU servers per CPU
server and so you'd be like you know 100 megawatts of GPUs would be served by even like 1 megawatt
or less of CPUs nowadays the ratio is like getting much much closer both for RL training and and for
inference agentic inference so then you you've just seen everyone run out of CPUs Amazon's volumes
on CPUs of CPU servers they're installing have 3x year on year right from this year versus last year
and so that there's just no capacity anywhere and that's causing a lot of instability not just in
GitHub but probably other places too I mean a lot of infrastructure today we talked about this like
every day it's normal to see that some infra provider be it GitHub or being like an actual not to
name like they go down like it's become quite a constant thing and so could be lack of CPUs but also
scale of the workloads and what not so

>> that everyone's infra code is vibe coded Yeah it could be that everyone's infra code is vibe
coded yeah could that be as well I don't think it's all but there could be there could be parts of
that that is there and so what I see which is interesting as well as the number of CPU workloads or
the number of that are running on us so Daytona has basically three use cases so it's like code and
command execution so if you like a a cloud code type of thing needs to run on a We have computer use
case cases which we see actually growing really fast. We've now launched today we announced our
Windows sandbox which runs on a CPU. So if you need an agent to do like on legacy software which is
like all finance, all support, all um that's all there. But I'll also to your point like
reinforcement learning, we have a bunch of people that usually use like Kubernetes. Now they would
use us. But the interesting thing is the the size and scale of these loads are insanely large and
they're growing insanely large. And we're like the smallest cloud in the world. So my interest to
what in the question is like if we as a very very small company have this much, what does that do at
the large scale, right? Like so um and we've had I'm curious if you have any insight on this, but
just just RL let alone the long running agents which are on their own, we we see customers coming
in. One of them ran a million one single customer yesterday in the span of 6 hours. Like 1 million
of these CPU workloads. So that's one customer. And so like how many of these customers are doing
RL? They're going to need this. I I don't know if you have any insights on this, but I'm just
curious.

Um I mean I mean there there there there are some pretty uh shocking metrics. Like a million VCPUs
sounds insane. Um but there some of the some of the scale of the workloads and contracts people are
signing are are even like more ridiculous than that, right? Um I'm sure that's because we're really
small. That's what I

>> Yeah, yeah. So so I guess I guess like when you look at like again like when you look at like the
Anthropic at Open AI of the world, they have they have fully just eaten the entire capacity of
multiple clouds, right? A lot of the impetus for the recent Amazon and Open AI deal was yes, Open AI
wanted money, yes, they needed compute, but they also just like went to Amazon and were like give us
your CPU.

>> CPUs, yeah. Right? Um and and before Open AI's stack was pretty much only on x86 CPUs, but Amazon
had tons of ARM CPUs and so they ported the whole thing, right? It's like anywhere I'll I'll port my
code base to get uh access, right? To access to CPUs. And so this is like the the level of like and
it's not that difficult to port port from x86 to ARM, but you know, like there's there's very few
dependencies that aren't working now, but um this is the level of like um engineering people are
willing to go to, right? Cuz usually devs are too lazy to do anything um and they'll just go get
capacity elsewhere, but there isn't capacity anywhere else.

Yeah, so I mean that's interesting like we're all x86. That's all we have. We don't have our our ARM
at the moment. But then like there's those two which I know, but also like Nvidia has their like
CPU, other people building out their CPUs. There's also differences between these CPUs. Are there
just going to be like these general purpose CPUs? There's also like you probably know more about
this than I do. I'm just like super curious. Um on the types of CPUs? Like now there's so many there
used to be just like x86 and ARM. That was it like for the most part. Now there's different types of
CPUs. Is it just because everyone's run out or are they like better at some things than others? Are
there anything I mean usually what happens like when there's a gold rush is the person with a broken
pickaxe can also sell their pickaxes. Yeah, yeah. Um but like yeah, I mean this the CPU market is
like quite dynamic, right?

Um you know, it it was mostly Intel AMD. I assume you mostly use Intel and AMD CPUs. Um Both of them
have said they're like fully sold out. They've sent price increase notices to their customers. Um so
they're not even competing with each other anymore. They're just like how many can I make and sell?
Um and likewise like Amazon had their Graviton CPUs. They've had what? Five, six generations now. Um
And Nvidia has their Vera CPU. Right. And Nvidia has their Grace and Vera CPUs.

Um and no one really deployed Grace standalone CPU boxes. There was like a couple small deployments
that Nvidia Nvidia did for PR with people, but in reality there's like very few like standalone CPU
deployments that Nvidia was able to do. Okay. Um but now well, just they're just not as good, right?

>> Okay. Um but now as we step forward, maybe their CPU got better. Um maybe they're bundling
better, but also just because they have capacity.

>> Because no one else has them. Yeah, they're they're they're able to get a lot more contracts on
their uh Vera CPUs uh that are going to deploy sort of later this year, early next year time frame
um is when they start deploying. So it's sort of like a very um dynamic market. And then and then
you've got like Microsoft and Google are starting to deploy their CPUs in volumes. Um ARM is going
to launch a CPU in like a few weeks uh that Meta is going to adopt and a few others are going to
adopt um like Cloudflare. And so there's going to be a lot more proliferation like ARM standalone
rather than like ARM licensing the IP to someone. So there's a lot more um diversification in the
market um which which happens when there's a gold rush, right? And then we'll see what actually is
the best quality and is left standing as the sort of supply demand gap get closes. Yeah.

But it seems that supply and demand will still grow like at least what I see like one the RL and it
it seems like RL is mostly done, you know, they do post trading on RL, but we have now vendors and
companies that are pitching and creating services that do RL in real time. And since you have like
some agents you have some SAS that's an agentic in the background and then it will do RL at the end
of the day basically to like learn against what it has done. And so that grows. But also these long
running agents, if they the way it seems to be working directionally is if the agents can work
longer and solve for more things, you can essentially ask them to do more and they will spin up more
and more of these agents which means more and more CPU boxes. So do you see that like from your
purview do you like I understand market dynamics and that'll probably converge at some point, but I
feel it's getting wider before it's shrinking the need for that. Yeah, I mean it it it's that's
totally the case because initially all the RL was like, let's do math proofs.

And I was like, okay, math proofs are really low on resources. And also the model, right? The
generator will generate tons of output and then it'll send the correct answer or what it thinks is
the correct answer to the server and then the server will verify it. Um but as we've moved forward,
right? Like it's it's not just that. It's like, oh actually the model is committing many times or
it's like trying to compile many times or it's trying to do unit tests throughout its agentic
process. Okay, now that's that's increasing the frequency in which the generator, I eat the model,
is sending to the verifier. Um and that loop gets tighter and tighter and tighter. And as we as we
continue to move to more complex RL, it's like the model will actually uh be verifying its output
constantly, right? Like if you imagine um let's say models that are training over the next year or
two is is let's say a robot model that's verifying and that's that's in in a like a world model,
right? So uh VLM is is navigating across the world trying to pick up things, put them down. Every
single action needs to be verified against the physics model that is sitting on some CPUs. And so
that's that's insanely way more CPUs than you need for say doing unit tests or running a math proof,
right? And when we look at like 01, that's like all it could do was math, right? Um and as we look
at like you know, sort of uh GVD 5.4 or Opus 46, like it's okay agentic software, but like as we
move forward to the next stage of, you know, whatever's coming, it's going to be models that can
understand, oh, I need to tie my shoe and like when I tie it, what's the strength strength, yeah.
like what's the tensile strength? All these things like as to the the has to be calculated cuz the
verifier is just generating, you know, what's the next step. Um but every step needs to be checked
way more often and the intensity of that calculation for checking the step it goes up a time.

>> Yeah. But there's also another thing and you probably know better than I is like the the the
level of the the the strength of the GPUs can handle in parallel a certain amount of CPUs boxes. And
so as we get next generations of GPUs, I feel that they will be able to spin up manage or work on
more CPUs than they do now which is another stressor on CPUs now. Yeah, I mean that's that's
certainly the case, right? GPU Well, GPUs are also just like getting way higher power, right? So one
GPU will equal many many more CPUs over time, right?

Um and GPUs are getting more expensive gen on gen on gen, whereas VCPUs are flat, slightly down.
Yeah. Um and so certainly it's a different scale, right? Like one Blackwell versus one Rubin,
performance is up X. Price is also up X. Um whereas, you know, you may buy last generation CPU, new
generation CPU and there's 192 VCPUs in this gen and last gen was like 96, right? So now you've got
way more CPUs, but the the price increase is equivalent to what you got in additional VCPUs. So it's
like sort of yeah, the the ratio will grow in the favor of VCPUs, but the cost will be sort of also
probably in the direction of CPUs, but not sure how much. Yeah. And and also the other stressor on
that and we've seen this with with larger customers when they have like they don't they have like a
time allotment for GPUs and they don't want their GPUs to be idle. So they rather pay uh for warm
pool running CPUs so that whenever tasks come from the GPU, the CPUs are they're hot. They're
essentially working, right? So they'll we we I say we cuz we do mostly CPUs are certainly the cheap
resource. I don't know if we're cheap, but cheap resource for this. And so that spends more GPUs
actually just because the cost of having an idle GPU is to is way more expensive, right? Yeah, it's
actually like a really interesting point, right? The business model is like no one does I mean sure,
there's on demand GPUs, but like Lambda has like 50,000 plus GPUs and only 4,000 of them are on
demand, right? And they're always sold out. So like no one really has on demand GPUs. Everyone's
signing at minimum like long-term, you know, multi-month contracts, but in most cases multi-year
contracts. Um and so like CPUs have been used to like you can spin them up and down, right? That's
why everyone moved to the cloud, right?

Um but with these RL workloads, it's like, okay, the GPU generate the generator, the model running
on a GPU generated a bunch of stuff. It sends it to the verifier. If the verifier is not ready and
waiting

>> Then it's idle. Then it's waiting.

>> Right. Like the GPU is just sitting there. So it's like, okay, well, I've already paid for this.
Yes. So if you can't get your instantaneous you know you know resources spun up on the CPU side and
in fact you should do it preemptively so it's not like loading you know the the simulator that you
or the generation the environment right you you're wasting money so yeah like that that makes a lot
of sense. And not only that then you have that running and then as soon as those are running you're
spinning up another warm pool of these so that every new iteration of them are are continually
growing. So what does that mean generally? So we skipped over RAM memory we didn't talk about that
where it's like GPU was a bottleneck RAM memory was a bottleneck and now CPUs. So just very closer
to home for most people is that like it's very hard to buy a PC today because it's like super
expensive is is that happening to the CPUs because we just mentioned that they're like they're
fairly inexpensive and flat does the market pressure now demand sort of that these prices now
increase?

Yeah I mean it's it's pretty much the case for all like PCs laptops building a PC that it's hard to
get you know Apple is pretty sold out of like Mac minis for example. We we bought a bunch of Mac
minis because people are switching from you know people who used a bunch of Excel and like Windows
are like okay I want to use clock code and OS X is obviously a better um dev environment right so we
just bought a bunch of Mac minis and people are deploying them and using them and and sort of I
think similar has happened across the space and then data centers are way more of an inelastic buyer
of resources and so that's also caused prices to go up right so like GPUs always were expensive and
video's margins have always been you know 70% plus CPUs the margins were not that high but they're
creeping up because Intel and AMD are raising prices and they're tight memory has like 4x in price
over the last like year and it's going to continue to go up and then now storage SSD right so it's
like all of the resources are SSDs are also up like three four x in price and going to keep going up
at least another like 60% not as much as DRAM but up a lot and so between these like four like these
things right it's like well the CPU capacity for Intel and AMD is somewhat fungible between and
substrate and all these things somewhat fungible between PCs and and data centers RAM and storage
are very fungible and so you've ended up with this like conundrum that like look screw the screw the
like normally humans screw the humans yeah you have to buy a Mac Mac mini now otherwise you'll never
escape the permanent underclass is like the thought process.

And one last note before we're close to the end but one thing not financial advice like Intel was in
a very bad spot like quite like recently. Still are. Yeah but does this pull them out? Um I mean
they'll do better but like it's not like it's like a long-term like you know oh the company's saved
right? Company's valued on like future cash flows but like and also like some potentiality they get
like Apple or someone else as a customer and this is actually like the funnier thing is it's not
because CPU demand is so high Intel have some short-term profits from that but you know others will
catch up AMD and Amazon and others will catch up on capacity that they have. More importantly is
that AI is buying all the capacity on 3 nanometer and 2 nanometer in a couple years that you know
people are having to turn to other directions right like one of the like you know people make all
these like nonsense reasons up why Nvidia acquired Groq part of it was because they want to have
really fast inference but like part of it is that Groq is manufactured on Samsung right?

Because there's no 3 nanometer capacity for them at TSMC they need a chip somewhere else and if you
just if AI is as crazy as like we believe it is and demand is as crazy as we believe it is it's
going to be even crazier next year and so like just make any decent chip and it'll sell right is
like sort of the philosophy there. Obviously there's a lot more they're doing there on the
architecture and stuff but same applies to like Apple is getting squeezed out right like TSMC told
them hey like get off of 3 nanometer move to 2 nanometer faster right?

Because all the AI chips are on 3 nanometer and it takes time right small mobile chips are easier to
make than big AI chips so all the AI chips are moving to 3 nanometer now right? MI350 from late last
year from AMD or Tranium 3 and TPUV7 from late last year or slash early this year from Amazon and
Google or you know Nvidia is launching Rubin next week right? That's that's also so all these things
are 3 nanometer and and they're just telling Apple to get off. They're telling Qualcomm and MediaTek
to get off and all three of these companies are like oh maybe we should use Intel because they're
not telling us to get off because they don't they can't manufacture AI chips.

Yeah so so it's it's pretty it's pretty tough for everyone. Um I have like a bunch of questions I'd
love to ask you we're like we have 20 seconds left so the next question I ask you is probably going
to go off so with that I'll just like keep us on time and appreciate so much for coming and talking
to us. Thank you so much.

>> you.

