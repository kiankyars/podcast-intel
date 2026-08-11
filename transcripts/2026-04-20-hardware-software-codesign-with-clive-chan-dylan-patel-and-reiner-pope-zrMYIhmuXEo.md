# Hardware-software codesign, with Clive Chan, Dylan Patel and Reiner Pope

- Date: 2026-04-20
- Channel: MatX
- Duration: 30:58
- URL: https://www.youtube.com/watch?v=zrMYIhmuXEo
- Source: `uv tool run youtube_transcript_api --languages en --format json zrMYIhmuXEo`
- Note: timestamps are preserved in the paired JSON file.

## Transcript

I'm I'm here with Clive and Riner. You two have both come over to my house often to talk about chips
and hardware software codees, but for some reason James Hills decided to stick a camera in her face
this time. Uh introduce yourselves.

>> Yeah, I I'm Riner. I um I'm CEO at Maddox. Uh we we make chips for uh large language models. Um
and then before that, I was doing um inference stack optimization at Google for for all.

>> Yeah, it's great to be here. Uh I'm a guy on X that likes to talk about hardware and software
code design.

>> Yeah. So I think I think like one of the things you two have taught me a lot about is just this
this whole hardware software design code space, right? So Riner, you wrote the Palm paper um and I
thought that was the best paper of like 23, maybe 22, I don't know when it came out, but

>> we had to stop publishing after that.

>> Yeah, that was the last paper that Google published that was like valuable.

>> Yeah.

>> In infra. Um

>> Yeah. And I thought that was super interesting. And then and then Clive you you you know you
worked on a number of really interesting things. Um and you're co-designing for a completely
different space before.

>> Yeah.

>> Um what does what does code mean?

>> So code design is when we can uh not only make the software better or the hardware better in
isolation given just like a fixed workload or a fixed piece of hardware. uh we want to make both
better and so we might want to uh change the hardware in a way that makes some sacrifices today that
will beep rewards in the future once we can design for that future hardware. The thing that always
confuses me is like uh when you're doing code design um what exactly are you doing right like you
know like it's like oh are you just changing the shapes of the map moles or like are you like what
what what kind of optimizations even exist in this space I mean I think like first thing is like the
sacrifice is is the key point right like uh what is a typical ML research paper it's uh I've made
some change to my model architecture um and therefore all the metrics look better as a result like
that's the architecture thing. Um you can do that without code design.

That is just ML research. It becomes code design when you say um actually some of these metrics are
getting worse. Um but that's because these are metrics run on the current generation Nvidia GPU. Um
and so uh maybe I should look at a slightly more generalized metric like what is the um the gate
count of this of this architecture or what is the uh energy cost of this architecture? What's the
intelligence per pickle um of this thing? Um and then so if you look at that more generalized um
metric I think uh that sort of starts to approach giving you the flexibility to make all of the
changes across the stack rather than just localized to the current generation of GPUs. So I think
like very simple things are uh to take a case study like if you look at the difference between a
swish activation function um evaluating uh swish requires um evaluating some exponential functions
those require um function lookup tables polinomial approximations um there's a lot of multipliers in
them uh can be quite energy intensive at the other extreme is to say relu is kind of the simplest uh
activation function at all compared to uh greater than zero is extremely simple to weight um and so
maybe it's cheaper in hardware to do uh to use relu rather than swish um but maybe it's worse in in
model quality and then now your question is which one should I use um I want to do that on the basis
of me um uh energy cost rather than rather than what one's faster on GPU the the example I'd love to
give is uh you can always make your systolic array or tensor core wider uh in order to get more
arithmetic into one place Um, but a lot of models are just not that wide. So if you increase the the
size of the tensor corn, you're not going to get any faster execution of that model. But if you tell
the ML researchers, make the model wider. I know it's like not completely efficient for ML, but in
net once you also account for the hardware efficiency gains, it will be better.

>> I mean, why not massively wide like one layer uh 10 million wide or something like that? Well, if
if you can build a 10 million wide uh tensor core that can run at the same power as a uh 128 wide
tensor core, like obviously that's that's the right choice to make, but obviously that's not
possible. So, so a bit of a philosophical question, right? You see papers like um let's say deepse
v3 their attention mechanism was the first one at least of a public paper where the arithmetic
intensity was equivalent to that of hopper right in terms of how many memory how much memory
bandwidth versus compute for the attention mechanism um you look at certain papers from other
Chinese labs where they're like uh I think I think like gen on genen I don't remember which lab it
was it might have been Alibaba it might have been someone else but genon the architecture was like
very similar except they went from like 100 layers to like 70 layers and that just made inference
like 20% % faster, right? Um, are these co-designes because they're not really influencing the
hardware.

