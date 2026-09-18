# Evidence

Evidence must preserve provenance for inventory claims.

Preferred sources include repository metadata, trees/snapshots, README/docs, CI/workflows, releases/tags, commits/PRs, tests/benchmarks, and explicit owner attestations.

Do not claim a feature, test suite, CI pipeline, or absence thereof without inspecting the relevant surface. Use UNKNOWN when evidence is incomplete.
## Operational evidence handling

The portfolio now uses a branch-aware review model.

For material findings, preserve:

`repository + branch/ref + commit + inspected surface`

Separate:

- OBSERVED / DERIVED / INFERRED / USER_REPORTED / UNKNOWN / CONTRADICTED evidence classes;
- ESTABLISHED / EXPERIMENTALLY_SUPPORTED / INFERENCE / HYPOTHESIS / OPEN claim status;
- assumptions, suggestions, decisions, gaps, and contradictions.

For cross-repository findings, preserve the chain:

`source repository/ref -> observation -> relationship or derivation -> portfolio claim`

Do not transfer claims merely because another repository uses similar terminology or architecture.

Review depth:

- D0 — metadata
- D1 — structural triage
- D2 — selected implementation
- D3 — deep comparison
- D4 — executed/reproduced verification

See `docs/PORTFOLIO_OPERATING_MANUAL_v0.2.md` and `docs/REPOSITORY_REVIEW_PROTOCOL_v0.1.md`.
