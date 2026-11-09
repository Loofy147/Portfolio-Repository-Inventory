# Portfolio Repository Inventory

A canonical inventory and analysis system for the `Loofy147` repository portfolio.

## Purpose

This repository is the system of record for understanding a large, heterogeneous repository portfolio. It separates observed repository facts from interpretation, repository identity from project/idea relationships, technical maturity from strategic value, and evidence from recommendations.

## Core principles

1. Do not infer absence from incomplete inspection. Use `unknown` when evidence is insufficient.
2. Every assessment is evidence-backed.
3. Repository != project != idea.
4. Preserve provenance, including useful failed or abandoned work.
5. Separate facts from decisions.
6. Do not destroy source history during inventory work.
7. Portfolio audit is non-blocking: active project work continues independently while portfolio analysis progresses in parallel.
8. Durable portfolio discoveries are recorded here when they become evidenced, rather than waiting for a full portfolio audit.

### Current target

`Loofy147/Wedgettok` is the current active implementation target. The remaining Core Working Set repositories are supporting/context sources and are consulted when their evidence or primitives are relevant.

## Core Working Set

The current primary working corpus is recorded in `records/CORE_WORKING_SET_2026-09-21.md` and contains six revalidated repositories:

- `Loofy147/Llms-mcp-android`
- `Loofy147/Machine`
- `Loofy147/unified-knowledge-work-system`
- `Loofy147/m0-durable-run`
- `Loofy147/la-rouine-platform`
- `Loofy147/Wedgettok`

Membership is a working-set decision, not a lineage or merge claim.

## Pipeline

`CENSUS -> STRUCTURAL TRIAGE -> CLUSTERING -> DEEP REVIEW -> DECISION -> REVALIDATION`

The pipeline is progressive and non-blocking. An incomplete portfolio audit does not stop valid work on an individual project.

## Decision vocabulary

`KEEP`, `MERGE`, `EXTRACT`, `FREEZE`, `ARCHIVE`, `UNKNOWN`.

These are evidence-backed portfolio decisions, not mandatory outcomes for every repository.

## Epistemic vocabulary

`OBSERVED`, `DERIVED`, `INFERRED`, `USER_REPORTED`, `UNKNOWN`.

## Census state

`inventory/repositories.json` is the durable repository register and remains distinct from dated census observations.

- `inventory/repositories.json` includes **319 recorded repository identities** at the prior inventory baseline.
- `inventory/current-census-2026-09-22.json` is the historical 2026-09-22 overlay; it must not be described as the latest census.
- `inventory/current-census-2026-11-09.json` is the latest observed connected-search reconciliation: **397 unique repository identities** in the union of GitHub repository search and the connected installed-repository search.
- GitHub repository search returned `100/100/100/97` across pages 1–4 = **397**.
- Connected installed-repository search returned `100/99/99/96` across non-empty cursor batches = **394**. Empty continuation cursors were traversed before completion.
- The two current sets are **not identical**: `Loofy147/Os`, `Loofy147/dzd-rates`, and `Loofy147/the-rainer-system` appeared in GitHub search but not in installed-repository search. No installed-only identities were observed.
- All **319** identities from the prior inventory are present in the combined 397-set. **78 identities are newly observed** relative to the stored register.

This is an observed, date-bound connected GitHub search result. Differences between search surfaces are preserved; they are not treated as proof of deletion, transfer, visibility changes, or ownership changes. The census establishes repository identity only. It does not classify all repositories as active projects or validate implementation capability.

The historical `inventory/repositories.json` and dated census overlays remain separate by design. Newly observed identities proceed through structural triage and evidence-backed review rather than automatic promotion.

## Inspection protocol

A README is descriptive evidence only. A sparse README does not imply a sparse repository.

The expected inspection order is:

`METADATA -> ROOT TREE -> BUILD/MANIFEST -> SOURCE -> TESTS/CI -> DATA/ARTIFACTS -> README/DOCS -> HISTORY`

Absence is only recorded when the relevant repository surface has actually been inspected.


## Professional repository handling

Repository reviews follow a reusable evidence/provenance protocol rather than an ad-hoc reading of README files:

- Active-project identification is based on repository + branch/ref + commit evidence, not semantic resemblance.
- Relevant research branches are inspected before deciding what is current, canonical, historical, or unmerged.
- Documentation, implementation, experiments, host-language mechanisms, object-language mechanisms, causal interpretation, and architectural implications are kept separate.
- Claims, assumptions, suggestions, decisions, unknowns, and contradictions are recorded as different evidence classes.
- Cross-repository relationships use explicit statuses such as `POSSIBLE_LINEAGE`, `ESTABLISHED_LINEAGE`, `HISTORICAL_REFERENCE`, and `SHARED_PRIMITIVE_CANDIDATE` rather than silently implying lineage.
- Durable discoveries are recorded here as soon as they are sufficiently evidenced; they do not wait for full portfolio coverage.

See:
- `docs/REPOSITORY_REVIEW_PROTOCOL_v0.1.md` — operational review and evidence-handling protocol.
- `schema/repository-review.schema.json` — machine-readable review record contract.

## Operating manual

The inventory is governed by a reusable repository-review operating model rather than ad-hoc inspection.

- `docs/PORTFOLIO_OPERATING_MANUAL_v0.2.md` — portfolio-wide operating model.
- `docs/REPOSITORY_REVIEW_PROTOCOL_v0.1.md` — repository/ref/evidence handling protocol.
- `docs/REVIEW_PACKET_TEMPLATE_v0.1.md` — reusable review packet.
- `schema/repository-review.schema.json` — machine-readable review contract (v0.2).
- `schema/relationship.v0.2.schema.json` — richer relationship record contract.
- `schema/relationship-inventory.v0.2.schema.json` — operational relationship-inventory envelope contract; `inventory/relationships.json` is canonical under this contract.

- `docs/REVIEW_MODES_v0.1.md` — selects the smallest appropriate review mode for identity, implementation, experiments, lineage, integration, or revalidation.
- `schema/review-log.schema.json` — machine-readable review-log contract (v0.2; future D4 entries require structured verification fields).
- `schema/decision.schema.json` — machine-readable decision contract.
- `schema/census-snapshot.schema.json` — machine-readable census observation contract.
- `reports/case-study-machine-log-os-2026-09-18.md` — concrete example of branch-aware project identification and historical-reference handling.
- `inventory/deep_reviews/2026-09-22-machine-revalidation.json` — latest observed Machine research-frontier ref and divergence snapshot.

The protocol is compatible with the existing v0.1 inventory records; new evidence may be added without rewriting historical records.

## Current phase

We remain in the **census / structural inspection phase**, with deep review progressing incrementally where it materially helps active projects or reduces integration uncertainty.

The audit is a parallel track, not a stop-the-world gate. No final portfolio architecture, forced consolidation, or irreversible strategic decision is required before coverage is complete.

The repository is therefore both:
- the durable record for portfolio-level discoveries that are already evidenced; and
- the coordination layer for a gradually expanding audit that must preserve unresolved states rather than invent certainty.

See `schema/` for machine-readable contracts.

## Executable validation

`python scripts/validate_inventory.py` validates the machine-readable inventory, cross-references, active decision linkage, and durable-provenance marker boundary. The same gate runs in `.github/workflows/inventory-validation.yml` for pull requests and pushes to `main`.

Current census observations are kept as explicit snapshots in `records/CENSUS_SNAPSHOTS_2026-09-22.json` plus the full identity overlay `inventory/current-census-2026-09-22.json`.