They're kind of looking at the hardware and the confines that it has and and then making their model
fit that hardware really well. Um,

>> I think a lot of people call a lot of things codeesign. Uh, but in

>> no true Scotsman is this. Yeah, I think in our in both of our narrow views, uh codeesign means
that um instead of designing your model specifically for the hardware capabilities like Deepseek has
done very well, uh or designing your hardware for uh models, which Nvidia has done very well, you're
looking at both at the same time and you're trading things off where you might actually make a
sacrifice on model quality in order in order to get much more efficient hardware utilization. or the
other way around such that end to end you're doing better.

>> It it seems to be and maybe just from the definition of it uh you get hardware companies that do
code design um pure model companies maybe less so or you know what's your read on that?

>> I mean you know a public example is Trevor's eye he posted a tweet uh screenshotting an image of
an email and that email was like hey here's what we want for hover next to Nvidia. Yeah. Um and
Nvidia did implement many of these things. Um I don't know what amount but they did implement some
of these things and then they released GPT 5.3 codeex um X high. Is there are there more are there
more words after? Is it just any of the numbers?

>> Yeah. Um anyways, you know, they released this model and they say it's co-designed with black
belt. Is that is that an example of a model lab

>> with someone else's external hardware? Yeah, seems like

>> Yeah.

>> Um I think I think you do often kind of get these ping-pong relationships where you get feedback
from from the model designers and then the hardware designers implement it and then the hardware
comes back and then the model designers get to take a look at it and then feedback kind of ping
pongs back and forth. Uh but uh maybe the larger ambition there is that we can look at both at the
same time. How do how do you do that when the ML researchers don't even know what they're going to
work on in like six to nine months and you're like hardware time cycles like I just the one I just
mentioned is three years.

>> Yeah. I mean I would say like hardware designers kind of have to have to predict where the model
researchers are going and like maybe take a um kind of squint on what their model researchers are
doing. Like I I think there's like it's possible to look at trends for sure. recent trends, for
example, seem to have been um hey look, Nvidia has a whole b bunch of um control resources on all of
their ends. Maybe we can figure out interesting ways to use them and do something more dynamic. So
like you can you can see people how they're responding to trends. I think longterm you can predict
the model is going to be exactly this shake. That's hard to do.

Um but we're going to use more of the resources that are available and less of the ones that aren't
is is a pretty straightforward thing to predict. I would say

>> one of the things I've heard from researchers and um is sort of some of these chips that seem
quite well co-designed right uh they actually hate um so an example is like uh TPUv6e uh trillium I
think is the public name uh ghost light is the name that everyone actually knows um but anyways it's
very common for people from deep mind to be like oh this this chip is really weird because it's got
like a terra oh sorry a pedaflop of compute and like 32 gigs of HPM. It's like quite a weird shape
relative to the other chips at the time, right? It's got like 1/4 the HPM or something like that of
a of a hopper and only half the flops. And if you look at real utilizable flops, it's it's like the
same, right? It's it's quite a weird chip. It makes sense in in many contexts, but I guess a lot of
researchers hate it because it confines where they can do the research. Is there a way code design
can go wrong? I mean, I kind of think you want to make a chip that people do hate to some extent.

Like, uh there there's people don't hate a chip if it's if it's got a very wide um basin uh of of
operating points where it can work in well. Um and I think that actually means you've left some
resources on the table. So, uh the like really you're looking for like you would like your model to
use all of the resources at 100% efficiency um or 100% utilization. Um uh but if you can do that and
sort of leave some slack around then maybe you could have typed something often that is make a
memory smaller because your batch size were too large or or if you have multiple different ways to
lay out a model on on the chip then um then probably there would have been one that was most
efficient and the fact you could do other ones um is a missed opportunity. So, I mean, like I think
it's a little glib to say that uh you want your users to hate you, but uh but to some extent they
should work pretty hard to actually uh get the most out of the hardware. I mentioned like sort of
one that's from perhaps your history. Uh maybe one that's also from perhaps your history is like,
you know, the the dojo trips chips. RIP, right? Um sat sad they're uh cancelled and restarted.

