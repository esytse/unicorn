# AI Energy / Power Delivery — End-to-End Value Chain

**Status:** Canonical evidence-backed E2E synthesis  
**Confidence:** **High** on the core physical / thermal bottlenecks; **Medium-High** on nuclear supply-chain scarcity; **Medium** on supplier-level economic capture before company underwriting  
**Last substantive update:** 2026-09-07  
**Backlog:** issue #51

## Executive conclusion

The energy constraint around AI is not one generic “power shortage.” It is a **coupled chain that converts primary energy into reliable, deliverable and thermally usable compute capacity**.

The research now supports a stronger thesis than the initial map:

> **AI infrastructure is constrained by speed-to-power and speed-to-usable-compute. The most valuable bottlenecks are the layers where qualified capacity expands slowly, switching is difficult, system failure is expensive and customers pay for schedule certainty.**

The bottleneck is also **mobile**. Solving one constraint commonly moves scarcity somewhere else:

```text
grid connection delayed
        ↓
onsite / behind-the-meter generation
        ↓
turbine slots + gas pipeline + permits become limiting
        ↓
power reaches site
        ↓
transformers / switchgear / electrical integration become limiting
        ↓
rack density rises
        ↓
power-conversion architecture changes
        ↓
cooling / heat rejection becomes limiting
        ↓
usable AI compute
```

Nuclear adds a second migration path:

```text
hyperscaler wants firm nuclear power
        ↓
existing licensed asset / restart / uprate if available
        ↓
otherwise new nuclear
        ↓
conversion → enrichment / HALEU → qualified fuel
        ↓
forgings / nuclear-grade components → EPC / QA / workforce
        ↓
reactor + turbine-generator
        ↓
transformers / transmission / electrical backbone
        ↓
cooling / heat rejection
        ↓
usable AI compute
```

The investment programme should therefore search for **architecture-resilient bottleneck owners**, not simply companies with high data-centre revenue growth.

---

## 1. Canonical system map

```text
AI / data-centre demand
        ↓
SITE + COMMERCIAL ACCESS
land / zoning / power rights / utility service / PPAs / water / permits
        ↓
PRIMARY ENERGY + FUEL
natural gas / uranium fuel cycle / renewables / hydro / other
        ↓
GENERATION
existing fleet / new utility generation / onsite generation
        ↓
GENERATION EQUIPMENT
large gas turbines / generators / balance of plant / inverters
        ↓
BULK TRANSMISSION
lines / conductors / substations / HV equipment / grid controls
        ↓
PHYSICAL INTERCONNECTION + SUBSTATION
network capacity / LPTs / transformers / switchgear / protection
        ↓
SITE DISTRIBUTION
feeders / cables / e-houses / modular substations / MV equipment
        ↓
BEHIND-THE-METER POWER
onsite generation / BESS / UPS / microgrid controls / islanding / protection
        ↓
DATA-CENTRE ELECTRICAL BACKBONE
MV/LV switchgear / transformers / UPS / busway / protection / controls
        ↓
GRID-TO-RACK ARCHITECTURE
AC → hybrid AC/DC → 800 VDC / rectification / DC protection / busway / DC/DC
        ↓
AI COMPUTE
GPU / accelerator / memory / networking load
```

A parallel thermal chain determines whether that electrical power is usable:

```text
chip / package heat
        ↓
cold plate / thermal interface
        ↓
rack manifold / connectors
        ↓
CDU / pumps / controls / heat exchanger
        ↓
facility water loop
        ↓
chiller / dry cooler / tower / hybrid heat rejection
        ↓
ambient environment
```

And two control loops feed back upstream:

- **load flexibility / orchestration** can reduce peak firm-power requirements;
- **energy management / storage** can smooth rapid AI load swings and change grid / generator sizing.

---

## 2. Common-basis E2E scorecard

Scores below refer to **structural bottleneck strength of the function**, not stock attractiveness. Where the layer is not a merchant supplier market, that distinction is explicit.

