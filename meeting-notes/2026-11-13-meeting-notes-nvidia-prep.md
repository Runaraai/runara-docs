---
title: Meeting notes Nvidia prep
date: 2026-11-13
time: 11:00 PST
attendees: Abhinaya Krishnamoorthy, Adam Tachner, Alon Konchitsky, Oz Nakash
source_id: 1JXKLbVBwQsSf5oesXphb0lA5HwJq-bAs4F270dgjC8w
---
## 

## **Nvidia prep**

Nov 13, 2026  
[Adam Tachner](mailto:adam@runara.ai) [oznakash@gmail.com](mailto:oznakash@gmail.com) [Oz Nakash](mailto:oz@runara.ai) [Alon Konchitsky](mailto:alon@runara.ai)

Hardware strategy review outlined heterogeneous inference setups and business models for Nvidia partnership and capital efficiency.

## **Document structure and strategic memo layout**

* Organize the pitch document into 5 main tabs with an executive summary at the top.  
* Include the AMD memo to highlight solution heterogeneity and create competitive market urgency.

## **Heterogeneous compute architecture and performance advantages**

* Pair new GPUs like H200 or B200 with older models like L40S, RTX 6000, or A100.  
* Demonstrate segregated prefill and decode or speculative execution across interconnected rack setups.  
* Achieve 2 to 5 times lower price per token and improved overall system throughput.  
* Leverage existing hardware entirely through software solutions instead of requiring alternative custom hardware.  
* Utilize an optimal balance of memory bandwidth, compute, and networking to make NVLink highly effective.

## **Business model and partnership execution plan**

* Target a business model where Nvidia supports building heterogeneous server configurations or trusted vendor partnerships.  
* Secure access to custom server racks or hardware trials to prove system capabilities on day one.  
* Require approximately \$25 million in capital to lease or purchase hardware equivalent to a \$250 million investment.  
* Define immediate, medium, and long-term milestones for optimizing existing GPU hardware performance.

## **Next steps**

- [ ] \[Oz Nakash\] Send the analysis: completed by oz to illustrate the heterogeneous compute market direction for review.  
- [ ] \[Unassigned\] Create an internal design plan: outlining the strategic path and requirement asks for the team.

**Want to see more?** [View the full notes]()  
Tip: You can always access your full notes from the left sidebar.

