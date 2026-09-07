# Transmission Deliverability & Large-Load Interconnection — Bottleneck Deep Dive

**Status:** Gate A validated for physical transmission deliverability; interconnection-process friction treated separately  
**Bottleneck Strength:** **4.7 / 5 physical transmission deliverability**; **4.2 / 5 current process / queue friction**  
**Confidence:** **High** on transmission need; **Medium** on persistence of process friction after reform; **Medium** on supplier-level economic capture  
**Last substantive update:** 2026-09-07  
**Backlog:** issue #38

## Executive conclusion

**CONCLUSION:** AI/data-centre growth is creating a genuine structural bottleneck in **transmission deliverability** — the ability to move sufficient power to a specific region / substation / site while maintaining reliability.

However, the current large-load interconnection problem contains two very different things:

1. **physical scarcity** — insufficient transmission capacity, congestion, substation capacity, generation adequacy and equipment;
2. **process scarcity** — study queues, tariff design, cost allocation, duplicative requests and legacy procedures that were not designed for hundreds-of-megawatts / gigawatt-class loads.

The first is structural and passes Gate A at **4.7/5**. The second is real today but much more vulnerable to regulatory reform, flexible service, co-location and demand-screening; it therefore scores **4.2/5 as a current system friction**, not as a durable merchant moat.

The crucial investment implication is:

> **The queue itself is not the profit pool. The likely profit pools are the physical solutions required when credible load survives the queue: transmission construction, grid equipment, advanced conductors / grid-enhancing technologies, substations and sometimes behind-the-meter generation.**

---

## 1. Why transmission matters

A power system can have enough annual generation and still be unable to serve a large AI campus.

Power must be:

- generated in or imported into the relevant electrical region;
- transmitted across lines with sufficient thermal / stability capacity;
- stepped through substations;
- delivered to the interconnection point;
- supported by enough generation / reserves under contingency conditions.

**INTERPRETATION:** "Available electricity" and **deliverable MW** are different assets.

A hyperscale campus can therefore be constrained even if regional generation statistics appear comfortable.

---

## 2. National evidence that transmission need is structural

**FACT:** DOE's July 2026 draft National Transmission Needs Study says there is a **pressing need for additional transmission infrastructure** because of load growth from data centres, manufacturing, other large industrial loads and electrification.

**FACT:** DOE says transmission is needed for three distinct reasons:

- new generation interconnection;
- new load interconnection;
- congestion relief / reliability.

**FACT:** DOE also notes that MISO, SPP, PJM and ERCOT have recently approved some of their largest transmission portfolios, with MISO's 2024 portfolio described as the largest U.S. transmission portfolio ever undertaken.

**INTERPRETATION:** The constraint is not a single isolated data-centre hub. The grid is simultaneously absorbing new loads, generation changes and reliability requirements across several major regions.

---

## 3. Why data-centre loads are unusually difficult

**FACT:** FERC's June 2026 large-load proceedings emphasize that new large loads can be **orders of magnitude larger** and more concentrated than traditional load growth.

**FACT:** FERC also highlights fast operational changes — large loads can change electricity consumption within seconds — which creates different planning and reliability requirements.

**INTERPRETATION:** A 500 MW or 1 GW campus is not equivalent to adding the same load gradually across millions of customers. The network must withstand concentration, contingencies and dynamic behavior at a specific node.

---

## 4. Large-load interconnection is currently a system bottleneck

**FACT:** On 18 June 2026 FERC directed all six RTO / ISO grid operators under its jurisdiction to justify or reform tariffs governing how data centres and other large loads connect to transmission.

The reforms explicitly address:

- application and study processes;
- transmission-cost transparency / cost shifting;
- co-location;
- flexible transmission service;
- nearby / electrically proximate generation;
- generation-adequacy information.

**INTERPRETATION:** FERC's action is strong evidence that the existing process itself has become a material bottleneck.

But this does **not** mean the process is structurally scarce in the same way as a transformer factory.

---

## 5. Why process friction should not be mistaken for durable scarcity

The current queue can shrink without any physical grid expansion if rules improve.

### 5.1 Flexible transmission service

**FACT:** FERC says non-firm / flexible transmission service can let large loads limit grid withdrawals under constrained conditions, reducing required network upgrades and speeding connection.

### 5.2 Co-location and electrically proximate generation

**FACT:** FERC's 2026 orders allow study of large loads together with nearby generation rather than treating them as unrelated requests.

**INTERPRETATION:** If a data centre brings new generation or accepts curtailment, some transmission upgrades can be deferred or avoided.

### 5.3 Regional accelerated processes

**FACT:** SPP has created High Impact Large Load processes designed to accelerate connection while pairing load with generation assessment / conditional service.

**FACT:** ERCOT replaced its prior large-load study process in 2026 with a new batch process for loads of 75 MW or greater.

**INTERPRETATION:** Administrative scarcity is already being redesigned. It should not be capitalized as though it were a decade-long proprietary moat.

---

## 6. Ghost demand is important contradictory evidence