| Layer / function | Structural scarcity | AI sensitivity | Substitutability | Architecture resilience | Evidence quality | Likely economic-capture mechanism | Timing |
|---|---:|---|---|---|---|---|---|
| Site with credible near-term power rights | High but location-specific | Very high | Medium | High | Medium-High | land / development premium; not a clean supplier layer | Now |
| Natural gas commodity | ~3.0 / regional | Medium-High | High globally | Medium | High | commodity / pipeline economics | Now |
| Uranium mining / U3O8 | **3.5** | Low-Medium near term | Medium | High | High | commodity contracting | Now + 2030s |
| UF6 conversion | **4.3** | Medium | Low-Medium | High | Medium-High | scarce qualified conversion capacity / long contracts | Now + 2030s |
| Western LEU enrichment | **4.6** | Medium | **Low** | **High** | High | SWU pricing / long-term contracts / strategic capacity | Now + 2030s |
| HALEU enrichment / deconversion | **4.7** | Low near term; High for advanced nuclear | **Very low today** | Medium-High | High on scarcity; Medium on demand timing | long-term fuel contracts / policy-backed capacity | Mainly 2030s |
| Existing operating nuclear asset | **4.6 asset scarcity** | Medium-High | Very low locally | High | High | long-term PPA / asset economics; **not supplier Gate A** | Now |
| Nuclear restart pathway | **4.4** | Medium-High | Very low | Medium | Medium-High | scarce brownfield asset / specialist services; not scalable market | 2027+ |
| Nuclear uprates | **4.2** | Medium | Low | High | High | equipment / engineering / outage services | 2026–2032 |
| New large / advanced reactor output | High project difficulty | Medium today; potentially High later | Medium across technologies | Medium | Medium | generation asset economics; deployment risk dominates | 2030s |
| Nuclear heavy forgings / long-lead components | **4.5** | Low near term; Medium-High 2030s | **Low** | Medium-High | High | reservation / qualified manufacturing slots | 2030s build cycle |
| Nuclear EPC / QA / skilled workforce | **4.4** | Low-Medium near term; High 2030s | Low | High | High | specialist engineering / services / execution | Restart + 2030s |
| Utility generation as broad category | ~3.6 | High | **High across technologies** | High | High | power / capacity prices | Now |
| **Large gas-turbine slots** | **4.6** | **High** | **Low** | Medium-High | **High** | reservation / new-unit pricing + long-lived service | Now–2030 |
| Reciprocating gensets | **3.6** | High | High | Medium | High | volume / service; limited scarcity | Now |
| **Physical transmission deliverability** | **4.7** | **High** | **Low locally** | **Very high** | **High** | EPC / conductors / grid equipment / GETs; capture must be tested | Now–2030s |
| Interconnection / queue process | ~4.2 current friction | Very high | Reformable | Low as standalone thesis | High | **not a durable merchant layer** | Now |
| **Transformers / critical substations** | **4.7** | **High** | **Low** | **Very high** | **High** | equipment pricing / capacity / service | Now–2030 |
| **MV/HV switchgear** | **4.4** | High | Medium | **Very high** | High | equipment / systems / service | Now–2030 |
| Site distribution / modular electrical systems | ~4.1–4.3 | Very high | Medium | High | Medium-High | integrated systems / execution | Now |
| **Integrated BTM / microgrid architecture** | **4.1** | **Very high** | Medium | Medium-High | Medium-High | design / controls / protection / execution / service | Now |
| Generic BESS hardware | **3.4** | High | **High** | Medium | High | volume / integration, not cell scarcity | Now |
| **Integrated data-centre electrical backbone** | **4.3** | **Very high** | Medium | **High** | **High** | integrated portfolio / qualification / service | Now |
| 800 VDC technical transition | ~**4.3 technical pressure** | **Very high** | — | Emerging | High | architecture shift, not itself a supplier moat | 2027+ |
| Generic 800 VDC supplier scarcity | **3.6** | Very high | **High / growing** | Medium | High | broad open-ecosystem volume | 2027+ |
| Rack-level generic power components | ~3.8 | Very high | Medium-High | Medium | Medium-High | content growth | Now–2030 |
| **Integrated thermal chain / qualified cooling capacity** | **4.4** | **Very high** | Medium | **Very high function-level** | **High** | capacity reservation / system integration / testing / service | Now–2030 |
| DTC liquid-cooling function | **4.2** | **Very high** | Medium | High | High | qualified system capacity; generic components weaker | Now |
| Generic cold plates / CDUs / manifolds | ~**3.8 supplier scarcity** | Very high | High / rising | Medium | High | volume; open standards limit lock-in | Now |
| Facility heat rejection | **4.2** | **Very high** | Medium | **Very high function-level** | High | integrated thermal capacity / engineering | Now |
| Water availability | Regional constraint | Medium-High | Architecture-dependent | Low | High | site economics; not universal cooling thesis | Now |

