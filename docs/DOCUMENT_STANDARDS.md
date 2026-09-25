# Governed document metadata standard

**As of:** 2026-09-25  
**Lifecycle:** GUIDANCE  
**Purpose:** keep authority, freshness and provenance legible without turning research into form-filling.

## Minimal rule

Metadata is **selective**. Add a field only when it resolves a real authority, freshness, versioning or provenance question. Existing documents do not need wholesale retrofitting merely to satisfy a template.

| Field | Use when |
|---|---|
| `Lifecycle` | the document could be mistaken for live authority or generated/derived state |
| `As of` / `Last substantive update` | a decision or research conclusion can become stale |
| `Concept` | a document explicitly declares `Authority: CANONICAL` |
| `Methodology/version` | interpretation depends on a named method/schema/version |
| `Canonical upstream` | a derived document has one authoritative input |
| `Upstream authorities` | a derived synthesis has several authoritative inputs |
| `Supersedes` / `Superseded-by` | a real document-level replacement exists |
| `Owner/workstream` | responsibility is otherwise ambiguous |
| `Evidence status` | evidence maturity materially constrains the conclusion |

Allowed lifecycle values are **CANONICAL, DERIVED, HISTORICAL, GUIDANCE, LOG, ARCHIVE**.

## Research semantics

Research must continue to distinguish **FACT**, **INTERPRETATION**, **HYPOTHESIS** and **OPEN QUESTION**. A metadata header does not replace that separation.

Company and theme templates therefore expose lifecycle/freshness and the four evidence semantics, while leaving version, supersession and ownership optional until they add information.

## Authority and derivation

A DERIVED document must identify its upstream authority or authorities and must not describe itself as canonical. A HISTORICAL or ARCHIVE document must not silently become the current decision surface. The repository-wide authority map remains `docs/REPOSITORY_GOVERNANCE.md`.

## Supersession

Use supersession only for an intentional replacement. Paths must resolve. Prefer a stable canonical path plus Git history over creating `v2`, `final`, or date-suffixed copies.

## Validation

`scripts/repo_integrity.py` validates declared lifecycle values, prevents DERIVED documents from claiming canonical authority, requires declared DERIVED documents to identify upstream authority, and validates concrete lifecycle/supersession paths. The checks apply when a document opts into an explicit lifecycle contract; they do not force metadata onto every historical file.