Maybe I heard restarted. Um

>> they they are also like really weird, right? in terms of like um you know I guess it comes back
to my question of like do people hate this right is is you know they're really really good at
convolutional neuronet networks um there's like some really interesting data locality stuff but then
like you have no memory bandwidth right like it's pretty bad um

>> I mean one of the one of the interesting constraints of chips is that they are two-dimensional
and you do actually have to confront this fact pretty actively when you're designing an ML chip um
and that's why architectures like systolic arrays exist that are very naturally suited to a two-
dimensional architecture whereas you also see architectures um many architectures that have like an
L2 L1 cache that is that wants to be connected to all the different processors that are on the chip
and that's maybe less suited to uh embedding into 2D

>> I guess but but in some way right like you know Tesla's a huge buyer of GPUs right um they
continue every you know six months or so announce a big deal with Nvidia. Um, of course they have
their dojo chips. Um, sort of going back to the whole point of like you've constrained the user a
lot, right? Um, maybe Dojo is not good at certain kinds of model architectures, right? uh is does
that slow down? Is there is there a point where you co-design too much and now all of a sudden like
you know you've left no flexibility on the table and you know you you've got you burned you know the
architecture into the silicon and like you end up with like something that no one can use for modern
stuff because ML research is moving way faster in different directions. Yeah, that's a challenge is
that you have to as a hardware designer kind of predict the future and uh you don't know where the
future is going to lead. Um I think the most reliable way to think about this is um just like when
you're doing ML research, you are thinking about scaling loss and you're thinking about what is the
how do I measure the direction that things are going so that I can launch a big run and then now
we're thinking about it in terms of what is the direction things are going so that I can design a
chip for where the models will be.

>> And then the other thing you said is 2D which makes sense on a chip level. Racks are
threedimensional though. So there's there's a point where that struck, right?

>> That's true.

>> Yeah,

>> you can definitely come with some very interesting network topologies in in these racks. Uh
there's the there's the Taurus for TPU famously. Uh there's um Nvidia has a I guess you would call
it a flattened butterfly. Isn't it just switched old all?

>> Yeah. All sorts of fancy names for the same thing. Um, what else is next generation TPUs have
dragon flies.

>> That's interesting.

>> The traniums, I don't know what the hell you'd call their architecture. It's like sort of a
Taurus. Now they've added switches, but there's like switches in different trays and like you can do
all kind of, but like there's multiple. It's weird. Um, it makes sense. It makes sense though once
you once you train an apple model. Yeah. Yeah, I guess I guess how does one like do you view it as
just a spectrum of like I'm overoptimizing for a problem or not or how much of this is like the art
of just like you know oh I think models will be there.

>> I mean I would say part of it is just you're providing the raw materials. Um you have to figure
out like I mean there's sort of a whole spectrum of where you can provide those raw materials. If
you provide um ingredients that are too small like individual gates that's what an FPGA is. It's 10x
less efficient than an XA. So don't do that. Um make the unit the grain size bigger. Um like
systolic array as the grain size. Uh that's really pretty efficient at that point. Um uh and so pick
the grain size appropriately. Um think about which fusions should be in place and are naturally
there. So maybe some operations always get fused together and so you can have them as a bigger grain
size. Um and then just try and expose those things uh with as little overhead as possible. Um, so I
mean that's sort of just like a hardware ccentric approach to it. It's not really saying necessarily
what are the models wanting and predicting what the models are, but it's just like the you can bound
your downside by doing that. Like I'm giving you all the things. Maybe I don't give you as much of
the things that I think you don't need, but mostly I'm giving you the raw materials to work with. So
I think that's a pretty safe hedge. Um what you can do better than by taking it into account what
you know about models is say well actually um so sure we know that multiply and add should always be
fused together into fuse multiply add uh but maybe I also know something about um attention
computations and I can take advantage of the fact that there's always a softmax there I can do
something special for that and so on and so uh there's sort of a one angle on this is just say um
bound your regret on on the hardware design uh with as much information as you're willing to use
about generally what I know about models.

>> Well, one of the areas where uh code design is is a little bit contentious is um the claim that
uh you can specialize a lot for transformers

