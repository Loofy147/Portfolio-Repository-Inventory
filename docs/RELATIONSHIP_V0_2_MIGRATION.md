# Relationship v0.2 migration

## Current state

`inventory/relationships.json` remains a legacy-contract dataset validated against `schema/relationship.schema.json`.

`schema/relationship.v0.2.schema.json` is the newer relationship contract. It requires an explicit epistemic `status` in addition to relation semantics and evidence references.

## Migration rule

Do not derive `status` mechanically from the legacy `confidence` field.

Each relationship must be reviewed at claim level and assigned one of the v0.2 epistemic states:

- `OBSERVED`
- `DERIVED`
- `INFERRED`
- `USER_REPORTED`
- `UNKNOWN`
- `CONTRADICTED`
- `OPEN`

A semantic similarity can be `INFERRED`; it does not become `OBSERVED` merely because confidence is high. Direct repository statements can support `OBSERVED` only when the evidence actually records that relationship.

## Completion boundary

This document records the migration requirement; it does not claim that the 24 legacy relationships have been migrated. Until a claim-level migration is completed, consumers must treat `inventory/relationships.json` as legacy epistemic data.
