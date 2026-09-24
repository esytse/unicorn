# Sensing / physical-world data bottlenecks

**Issue:** #173  
**Date:** 2026-09-24  
**Status:** discovery screen — first pass  
**Parent:** `research/cross-theme/scarce-complement-map.md`

## Research question

Which sensing modalities remain scarce enough to support durable supplier rents as Physical AI scales, rather than simply benefiting from higher unit demand?

## First-pass conclusion

**The investable bottleneck is not "sensors" generically.** Commodity cameras, IMUs and many discrete sensors face integration, price erosion and multi-sourcing. The more defensible lanes combine difficult physics with qualification, calibration, perception software, installed developer ecosystems or application-specific certification.

The strongest current lanes for further underwriting are:

| Lane | Scarcity / capture hypothesis | Main release risk | First listed screen |
|---|---|---|---|
| 3D lidar + perception | range/precision, reliability, calibration and perception integration can create qualification + ecosystem switching costs | rapid ASP decline, solid-state/vision substitution, OEM insourcing | **Ouster (OUST)** |
| Industrial machine vision + 3D depth | factory qualification, application libraries, installed base and integration know-how can matter more than camera BOM | cheaper AI vision, generic cameras, integrator capture | **Cognex (CGNX)** |
| High-end image sensors | process/IP/yield and stacked sensor capability can retain economics at the premium edge | smartphone concentration, capacity catch-up, module/platform integration | **Sony Group (SONY)** |
| Precision metrology / 3D measurement | accuracy, calibration, workflow/software and certification can create durable switching costs | cyclic industrial capex, software abstraction | **Hexagon AB** / metrology peers |
| Safety-grade multimodal perception | certification + redundancy across lidar/camera/radar may become a release gate | platform vendors bundle sensing/perception | screen through QNX-adjacent ecosystem; listed pure plays still weak |

## Why Ouster moves to the front of the discovery queue

Current primary evidence makes Ouster the cleanest **economic-capture test**, not yet a Gate-E promotion.

- Q2 2026 revenue was **US$55m, +56% y/y**; product revenue was **US$53m, +51%**.
- More than **17,000 lidar + camera sensors** shipped in Q2; lidar was ~53%.
- GAAP gross margin reached **49%** and non-GAAP gross margin **53%**.
- Demand cited by the company is already industrial/smart-infrastructure: warehouse automation, yard logistics and intelligent transportation.
- The Stereolabs combination expands the stack from lidar toward cameras, AI compute, sensor fusion and perception software.

### What must be proved before promotion

1. **Normalised margin:** Q2 benefited from a one-time COGS refund; prove sustainable product economics without one-offs.
2. **Price vs volume:** unit growth must outrun ASP erosion and not rely on uneconomic pricing.
3. **Customer retention / qualification:** show repeat deployments and evidence that switching is costly.
4. **Software/perception capture:** prove the unified stack increases recurring or higher-margin economics rather than merely expanding hardware BOM.
5. **Competitive substitution:** test camera-only, radar, alternative lidar architectures and platform bundling.
6. **Cash conversion:** adjusted EBITDA remains negative; growth must translate to durable FCF.
7. **Valuation:** only after the above should Gate-E test 18-month asymmetry.

## Cognex / RealSense: important new validation

On 22 Sep 2026 Cognex announced a definitive agreement to acquire RealSense for about **US$500m** from existing cash. Cognex says RealSense should generate **US$80–90m 2026 revenue**, >50% growth, and estimates robotic perception at ~US$600m today growing >25% annually to ~US$1.6bn by 2030.

This is strategically useful evidence: an established industrial machine-vision company is paying to add 3D depth perception, proprietary technology and a developer community rather than assuming generic 2D cameras are sufficient.

It does **not** prove sector-wide scarcity or validate the buyer's valuation. The next Cognex underwrite should test whether RealSense adds a durable robotic-perception moat or simply moves Cognex into a faster-growing but increasingly commoditised hardware category.

## Modality tests

### Commodity RGB cameras — LOW scarcity by default
High unit growth is plausible, but generic hardware is readily sourced. Promote only where stacked sensor/process technology, specialised spectral capability or application qualification creates measurable economics.

### 3D depth / stereo — MEDIUM
Depth is more valuable for manipulation/navigation, but hardware can commoditise. Durable capture is more likely in calibration, developer ecosystem, perception models and qualified deployment.

### Lidar — MEDIUM, potentially HIGH in qualified niches
Physics/performance and reliability matter, but historical lidar pricing shows severe commoditisation risk. The investable case requires evidence of volume + margin + repeat deployment simultaneously.

### Radar — MEDIUM
Weather robustness and safety redundancy are useful, but automotive scale and semiconductor integration can shift rents toward chip/platform vendors.

### Force/tactile sensing — HIGH technical importance, LOW current public capture confidence
Manipulation needs feedback, but public listed exposure is fragmented and economics are not yet material enough for promotion.

### Precision metrology — MEDIUM-HIGH
Where sensing becomes measurement used for release/quality decisions, calibration, traceability and workflow integration can support stronger switching costs than generic perception.

## Scarcity / capture scorecard

| Test | Ouster | Cognex + RealSense | Generic sensor vendor |
|---|---|---|---|
| Physics / performance differentiation | High | Medium-High | Low-Medium |
| Qualification / switching | Medium, to prove | High in legacy machine vision; RealSense to prove | Low |
| Software / ecosystem leverage | Improving | Potentially High | Low |
| Current revenue materiality | High | High | varies |
| Current profitability | Not yet durable | Established parent profitability | varies |
| Commoditisation risk | High | Medium | High |
| **Research priority** | **P1 Gate-D candidate** | **P1 strategic-event underwrite** | **Reject unless special evidence** |

## Falsification

Downgrade the sensing lane if:
- shipment growth is accompanied by structural ASP/gross-margin compression;
- perception software is bundled free by compute/platform vendors;
- customers multi-source without qualification friction;
- camera/radar/lidar substitution prevents supplier-specific pricing;
- sensor capex grows but supplier FCF does not;
- physical-AI deployments remain pilot-heavy rather than production-scale.

## Next actions

1. Open a bounded **Ouster Gate-D/Gate-E candidate underwrite**: normalised margins, ASP/unit bridge, customer concentration, repeat deployment, Stereolabs economics, valuation.
2. Open a **Cognex/RealSense event underwrite**: transaction economics, depth-camera moat, developer ecosystem and post-deal earnings contribution.
3. Screen Sony/Hexagon only after these two tests; they are more diversified and sensing exposure may be too diluted for Unicorn's 18-month return requirement.
4. Keep tactile/force sensing on discovery watch until listed revenue exposure becomes material.

## Sources reviewed

- Ouster Q1/Q2 2026 and FY2025 investor releases.
- Ouster investor materials on Stereolabs/unified sensing and perception.
- Cognex / RealSense 22 Sep 2026 acquisition announcement and SEC-filed release.
- IFR 2026 humanoid-robot deployment data used only as adoption context, not as a TAM valuation input.