>> and maybe even burn in the architecture in some sense. Um what do you think of that of the of the
claim that you can get 3x 10x gains from specializes specifically for transformers? Pick the grains
that you're working on. Um large matrix metifies is a very clear one. Um like grain size continues
to give you returns. It they diminish for sure but um uh if you have lower precision matrix
multiplies they diminished like they have diminished less than than if it uh like just your the uh
denominator is larger or is smaller and so the the numerator becomes more important. Um uh and so I
mean like what approach we take for example is just to say um major multiply and uh and some stuff
in attention is is the place of specialization. Um but like don't take it all architecture to to
appropriate size pieces.

>> In uh you know Ilia's words right we're in the age of research. Um you know people are trying all
sorts of crazy stuff. Um and I feel like two three years ago if you saw something that wasn't a
transformer at least personally I ignored it. Um but now I see some of this like weird stuff and I'm
like oh this is interesting. I still don't put much time into it but like I look at least look at
it. Um, and if that's the case, right, you know, you know, as we move beyond transformers or at
least you should have some as an as an AI lab, right, if you're an openthropic GDM, you should at
least have some portion of your compute into highly flexible uh, compute, right? So, so as an
example, um TPUs aren't the best at like fine grained like routing and dynamicism and um the
programming model at least is pretty painful to do that especially if you're just doing research and
not like doing real training or inference, right?

And so you see that with like you know doing dynamic stuff with palace and jacks and XLA is just a
pain in the butt. Um and on the other hand like GPUs because they have all these small cores are
actually much better at this. Um and so Google still has some GPUs for deep mind. Uh, do you think
that's like a long-term state where every lab should have at least some budget of like, hey, screw
it, let's let's do some like weird wacko [ __ ] on the CPUs, too, right?

Like,

>> I mean, it depends on how much room there is to to optimize. Uh, on the one hand, you can argue
that uh transformers are kind of a they're sufficiently general architecture that they're within a
small constant factor of whatever possible thing you could possibly think of. Um, or we could go the
other way and be like, well, the brain has neurons and something something about the amount of
energy it takes to do something in a neuron. Um, therefore, there's thousandx gains if we just
change the architecture. And

>> this is this is what R's company are doing, right? He's like he's like doing code design from
models all the way down to hardware, but he's doing like crazy analog [ __ ]

>> right? So if you're in a world where you think that things are going to happen like that, you
should absolutely be looking at all this future model research and really focusing on that. And if
you're thinking that things are going to be more stable from now on, let's just focus on increasing
the grain size, uh making sure that we can really run what we think is important efficiently and not
focus so much on these like I don't know 1.2x 1.5x gains where we could get more from the hardware.
And I don't know which one we're in.

>> I mean, you said Ilia. I I don't know what's on his mind, but what it sounds like is on his mind
is not necessarily at all model architecture. There's a lot you can do loss function um training
data and so on. Um or or even just like take a transformer layer and then who knows alternate it
with something else or uh all of these things which are available within the um the world of um
architectures that have like substantially be had some of the first of transformers down at least.
Um uh I think it's funny by the way you said you don't know what I was thinking. I think no one
does.

>> Yeah. Right.

>> Yeah.

>> If you know if you look at the like Yeah, of course he does. Um and and his people do but I think
they're very close lips. to the point where like, you know, SF gossip is usually at least somewhat
okay about people and companies and things that are happening, but then like, you know, I've heard
all the way from like they're making cyber weapons to like they're just trading financial markets.
And

>> who knows,

>> they're doing everything in between. Who knows? Yeah.

>> Ilia is uh sees very far for sure. But uh like ultimately comes down to whatever he ends up
shipping.

>> Okay. So So like let's let's take take yourselves back to like 2022. was it when he was starting
to write internally at OpenAI about reasoning, right? Um which eventually became strawberry and all
these other things, right? Um you know, he he tried many many different things in this direction and
finally I think it was Yakob figured it out. I'm not sure if it was him or not. Um, sorry if it was
someone else, but you know, they they figured out like some form of, you know, test time scaling,
you know, verifiable rewards, you know, this whole RL pipeline that has now been sort of giving us
crazy gains over the last It's actually only been 14 months, by the way,

>> really

>> since the first reasoning model.

>> Wow.

