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

## Current phase

We remain in the **census / structural inspection phase**, with deep review progressing incrementally where it materially helps active projects or reduces integration uncertainty.

The audit is a parallel track, not a stop-the-world gate. No final portfolio architecture, forced consolidation, or irreversible strategic decision is required before coverage is complete.

The repository is therefore both:
- the durable record for portfolio-level discoveries that are already evidenced; and
- the coordination layer for a gradually expanding audit that must preserve unresolved states rather than invent certainty.

See `schema/` for machine-readable contracts.