### Interpretation of the table

The top score alone is not enough. For investment capture, the attractive combination is:

> **scarcity × AI sensitivity × supplier concentration × architecture resilience × evidence of price / margin / service capture**.

That is why a 4.7/5 physical transmission bottleneck may not produce the same economics as a 4.6/5 gas-turbine bottleneck: the former can be spread across utilities, permitting, EPC and many equipment layers, while turbine reservations sit in a much more concentrated merchant OEM market.

---

## 3. Demand forcing function — more MW and more MW per rack

**FACT:** IEA projects global data-centre electricity consumption rising from about **485 TWh in 2025 to ~950 TWh in 2030**. See the energy thesis and source links in the underlying deep dives.

**INTERPRETATION:** Two independent demand vectors matter:

1. **site-scale load growth** — hundreds of MW to GW-class campuses;
2. **rack-density growth** — much more power and heat in a smaller physical footprint.

The first stresses generation, transmission, substations and site access. The second stresses electrical conversion, protection, copper / busway and thermal management.

**HYPOTHESIS:** The best bottleneck owners may be companies exposed to both vectors rather than to electricity volume alone.

---

## 4. Site, land, power rights and permits — economically scarce, difficult to own as a supplier

A data-centre site is valuable only if it has a credible path to energisation and heat rejection.

Relevant dependencies:

- land / zoning;
- utility service and network studies;
- transmission / substation proximity;
- gas-pipeline proximity if onsite generation is planned;
- water / heat-rejection envelope;
- local air / environmental permits;
- PPA / generation contracting;
- construction labour and local political support.

**INTERPRETATION:** “Land with power” is a different asset from land with a speculative queue position.

**COUNTERPOINT:** Site constraints can be mitigated through relocation, flexible service, co-location and BTM power. Therefore the site / queue itself is not the primary supplier hunting ground.

---

## 5. Primary energy and fuel — scarcity increases downstream of the commodity

### Natural gas

Gas itself is generally not the strongest global bottleneck. The more relevant constraints are **local pipeline capacity, turbine equipment, permits and reliable delivery to a specific site**.

### Uranium

The nuclear deep dive finds uranium mining at only **3.5/5** relative to downstream fuel-cycle bottlenecks.

### Nuclear fuel chain

The constraint steepens downstream:

```text
U3O8
→ UF6 conversion 4.3
→ Western LEU enrichment 4.6
→ HALEU enrichment / deconversion 4.7 where required
→ qualified fuel fabrication
```

**INTERPRETATION:** Nuclear is a good example of why commodity exposure and bottleneck exposure are not the same thing. The harder-to-replicate value sits in licensed / qualified transformation capacity, not necessarily the mined material.

---

## 6. Generation — firm capacity matters more than generic annual MWh

Broad generation remains substitutable across gas, renewables, hydro, nuclear and other resources at a regional-system level.

The constraint becomes stronger when the requirement is:

> **large blocks of firm power, at a defined location, on a short timetable.**

### Near-term nuclear route

The nuclear research shows the fastest credible nuclear sequence through 2030 is:

```text
existing operating output
→ life extension / long-term PPA
→ selected restart
→ uprate
```

**FACT:** Microsoft supports the 835 MW Crane restart; Meta agreements preserve / contract operating nuclear output and support uprates. NRC's expected uprate schedule totals roughly **2.42 GW electric through 2032**. See `deep-dives/nuclear-supply-chain.md`.

### New nuclear route

Most advanced / large new-reactor output is a **2030s** pathway. It matters strategically but should not be counted as a solution to the 2026–2029 speed-to-power problem.

---