>> Anyways, uh, it's only been like 14 months. Is there something like you know you know like if if
if codeesign is like oh well if you go back to 2022 everyone was thinking pre-training era you know
just keep scaling pre-training and now you're like wait actually Ilia was saying in 2022 it's not
pre-training actually we need to we need to codeesign for sampling um what what would do you think
like what do you think about codeesign there and like what what are your thoughts of like hey um
what would you have done differently if you're like an Nvidia or someone else and in 2022 you
decided this

>> yeah I I think that the challenge there is that you can always have these paradigm shifts where
suddenly sampling becomes so much more important to increasing the intelligence of the model. So
you're no longer doing as much pre-training. You're now doing all of these uh these decode passes
where your arithmetic intensity is very low. You need a ton of memory bandwidth. Suddenly
everything's changed for the hardware. Um, and you can't really predict that as a hardware person.

>> Wait, so if OpenA II made the chip in 2022 when everyone was pre-training field and only Ilia was
like, let's sample a reasoning, then the chip would be in the wrong direction, right?

>> You got to come in with with some amount of flexibility as to as to where you think things are
going to go. And like at the time like Ilia was the only person who thought this eventually it was
two people, three people and then eventually suddenly the whole company and the whole industry I
think the labs have to hedge in this way like and I mean they have to hedge across different
hardways. Um as a result I think sort of the incentives for hardware vendors are maybe different in
that um and and it really depends whether you're invid product like your next generation Nvidia
product has to sell. Um well no but they're making three products now right they're doing the
they're doing the mainline they're doing the CPX right higher arithmetic intensity they're doing the
like the Grock stuff right with it's like a you know they're doing with 3D RAM instead of like SRAMM
but like you know

>> they're making different bets

>> there's yeah there's some amount of that so if you can make multiple products that's another way
to hedge for sure um most companies that aren't Nvidia or maybe Google um can't spin off multiple
products simultaneously so I mean I think the right thing like for for companies that are making
that choice is just like make the best guess and try. Um I think like if your best guess is like as
making hardware trying to hedge across all all possible scenarios um you just don't win. Um like you
don't win any in any of the scenarios. Um you totally can as a lab because you can wait and see and
and decide which one to buy. But but as a as a hardware vendi you have to make some some some effort
for sure. So, so I guess I guess I'm curious of your two perspectives, right? Like, you know,
Ferubus Grock, they were working on something that and and they were not focused on the low latency
sampling regime, I don't think. Um, yeah, I think some

>> it seems like they kind of fell into that accidentally where they were,

>> but it's now a codeesign point that actually makes a ton of sense.

>> Exactly. Exactly. They it it worked out so well because they were working on these confets that
were very small and could fit entirely on

>> the other picture I heard is it's LSTMs that were also like very uh

>> very small very very uh sequential.

>> Yeah.

>> Yeah. And so so you can fit that all into one tile. Same thing for for for Dojo as well. Uh and
then suddenly LLMs come along. It actually turns out you do need to be able to have like terabytes
of parameters. Now uh and that's a very different regime. But in this specific market where you
really really care about low latency above all else like encoding uh like in quite a few um these
like thinking models or just just take too long. Um this actually really matters and this is a
really good niche for them to be in. So I mean my take at least on on on the low latency thing is uh
I mean if you look at what that means you are um I mean you want low latency for sure uh and SRAMM
is really the only only strategy to get there. Maybe the 3D stack HD RAM is is um there's an
approach that will get you close to that. Um it's it's interesting for other reasons like KV cache.
Um but then what do you do with all of that compute? Like you've made a you've made a product that
has a lot of compute because of the other use cases for prefill and training and so on. Um, and I
mean if you look at lab pricing, it kind of looks like the fact just the fact that pre-filled tokens
are, I don't know, five times cheaper than decode tokens says something about what utilization or
efficiency is in prepole versus decode.

That probably means that during decode you have a whole bunch of compute sitting idle. I think like
the biggest uh research agenda for taking advantage of that is to say hey can I take a model and uh
make uh the um the MLP much bigger and somehow use those spare flops like 80% of your flops are
sitting idle do anything at all it must be better than doing nothing and and and take advantage of
that um I mean simplest thing to do is just crank up the MLB size by a factor five and and take
advantage of that

