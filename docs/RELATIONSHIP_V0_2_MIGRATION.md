# Relationship v0.2 migration

## Current state

`inventory/relationships.json` is now the **canonical operational relationship dataset** under the v0.2 epistemic model.

The previous v0.1 dataset is preserved exactly at:

`inventory/relationships.v0.1-legacy.json`

The migration contains all 24 legacy relationship records. Relation semantics, confidence, evidence references, and notes were preserved. Each migrated record now also carries an explicit epistemic `status`, a `status_basis`, and a `next_test`.

## Epistemic rule

Status was not derived mechanically from `confidence`.

The migration classified each relationship from the claim language and evidence notes:

- `OBSERVED`: the recorded evidence explicitly states or directly links the relationship.
- `DERIVED`: the relationship is derived from multiple cited surfaces or explicit conceptual connections.
- `INFERRED`: the relationship is a candidate inference or remains explicitly unverified.

This classification is an epistemic normalization step. It is **not** a claim that the underlying lineage, dependency, or equivalence has been independently proven.

## Remaining boundary

Candidate lineage and reuse relationships remain unresolved where their source notes require chronology, tree comparison, imports, copied-code analysis, or other discriminating checks. Those relationships remain non-final and retain explicit next-test instructions.

Future relationship updates must use the v0.2 contract and must preserve the distinction between relation semantics, epistemic status, confidence, and evidence provenance.
