# AI Memory Bottleneck Research Plan

**Status:** Active research plan  
**Created:** 2026-09-07  
**Purpose:** Turn the first-pass memory value-chain map into a ranked, evidence-based view of structural bottlenecks and the companies most likely to capture disproportionate value from them.

## 1. Decision we want to reach

The research should ultimately answer two separate questions:

1. **Where are the real structural bottlenecks in the AI-memory value chain?**
2. **Which investable companies capture the economics of those bottlenecks strongly enough for AI-driven demand to materially change their earnings trajectory?**

These questions must remain separate. A severe technical bottleneck can still be a poor investment opportunity if the value is captured by a very large incumbent, passed through to customers, competed away, or already fully reflected in valuation.

## 2. Current starting point

The current value-chain map identifies the strongest first-pass bottleneck candidates as:

1. HBM stacking / bonding / thermal / yield
2. Advanced packaging / interposers / substrates
3. DRAM / HBM wafer capacity and yield
4. Test / known-good-die / burn-in
5. Wafer thinning / TSV / precision processing
6. Memory-interface / MRDIMM buffer chips
7. Thermal / power / package materials
8. CXL memory expansion / pooling
9. Emerging non-volatile memory

The next phase should go **one layer deeper than the obvious memory vendors** and identify equipment, materials, IP, interface and test suppliers whose products are difficult to substitute.

## 3. Research principle

We are looking for **structural dependency**, not simply growth.

A bottleneck is more attractive when:

- the physical problem gets harder with each generation;
- demand can outrun capacity;
- capacity is slow or expensive to add;
- there are few qualified suppliers;
- qualification and switching are difficult;
- failure at that step prevents the whole system from shipping;
- the supplier can retain some of the economics through pricing, margins, share or volume leverage.

Every deep dive should actively search for evidence that the apparent bottleneck is temporary, easy to substitute, vertically integrated, or economically unattractive.

---

## 4. Two-score framework

Do not collapse technical bottleneck strength and investment attractiveness into a single score too early.

### A. Bottleneck Strength Score — 1 to 5

Score each dimension from 1 to 5 and record the evidence.

| Dimension | Question |
|---|---|
| Physical difficulty | Does the next generation make the problem materially harder? |
| Supply elasticity | How quickly can industry capacity expand? |
| Supplier concentration | How many suppliers can actually meet the requirement at scale? |
| Qualification / switching | How long, risky or expensive is it to change supplier? |
| System criticality | Does failure or shortage at this step constrain shipment of the final AI system? |

A bottleneck should normally reach **4/5 or higher** before we spend substantial time on company-level valuation work.

### B. Investment Capture Score — 1 to 5

Only score this after the bottleneck itself is validated.

| Dimension | Question |
|---|---|
| Revenue sensitivity | Would AI/HBM growth materially affect this company's revenue or earnings? |
| Pricing / margin capture | Is there evidence the company can retain economics rather than pass them through? |
| Competitive durability | Is the company's position protected by IP, process know-how, installed base or qualification? |
| Market-share runway | Can the company gain share or sell more content per system? |
| Asymmetry | Is the company small enough for the opportunity to matter materially? |
| Valuation / execution | Is the upside already priced in, and can the company finance and execute the required expansion? |

A strong research candidate requires **both** a real bottleneck and credible economic capture.

---

## 5. Research sequence

The work should proceed in waves. We should not try to deep-dive every layer simultaneously.

### Wave 1 — HBM stacking, bonding, thermal and yield

**Priority:** Highest

This is the first deep dive because the physical problem appears to worsen as stack height, bandwidth and thermal density rise.

#### Decompose the process

Map the sub-steps separately:

1. TSV formation
2. wafer thinning
3. temporary bonding / debonding
4. dicing / die preparation
5. die stacking
6. thermo-compression / other bonding approaches
7. MR-MUF / TC-NCF / underfill and molding approaches
8. warpage control
9. thermal-interface and heat-removal materials
10. metrology / inspection
11. known-good-die and stack-level test

#### Questions

- Which sub-step is actually limiting yield or throughput today?
- Which problems become harder at 12-high and 16-high stacks?
- Which processes differ materially between SK hynix, Samsung and Micron?
- Are suppliers qualified across multiple memory vendors, or captive to one process architecture?
- What equipment/material categories have long lead times or limited qualified capacity?
- Where does hybrid bonding change the supplier map?
- Which suppliers gain content per HBM stack as complexity rises?

#### Deliverable

`research/memory/deep-dives/hbm-stacking-thermal.md`

