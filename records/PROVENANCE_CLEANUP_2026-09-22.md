# Provenance cleanup — 2026-09-22

The catalog contained conversation-scoped `fileciteturn...` markers. These identifiers are not durable repository provenance and were removed from the affected catalog cards in this change.

Affected files:

- `catalog/repository-cards-004.md`
- `catalog/repository-cards-007.md`
- `catalog/repository-cards-013.md`
- `catalog/repository-cards-016.md`
- `catalog/repository-cards-031.md`
- `catalog/repository-cards-035.md`
- `catalog/repository-cards-038.md`
- `catalog/repository-cards-039.md`
- `catalog/repository-cards-040.md`
- `catalog/repository-cards-041.md`

The textual observations are preserved. The removed markers are not replaced with invented repository citations. Where a historical card no longer contains durable repository/ref information, the observation remains historical and should be revalidated before being promoted into current decision evidence.

The validation gate rejects new conversation-scoped filecite markers in tracked inventory content.
