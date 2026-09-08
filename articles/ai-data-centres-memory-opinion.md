# Opinion paper seed — AI data centres and memory

**Status:** Draft insight capture  
**Date:** 2026-09-08  
**Purpose:** Capture the core argument and reader value for a future opinion article focused on AI data centres and memory. This is an editorial framing document, not a change to the canonical memory thesis or watchlist.

## Working premise

**FACT:** McKinsey estimates roughly **$6.7 trillion** of global data-centre investment through 2030, including approximately **$5.2 trillion for AI workloads**.

**FACT:** McKinsey separately estimates more than **$1.7 trillion** of data-centre infrastructure capex excluding IT hardware through 2030.

**FACT:** The IEA reports that capital expenditure by five large technology companies exceeded **$400 billion in 2025** and could rise by roughly **75% in 2026**.

**INTERPRETATION:** The strategic question is therefore not simply how much AI infrastructure is being built, but how much of the installed compute can actually be kept productive.

## Core opinion

**HYPOTHESIS:** We tend to measure AI infrastructure by what we install: megawatts, racks, GPUs, accelerators and data-centre capacity. We should increasingly measure it by **productive compute** — how much useful work the infrastructure can deliver once memory bandwidth, capacity, latency, data movement, power and thermal constraints are taken into account.

**HYPOTHESIS:** Memory is central to this distinction. As accelerators become more powerful, system performance depends increasingly on supplying them with the right data quickly and economically enough to keep them busy. More compute does not automatically translate into proportionally more useful AI capacity if the memory system cannot keep pace.

## Why readers should care

**INTERPRETATION:** The article should give readers a different mental model for thinking about AI data-centre capacity:

> **Installed compute is not the same as useful compute. Memory architecture increasingly determines the gap between the two.**

This matters because trillions of dollars are being committed to AI infrastructure. If memory architecture materially influences accelerator utilisation, power efficiency and workload economics, it is not a narrow semiconductor issue; it is a question about the productivity of one of the largest infrastructure build-outs underway globally.

## Key insights to develop

### 1. Memory is moving from component choice to data-centre architecture

**HYPOTHESIS:** HBM is the most visible part of the shift, but the larger issue is how memory is organised around compute. Bandwidth, capacity, latency, physical proximity and energy cost increasingly need to be considered together.

**HYPOTHESIS:** The future AI data centre is likely to use a hierarchy rather than a single memory technology, potentially combining on-chip SRAM/cache, HBM, conventional DRAM, CXL-attached or pooled memory, and flash/storage tiers according to workload needs.

### 2. Training and inference create different memory problems

**INTERPRETATION:** Frontier training has emphasised bandwidth. Large-scale inference may broaden the constraint toward capacity and economics as model weights, context windows and KV caches grow.

**OPEN QUESTION:** To what extent will the memory architecture optimised for training differ from the architecture that minimises cost per useful inference workload?

### 3. More GPUs do not automatically mean proportionally more useful AI capacity

**HYPOTHESIS:** A facility filled with accelerators that cannot be supplied with data efficiently is an under-utilised capital asset. The relevant measure of capacity therefore shifts from accelerator count toward how effectively compute, memory and interconnect operate as a system.

### 4. Memory architecture affects power and cooling economics

**FACT:** Moving data consumes energy, and memory density/proximity contribute to package and rack thermal challenges.

**INTERPRETATION:** As data centres become increasingly power constrained, the energy cost of moving and storing data becomes part of infrastructure economics rather than an isolated chip-design concern.

### 5. HBM scaling creates manufacturing-system constraints

**FACT:** HBM4 and later generations increase complexity in stacking, bonding, logic base dies, packaging, testing, yield and thermals.

**INTERPRETATION:** Increasing nominal DRAM capacity does not automatically produce usable HBM capacity if downstream manufacturing steps remain constrained. The memory roadmap is therefore increasingly intertwined with advanced packaging and manufacturing capability.

### 6. The strategic question changes

Instead of asking only **"How many accelerators can we deploy?"**, infrastructure leaders should increasingly ask:

- How much of that compute can we keep productive?
- Which workloads are bandwidth constrained versus capacity constrained?
- Which workloads genuinely require HBM?
- Where can slower or lower-power memory tiers improve economics?
- How much energy is spent moving data rather than computing on it?
- At what point does improving the memory system deliver more value than adding another accelerator?

## Potential audience

The article should be readable beyond memory specialists and useful to:

- data-centre and AI-infrastructure leaders;
- semiconductor and systems executives;
- enterprise technology leaders planning large-scale AI deployments;
- strategy leaders thinking about AI capex and utilisation;
- technically curious executives and analysts following the AI infrastructure build-out.

The intended reader takeaway is not "HBM demand is growing." It is:

> **The industry may be using the wrong unit of AI capacity. Installed compute is easy to count; productive compute is what matters, and memory increasingly determines the difference.**

## Potential framing / title

**We Are Building AI Data Centres Around Compute. Memory May Decide How Useful They Are.**

Alternative:

**We Measure AI Data Centres by Compute. We May Be Measuring the Wrong Thing.**

## Sources

- McKinsey, *The $7 trillion data center build-out: How industrials can capture their share* — https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-7-trillion-dollar-data-center-build-out-how-industrials-can-capture-their-share
- McKinsey, *Scaling bigger, faster, cheaper data centers with smarter designs* — https://www.mckinsey.com/industries/private-capital/our-insights/scaling-bigger-faster-cheaper-data-centers-with-smarter-designs
- IEA, *Key questions on energy and AI — Executive summary* — https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
- Existing HBM manufacturing, packaging, testing and thermal evidence is preserved in `sources/source-register.md` and the canonical files under `research/memory/`.

These figures and interpretations should be revalidated against the latest available sources immediately before publication.