Include a process map, supplier map, bottleneck score, evidence against the thesis, and a shortlist of companies for deeper work.

---

### Wave 2 — Advanced packaging and interposers

**Priority:** Very high

The goal is to move beyond the headline fact that CoWoS capacity is constrained and identify **what inside the packaging process is actually hard to scale**.

#### Decompose

- silicon / RDL interposer production
- advanced lithography steps
- redistribution layers
- substrate supply
- bumping / micro-bump or alternative interconnect
- bonding / assembly
- inspection and metrology
- warpage control
- package-level thermal management
- final package test

#### Questions

- Which equipment or material categories gate incremental CoWoS-like capacity?
- Which suppliers are single- or dual-sourced?
- What must be qualified with TSMC, memory vendors or accelerator customers?
- Which constraints disappear if packaging architectures move from silicon interposers toward RDL or other approaches?
- Which suppliers sell across TSMC, ASE, Amkor, Samsung and other packaging ecosystems?

#### Deliverable

`research/memory/deep-dives/advanced-packaging.md`

---

### Wave 3 — Test, known-good-die and burn-in

**Priority:** High

Testing becomes more valuable when one bad die can destroy an expensive multi-die package.

#### Decompose

- wafer probe
- DRAM die test
- known-good-die selection
- HBM stack test
- high-speed memory test
- accelerator / SoC test
- final package test
- burn-in / reliability
- probe cards, handlers and sockets

#### Questions

- Does tester intensity per unit increase as HBM generations advance?
- Is test time increasing or decreasing?
- Which test steps are unique to HBM?
- Where are capacity constraints occurring?
- Which suppliers have the strongest installed-base or qualification moat?
- Are there smaller suppliers with greater revenue sensitivity than Advantest?

#### Deliverable

`research/memory/deep-dives/test-and-known-good-die.md`

---

### Wave 4 — Wafer thinning, TSV and precision processing

**Priority:** High but dependent on Wave 1

This should be treated as a separate deep dive only after Wave 1 identifies which wafer-preparation steps are truly critical.

#### Questions

- How thin are HBM dies becoming by generation?
- What happens to breakage, warpage and yield as thickness falls?
- Are grinding, polishing, dicing or temporary-bonding tools difficult to substitute?
- Which tools are already installed across all three HBM manufacturers?
- Does hybrid bonding increase or reduce demand for any of these steps?

#### Deliverable

`research/memory/deep-dives/wafer-processing-tsv.md`

---

### Wave 5 — Memory interfaces, MRDIMM and CXL

**Priority:** Medium, but potentially the cleanest smaller-company opportunity

This is a different bottleneck from HBM manufacturing. The research question is whether increasing memory speed and capacity make specialist interface/controller silicon structurally mandatory.

#### Separate the layers

1. DDR5 register clock drivers / data buffers
2. MRDIMM multiplexing and interface silicon
3. PMIC / clocking support
4. CXL memory-expander controllers
5. CXL switches
6. firmware / interoperability

#### Questions

- What is mandatory versus optional in each architecture?
- How concentrated are market shares?
- How long is server-OEM / CPU-platform qualification?
- What can CPU vendors or hyperscalers integrate themselves?
- Does each DDR generation increase chip content per DIMM?
- Is CXL adoption creating a new market or simply shifting value among incumbents?

#### Deliverable

`research/memory/deep-dives/interfaces-cxl.md`

Montage Technology should be assessed inside this workstream rather than treated as validated in advance.

---

## 6. Benchmark workstream — DRAM/HBM manufacturers

SK hynix, Micron and Samsung should remain a **benchmark**, not the main hunting ground.

Track:

- HBM mix and capacity allocation
- node migration
- HBM pricing / contracts
- capital expenditure
- yields where disclosed
- customer concentration
- gross-margin impact

This tells us how valuable the bottleneck is at the system level and whether economics are flowing upstream into equipment/material suppliers.

The objective is not to repeatedly re-underwrite the large memory manufacturers unless new evidence suggests they remain the best way to capture the thesis.

---

## 7. Supplier discovery process

For each validated bottleneck, build the supplier universe systematically rather than starting from familiar stocks.

### Pass 1 — Process suppliers

Identify all meaningful suppliers of:

- equipment
- materials
- test / metrology
- interface silicon / IP
- assembly / packaging services

### Pass 2 — Qualification evidence

Look for evidence of:

- named HBM / DRAM / advanced-packaging customers
- design wins
- qualified-vendor status
- installed-base share
- customer concentration
- multi-year supply agreements
- customer capex linked to supplier orders

Treat vague references to "AI demand" as weak evidence.

