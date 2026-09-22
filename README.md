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

## Census state — 2026-08-30

The current repository census stored in `inventory/repositories.json` was generated from GitHub repository search pages 1–4 with `100/100/100/13` results, deduplicated by repository full name, yielding **313 observed repository records** in that snapshot.

This is a search-based snapshot, not a proof that no additional repositories exist outside the search result set or current connector visibility.

A later direct GitHub observation on 2026-09-18 exposed a larger accessible set, but that observation has not yet been promoted to the canonical stored census. The two snapshots must remain distinct until a deliberate re-census and reconciliation are performed.

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
- `schema/relationship.v0.2.schema.json` — richer cross-repository relationship contract.

- `docs/REVIEW_MODES_v0.1.md` — selects the smallest appropriate review mode for identity, implementation, experiments, lineage, integration, or revalidation.
- `schema/review-log.schema.json` — machine-readable review-log contract (v0.2; future D4 entries require structured verification fields).
- `schema/decision.schema.json` — machine-readable decision contract.
- `schema/census-snapshot.schema.json` — machine-readable census observation contract.
- `reports/case-study-machine-log-os-2026-09-18.md` — concrete example of branch-aware project identification and historical-reference handling.

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

Current census observations are kept as explicit snapshots in `records/CENSUS_SNAPSHOTS_2026-09-22.json`; they must not be collapsed into a single current-total claim.
