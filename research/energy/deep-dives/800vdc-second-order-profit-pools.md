# 800 VDC Second-Order Profit Pools — Concentration Test

**Status:** Narrow sub-layer concentration test complete; no 800 VDC sub-layer passes supplier-scarcity Gate A yet  
**Backlog:** #73  
**Last substantive update:** 2026-09-08  
**Confidence:** High that 800 VDC is an architecture transition; Medium-High that supplier concentration is currently insufficient for a new bottleneck thesis

## Executive conclusion

**CONCLUSION:** The move to 800 VDC is becoming more credible and more standardized, but the evidence continues to **falsify a broad supplier-scarcity thesis**. Even after going one level deeper into conversion, DC protection, busway, power semiconductors and energy storage, no narrow layer yet combines all four requirements needed for a new Gate-A investment bottleneck:

1. unavoidable function;
2. concentrated qualified supply;
3. difficult switching / process-of-record lock-in;
4. visible pricing / margin / backlog capture.

The most technically interesting narrow function is **fast, selective DC fault protection / solid-state and hybrid breakers**. DC fault interruption is genuinely harder than AC protection because current does not naturally cross zero and capacitor discharge creates severe di/dt / coordination problems. But the supplier market is already forming around multiple capable players: ABB has an IEC-certified high-voltage DC breaker platform, Eaton has a complete 100–2,000 A 800 VDC solid-state / hybrid breaker line in engineering samples, and the broader NVIDIA/OCP architecture deliberately defines common interfaces for interoperable hardware.

Similarly:

- **MVAC-to-800 VDC / solid-state transformer (SST) blocks** are strategically important but remain an open specification with ABB, Eaton, GE Vernova, Hitachi Energy, Siemens, Heron Power and others developing approaches.
- **800 VDC-to-low-voltage DC/DC** is technologically demanding but has a very broad silicon ecosystem: Infineon, Analog Devices, MPS, Navitas, Onsemi, Renesas, ROHM, STMicroelectronics, Texas Instruments, Power Integrations and others.
- **power racks / sidecars / busway / BBU** are being developed by Delta, Flex, LiteOn, Megmeet, Eaton, Vertiv, Schneider and multiple ODMs.

The key conclusion is:

> **800 VDC is likely to create a large equipment cycle and content migration, but the standard is being designed to prevent exactly the kind of single-vendor lock-in we are searching for.**

The existing broad supplier-scarcity score of roughly **3.6 / 5 remains appropriate**. No company is added to the watchlist from #73.

---

## 1. Why 800 VDC matters

**FACT:** NVIDIA, Google and Microsoft are standardizing 800 VDC through the Open Compute Project for next-generation AI factories.

**FACT:** NVIDIA says the architecture is intended to support megawatt-scale racks, reduce conversion stages, reduce copper / cable bulk and improve end-to-end power efficiency.

**FACT:** Full-scale native 800 VDC infrastructure is aligned with 2027-era NVIDIA Kyber systems, while hybrid MGX-compatible 800 VDC power racks provide an earlier transition path in existing AC facilities.

**FACT:** OCP / NVIDIA reported in August 2026 that **more than 80 equipment manufacturers and infrastructure companies** are already building to the specification.

**INTERPRETATION:** This strengthens the *architecture adoption* thesis but weakens the *supplier scarcity* thesis. The ecosystem is being formed before volume deployment, with interoperability as an explicit design objective.

---

## 2. Common-basis narrow-layer ranking

| Sublayer | Functional difficulty / importance | Current supplier concentration | Qualification / switching | Capture evidence | Supplier-scarcity conclusion |
|---|---:|---:|---:|---:|---|
| **DC fault protection / SSCB / hybrid breaker** | **4.5** | 3.3 | 4.0 | 3.2 | **Best narrow watch; ~3.7/5, no Gate A yet** |
| MVAC-to-800 VDC / SST / transformer-rectifier block | **4.4** | 3.2 | 3.8 | 3.1 | ~3.6/5; architecture unsettled / multi-vendor |
| 800 VDC-to-48/12 V high-density DC/DC | 4.2 | 2.8 | 3.6 | 3.1 | ~3.4/5; very broad semiconductor ecosystem |
| DC busway / high-current connectors / distribution | 4.0 | 3.0 | 3.5 | 3.2 | ~3.4/5; content growth, weak concentration evidence |
| DC-native BBU / energy-storage integration | 4.0 | 2.9 | 3.4 | 3.1 | ~3.3/5; multiple architectures / vendors |
| power semiconductor devices (SiC / GaN / silicon) | 4.1 | 2.6 | 3.2 | 3.3 | ~3.2/5; technology growth rather than supply chokepoint |

These are **research scores, not investment recommendations**.