### Pass 3 — Economic exposure

Estimate for each company:

- % of revenue exposed to the relevant process
- growth of that revenue
- gross / operating margins
- incremental capital needs
- backlog / book-to-bill where meaningful
- customer concentration
- likely content per HBM stack or package

### Pass 4 — Investment asymmetry

Ask:

> If the bottleneck doubles in economic value over 3–5 years, how much can this company's revenue, earnings and valuation plausibly change?

This is the key filter for distinguishing a great company from a potentially asymmetric opportunity.

---

## 8. Evidence standard

Each material claim should ideally be supported by two different source classes when possible.

### Preferred order

1. regulatory filings / audited disclosures
2. technical standards and peer-reviewed papers
3. customer / supplier primary disclosures
4. earnings calls and investor presentations
5. reputable industry research
6. specialist journalism
7. community discussion only for generating questions

### Triangulation rule

For claims such as "X is a bottleneck", try to establish at least three of:

- a customer says it is constrained;
- the supplier is expanding capacity;
- lead times / backlog are elevated;
- technical literature explains why the process is hard;
- competitors cannot easily substitute;
- pricing / margins show economic capture.

---

## 9. Falsification work

Every deep dive must contain a section titled **Evidence against the bottleneck thesis**.

Search specifically for:

- rapid capacity additions
- second-source qualification
- process simplification
- vertical integration
- alternative architectures
- falling equipment intensity
- customer bargaining power
- commoditisation
- margin compression despite strong demand

A research stream should be deprioritised if the physical constraint is real but suppliers cannot capture economics.

---

## 10. Completion gates

### Gate A — Bottleneck validated

Advance to company deep dives only if:

- Bottleneck Strength Score is approximately **4/5 or higher**;
- evidence comes from at least two independent source classes;
- the constraint appears structural across more than one product generation;
- there is no obvious rapid substitute that destroys the thesis.

### Gate B — Company candidate validated

Promote a company from `Research queue` to `Investigating` only if:

- it has meaningful exposure to a validated bottleneck;
- there is evidence of qualification / customer adoption;
- the opportunity can materially affect its financials;
- the relevant market is not obviously commoditised.

### Gate C — High-conviction research candidate

This should be rare. Require:

- strong bottleneck evidence;
- strong competitive-position evidence;
- clear economic capture;
- manageable balance-sheet / execution risk;
- valuation that still leaves plausible upside;
- explicit thesis breakers and monitoring indicators.

---

## 11. Working outputs

Maintain five living outputs:

1. `value-chain.md` — canonical end-to-end map
2. `research-plan.md` — this execution plan
3. `deep-dives/*.md` — one canonical file per bottleneck
4. company files — only after a supplier passes Gate A
5. `watchlist.md` — cross-theme prioritisation after evidence supports a status change

Do not create parallel "final" copies. Git history is the version record.

---

## 12. Agent + collaborator workflow

The research is designed for parallel agent work without requiring either collaborator to manage Git manually.

For each workstream:

1. one agent builds the primary evidence case;
2. a second pass should actively challenge or falsify the conclusion;
3. the agent updates the canonical deep-dive file;
4. source links and conflicting evidence are preserved;
5. the agent updates `CHANGELOG.md` when conclusions/confidence change;
6. the agent opens a PR;
7. the Research governance check runs;
8. the PR auto-merges after required checks pass unless manual review was explicitly requested.

Avoid having two agents edit the same deep-dive file simultaneously. Parallelise by bottleneck instead.

---

## 13. Recommended order of execution

### First

**HBM stacking / bonding / thermal / yield**

This should produce the first supplier longlist and tell us whether wafer processing, bonding equipment, molding/underfill, thermal materials or metrology deserve separate company deep dives.

### Second

Run **advanced packaging** and **test** in parallel.

### Third

Use the findings from HBM stacking to decide whether **wafer thinning / TSV / precision processing** deserves its own full workstream.

### Fourth

Run **interfaces / MRDIMM / CXL**, with Montage Technology as one candidate to test rather than the assumed winner.

### Fifth

Create a cross-bottleneck ranking that compares:

- Bottleneck Strength Score
- Investment Capture Score
- best public candidates
- best emerging/private candidates to monitor
- key thesis breakers

---

## 14. Immediate next action

Start the HBM stacking / thermal workstream by answering one narrow question first:

> **As HBM moves from 8/12-high toward 16-high and future bonding architectures, which process steps become disproportionately harder, and which external suppliers are required to solve them?**

The first research pass should map the process before ranking companies. This prevents us from selecting stocks first and inventing the bottleneck thesis around them.
