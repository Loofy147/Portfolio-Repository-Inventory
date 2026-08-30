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

## Initial census

On 2026-08-30, the connected GitHub inventory endpoint exposed an owner listing of 100 repositories for the initial pass. These records are stored in `inventory/repositories.json` as **observed metadata only**. This is not a claim that the full GitHub portfolio contains only 100 repositories; the connector did not expose a second page.

The next step is to obtain the remaining repository set and then perform structural triage before making strategic decisions.

See `schema/` for machine-readable contracts.