---

## 3. DC protection — strongest technical chokepoint, not yet a supplier bottleneck

### 3.1 The technical problem is real

**FACT:** NVIDIA's 800 VDC architecture places overcurrent protection devices at multiple boundaries between the power room, hall, row and IT rack.

**FACT:** NVIDIA explicitly identifies fuse/disconnect combinations, emerging solid-state devices and safety breakers as required protection approaches.

**FACT:** Eaton's 800 VDC technical material describes fast capacitor-discharge transients as a challenge for traditional protection. Selective coordination requires protection devices that can detect and interrupt severe DC fault currents fast enough without unnecessarily taking down upstream equipment.

**INTERPRETATION:** Protection is one of the few 800 VDC functions where higher voltage creates a genuinely new reliability / safety qualification problem rather than simply scaling an existing component.

### 3.2 But multiple credible suppliers are already present

**FACT:** ABB's SACE Infinitus is presented by ABB as the first IEC-certified circuit breaker designed to make DC viable in high-voltage environments.

**FACT:** Eaton's 2026 architecture material shows a **100 A–2,000 A** line of 800 VDC solid-state and hybrid solid-state circuit breakers, with engineering samples available in 2026 and customer pilot programs being sought.

**FACT:** Eaton and ABB are both collaborating directly with NVIDIA on 800 VDC architectures, alongside Schneider Electric, Vertiv and multiple other electrical-platform companies.

**INTERPRETATION:** DC protection should remain a monitoring lane because early qualification could still concentrate around a handful of platforms. But current evidence is already inconsistent with a single process-of-record or two-supplier chokepoint.

**Score: ~3.7 / 5 supplier scarcity — no Gate A.**

**OPEN QUESTION:** Which breaker designs earn production qualification at hyperscaler scale in 2027, and does field reliability create durable incumbent lock-in after the open-standard phase?

---

## 4. MVAC-to-800 VDC / SST — high-value architecture block, intentionally open

**FACT:** OCP's 2026 work includes an **LVDC Solid-State Transformer specification**, and NVIDIA describes a future facility-scale DC power block that converts medium-voltage AC toward 800 VDC in a much more direct path.

**FACT:** NVIDIA's current partner ecosystem includes ABB, Eaton, GE Vernova, Hitachi Energy, Mitsubishi Electric, Siemens, Schneider Electric, Vertiv and Heron Power among other infrastructure participants.

**FACT:** ABB's 800 VDC technical roadmap explicitly lists high-efficiency MVAC-to-LVDC converters as a core technology to be developed.

**INTERPRETATION:** This function can become a high-value system block because it combines transformation, conversion, protection and controls. But the architecture is still under development, and the specification is being standardized before commercial volume. At this stage, a platform company that can integrate the block is more plausible than a narrow merchant monopoly.

**Score: ~3.6 / 5 supplier scarcity — no Gate A.**

### Jinpan SST optionality

Hainan Jinpan's 13.8 kV North-American-grid SST prototype remains relevant evidence that smaller manufacturers can enter this layer. But that same entry evidence weakens the case for assuming only one or two global suppliers will dominate. SST remains optionality, not base-case earnings.

---

## 5. High-density DC/DC — important technology, too many credible silicon paths

**FACT:** Infineon introduced 800 VDC high-voltage intermediate-bus-converter reference designs in March 2026 using CoolGaN devices, including 800-VDC-to-50-V and 800-VDC-to-12-V approaches.

**FACT:** Infineon also introduced 30 kW 800 VDC-capable server power solutions and a 24 kW SiC battery-backup reference design that connects directly to an 800 V DC bus.

**FACT:** NVIDIA's silicon ecosystem includes Analog Devices, Infineon, Innoscience, MPS, Navitas, Onsemi, Power Integrations, Renesas, Richtek, ROHM, STMicroelectronics, Texas Instruments, AOS and others.

**INTERPRETATION:** Power-density requirements create large semiconductor content growth and can support strong individual products, but there is no evidence today of a sufficiently concentrated silicon process-of-record to classify 800 VDC DC/DC as a structural supplier bottleneck.

**Score: ~3.4 / 5.**

---

## 6. Power racks / sidecars / busway — product opportunity, not demonstrated scarcity

**FACT:** NVIDIA's hybrid transition uses MGX-compatible 800 VDC power racks before native facility-level deployment.

**FACT:** LiteOn presented 330 kW, 660 kW and 1.2 MW 480 VAC-to-800 VDC systems under development alongside 800 VDC DC/DC shelves / modules.

**FACT:** Delta has publicly presented its own 800 VDC and modular data-center solutions. Eaton, Schneider, Vertiv, Flex, Megmeet and other power-system suppliers are also part of the ecosystem.

