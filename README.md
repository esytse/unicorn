# Unicorn Research

A collaborative research repository for identifying emerging companies and technologies with asymmetric upside, especially where structural bottlenecks create durable value.

Git history is the authoritative version record. Do not create duplicate files such as `final-v2.md` or `revised-final.md`; update the canonical document and let Git preserve the history.

## Research streams

- `research/memory/` — AI memory, data movement, interfaces and related bottlenecks
- `research/robotics-actuators/` — robotics actuator value chain and emerging players
- Additional themes can be added under `research/` without creating a new repository

## Key files

- `AGENTS.md` — mandatory operating instructions for any AI agent working in this repository
- `CHANGELOG.md` — human-readable record of substantive research changes
- `watchlist.md` — cross-theme research candidates and current status
- `sources/source-register.md` — source provenance register
- `CONTRIBUTING.md` — simple workflow for collaborators who do not use Git day to day

## Default workflow

1. Ask an agent to read `AGENTS.md` before doing anything.
2. The agent researches or updates the requested theme.
3. The agent edits the canonical Markdown files on a branch.
4. The agent updates `CHANGELOG.md` for substantive changes.
5. The agent opens a pull request and summarises what changed, why, and what remains uncertain.
6. A human reviews the diff before merge.

The agent should not merge its own substantive research changes.

## Example instruction to an agent

> Read `AGENTS.md` and the relevant existing research first. Research the actuator opportunity, update the canonical documents with sourced evidence, mark facts vs inference vs hypothesis, update the changelog if conclusions change, and open a pull request for review. Do not merge it.

## Research principles

- Evidence before narrative
- Facts, interpretation and hypotheses are clearly separated
- Conflicting evidence is preserved rather than hidden
- Thesis changes are explicit and traceable
- Uncertainty and confidence are recorded
- Sources should be attributable and recoverable