## 7. Large gas turbines — the clearest concentrated merchant equipment bottleneck

**Validated Bottleneck Strength: 4.6/5.**

The key evidence is unusually direct:

- multi-year slot reservations;
- GE Vernova gas backlog / reservation commitments vastly larger than annual output;
- Siemens Energy sold-out capacity through FY2028 and rapidly filling later years;
- hot-section blades / vanes identified as manufacturing constraints;
- favorable new-unit pricing / margin evidence;
- concentrated advanced-class supplier set;
- recurring long-lived service economics.

**INTERPRETATION:** This is currently one of the best examples where a system constraint maps cleanly into a merchant profit pool.

**FALSIFICATION:** GE / Siemens / Mitsubishi are expanding capacity. Scarcity should be normalized, not capitalized indefinitely.

---

## 8. Nuclear manufacturing — highly scarce, but mainly a 2030s industrial cycle

### HALEU / enrichment

- HALEU: **4.7/5**;
- Western LEU enrichment: **4.6/5**;
- UF6 conversion: **4.3/5**.

These layers combine concentration, geopolitical substitution, licensing and multi-year capacity expansion.

### Heavy components

**Large forgings / long-lead components: 4.5/5.** DOE supply-chain work says the United States lacks domestic capacity for the largest nuclear forged / cast components; developers have already reserved qualified manufacturing capacity.

### EPC / workforce

**Nuclear EPC / QA / workforce: 4.4/5.** The constraint is accumulated nuclear experience, qualification, documentation and commissioning capability, not generic construction labour.

**INTERPRETATION:** Nuclear offers potentially exceptional scarcity but weaker near-term AI sensitivity than turbines / electrical / cooling. Issue #52 must penalise time-to-revenue and project execution rather than simply rank nuclear by technical scarcity.

---

## 9. Physical transmission — the system bottleneck is real even if the queue improves

**Validated Bottleneck Strength: 4.7/5.**

The transmission deep dive separates:

- **physical scarcity** — rights-of-way, conductors, substations, network capacity, engineering / construction;
- **process scarcity** — queue rules, studies, tariffs and cost allocation.

**FACT / INTERPRETATION:** FERC / RTO reforms, flexible service and project-maturity screens can reduce process friction. They do not create physical transmission capacity by themselves.

Advanced reconductoring, dynamic line rating and power-flow control can release more capacity from existing corridors, so the investable thesis is broader than “build more transmission lines.”

Likely value pools:

- engineering / EPC;
- conductors;
- grid-enhancing technologies;
- substations;
- transformers / switchgear;
- protection / controls.

**OPEN QUESTION:** How much of the physical bottleneck converts to attractive supplier margins rather than regulated / project volume?

---

## 10. Interconnection queues — a constraint, not the durable profit pool

The initial map called large-load interconnection the highest 4.8/5 bottleneck. That conclusion is now revised.

**Previous conclusion:** large-load interconnection / queue friction was treated as the highest system bottleneck.

**New conclusion:** current process friction is real, but it is **reformable and not a standalone durable merchant layer**. The enduring scarcity is the physical equipment / network / engineering required by credible projects after speculative “ghost demand” is removed.

**Implication:** Do not invest in a narrative based on raw queue GW. Follow funded projects, deposits, equipment orders, construction and energisation milestones.

---

## 11. Transformers and critical substations — highest architecture resilience in the chain

### Transformers

**Validated Bottleneck Strength: 4.7/5, High confidence.**

Structural reasons:

- custom engineering / fragmented specifications;
- electrical-steel and copper dependencies;
- factory test capacity;
- utility qualification;
- transport constraints;
- slow factory expansion;
- critical reliability requirements.

The strongest revealed-preference evidence is customers paying extraordinary logistics / schedule costs to secure transformers.

### MV/HV switchgear

**Validated Bottleneck Strength: 4.4/5.**

Supply is broader than transformers, but protection / interruption / switching remain mission-critical and largely unavoidable across grid, BTM and data-centre architectures.

**Architecture resilience:** **Very high.** Whether the power comes from grid, gas, nuclear or onsite sources, transformation, switching and protection remain necessary somewhere in the path.

---

