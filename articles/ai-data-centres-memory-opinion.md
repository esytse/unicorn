# We Are Building AI Data Centres Around Compute. Memory May Decide How Useful They Are.

**Status:** Draft opinion article  
**Date:** 2026-09-08  
**Editorial frame:** AI data-centre productivity through the lens of memory architecture. This article does not alter the canonical memory thesis, rankings or watchlist.

The artificial intelligence boom is rapidly becoming an infrastructure boom.

By the end of the decade, trillions of dollars are expected to be spent on data centres, much of it to support AI. The visible markers of this expansion are familiar: new campuses, larger power commitments, denser racks and an extraordinary appetite for accelerators.

The industry has consequently developed a fairly simple shorthand for AI capacity. More megawatts, more GPUs and more racks generally mean more compute.

That is increasingly an incomplete way of looking at it.

The more powerful processors become, the more their performance depends on something less glamorous: getting enough data to them, quickly enough, to keep them busy. A processor capable of performing enormous numbers of calculations is of limited use if it spends too much of its time waiting for information to arrive.

This is why memory is moving towards the centre of the AI infrastructure problem.

High-bandwidth memory, or HBM, has become one of the most visible beneficiaries of the AI boom precisely because it addresses this problem. By placing large amounts of extremely fast memory close to an accelerator, HBM allows data to move at rates conventional memory architectures struggle to sustain.

But focusing on HBM demand alone risks missing the more important shift.

The question is no longer simply how much memory an accelerator contains. It is how memory is organised around compute, how quickly data can move through the system, how much energy that movement consumes and how the architecture changes as workloads move from training frontier models to serving them at enormous scale.

In other words, the AI data centre is beginning to look as much like a memory architecture problem as a compute problem.

This matters because the industry is making very large capital commitments on the assumption that installed compute translates into useful capacity. Those two things are not necessarily the same.

A data centre containing tens of thousands of accelerators is an impressive asset. But its economic value ultimately depends on how productively those accelerators can be used. Memory bandwidth, memory capacity, interconnect, power and thermal limits all influence that utilisation.

The distinction becomes particularly important as AI shifts increasingly towards inference.

Training the largest models has placed huge emphasis on memory bandwidth. Large numbers of accelerators must exchange and process vast quantities of data, which has helped make HBM an essential part of leading AI systems.

Inference introduces a somewhat different problem.

The model still has to be held somewhere. Longer context windows increase memory requirements. KV caches grow as conversations and workloads become more complex. Serving millions of users places greater pressure on cost per query and energy consumption.

For some workloads, maximum bandwidth will remain critical. For others, memory capacity and cost may matter just as much.

That makes it increasingly unlikely that the future AI data centre will be built around a single memory technology.

A more plausible outcome is a hierarchy. The fastest and most frequently accessed data sits closest to the processor, in cache and HBM. Larger pools of conventional DRAM provide capacity further away. Technologies such as CXL may allow memory to be expanded, pooled or shared more flexibly across systems. Flash and other slower tiers can absorb data that does not need to live permanently beside the accelerator.

None of these technologies replaces the others. Their importance depends on the workload.

That is a significant change in how data-centre architecture should be thought about. Memory stops being something selected after the processor and becomes something that helps determine the architecture around it.

It also brings memory into areas that would traditionally have been treated as separate engineering disciplines.

Power is one.

Moving data consumes energy. As AI clusters grow larger, the energy required to move information between memory and processors, across packages and eventually across racks becomes increasingly relevant. When electricity and grid access are already constraints on new data-centre capacity, wasting power moving data unnecessarily becomes an infrastructure problem, not merely a chip-design problem.

Cooling is another.

Putting more compute and memory into increasingly dense packages raises the thermal load that must be managed. HBM itself is becoming more complex as stacks become taller, dies thinner and integration with accelerator logic tighter. The manufacturing challenge therefore extends into packaging, bonding, test, yield and thermal management.

This is one reason simply increasing semiconductor capacity does not guarantee that usable AI capacity rises at the same rate.

Memory has to be fabricated, stacked, bonded, tested and integrated. Advanced packages have to yield reliably. The final system has to dissipate heat. Power has to reach it. Data has to move through it efficiently.

Improving one part of this chain often reveals the next constraint.

That dynamic is easy to overlook because the industry naturally focuses on the most visible scarcity. For several years, that has been accelerators. It may continue to be so in important parts of the market.

But bottlenecks move.

Once enough compute is available, the next question is whether it can be fed. Once memory bandwidth increases, capacity may become the constraint. Once memory capacity expands, interconnect or power may matter more. Increasing rack density can then move the problem into cooling.

The danger is therefore to confuse the thing being installed with the thing creating useful capacity.

This matters well beyond semiconductor design.

For companies building AI infrastructure, it suggests that accelerator count is an increasingly crude measure of capability. A better measure is productive compute: the amount of useful work a system can deliver after memory, networking, power and thermal constraints are taken into account.

For enterprises buying AI capacity, it means headline hardware specifications may tell less about economics than utilisation and workload architecture. The cheapest system will not necessarily be the one with the cheapest processor, nor the fastest system the one containing the most expensive accelerator.

And for the wider technology industry, it points towards a change in where engineering effort will need to go.

The first phase of generative AI was dominated by the question of whether enough compute could be assembled to train increasingly powerful models. The next phase is likely to be more concerned with making that infrastructure efficient enough to operate at very large scale.

Memory sits directly in the middle of that transition.

We are spending extraordinary sums building AI data centres. It would be a mistake to measure the success of that build-out simply by counting the accelerators going into them.

The more important question is how much of that compute can actually be kept productive.

Memory may increasingly determine the answer.

---

## Source notes for editorial validation

- McKinsey, *The $7 trillion data center build-out: How industrials can capture their share* — estimates roughly $6.7tn of global data-centre investment through 2030, including approximately $5.2tn for AI workloads.
- McKinsey, *Scaling bigger, faster, cheaper data centers with smarter designs* — estimates more than $1.7tn of data-centre infrastructure capex excluding IT hardware through 2030.
- IEA, *Key questions on energy and AI — Executive summary* — reports that capex by five large technology companies exceeded $400bn in 2025 and could rise by roughly 75% in 2026.
- Existing HBM manufacturing, packaging, testing, thermal and interface evidence is preserved in `sources/source-register.md` and the canonical files under `research/memory/`.

External figures and time-sensitive claims should be revalidated immediately before publication.