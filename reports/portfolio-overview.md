# Portfolio Overview

Current phase: **Census + Structural Triage**, with portfolio audit running as a **non-blocking parallel track**.

## Operating model

Portfolio review is now governed by a branch-aware evidence model. The review unit is not the repository name alone; for material technical claims it is `repository + branch/ref + commit + inspected surface`.

Review depth is progressive (D0-D4), and repository state, evidence class, claim status, assumptions, suggestions, decisions, relationships, unknowns, and contradictions are kept separate.

The durable operating documents are:
- `docs/PORTFOLIO_OPERATING_MANUAL_v0.2.md`
- `docs/REPOSITORY_REVIEW_PROTOCOL_v0.1.md`
- `docs/REVIEW_PACKET_TEMPLATE_v0.1.md`
- `schema/repository-review.schema.json`
- `schema/relationship.v0.2.schema.json`

## Census

The canonical stored census contains **313 deduplicated repositories**, collected on 2026-08-30 from four search pages (100/100/100/13).

This is an accessible census snapshot, not a proof that every possible repository surface is included. A later direct GitHub observation on 2026-09-18 exposed a larger accessible set, but it has not been promoted to the canonical inventory yet.

The census must be deliberately refreshed and reconciled before the stored repository set is replaced or promoted.

## Structural triage rule

We inspect evidence-bearing surfaces before interpreting a repository:

- root tree;
- README and maintained documentation;
- dependency/package manifests;
- tests and test configuration;
- CI/workflow configuration;
- deployment artifacts;
- specialized research or engineering artifacts.

A file's presence is a **signal**, not proof of correctness. Documentation claims are not verification. Missing evidence is `UNKNOWN` unless the relevant surface was actually inspected.


## Repository review standard

The structural triage phase now uses a dedicated operational protocol and machine-readable review contract:

- `docs/REPOSITORY_REVIEW_PROTOCOL_v0.1.md`
- `schema/repository-review.schema.json`

The standard requires repository + branch/ref + commit provenance, separates current/research/historical state, and keeps claims, assumptions, suggestions, experiments, and cross-repository relationships distinct.

## Operating rule

Active projects continue on their own valid tracks.

The portfolio audit does **not** become a prerequisite for project execution. Instead, portfolio review advances incrementally and records durable findings as they become sufficiently evidenced.

Portfolio-level synthesis must not be confused with final architecture selection. Until the evidence supports a stronger conclusion:

- project-local architecture remains authoritative;
- unresolved relationships remain unresolved;
- small reversible reuse is preferred;
- global merges/extractions are not required;
- old, sparse, or duplicated-looking repositories are not discarded without evidence.

## Initial findings

Five repositories have received a targeted structural pass:

| Repository | Current triage signal | Priority |
|---|---|---|
| `ai-meta-orchestrator` | Nontrivial application structure; CI, Jest, package lock, Docker; README quality is weak/template-like | High |
| `canonical-capability-core` | Substantial research/engineering baseline with explicit contracts, evidence, execution, reconciliation and verification artifacts | High |
| `algeria-ai-product-fabric` | Platform/research monorepo with separated core, adapters, domains, evals and an explicit document-decision vertical | High |
| `Software-res` | v0.2.0 evidence-validation PoC with explicit release scope and verification/non-claims | High |
| `Healer-` | Large mixed mathematical/native/experimental system; strong claims require independent verification | High |

Detailed records are in `inventory/triage.json`.

## Relationships discovered for deeper review

The first pass identifies relationship **candidates**, not finalized lineage:

- `Software-res` ↔ `canonical-capability-core`: possible shared evidence/execution design lineage.
- `algeria-ai-product-fabric` ↔ `canonical-capability-core`: possible reuse/composition of evidence-governed primitives.
- `Healer-` ↔ `-Fiber-Stratified-Optimization---FSO-`: possible FSO relationship based on repository terminology; target not yet inspected.
- `algeria-multi-agent-platform` ↔ `algeria-multiagent-platform`: probable duplicate/successor candidate because of near-identical naming; requires content and history comparison.

## Next gate

There is **no stop-the-world portfolio gate**.

Continue active project work. In parallel, expand structural triage across the portfolio and selectively deep-review clusters or repositories when doing so can materially improve an active project, establish durable lineage, reduce duplicated complexity, or reduce future integration risk.

Do not promote a candidate relationship to established lineage without content/history evidence.
