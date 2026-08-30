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

## Pipeline

`CENSUS -> STRUCTURAL TRIAGE -> CLUSTERING -> DEEP REVIEW -> DECISION -> REVALIDATION`

## Decision vocabulary

`KEEP`, `MERGE`, `EXTRACT`, `FREEZE`, `ARCHIVE`, `UNKNOWN`.

## Epistemic vocabulary

`OBSERVED`, `DERIVED`, `INFERRED`, `USER_REPORTED`, `UNKNOWN`.

## Census state — 2026-08-30

The current repository census stored in `inventory/repositories.json` was generated from GitHub repository search pages 1–4 with `100/100/100/13` results, deduplicated by repository full name, yielding **313 observed repository records** in that snapshot.

This is a search-based snapshot, not a proof that no additional repositories exist outside the search result set or current connector visibility.

## Inspection protocol

A README is descriptive evidence only. A sparse README does not imply a sparse repository.

The expected inspection order is:

`METADATA -> ROOT TREE -> BUILD/MANIFEST -> SOURCE -> TESTS/CI -> DATA/ARTIFACTS -> README/DOCS -> HISTORY`

Absence is only recorded when the relevant repository surface has actually been inspected.

## Current phase

We are still in the **census / structural inspection phase**. Repository cards are being added continuously. No strategic portfolio decisions are made until coverage and cross-repository reconciliation are complete.

See `schema/` for machine-readable contracts.
