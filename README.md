# Unicorn Research

A collaborative research repository for identifying emerging companies and technologies with asymmetric upside, especially where structural bottlenecks create durable value.

Git history is the authoritative version record. Do not create duplicate files such as `final-v2.md` or `revised-final.md`; update the canonical document and let Git preserve the history.

## Research streams

- `research/physical-ai/` — umbrella Physical AI value chain: data, simulation, embodied models, edge compute, sensing, deployment and cross-embodiment bottlenecks
- `research/robotics-actuators/` — embodiment-specific actuator / precision-motion substream within Physical AI
- `research/memory/` — AI memory, data movement, interfaces and related bottlenecks
- `research/energy/` — AI/data-centre energy, grid, power-delivery and speed-to-power bottlenecks
- Additional themes can be added under `research/` without creating a new repository

## Key files

- `AGENTS.md` — mandatory operating instructions for any AI agent working in this repository
- `CHANGELOG.md` — human-readable record of substantive research changes
- `watchlist.md` — cross-theme research candidates and current status
- `sources/source-register.md` — source provenance register
- `CONTRIBUTING.md` — simple workflow for collaborators who do not use Git day to day
- `research/_templates/` — reusable structures for new themes and company deep dives

## Default workflow

1. Ask an agent to read `AGENTS.md` before doing anything.
2. The agent researches or updates the requested theme.
3. The agent edits the canonical Markdown files on a branch.
4. The agent updates sources and `CHANGELOG.md` where required.
5. The agent opens a pull request that records what changed, why, evidence, confidence and uncertainty.
6. Automated governance checks run.
7. If the checks pass, the PR can auto-merge. Human approval is not required by default.

Pull requests are primarily an audit trail and safety boundary, not a manual approval queue.

If someone prefers not to formulate an agent prompt directly, GitHub's **Research request** issue template can capture the question and starting context in a structured way.

## Example instruction to an agent

> Read `AGENTS.md` and the relevant existing research first. Research the requested Physical AI bottleneck, update the canonical documents with sourced evidence, mark facts vs interpretation vs hypothesis, update the changelog if conclusions change, open a pull request, and merge only after required checks pass.

## When to request manual review

Manual review is optional. Ask for it when you specifically want a second pair of eyes before a conclusion enters `main`, for example a major thesis reversal or an unusually consequential decision.

## Research principles

- Evidence before narrative
- Facts, interpretation and hypotheses are clearly separated
- Conflicting evidence is preserved rather than hidden
- Thesis changes are explicit and traceable
- Uncertainty and confidence are recorded
- Sources should be attributable and recoverable
