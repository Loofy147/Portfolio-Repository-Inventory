# Repository Memory — Batch 042

> Scope: continued repository census and evidence capture. This batch records observed identity, surface, and lineage signals. It does not make keep/merge/archive decisions.

## 1. Discovery additions / confirmed current identities

| Repository | Observed identity / surface | Evidence level | Notes |
|---|---|---|---|
| `new-AGI` | Epistemological Engine V3; autonomous cross-domain discovery, mathematical theory resolution, paper generation; `unified_engine.py`, `paper_generator.py`, `results/`, `data/`, `legacy/` | README + structure claim | Research system; mathematical/empirical claims require independent reproduction. |
| `NeuraSynth` | Flask talent/project platform with automation, project health, financial APIs, tests | README | Product application surface; implementation depth still requires tree/source inspection. |
| `SPEC-BPE` | Specificity-guided Pair Encoding v2.1; tokenizer, HF wrapper, production training, benchmark, SLA audit, persistent-homology scoring | README | Strong algorithm/research candidate; equations and benchmark claims are not independently established yet. |
| `recursive-audit` | Recursive Evidence-Audit System (REAS); directed claim graphs, bi-temporal reasoning, evidence bindings, CI/pre-commit gates, incremental audits, event bus, JSON patching, visualization, telemetry | README | Strong epistemic verification system; notable overlap with evidence/verification work elsewhere. |
| `orbit-agent` | Orbit Wars game environment with continuous 2D space, orbital planets, comets, fleet dynamics, collision/combat rules and agent API | README | Kaggle/game-agent environment rather than generic agent platform. |
| `TNN-ARC-AGI-2026` | Hybrid ARC-AGI solver using D4 symmetry and color-logic sheaves; claims topological validation and sub-second synthesis | README | Research/competition artifact; results remain claims until source/task execution is reviewed. |
| `Symlib` | Global-structure library around `0 → H → G → G/H → 0`; G3 torus specification, four intelligence fibers, named theorems, 195-test claim | README | Important mathematical/research lineage candidate with `Global-theorem-`, `Solver`, HAG and related repositories. |
| `Fusion-Engine` | Repository identified, but README gives no semantic content beyond the project name | metadata/README | Needs source/tree inspection. |
| `oncoder` | Repository identified, README minimal | metadata/README | Needs source/tree inspection. |
| `Yassir-agent` | Repository identified | metadata | Needs source/tree inspection. |
| `Rainar` | Repository identified | metadata | Needs source/tree inspection. |
| `Jack-sparo` | Repository identified | metadata | Needs source/tree inspection. |
| `Full-system-repository` | Repository identified | metadata | Needs source/tree inspection. |
| `Marlboro` | Large repository surface (~22MB GitHub size), identity not established in this batch | metadata | High-priority inspection candidate. |
| `NeuraSynth` | ~15MB repository, Flask application surface from README | metadata + README | Potential product-family candidate. |
| `TNN-ARC-AGI-2026` | ~65KB repository | metadata + README | Small research artifact; keep distinct from `ARC-AGI-NCA-Solver`. |
| `Software-res` | Current authoritative public repository for Software Resilience work; paired with `Ai-evaluation-system` Phase A | metadata + prior evidence | Lineage relationship should be represented, not collapsed. |
| `SPEC-BPE` | Public algorithm repository | README | Distinct from generic BPE/template repositories. |
| `Workflows-academy` | Large repository (~4.3MB) | metadata | Needs deeper tree/source inspection; related by name to `Workflows--ci-cd` and `Workflows-n8n-builder-`. |
| `Mobil-chain` | Repository identified (~1.5MB) | metadata | Blockchain/mobile lineage candidate; needs source inspection. |
| `Loofyloo-` | Repository identified | metadata | Needs source/tree inspection. |
| `Skkiler` | Repository identified (~0.6MB) | metadata | Likely related by naming to `Boofa-skiler`; relationship not assumed. |
| `School-` | Repository identified (~0.58MB) | metadata | Needs source/tree inspection. |
| `leverscan-app` | Repository identified (~0.32MB) | metadata | Needs source/tree inspection. |
| `The-new-era` | Repository identified (~3.7MB) | metadata | Needs source/tree inspection. |
| `Prompts-dashboard-` | Repository identified (~0.6MB) | metadata | Needs source/tree inspection. |

## 2. High-value lineage observations

### `new-AGI` ↔ epistemic/research lineage
`new-AGI` explicitly preserves a `legacy/` directory of earlier developmental engines and a machine-generated-results/paper path. This is a repository where developmental history is part of the artifact, not noise.

### `recursive-audit` ↔ evidence-governed systems
REAS introduces a formal directed-claim-graph verification layer, bi-temporal state, evidence anchoring, retraction propagation, and CI merge gating. This should later be compared structurally with `canonical-capability-core`, `external-staging-authority`, `Software-res`, and `Ai-evaluation-system` rather than treated as an unrelated project.

### `Symlib` ↔ mathematical family
`Symlib` explicitly presents a global-structure/symmetry program with a short exact sequence and named theorems. It is therefore a high-priority lineage target alongside `Global-theorem-`, `Solver`, `Symmetric-HAG`, `-Highly-Symmetric-HAG`, `TGI-Market-Engine`, and related FSO/topological work.

### Trading/research family
`Cwc-loofy`, `SPEC-BPE`, `NeuraSynth`, `Tycoon-`, `Grok-supreme`, `Crypto-spaces-`, `vO_trading_donors`, `Meta-meta`, and `Quantum-market-analyzer-` continue to show that research, trading, product prototypes, and evaluation artifacts are spread across multiple repositories. No equivalence is asserted yet.

## 3. Census mechanics

`search_repositories(query="user:Loofy147")` returned additional repositories on pages 1–3 that were absent from earlier batches, confirming that a single listing method is not sufficient for complete historical census coverage. Therefore the inventory must retain:

- enumeration source/method;
- current repository identity;
- current default branch;
- observed tree/source evidence;
- provenance/possible upstream relationship;
- unresolved state;
- later lineage links.

The number of repositories returned by any single API/search view is not treated as the owner's true historical portfolio total.

## 4. Current unresolved examples

`Fusion-Engine`, `oncoder`, `Yassir-agent`, `Rainar`, `Jack-sparo`, `Full-system-repository`, `Marlboro`, `Mobil-chain`, `Loofyloo-`, `Skkiler`, `School-`, `leverscan-app`, and `The-new-era` remain explicitly unresolved at semantic level until their source trees are inspected.