**INTERPRETATION:** There may be excellent companies in this layer, but product count and multi-vendor participation are expanding before high-volume rollout. The evidence currently supports **volume / content growth**, not a hard-to-substitute merchant bottleneck.

**Score: ~3.4 / 5.**

---

## 7. DC-native BBU / storage — architecture still fluid

**FACT:** NVIDIA includes integrated, multi-time-scale energy storage in its high-voltage architecture because AI loads can change rapidly and facilities need buffering / ride-through capability.

**FACT:** Infineon's 24 kW 800 VDC BBU reference design demonstrates direct high-voltage battery-to-bus conversion with >99% efficiency.

**INTERPRETATION:** Storage integration is important, but the function can be implemented through multiple battery, UPS, BBU and facility-storage architectures. This increases substitution and weakens a narrow hardware scarcity thesis.

**Score: ~3.3 / 5.**

---

## 8. The open-standard design is the strongest falsification evidence

The most important evidence in #73 is not a component announcement. It is the architecture's governance model.

**FACT:** Google, Microsoft and NVIDIA explicitly say they are working through OCP to establish an **open, standardized** 800 VDC architecture that can be adopted broadly.

**FACT:** NVIDIA says specifications define common interfaces so hardware from different vendors can operate in the same facility.

**FACT:** More than 80 ecosystem companies are participating before mass deployment.

**INTERPRETATION:** Standardization can accelerate the total market while **reducing supplier lock-in**. It may create very large revenue pools without creating the kind of scarcity economics that the unicorn research framework is designed to find.

This is the same distinction established elsewhere in the energy work:

> **Technology adoption ≠ supplier concentration ≠ investment asymmetry.**

---

## 9. What #73 changes

It does **not** change the existing ~3.6 / 5 broad 800 VDC supplier-scarcity score.

It refines the monitoring hierarchy:

1. **DC fault protection / solid-state & hybrid breakers** — highest-priority narrow watch.
2. **MVAC-to-800 VDC / SST blocks** — potentially high-value system integration lane.
3. **high-density DC/DC** — large semiconductor opportunity, currently too many credible suppliers.
4. **busway / sidecar / power racks** — strong content cycle, weak concentration evidence.
5. **DC-native BBU / storage** — important but highly substitutable architecture.

No company is promoted or given a dedicated underwriting issue from #73. Any future reopening should require **production qualification / process-of-record evidence, meaningful market-share concentration, pricing or margin evidence, or failure of competing vendors to qualify**.

The next step remains #74: compare the second-order results across transformer OLTCs, turbine hot-section components and 800 VDC. On current evidence, **OLTCs / Huaming are the only new second-order lane that clearly improves the candidate-discovery frontier**.

---

## Sources

Primary / standards / company:

- NVIDIA 800 VDC architecture: https://www.nvidia.com/en-eu/data-center/technologies/800-vdc-architecture/
- NVIDIA August 2026 architecture / OCP update: https://blogs.nvidia.com/blog/800-vdc-power-architecture-ai-factory/
- Open Compute Project, Google / Microsoft / NVIDIA standardization, 2026-08-11: https://www.opencompute.org/index.php/blog/powering-the-next-era-of-ai-how-google-microsoft-and-nvidia-are-standardizing-and-accelerating-the-industry-transition-to-lvdc
- NVIDIA 800 VDC technical architecture: https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/
- ABB / NVIDIA 800 VDC collaboration: https://new.abb.com/news/detail/129805/abb-to-develop-next-generation-ai-data-centers-with-nvidia
- ABB 800 VDC white paper: https://resources.news.e.abb.com/attachments/published/129788/en-US/3515A12A5C51/ABB_800_VDC_NVIDIA_white_paper.pdf
- Eaton 800 VDC architecture: https://www.eaton.com/gb/en-gb/company/news-insights/news-releases/2025/eaton-unveils-next-generation-architecture.html
- Eaton 800 VDC technical architecture / protection: https://ewh.ieee.org/r3/nashville/events/2026/Eaton_DC%20Next%20Gen%20Architecture%20-%20202602%20-%20IEEE.pdf
- Infineon 800 VDC HV IBC: https://www.infineon.com/technology-news/2026/infpss202603-067
- Infineon 800 VDC BBU: https://www.infineon.com/technology-news/2026/infpss202606-093
- Infineon 800 VDC-capable 30 kW power solution: https://www.infineon.com/technology-news/2026/infpss202606-094
- LiteOn NVIDIA GTC 2026 800 VDC power systems: https://www.nvidia.com/gtc/session-catalog/sessions/gtc26-ex82089/
- Delta NVIDIA GTC 2026 800 VDC session: https://www.nvidia.com/en-us/on-demand/session/gtc26-s82097/