## 12. Behind-the-meter power — a bypass that moves scarcity

**Integrated BTM / microgrid architecture: 4.1/5.**

The investment insight is not “onsite generation is scarce.” It is:

> **The ability to design, permit, synchronize, protect and operate a site-specific power system can shorten time-to-power.**

A BTM architecture can combine:

- gas turbines / gensets;
- fuel cells;
- BESS / UPS;
- grid service;
- microgrid controls;
- islanding / protection;
- dynamic load management.

But BTM often creates a new chain:

```text
grid delay
→ onsite power
→ turbine slot / genset / fuel-cell availability
→ gas pipeline / fuel / emissions permit
→ redundancy / overbuild
→ switchgear / controls / storage
→ thermal constraint
```

### What did not pass

- generic BESS hardware: **3.4/5**;
- gensets: **3.6/5**.

The integrated architecture is more defensible than the commodity hardware.

---

## 13. Data-centre electrical backbone — direct AI sensitivity, broader competition

**Validated Bottleneck Strength: 4.3/5.**

The backbone includes:

- MV/LV switchgear;
- transformers;
- UPS;
- PDU / RPP;
- busway;
- breakers / fuses;
- monitoring / controls;
- backup / BTM interfaces;
- modular power rooms / skids.

**FACT:** Eaton, Schneider and Vertiv show strong 2026 data-centre order / backlog and margin evidence in the underlying deep dive.

**INTERPRETATION:** The bottleneck is less about one rare component and more about **qualified integrated capacity, sequencing, testing and reference architecture**.

This layer has very high AI sensitivity, but the supplier base is much broader than advanced gas turbines or enrichment.

---

## 14. 800 VDC — major architecture transition, weak broad scarcity thesis

### Technical conclusion

The move from repeated low-voltage conversions toward 800 VDC becomes increasingly compelling as rack power reaches hundreds of kW and potentially MW scale.

**Technical pressure: ~4.3/5.**

### Supplier conclusion

**Broad supplier scarcity: only ~3.6/5.**

Why:

- Google, Microsoft and NVIDIA are standardising the architecture through OCP;
- 80+ ecosystem participants are already developing compatible equipment;
- interoperability is an explicit design objective.

Potential future narrow bottlenecks:

- MVAC → DC transformer-rectifier / solid-state power blocks;
- DC fault protection / solid-state breakers;
- high-power DC busway / connectors;
- high-density DC/DC conversion;
- DC-native UPS / BESS integration.

**INTERPRETATION:** 800 VDC is likely to **redistribute value**, not create a moat for every company with an 800 VDC product.

---

## 15. Cooling / heat rejection — the final conversion from MW to usable compute

### Integrated thermal chain

**Validated Bottleneck Strength: 4.4/5, Medium-High confidence.**

A power allocation is only useful if the facility can remove the corresponding heat.

The strongest scarcity evidence is the **> $4bn Modine cooling-capacity agreement plus $165m customer prepayment** to fund capacity expansion. That is direct revealed preference for thermal schedule certainty.

### Direct-to-chip liquid cooling

**Function score: 4.2/5.**

DTC is becoming structurally important at high density, but OCP standardisation and multi-vendor manufacturing reduce generic cold-plate / CDU scarcity to ~**3.8/5**.

### Facility heat rejection

**Function score: 4.2/5.**

Heat must leave the site regardless of whether the implementation uses:

- chillers;
- dry coolers;
- cooling towers;
- hybrid / adiabatic systems;
- warm-water / chiller-less architectures.

**Key distinction:** **heat rejection is architecture-resilient; chillers are not.**

---

## 16. Cross-cutting dependency map

### Specialist materials

| Dependency | Where it matters | Why it can constrain |
|---|---|---|
| GOES / electrical steel | transformers | constrained qualified supply / exact grades / long equipment cycles |
| Copper / conductors | transformers, cables, busway, cooling | high content; commodity availability can amplify but usually does not create the moat by itself |
| Turbine hot-section alloys / blades / vanes | gas turbines | difficult manufacturing / high-temperature qualification |
| Nuclear forgings / specialty steels | reactor vessels / steam generators / structures | extreme size, material quality and nuclear QA |
| Power semiconductors / modules | conversion, 800 VDC, UPS | high technical importance but broad supplier ecosystem today |