*You should review Gemini's notes to make sure they're accurate. [Get tips and learn how Gemini takes notes](https://support.google.com/meet/answer/14754931)*  
Nov 13, 2026

## **Nvidia prep**

Invited [Adam Tachner](mailto:adam@runara.ai) [oznakash@gmail.com](mailto:oznakash@gmail.com) [Oz Nakash](mailto:oz@runara.ai) [Alon Konchitsky](mailto:alon@runara.ai)

Attachments [Nvidia prep](https://calendar.google.com/calendar/event?eid=NjRxM2VwMWs2dGhqOGI5amM1aTNjYjlrY2txamliOXBjNHJqMGJiMmNvczMwYzltNmNwamNkYjI2YyBhbG9uQHJ1bmFyYS5haQ)

Meeting records [Transcript](https://docs.google.com/document/d/1JXKLbVBwQsSf5oesXphb0lA5HwJq-bAs4F270dgjC8w/edit?usp=drive_web&tab=t.i9porw6asasd) 

### **Summary**

Hardware strategy review outlined heterogeneous inference setups and business models for Nvidia partnership and capital efficiency.

**Heterogeneous Inference Setup Overview**  
Heterogeneous setups pairing old and new GPUs achieve massive cost reductions and performance increases. Software-based approaches eliminate the need for hardware integration from competitors.

**Business Model and Partnership**  
Hybrid servers represent optimal use of Nvidia hardware requiring direct support. Strategy encapsulates heterogeneous compute entirely within the ecosystem rather than pushing customers to external vendors.

**Pitch Strategy and Implementation**  
Demonstrating high-leverage inference compute lowers costs using purely Nvidia technology. Immediate optimization provides performance gains for enterprise customers while advancing toward custom configurations.

### **Decisions**

## Aligned

* **Establishment of document tab structure** The document structure will consist of six specific tabs, including an executive summary, Neotron 3.5, Lightning 30B, Renara versus Fireworks together, base 10, and an AMD memo.

### **Next steps**

- [ ] \[Oz Nakash\] Send the analysis: completed by o to illustrate the heterogeneous compute market direction for review.

- [ ] \[Unassigned\] Create an internal design plan: outlining the strategic path and requirement asks for the team.

### **Details**

**Document Structure and Tab Organization**: Adam Tachner outlined the organization of the meeting document, specifying that it will contain an executive summary at the top followed by five specific tabs: Neotron 3.5, Lightning 30B, the Renara and Fireworks combination, base 10, and a sixth tab dedicated to the AMD memo. Oz Nakash requested a review of the overview expectations to ensure accurate note-taking.

---

**AMD Memo and Heterogeneous Inference Setup**: Adam Tachner explained that the AMD memo is included to highlight solution heterogeneity and create FOMO regarding an intentional collaboration with AMD. Alon detailed a heterogeneous setup utilizing a fast or new GPU paired with an old GPU (such as an H200 or B200 combined with an L40S or RTX 6000\) on the same rack or interconnected nodes to demonstrate segregated prefill and decode, or speculative prefill and decode. Alon predicted this setup would achieve a two to five times reduction in cost and increase performance by three to four hundred percent ([00:01:07](#00:01:07)). Oz Nakash added that this approach provides massive acceleration using older, slower hardware alongside fast GPUs, and expressed willingness to demonstrate this on any models, including frontier models ([00:03:23](#00:03:23)).

---

**Hardware Limitations, Software Solutions, and Neotron Integration**: Oz Nakash noted that they lack direct control over client data center racks, but previous tests over slow peripheral component interconnect connections showed very strong performance, indicating high confidence in the approach. Oz Nakash pointed out that this software-based approach eliminates the need for competitors like Apple, ARM, or Matrix to integrate hardware solutions ([00:06:16](#00:06:16)). Additionally, Oz Nakash mentioned that they plan to request addition to the list of Neotron providers after proving their performance, a timing supported by Adam Tachner to ensure proof precedes the request ([00:07:31](#00:07:31)).

---

**Proposed Business Model and Nvidia Partnership**: Adam Tachner stated the primary goal is to propose that hybrid servers represent the best use of Nvidia hardware, with the intent to build a business around them requiring Nvidia's direct support or connection to a trusted partner ([00:08:37](#00:08:37)). Adam Tachner argued that NVLink is powerful but often overkill, and maximum advantage can be taken with less expensive systems if there is an optimal balance of memory bandwidth, compute, and networking ([00:09:51](#00:09:51)). Oz Nakash and Adam Tachner agreed that while this strategy involves encouraging Nvidia to support more cost-effective configurations, it uniquely encapsulates heterogeneous compute entirely within Nvidia's ecosystem rather than pushing customers to external vendors like ARM or Apple ([00:11:13](#00:11:13)).

---

**Hardware Configuration, Architecture, and Capital Considerations**: Adam Tachner described the strategy as creating a new hardware architecture through a specific combination of chips in close proximity without needing to design a new chip, seeking a capital-light way to build the business ([00:15:24](#00:15:24)). Subas joined the discussion as Oz Nakash detailed a model using four nodes of older compute (such as the RTX 6000\) and four nodes of newer compute (such as the B200) connected via fast networking to test software optimizations ([00:16:42](#00:16:42)). Oz Nakash estimated that approximately twenty-five million dollars in capital would be required to lease or purchase hardware equivalent to a two-hundred-fifty-million-dollar investment ([00:17:48](#00:17:48)). Adam Tachner acknowledged that substantial capital is needed for hardware and leasing, making a proof of concept essential for subsequent fundraising ([00:20:43](#00:20:43)).

---

**Refined Pitch Strategy and Client Introductions**: Adam Tachner summarized the pitch to Nvidia: demonstrating a higher-leverage inference compute approach that lowers inference costs by five to ten times using purely Nvidia technology, while requesting access to heterogeneous systems or a partner with credit ([00:22:13](#00:22:13)). Oz Nakash suggested based on internal feedback that they should avoid directly asking Nvidia for capital, recommending instead that they ask for introductions to data center clients or labs to prove performance improvements on existing hardware ([00:23:37](#00:23:37)).

---

**Value Propositions and Phased Implementation Strategy**: Oz Nakash emphasized the importance of presenting an immediate, medium, and long-term vision to Michael and the team, rather than focusing solely on distant goals. Adam Tachner and Oz Nakash agreed that the immediate term can involve optimizing existing Blackwell or other hardware to provide immediate inference performance gains for enterprise customers and neoclouds, while advancing toward custom configurations ([00:26:19](#00:26:19)).

*You should review Gemini's notes to make sure they're accurate. [Get tips and learn how Gemini takes notes](https://support.google.com/meet/answer/14754931)*

*How is the quality of **these specific notes?** [Take a short survey](https://google.qualtrics.com/jfe/form/SV_5bXzKQfylMIhSXc?confid=WfTXbLb1ODiw4CBcU-ZoDxIQOAIIigIgABgDCA&detailLevel=standard&hasImages=False&entryPoint=footerMain&isGoogler=False&lang=en-US) to let us know your feedback, including how helpful the notes were for your needs.*

Nov 13, 2026

## **Nvidia prep \- Transcript**

### **00:00:00**

**Adam Tachner:** that would be a super valuable thing for you. And so,

**Oz Nakash:** Right.

**Adam Tachner:** so that should all be covered in the in the upfront summary menu meu and um memo. And instead of calling it summary, let's call it uh executive summary, I guess.

**Oz Nakash:** Adam, just for the note takingaking, apologize I didn't turn it on. Uh, can you repeat the kind of overview what is expected? So, we will we will have it as well.

**Adam Tachner:** Yeah, absolutely. But I think Abby started recording about 20 minutes ago on her phone. So So um but but um but I think

**Oz Nakash:** I'm taking notes on my phone though.

**Adam Tachner:** that so so so what you want to do is uh we're going to have five tabs in the document. We're going to have an executive summary at the top. Then we're gonna have Neotron 3.5, Lightning 30B. And then the Renara versus Fireworks together and base 10\. And then no, the sixth tab is we're also going to include the AMD memo.

### **00:01:07** {#00:01:07}

**Adam Tachner:** And um and we're going to include the AMD memo for two reasons. one is to highlight the heterogeneity uh of our solution and the other is to create a little bit of FOMO. We want them to think that we're actually working with AMD and it's our intention to do so. Um, as for um a paragraph in the executive sum summary that gets to the specifics of how we can divide up the the the inference problem. I'll let Alon summarize that again um for the transcript. So can you say again Alon what it is that we're trying to prove to them in terms of our ability to divide up the workload across heterogeneous devices. is

**Oz Nakash:** Yes. So I recommend to do hogrogenous um setup which would be for example um like a fast GPU or a new GPU with an old GPU and that could be either when they are on the same wreck so two nodes like let's say one um H200 and one one node of H200 or or or B200 and one node of um let's say L40S or RTX 6000 any any of them where we demonstrate that we can do segregated um prefill and decode um or Um we demonstrate like speculative either prefill or decode on those two and we accelerate the the tokens or or we reduce dramatically the price or we get like three 400% more performance from the from the setup which is um just by

### **00:03:23** {#00:03:23}

**Oz Nakash:** using a kind of an old slow GPU um in addition to the to the fast GPU and and and we are happy to request this setup maybe two nodes or or or two Rex whatever they wanted to give us and we'll demonstrate it on on on any models that they choose to and and we are even open to do that on the frontier models. So if the frontier models would want to go to somebody like Dimatrix or Apple or ARM and and Nvidia were willing to show to Nvidia that that's something that we can do

**Adam Tachner:** Excellent.

**Oz Nakash:** even only on Nvidia hardware. So they don't need to go to other hardware to get such a performance.

**Adam Tachner:** And um and can you articulate with any specificity technically speaking what it is that we'll be able to show them in terms of a cost or performance advantage on those heter those proposed heterogeneous servers? In other words, can you predict how advantageous that will Okay.

**Oz Nakash:** Yes, I believe that that would be between like a two to five times cheaper if we do so.

### **00:04:58**

**Oz Nakash:** So, for example, if we team up with a B, if we're teaming up with a B200 or H200, a much cheaper and older and less powerful compute like L40S or maybe the RTX 6000 or or or or maybe even the A100. we we will we will get between two to five times better price per token and better throughput.

**Adam Tachner:** Got it.

**Oz Nakash:** I will I will just interject a quick question. Does one of the graph indicates that type of like 5x 7x that we're sending? Like do we have a graph that shows that? So we were able to demonstrate. I don't remember if we got so much. I think we got the because the first uh the connection was not so we cannot tell truly like the exact numbers that we can get because that that's the actual ask like we want those to be in the same rack. So what do we need? So what what do we need to have in order to do so? Yeah. Either on the same rack okay or two racks that are interconnected very fast.

### **00:06:16** {#00:06:16}

**Oz Nakash:** Yeah. So we cannot we do not have control to those racks because that is in their data centers. And by the way, Adam, like do we have maybe it's a thought for but but one moment that that's the prediction and and we have actually tried with the same hardware. So even over PCI which is pretty slow connection we have got very very good performance. So we are pretty confident that we can do that if they give us this the thing and again the the idea is that the competition like Apple or ARM or the matrix or anyone else would not need to go and and integrate everything in the hardware side. The idea is that everything could be solved on just software with all inclusive Nvidia hardware. They don't need to go and try to find something else to do that. And I think that we should also state one or two notes on the on the on on on this SRAMM move. I think that there's no need to run to rush into SRAMM right now.

### **00:07:31** {#00:07:31}

**Oz Nakash:** And this is another direction that we would like to to explore if they would be interested. So maybe that would be another request if we wanted to to ask for that. And one more ask like unrelated to this but uh since we have been deploying these neatron models and comparing them and we have better performance than few of the providers do we intend to uh request them to add us to their list of neatron providers? Yes. Yeah. I'm sure that they will add us after we show them, but um this is something that we'll ask later. That's a because if we ask from the beginning, they wouldn't they wouldn't want we need to prove something

**Adam Tachner:** But but let's be clear though this is a really important question Naj is asking be what we we need to come to them with sort of a what I would call a target business model where we need their support right so The I think that the the big request is we propose to prove to you that these hybrid servers are the best possible use of your hardware.

### **00:08:37** {#00:08:37}

**Adam Tachner:** Um, we want to build a business actually out of building those and we either want Nvidia's direct support to do that or for you to hook us up with a a vendor you trust that can become our partner to build these out. Because what could happen quite readily is they could end up just saying, "Oh, this is great. Yeah, we'll take this new configuration and we'll start selling it to everybody. Thanks for the idea." Now, obviously, if they don't have our software and our insight, they can't do that, right? So, we want to give them a path for basically releasing that energy. Does that make sense?

**Oz Nakash:** Yes. Yeah.

**Adam Tachner:** Okay. All right. Yeah, that sounds good.

**Oz Nakash:** And remember and remember Michael came from the connectivity from the Melanox opportunity. So he's a he's extra motivated to show that the connectivity is very important. So, and that's what we're asking. We're actually asking him, you know, give us just a one of your connectivities between one node to another or between one rack to another.

### **00:09:51** {#00:09:51}

**Oz Nakash:** And that's because currently it's not the bottleneck, right? The connectivity is not the bottleneck. The connectivity is the bottleneck because we were not able to access two two nodes, you know, two two just computers that sit one by another. Even GCP is not willing to give us this access for us. I'm saying like from performance perspective, it's not necessarily the bottleneck. No, no, it's not. If you have a fast connection, that's not the bottleneck.

**Adam Tachner:** I yeah I I I think we have to figure out the right way to express this and probably then capture it in the executive summary. I think that the right way to put it is something like having all this envy link is great, but the truth is it's overkill. The envy link is so valuable if you have the right balance of networking and compute. We can take maximum advantage with far less expensive systems if we have just enough of the NVLink. So our point is that NVLink is more powerful than Nvidia realizes. We can unleash the power of NVLink in the by providing a system with the optimal balance of memory bandwidth, compute and networking.

### **00:11:13** {#00:11:13}

**Adam Tachner:** The truth is we don't need that much networking because it's so powerful. You see my point? I mean, you have to be really careful here because what we're really telling them to do is sell more cheaper stuff. You'll get more juice out of these older lemons uh if you work with our stuff. And that's a dangerous prospect because it means they don't have to sell as much of the advanced stuff. But um but we can bring a lot of, you know, value to their customers. So I think that's why we have to champion a business model where we actually prove this out and then it becomes something more interesting more broadly. Am I correct alone that with that characterization and am I also correct that the only way to really take advantage of this architecture is with our software or can anybody do

**Oz Nakash:** So if everybody can do it, I I I don't know if if if everybody could have done it, they would probably have done it. They had many years to do it and and there has been yes so many years to do that and nobody has done it.

### **00:12:24**

**Oz Nakash:** That's one. two um we're not telling them to sell less expensive. We're not telling them that they would reduce their sales quantity of the expensive GPUs. We're telling them that they are spending a lot of efforts and a lot of time on trying to bring these weak secondary solutions like ARM, Apple, Datrix and everybody else to be these weak hardware to to do the speculative workload and and what we're really offering them is hyrogenous compute which is all encapsulated within

**Adam Tachner:** Ah,

**Oz Nakash:** Nvidia because they are spending so much money

**Adam Tachner:** I get it. Yeah, that's great.

**Oz Nakash:** and so much efforts onrogenous compute this is what gave Gim like \$350 million that's what gave Dimatrix so much money that's what gave so so many you know different parties out there that that that's what they are saying so let and and there's no need to to buy it from Nvidia because they do have all these hardware already. So let me see if I understand correctly. Basically it allows if if someone or you know any kind of an enterprise or data center they want like currently they are looking to buy not a tradenous just like one type of the Nvidia models because working will degrade the performance and we are actually allowing to utilize and to to use it better.

### **00:14:12**

**Oz Nakash:** No, it wouldn't degrade. We are offering an hetrogenous without without rea degraded performance for inference. No, without an era they don't do hetrogenous usually. They don't do it at all. I I know that's what I'm saying. So we are allowing them to do so with our solution or not? Yes. Is this what we're doing? Yes. Okay. And Adam, is is this point clicked to you as well?

**Adam Tachner:** Yes. Uh, absolutely. In fact, it's something I've been talking about in my meetings with the VCs. I'm basically telling them, look, I'm pretty sure that we have a unique advantage, excuse me, with a with a configuration of hardware that doesn't exist right now. And the reason it doesn't exist is because nobody really understands how to make this hardware work together. And unless you have actual server scale proximity, um it's a hard thing to do. So basically what we're offering to do is create a new hardware architecture without creating a new chip, right?

### **00:15:24** {#00:15:24}

**Adam Tachner:** It's just a combination of chips in the right proximity in a server or in a in in a rack. Um, and we're looking for the most capital light way of actually building that business. It's complimementaryary to the core of what we're doing. It's not a substitute, but it's actually the best way to monetize our ideas because we'll basically have a proprietary hardware advantage for, you know, for our software. So yeah, I I get it completely and it's something I've been dancing around, but obviously it's the first time we'll be able to pitch it to someone who could easily resource the idea um and they could invest in us or whatever. But yeah, I think if we have if we truly have the secret sauce that enables this architecture to work, then um it will be very easy to fund this business. If we can get them to support us with a, you know, or or introduce us to a partner, it could be Dell or Super Micro that'll basically build these systems for us. Make sense?

**Oz Nakash:** The system has the systems has been built.

### **00:16:42** {#00:16:42}

**Oz Nakash:** And by the way, Subas just got into the room and we're we're just talking about this model of how to take like older compute and and newer compute. let's say the RTX 6000 and the maybe the B200 and we do like any speculative either peripheral at the code or or segregated together but what we're trying to do is we would like to take let's say four nodes from from this one four nodes from this one we assume that they are super fastly connected in the same rack or through envink or whatever it is and we're trying to run models that are having these two. But what we would like to do is to model that out. We say we have four of those. We pay like 100,000 for this. We have four of those. We pay 100,000 for these. They are fastly connected. How we can do some some of our software or or or tricks to to do that. So that's that's where we stopped. And and Adam, I think that's that's correct.

### **00:17:48** {#00:17:48}

**Oz Nakash:** Um may maybe we can um maybe we can even tell them that we are willing to um to design something like this. We don't need to we just say spec what do we want and and maybe they will again they don't need to build something special. They just take the exact same box that we have here you know on on the ground and and we connect it to another box and that's all. May maybe they would be willing to kind of loan us

**Adam Tachner:** Well,

**Oz Nakash:** or give

**Adam Tachner:** let me so let me ask you this question. If we weren't having this meeting with Nvidia and we were just saying all right this is gonna be our business plan is going to be basically providing inference using this special configuration of the systems. Then what we would do is go out and raise enough money to buy these systems to prove it out. We would source the hardware and then we would build from there. Correct.

**Oz Nakash:** Um yes yes yes but but I don't think that that's something that would you know I don't think that we need to spend a lot of money to do that you know for example um if we if we maybe uh spend um I think it wouldn't be more than than 20 or \$25 million and and and we could really get such a such a you know hardware either leased or or or purchased.

### **00:19:24**

**Oz Nakash:** I think that that would enable like um 200 like a comparable of \$250 million equivalent computer investment in computer in hardware at that rate. So I think that if we had this like um maybe \$25 million to to do that and I I think that that would be again that that would open that would be the holy grail heterogeneous compute that everybody is trying to to prove like parasale and and again I'll send you the the analysis that o did it's exactly that way and gimlet exactly the Everybody is going this direction. They're saying we want a lot of money because we are going to enable like a heterogeneous compute but they do that with like let's say Nvidia and Datrix or Nvidia and and maybe

**Adam Tachner:** Right.

**Oz Nakash:** Apple.

**Adam Tachner:** Right.

**Oz Nakash:** We we can go to Apple and tell them we can do that for you and and and we give you the the blueprint and the software to do that.

**Adam Tachner:** Right.

**Oz Nakash:** And I think that would be very very impressive. But we do need to get the hardware.

### **00:20:43** {#00:20:43}

**Oz Nakash:** We were not even able to get it even when we are paying for it to GCP or others. They're not willing to to give us this this you know this trial.

**Adam Tachner:** Right.

**Oz Nakash:** But yes,

**Adam Tachner:** Yeah.

**Oz Nakash:** that's a that's something that is very very powerful.

**Adam Tachner:** Yeah, it makes sense. Yes. So, we'd need the problem is we'd need the money uh not only to buy the harbor, but we'd also need the money to lease the and so you need a pretty substantial amount of capital even to do this at a modern. So basically what we're asking for is just sufficient proof of concept that would allow us to then go out and raise the capital necessary to build a new to build a new fireworks that uh provides this leverage and superior performance.

**Oz Nakash:** You're fragmented. We cannot hear you. Yeah, Adam, we cannot hear you.

**Adam Tachner:** Sorry about that. I got in my car, but I was Can you hear me?

**Oz Nakash:** Yeah, we're losing you.

### **00:22:13** {#00:22:13}

**Oz Nakash:** It's been sound static.

**Adam Tachner:** Guys, can you hear me? Oh, sorry.

**Oz Nakash:** I think now it's coming back.

**Adam Tachner:** Okay, good. Sorry about that. Yeah, I got in my car. So just to summarize just to summarize then the the the pitch to Nvidia and frankly there's an argument to be made the pitch to VCs as well but but we'll get there is we basically have this much higher leverage approach to um to to inference compute. Um we think we can effectively drive down the cost of compute by five or 10x for inference. Um the attractive thing for Nvidia is that we can do it using purely Nvidia technology. They don't have to cross to other vendors. Um but if if they don't support us, then we could do that too. So there's a threat there, which is good. And um and basically we just need them to give us access to these heterogeneous systems or point us to a vendor who can give us access to them with credit so that we don't have to because we don't have a lot of money and and then we can prove this out and then we'll scale it up from there and go out and raise money and if Nvidia wants to invest that's great.

### **00:23:37** {#00:23:37}

**Adam Tachner:** I think that's it in a nutshell, right?

**Oz Nakash:** Right. Although we heard from internal people at Nvidia that is better not to ask them for capital because every time somebody is asking for capital they are they are kind of pushing back. So I think that we should just say

**Adam Tachner:** It's fine. Yeah, I agree. Yeah, that sounds good.

**Oz Nakash:** Okay. So it sounds to me like there is a good plan for the introgenius but um like for let's say for example if they will introduce us like the other kind of um the other avenue if they will introduce us to one of their companies clients that they have data center what can we prove day one that the performance is higher like what I feel is that When we are defining what is the ask, we need to think about it properly before the meeting of course and and list it out. But maybe we can one of the ask will be that if they can introduce us to one of their potential clients that they have a lab or or do it in their own lab and show that the performance for each type of a equipment like hardware is already going high.

### **00:24:54**

**Oz Nakash:** So day one even without like too much of a development we can bring the benefit on

**Adam Tachner:** So, um, so let me see if I understand what you're asking. Um, I I think I I think that your question sort of gets to the heart of the struggle that we've been having in that we we know we can do great things with any sort of compute that we have access to, but we've had access to very little compute. And so if they wanted to introduce us to a data center partner or whatever that was setting aside this sort of custom server rack configuration just setting that aside for the moment then

**Oz Nakash:** Exactly. Yeah.

**Adam Tachner:** we could then then we could certainly use our technologies to prove that we can do more with what they have. We can squee we can squeeze more juice out of any lemon, right?

**Oz Nakash:** that our control plane can do this. Yes.

**Adam Tachner:** Exactly. Um but the real advantage would come from a from a con custom configuration that would allow us to basically get just the right ratio of of networking memory bandwidth and compute and and then and the good news is that actually drives down the cost.

### **00:26:19** {#00:26:19}

**Adam Tachner:** Now, we we actually think that this level of thinking could end up driving Nvidia to build different chips, right? And Michael will probably figure that out, but that'll be a separate level of the conversation. But to answer your question, Oz, I I agree. I think that there's um it's very easy for us to say, yeah, in the meantime, we intend to work with anybody who needs compute. enterprise customers, we've developed a solution for them. those who are selling compute like Neoclouds certainly we can make their stuff more productive and easier to run different combinations of hardware and workloads etc etc right so there's there's a value proposition for for each of these guys uh but there's but

**Oz Nakash:** Exactly. So I would love exactly.

**Adam Tachner:** there's an ideal value proposition that we're trying to get to as quickly as possible

**Oz Nakash:** So the way I'm thinking about it is like from this meeting I want Michael and the team to have kind of a vision of what can we offer immediate term, medium-term and long term. So it's not like coming with oh that's a good idea for 2028\.

### **00:27:26**

**Adam Tachner:** Yeah.

**Oz Nakash:** I want something that tomorrow morning they can implement or do something right away like and and just a thought again I don't know what you think about it but if we're proving that

**Adam Tachner:** Yeah.

**Oz Nakash:** they're giving us any blackwell or any kind of hardware and we can optimize and and squeeze more juice right away tomorrow morning maybe they can pair it and sell it.

**Adam Tachner:** Right.

**Oz Nakash:** Hey guys, now go work with Ranera because it will allow you to get more inference right away.

**Adam Tachner:** Yeah, I I I agree. We just have to make sure they understand that, like you said, there's a there's good and then there's better and here's better and here's best, right?

**Oz Nakash:** Exactly.

**Adam Tachner:** And and and they could do all three of those as quickly as possible. It's a question of how quickly they're willing to move.

**Oz Nakash:** I agree. I agree.

**Adam Tachner:** Yeah.

**Oz Nakash:** So um we need to come up with internal definition kind of a design plan of what we see the path and what is our asks as well for from you know from them.

**Adam Tachner:** Yeah. Yeah. Okay, that sounds good.

**Oz Nakash:** Perfect. Thank you very much.

**Adam Tachner:** All right. Thanks.

**Oz Nakash:** Thank you.

**Adam Tachner:** Thanks, guys. I'll see you a little bit later.

**Oz Nakash:** Thanks everyone. Bye-bye.

**Adam Tachner:** Bye.

### **Transcription ended after 00:28:51**

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*