>> we're at an age where you see a lot of disagregation right um people were doing uh disagregation
of pre-fill and decode. Initially they were doing on the same chips um doing things like chunk pre-
fill as well. Anything to anything to sort of like get utilization up higher uh then they started
doing disagregated pre-filled decode on different kinds of chips, right? Um at least that's what's
Nvidia's pitch today. Um and then there's sort of like we we you know we've at least built our own
shitty simulator which is internally which probably worse than yours and worse than yours. Um but at
least it's like given us some ideas on like hey actually you would want to you may want to
disagregate the MLP from the attention even right and MLP you could have the weights in let's say
SRAMM or 3D RAM and the attention you want through HPM and this is something that we've also like
sort of like I guess

>> what where do do you see this wave because you're both you know you're making one chip right like
at least my understanding is you're making one chip um there's a wave of like different optimization
points for pre-fill decode um you know s if in a sampling heavy regime versus in a regime where
you're doing a lot of backwards passes. Um

>> yeah I I think I think it's really cool to think about decoupling uh where for example sparse uh
sparsees where you suddenly are decoupling your the amount of math you have to do and the amount of
a kind of effective model capacity for knowledge. Um, and this really affects the hardware in a lot
of ways because now you're not you're not tied together like that anymore. Now you can have much
less arithmetic intensity for the same amount of HBM uh same amount of HPM bandwidth uh for reading
the parameters.

And so decoupling the attention in the the MLP is very interesting because these are very different
operations. uh and if you do put these on different devices uh maybe even like totally different
memory technologies even uh like you're suggesting I think you can have a lot of wins. Uh it is
maybe a little bit scary from the software perspective. Uh now you have to coordinate two different
types of devices. Um who knows what's going to happen there. some of the like the the thing that
makes it scary is you have to decide um somewhat arriori of uh how many resources go on this side
and how many res results has gone that side.

That's true. Um and so uh that ends up baking in this is going to be my ratio of attention to MLB or
toe or something like that. Um and I mean we make those decisions all the time. We pick on resource
balances between memories and and and compute and so on. Um this is one more of them. Um, and it's
sort of like uh I'm sort of doubling all the decisions I make. I make all the decisions on the left
and then I make all the decisions on the right to some and and then I guess the other thing that you
can get like if the the trade-off is it also removes your ability to steal um dynamically uh like uh
uh steal resources between attention and and and and Emily. So uh a classic thing is to um be
fetching always be fetching KBs from HBM. um even while you're running um uh and and then use a
little bit of the HPM bandwidth of het weight or something up like that as well. Um and so uh
sliding away that that that divider is is something you can do on a single chip and it's difficult
to do on multiple chips. As the workloads become more expensive for sure like the um just find every
little part and make the the best thing you can for those little parts seems like a long-term trap.
It's just like when is the right time is is the question. So, one of my pet peeves in quantization
papers is that uh they come out with a claim that says we're 97% as accurate as uh as the full
thing. And turns out if you look into the numbers actually this is like downgrading a 70 billion
model to an 8 billion model. Um how do you think about this?

>> Yeah. What what does accurate even mean? Right? like you take perplexity and it's like one over
97% of complexity or enough

>> or like 97% uh MMLU score or something like that. Yeah, I

>> it's it's 97% of the MMO score once you did post quantization training, you know, that's usually
what they do

>> like you see these companies advertising like these.1% differences on these uh on these emails.
So I mean the problem behind this right is the um exponential or logarithmic relationship between
amount of compute and and like complexity improvement or something like that. Uh so so that's what
gives you all of this sensitivity to those small things. Um why not just hit the same quality with
model parameters? That seems a much fairer weight. So um I think that it should be the standard for
how how you do these things. we in general we find that we need to increase the model size by 40% in
order to hit the same quality level and a better paper would be 35% instead of 45% then yeah makes
sense that the way I like to frame it is perplexity per pjle where if you are the same perplexity
how many pigles how much energy did you take to generate this token

>> per page so if I have twice as many pigles I get twiceity

>> that's not literally division It's a there's a prito there. Okay.

>> What isn't your license plate? Can you tell us your license plate?

>> It's exlop.

>> It's ex flop. Oh, I thought it was intelligence per page or something like this.

>> PJ P R O P. Pikachu's per OP is open.

>> It is open. Oh, wow. PJ per pit too would be pretty good, but that that's too many letters.