### EPC / skilled labour / commissioning

Scarcity exists at several levels:

- transmission construction / utility engineering;
- high-voltage electrical installation;
- data-centre commissioning;
- nuclear-quality EPC / welding / inspection;
- thermal integration / fluid-system commissioning.

**INTERPRETATION:** Human capability can be a genuine bottleneck but is often difficult to own with durable high-margin economics. It should be scored separately from the physical function.

### Factory test / qualification

Repeated across the chain:

- transformers;
- switchgear;
- turbines;
- nuclear components;
- UPS / electrical systems;
- CDUs / cooling systems.

This is one reason factory expansion is slower than simply adding floor space.

### Service / installed-base economics

Potentially important for:

- gas turbines;
- nuclear plants / fuel / outage services;
- transformers / switchgear;
- UPS / electrical platforms;
- cooling / controls.

**HYPOTHESIS:** Installed-base service may be more durable than temporary equipment scarcity and should receive explicit weight in company Investment Capture.

---

## 17. Bottleneck migration map

### Migration A — queue reform does not equal power delivery

```text
interconnection queue delay
→ FERC / RTO reform + stronger project screens
→ speculative demand falls
→ credible projects remain
→ physical transmission / substation / transformer work becomes visible
```

**Investment implication:** follow physical orders and construction, not queue headlines.

### Migration B — bypassing the grid

```text
grid connection too slow
→ BTM / onsite generation
→ turbine slots / gas pipeline / permits / land
→ microgrid switchgear / controls / storage
→ electrical backbone
→ cooling
```

**Investment implication:** grid bypass can strengthen multiple equipment bottlenecks simultaneously.

### Migration C — new generation does not bypass the grid chain

```text
new gas or nuclear generation
→ generator / turbine island
→ transformers / switchgear
→ transmission
→ data-centre site
```

**Investment implication:** adding generation can increase demand for already-constrained grid equipment.

### Migration D — nuclear moves the bottleneck upstream before it moves downstream

```text
advanced nuclear demand
→ conversion / enrichment / HALEU
→ qualified fuel
→ forgings / nuclear-grade components
→ EPC / QA / workforce
→ plant
→ existing grid bottlenecks
```

**Investment implication:** nuclear supply-chain scarcity may appear years before reactor electricity revenue.

### Migration E — 800 VDC

```text
54 VDC / repeated conversion becomes inefficient
→ 800 VDC architecture
→ some legacy PSU / PDU stages shrink
→ value shifts toward MV/DC conversion + DC protection + busway + DC/DC
→ open standards broaden supplier set
```

**Investment implication:** architecture change creates content shifts, not automatic scarcity.

### Migration F — thermal architecture

```text
higher rack heat flux
→ DTC liquid cooling
→ warmer coolant enables dry / hybrid heat rejection
→ conventional chiller content may fall
→ heat-rejection function remains mandatory
```

**Investment implication:** own the thermal function across architectures, not one implementation.

---

## 18. Two timing horizons

### 2026–2030 — immediate speed-to-power / usable-compute constraints

Highest relevance:

- physical transmission;
- transformers / substations;
- MV/HV switchgear;
- large gas-turbine slots;
- integrated data-centre electrical systems;
- BTM / microgrid integration;
- cooling / heat rejection;
- existing nuclear output / life extension / restart;
- LEU enrichment / conversion supporting the operating fleet;
- local gas-pipeline / permitting constraints.

### 2030s — industrial buildout and architecture optionality

Additional relevance:

- advanced / large nuclear construction;
- HALEU / advanced fuel;
- heavy nuclear forgings / qualified components;
- specialist nuclear EPC / QA workforce;
- repeat SMR / advanced-reactor manufacturing;
- mature 800 VDC direct-MV architectures;
- potentially new power-conversion / protection bottlenecks.

**INTERPRETATION:** A high structural score with a 2030s demand horizon should not outrank a slightly lower score with direct 2026 earnings sensitivity without explicit adjustment.

---

## 19. Where the evidence says **not** to hunt broadly

