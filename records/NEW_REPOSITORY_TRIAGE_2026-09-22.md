# New Repository Structural Triage — 2026-09-22

This record covers the 20 repository identities newly observed in the 2026-09-22 current census relative to the stored 319-record inventory.

## Provenance boundary

Six of the 20 are confirmed GitHub forks of external upstream repositories:

- `Loofy147/METATRON` ← `sooryathejas/METATRON`
- `Loofy147/spacy-models` ← `explosion/spacy-models`
- `Loofy147/spaCy` ← `explosion/spaCy`
- `Loofy147/LinuxOnAndroid` ← `devwithzachary/LinuxOnAndroid`
- `Loofy147/Agora-32Bit` ← `Legend-droid7/Agora-32Bit` (source: `newo-ether/Agora`)
- `Loofy147/moirae` ← `pchrysostomou/moirae`

These remain portfolio-visible identities but are classified as external references rather than first-party candidate implementations.

## Triage routes

| Route | Count | Meaning |
|---|---:|---|
| DEEP_REVIEW | 10 | Substantive first-party candidates with evidence that a deeper review can materially reduce uncertainty or enable reuse/validation |
| REFERENCE_ONLY | 7 | External fork or explicitly killed artifact; preserve provenance and use as reference rather than treating as first-party work |
| LINEAGE_REVIEW | 2 | Adjacent project where repository/history comparison is needed before deciding whether it is a successor, parallel line, or separate artifact |
| HOLD | 1 | Insufficient implementation evidence for useful deeper review |

## Deep-review candidates

- `adaptive-reasoning-os` — research line directly overlapping adaptive selection, verification, lifecycle, and bounded control questions.
- `ledger-system-source-of-truth` — concrete contradiction/decision ledger with MCP/hub adapters.
- `My_browser` — current acquisition/evidence kernel with CI-backed gate and downstream experiment.
- `Economic-luncher` — reproducible economic-cost topology engine with dated pricing snapshots.
- `algeria-digital-venture-operating-system` — substantive Algeria-market platform scaffold.
- `robust-fusion-platform` — implemented web + Python engine bridge + persistence + CI.
- `Bounties` — evidence-gated external security research track with human submission control.
- `trading-validations-principles` — large provenance-preserving validation/research artifact with real-data gates.
- `moaziz-supreme-engine` — bounded evidence/calibration/self-improvement protocol directly relevant to the operating model.
- `spotup-platform` — substantive product platform with schema/server/runtime surface and many explicit unfinished gates.

## Lineage review

- `Wedgettok-Next` ↔ `Wedgettok`: the repository describes itself as a second-generation version while remaining structurally separate. Compare history, contracts, test coverage, and product thesis before treating it as successor, parallel implementation, or extraction source.
- `la-rouine-agent` ↔ `la-rouine-platform`: fresh Eve scaffold versus the existing Experience/runtime platform; current content is too thin to establish lineage.

## Reference-only findings

- `Compute-Qualification-Infrastructure` has an explicit KILLED decision and preserved research value.
- `METATRON`, `spacy-models`, `spaCy`, `LinuxOnAndroid`, `Agora-32Bit`, and `moirae` are external forks with useful technical/reference value.

## Hold

- `Residual-Opportunity-Scanner` currently exposes only a minimal README; no substantive implementation evidence was found at the current ref.

The machine-readable source of truth for this triage is `inventory/current-triage-2026-09-22.json`.