**FACT:** Reuters reported in September 2026 that U.S. data-centre power requests exceeded **700 GW**, more than ten times estimated current U.S. data-centre usage, prompting growing concern about speculative / duplicate projects.

**FACT:** Texas and other jurisdictions are imposing stronger financial / identity / project-maturity requirements; utilities have cut forecasts materially after deposit / commitment requirements removed less-credible requests.

**INTERPRETATION:** Raw interconnection-queue MW is a poor demand forecast.

The correct evidence hierarchy is:

1. executed customer / utility contracts;
2. financial security / deposits;
3. approved / funded transmission projects;
4. land / permitting / equipment commitments;
5. unqualified interconnection requests last.

**CONCLUSION:** Ghost demand weakens naive forecasts of required grid buildout but does **not** eliminate the transmission bottleneck for projects that remain credible after screening.

---

## 7. Physical transmission scarcity survives queue reform

Even if queue administration becomes efficient, credible projects can still require:

- new transmission lines;
- reconductoring;
- substation expansion;
- transformers and breakers;
- reactive-power / stability equipment;
- generation reinforcement;
- protection and control changes.

**FACT:** DOE's 2026 Needs Study is based on current and anticipated physical congestion / capacity needs, not only queue counts.

**INTERPRETATION:** Process reform can remove false demand and unnecessary network upgrades, but it cannot make a thermally / stability-constrained transmission corridor carry unlimited power.

---

## 8. Why greenfield transmission is hard to expand

Transmission projects face several coupled constraints:

- rights-of-way;
- siting and permitting;
- state / local approvals;
- environmental review;
- cost allocation;
- engineering;
- conductors / towers;
- transformers / switchgear;
- specialized construction workforce;
- outage windows for existing-system work.

**INTERPRETATION:** The bottleneck is partly regulatory but also deeply physical. A line is a large distributed infrastructure project rather than a factory product that can simply be shipped faster.

FERC Order 1920 and subsequent reforms improve long-term planning, but implementation itself is occurring over several years.

---

## 9. Transmission can be expanded faster without building new corridors

This is the most important evidence against treating greenfield lines as the only solution.

### Advanced reconductoring

Existing towers can sometimes carry advanced conductors with higher ampacity than conventional conductor.

### Dynamic line rating

Real-time weather / conductor conditions can reveal additional safe transfer capacity versus static assumptions.

### Power-flow control

Devices can redirect flows away from constrained paths.

**FACT:** DOE's 2026 SPARK program explicitly prioritizes advanced reconductoring and other advanced transmission technologies to increase usable capacity on existing rights-of-way and deliver **speed-to-power** faster than some conventional builds.

**INTERPRETATION:** This does not weaken the transmission thesis; it changes **where value may accrue**. If rights-of-way are scarce, technologies that unlock more MW from existing corridors may have unusually high system value.

---

## 10. Investment-capture map

### 10.1 Regulated transmission owners

They can earn regulated returns on approved capital investment.

**Attraction:** enormous capital need / rate-base growth.

**Constraint:** returns are usually regulated; capital intensity and political cost allocation can limit asymmetry.

**INTERPRETATION:** Transmission owners may provide durable earnings growth but are not automatically the highest-upside expression of the bottleneck.

### 10.2 EPC / construction / engineering

Large grid portfolios require engineering, procurement, construction and maintenance capacity.

**FACT:** Quanta Services reported Q2 2026 total backlog of about **$53.4 billion** and remaining performance obligations of **$33.6 billion**, with both materially above year-end 2025.

**INTERPRETATION:** Specialized labor / project execution may itself become a bottleneck as utilities attempt to build many projects simultaneously.

### 10.3 Grid equipment

Transformers, switchgear and substations — already validated separately — benefit directly from transmission expansion.

### 10.4 Advanced conductors / GETs

Potentially high-value because they can shorten delivery time and avoid new rights-of-way.

**OPEN QUESTION:** Do suppliers capture enough pricing / proprietary value, or do these technologies become standardized components within utility capex?

### 10.5 Onsite / behind-the-meter alternatives

If transmission upgrades take too long, the bottleneck can migrate toward turbines, gensets, switchgear, storage and microgrid integration.

---

## 11. Supplier / service concentration

Physical transmission is not controlled by one or two suppliers.

Construction / engineering firms include multiple large regional and national contractors; equipment vendors include several global electrification firms; utilities / transmission owners vary by region.

**INTERPRETATION:** Supplier concentration is weaker than in large gas turbines or some transformer categories.

The structural moat is therefore more likely to reside in:

- specialized high-voltage execution capability;
- scarce skilled labor;
- backlog / customer relationships;
- integrated equipment + engineering;
- proprietary high-capacity conductor / control technology;
- regional rights / regulated asset ownership.

---

## 12. Transmission-deliverability bottleneck score