The programme has falsified several simplistic theses:

- **“Buy electricity generators because AI needs power.”** Broad generation is substitutable and often regulated / commodity-like.
- **“Interconnection queues are the investment.”** Process friction can reform; physical network work is the durable layer.
- **“Buy any battery company.”** Generic BESS hardware is 3.4/5, with broad supply and substitution.
- **“Buy any genset company.”** Demand is strong, but gensets are only 3.6/5 on scarcity.
- **“800 VDC creates a new monopoly layer.”** The architecture is important, but the ecosystem is explicitly open.
- **“Liquid cooling means every cold-plate vendor wins.”** Technical necessity is stronger than component scarcity.
- **“Uranium is the nuclear bottleneck.”** Downstream conversion / enrichment / qualified manufacturing are structurally tighter.
- **“SMRs solve the current AI power gap.”** Most commercial new-reactor output is a 2030s pathway.

---

## 20. Current E2E frontier before company underwriting

### Strongest immediate physical bottlenecks

- **transformers / critical substation equipment — 4.7**;
- **physical transmission deliverability — 4.7**;
- **large gas-turbine equipment / slots — 4.6**;
- **integrated thermal chain — 4.4**;
- **MV/HV switchgear — 4.4**;
- **integrated data-centre electrical backbone — 4.3**.

### Strongest nuclear supply-chain bottlenecks

- **HALEU enrichment / deconversion — 4.7**, but mainly 2030s advanced-reactor demand;
- **Western LEU enrichment — 4.6**;
- **large nuclear forgings / heavy components — 4.5**;
- **nuclear EPC / QA / qualified workforce — 4.4**;
- **UF6 conversion — 4.3**.

### Moderate / integration bottlenecks

- DTC cooling function — 4.2;
- facility heat rejection — 4.2;
- integrated BTM architecture — 4.1.

### Growth layers that do not currently pass scarcity Gate A

- generic cold plates / CDUs — ~3.8 supplier scarcity;
- rack-level generic power components — ~3.8;
- gensets — 3.6;
- generic 800 VDC ecosystem — 3.6;
- uranium mining — 3.5;
- generic BESS — 3.4.

---

## 21. What #52 must decide

The E2E map is now sufficiently complete to stop broad discovery.

Issue #52 should rank the validated functions by more than Bottleneck Strength. It must weight:

1. direct AI earnings sensitivity;
2. supplier concentration;
3. pricing / margin / reservation evidence;
4. architecture resilience;
5. time to add qualified capacity;
6. service / installed-base economics;
7. capital intensity / overbuild risk;
8. non-AI demand support;
9. timing — 2026–2030 versus 2030s;
10. availability of investable listed suppliers with meaningful company-level sensitivity.

Only a small top tier should proceed to Investment Capture #53.

---

## 22. Core interpretation

**FACT:** Multiple independent deep dives now show direct capacity-reservation, backlog, lead-time, prepayment, qualification and expansion evidence across turbines, transformers, electrical equipment, cooling and nuclear fuel / manufacturing.

**INTERPRETATION:** The AI-energy buildout is best understood as a **serial constrained system**, not a commodity-demand story.

**HYPOTHESIS:** The best risk-adjusted investments will be suppliers that satisfy four conditions simultaneously:

> **own a validated bottleneck + remain necessary as architecture changes + convert scarcity into margin / service economics + remain small / cheap enough for the earnings change to matter.**

That hypothesis is the starting point for #52 and #53, not a conclusion about any individual stock.

---

## Canonical supporting research

- `research/energy/thesis.md`
- `research/energy/research-plan.md`
- `research/energy/deep-dives/transformers-grid-equipment.md`
- `research/energy/deep-dives/transmission-large-load.md`
- `research/energy/deep-dives/dispatchable-generation.md`
- `research/energy/deep-dives/electrical-backbone-800vdc.md`
- `research/energy/deep-dives/behind-the-meter-microgrids.md`
- `research/energy/deep-dives/cooling-heat-rejection.md`
- `research/energy/deep-dives/nuclear-supply-chain.md`

The underlying deep dives contain recoverable primary / standards / regulatory source URLs and the contradictory evidence supporting each score.
