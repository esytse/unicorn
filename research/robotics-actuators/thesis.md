# Robotics Actuators — Working Thesis

**Status:** Active Gate-A discovery  
**Confidence:** **Medium on architecture decomposition; Low-Medium on supplier bottlenecks**  
**Last substantive update:** 2026-09-08

## Current thesis

**INTERPRETATION:** Advanced-robot actuation should not be researched as a single "actuator manufacturer" market. The investable question is which **motion-conversion and industrialization functions** remain difficult to substitute after robot architectures, supplier competition and vertical integration mature.

The initial E2E map identifies four distinct actuation economies:

1. **high-ratio rotary joints** using strain-wave, cycloidal/RV or precision planetary transmission;
2. **low-ratio / quasi-direct-drive rotary joints** prioritizing backdrivability and control bandwidth;
3. **linear joints** using planetary roller screws / ball screws where very high force over short stroke is attractive;
4. **dexterous hands**, whose microactuation, bearing, wiring and force/tactile sensing problems differ from body joints.

No single architecture currently appears capable of winning every body zone.

## Strongest preliminary bottleneck hypotheses

These are research priorities, not completed Gate-A findings:

1. **Planetary roller screws / high-force linear conversion — 4.4 preliminary.** Precision thread/roller manufacture, preload and load sharing may create a narrow process moat, but adoption is architecture-dependent.
2. **Precision strain-wave reducer manufacture — 4.3 preliminary.** Compact high-ratio/low-backlash performance is important, but Chinese mass production and alternative architectures weaken any thesis of permanent incumbent scarcity.
3. **Integrated actuator industrialization / calibration — 4.3 preliminary.** Repeatable tolerance stack, preload, encoder zero, torque calibration, thermal behavior, EOL test and field reliability may be harder to scale than individual catalog components.
4. **Dexterous-hand microactuation — 4.1 preliminary.** Miniaturization and force control are difficult, but winning hand architecture remains highly uncertain.
5. **Compact cycloidal/RV — 4.1 preliminary.** Strong rigidity/shock performance; humanoid share is not yet established.
6. **Precision planetary / QDD — 4.0 preliminary.** Dynamic performance is attractive, but the gear-making supplier base is broader and large motors/thermal load can offset the mechanical advantage.

## Early evidence that changes the original thesis

**FACT:** Schaeffler's humanoid BOM model estimates rotary actuator integration at ~25% and linear actuator integration at ~30%, with dexterous hands at ~20%. This is a supplier estimate, not an industry standard, but it is strong evidence against researching humanoids as a harmonic-reducer-only opportunity.

**FACT:** In 2026 Schaeffler disclosed actuator supply partnerships with Humanoid and Hexagon Robotics. Humanoid says its five-year agreement makes Schaeffler preferred supplier for more than half of its wheeled-platform joint-actuator demand through 2031 and is expected to represent a **seven-digit number of actuators**.

**FACT:** Harmonic Drive Systems previously disclosed prototype supply to multiple humanoid startups and mass production for some customers, while its 2026 plan identifies AI robots as a focus area.

**FACT:** Laifual's 2026 Hong Kong listing document says it was one of two Chinese manufacturers that had achieved mass-production/delivery of harmonic reducers for humanoid robots by end-2025.

**INTERPRETATION:** The reducer opportunity remains real, but the likely moat is increasingly **qualified precision manufacturing + life consistency + joint integration**, not ownership of a gearbox concept or historical patent position.

## What may not be bottlenecks

Current preliminary scores keep these below the main Gate-A line until stronger evidence emerges:

- frameless motors — high content but broad supplier base;
- encoders / resolvers — technically critical but multiple sensing architectures;
- general bearings — very high unit content but global supply breadth;
- servo drives / power electronics — mature ecosystem;
- brakes / locks — joint-dependent and relatively substitutable;
- thermal / lubrication — physically critical but economic capture may be diffuse.

A component can be an excellent volume beneficiary without becoming a scarce profit pool.

## Key thesis tension

The central tension is now:

> **Will value remain in specialist precision components, or migrate into integrated actuator platforms and high-volume industrialization?**

Schaeffler is direct evidence that automotive/industrial motion suppliers can enter the humanoid stack with complete planetary, strain-wave and linear actuator platforms. Harmonic Drive Systems and Nabtesco remain important specialist benchmarks, while Chinese strain-wave suppliers provide strong falsification against assuming permanent Japanese scarcity.

## Thesis breakers

- Rapid standardization / easy multi-sourcing of complete actuator modules
- Robot OEM vertical integration of gearboxes, motors, sensing and calibration
- Comparative lifetime data showing lower-cost reducers/screws are good enough
- Humanoids remaining low-volume or shifting to lower-DOF/wheeled/simpler architectures
- Dexterous hands losing to simple end-effectors or underactuated grippers
- Lower-limb architecture moving away from roller screws before scale
- Automotive-scale entrants eliminating specialist capacity scarcity faster than demand grows
- Strong technology exposure that does not move total-company earnings

## Active research programme

- **#78** rotary reducer architectures — P1
- **#79** linear actuators / roller screws — P2
- **#80** dexterous-hand microactuation — P3
- **#81** motors / encoders / force sensing / bearings — P4
- **#82** drives / brakes / thermal / industrialization — P5
- **#83** common-basis synthesis and Gate-B shortlist — P6

See `value-chain.md` for the E2E map and `research-plan.md` for evidence standards and completion gates.

## Current company treatment

No company is promoted to `Watch` or high conviction from the E2E map alone.

Current evidence-backed benchmarks/candidates for later Gate-B work include:

- Harmonic Drive Systems;
- Nabtesco;
- Schaeffler / Ewellix;
- MinebeaMitsumi;
- selected Chinese strain-wave suppliers where primary production/customer evidence can be recovered;
- specialist sensing/bearing/linear-motion suppliers only if #79–#81 establish real scarcity.

Company status must wait for the architecture-specific Gate-A work.