| Dimension | Score | Rationale |
|---|---:|---|
| Physical / engineering difficulty | **4.8** | large distributed infrastructure, stability / protection engineering, outage coordination |
| Supply elasticity | **4.8** | multi-year siting / construction / equipment cycles |
| Supplier concentration | **3.8** | broader contractor / equipment ecosystem than transformers or turbines |
| Qualification / switching cost | **4.4** | high-voltage execution, utility standards, safety / reliability requirements |
| System criticality | **5.0** | credible load cannot be served if network cannot deliver MW |
| Architecture resilience | **4.7** | grid path remains important even with onsite power; bottleneck can migrate to local network / equipment |
| Pricing / backlog evidence | **4.4** | large approved transmission portfolios and strong EPC/equipment backlogs; direct transmission pricing is regulated / fragmented |

**Bottleneck Strength: 4.7 / 5 — Gate A passed.**

---

## 13. Interconnection-process friction score

| Dimension | Score | Rationale |
|---|---:|---|
| Physical / engineering difficulty | **3.5** | studies are technically complex but largely process / modeling rather than hardware |
| Supply elasticity | **3.8** | engineering staff / study capacity can expand; software/process reform helps |
| Supplier concentration | **2.5** | not a concentrated merchant supplier market |
| Qualification / switching cost | **4.2** | utility / RTO processes are region-specific and regulated |
| System criticality | **4.8** | no connection without studies / tariff service |
| Architecture resilience | **3.6** | flexible load, co-location and new rules can materially reduce friction |
| Economic-capture evidence | **3.0** | scarcity does not directly translate into a high-margin merchant profit pool |

**Current friction score: 4.2 / 5 as a system constraint, but NOT a standalone Gate-A investment layer.**

The distinction is deliberate: it can stop projects while still being a poor place to seek equity-market asymmetry.

---

## 14. What FERC reform can and cannot fix

### Can improve

- duplicative application processing;
- lack of standardized large-load service;
- sequencing of load / generation studies;
- cost transparency;
- flexible / non-firm connection options;
- some unnecessary network upgrades.

### Cannot instantly fix

- overloaded corridors;
- lack of substation capacity;
- transformer / switchgear shortages;
- generation adequacy;
- rights-of-way;
- construction labor;
- physical stability constraints.

**INTERPRETATION:** Successful reform may actually **increase demand for physical grid equipment** by allowing credible projects to move through the study process faster.

---

## 15. Thesis breakers / monitoring

The physical transmission thesis weakens if:

- credible data-centre / industrial load forecasts fall sharply after ghost-demand screening;
- major regional transmission portfolios are cancelled or persistently underbuilt;
- advanced reconductoring / GETs create enough capacity that greenfield transmission demand falls materially;
- flexible large-load service becomes widespread enough to avoid most network reinforcement;
- data centres systematically relocate to unconstrained regions rather than paying for grid expansion;
- behind-the-meter generation becomes the dominant architecture for incremental AI campuses;
- EPC / equipment backlog falls while pricing / margins normalize despite continued AI construction.

The process-friction thesis weakens much faster if:

- FERC / RTO tariff reforms materially shorten study timelines;
- deposits / financial-security rules remove large amounts of speculative queue demand;
- integrated load + generation studies become standard practice.

---

## 16. Decision

**Physical transmission deliverability: Gate A PASSED — 4.7 / 5, High confidence.**

**Large-load interconnection-process friction: real today, but do not treat as a durable standalone profit pool.**

The energy research now has two validated structural functions:

1. **transformers / critical grid equipment**;
2. **physical transmission deliverability**.

The next validation priority is **dispatchable generation equipment**, where supplier concentration and service economics may offer a more direct merchant profit pool than regulated transmission ownership.

---

## Sources

### Government / system evidence

- DOE — 2026 Draft National Transmission Needs Study: https://www.energy.gov/oe/national-transmission-needs-study
- DOE — release of 2026 Draft National Transmission Needs Study: https://www.energy.gov/oe/articles/does-office-electricity-publishes-2026-draft-national-transmission-needs-study
- DOE — SPARK advanced reconductoring / transmission technologies: https://www.energy.gov/oe/speed-power-through-accelerated-reconductoring-and-other-key-advanced-transmission-technology
- FERC — Large Load Integration action, 18 June 2026: https://www.ferc.gov/news-events/news/ferc-launches-aggressive-targeted-action-speed-large-load-integration
- FERC — Commissioner Rosner large-load remarks: https://www.ferc.gov/news-events/news/commissioner-rosners-remarks-large-load-show-cause-orders-e-7-e-12-june-18-2026
- FERC — Order No. 1920 explainer: https://www.ferc.gov/explainer-transmission-planning-and-cost-allocation-final-rule
- ERCOT — Large Load Integration: https://www.ercot.com/services/rq/large-load-integration
- SPP — High Impact Large Load Integration: https://www.spp.org/largeload/

### Commercial / falsification evidence

- Quanta Services — Q2 2026 results: https://investors.quantaservices.com/news-events/press-releases/detail/402/quanta-services-reports-second-quarter-2026-results
- Reuters — U.S. ghost-demand / Texas large-load screening, 1 September 2026: https://www.reuters.com/business/texas-halt-powering-data-centers-reflects-us-reckoning-over-ghost-demand-2026-09-01/
