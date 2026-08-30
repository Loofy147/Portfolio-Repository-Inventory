# Repository Cards — Batch 023

Inspection date: 2026-08-30
Purpose: descriptive census only. No strategic decision is assigned here.

## 1. general-engine
- Observed surface: README is only 16 bytes, but the tree contains `causal_hypothesis_loop_v4.py` (~14.5KB), `engine/`, `run_simulation.py`, and `tests/`.
- Source evidence: the V4 loop generates synthetic ground truth with controlled noise, fits a multi-modal power-law model using Huber regression, estimates covariance/uncertainty, simulates predictive distributions, evaluates coverage/R2/error ratios, actively samples candidate points, and mutates model exponents. The inspected file continues into an evolutionary engine.
- Current interpretation: causal/hypothesis-discovery and model-evolution research implementation; substantially richer than README indicates.
- Unknowns: contents of `engine/` and `tests/`, actual experiment outcomes, runtime status, and lineage to other causal-research repositories.
- Review state: `D2-source-inspected`.

## 2. screal
- Observed surface: Android/Gradle project with `app/`, `assets/`, Gradle build files, `.env.example`, `.build-outputs/`, `metadata.json`, and a tracked `debug.keystore.base64` artifact.
- README identifies it as an AI Studio app intended to run through Android Studio and use a Gemini API key.
- Current interpretation: real Android AI application surface, apparently generated/imported from AI Studio; provenance and local modifications need separation.
- Security/provenance signal: tracked debug keystore artifact is present; treat as a credential/signing-material review item without exposing its contents.
- Unknowns: app functionality, source architecture, test state, and whether the signing artifact is intentional/safe.
- Review state: `D2-candidate`; `security-provenance-review`.

## 3. Tycoon-
- Observed surface: `src/`, `outputs/`, `requirements.txt`, and substantial README documenting Deep R-Learning experiments, multi-agent simulations, financial stress testing, and the Rho metric.
- README reports a transition from Rho=-20 in a prior run to Rho=+50 after an "Economic Stimulus + Adaptive Normalization" intervention, and labels the project complete.
- Current interpretation: reinforcement-learning research/experiment repository with saved visual outputs; not yet evidence of independently reproduced results.
- Unknowns: exact RL implementation in `src/`, experiment configuration, random seeds, baselines, statistical treatment, and test/CI evidence.
- Review state: `D2-source-needed`; claims remain unverified.

## 4. HAMHA-LMA
- Observed surface: large README plus `.github/`, CHANGELOG, DEPLOYMENT.md, Dockerfile.prod, Makefile, PROJECT_STRUCTURE.md, API/CLI/config files, and architecture image artifacts.
- README describes a hexagonal multi-head attention mechanism governed by a Lead Meta-Architect with telemetry, causal graph, hypothesis generation, prediction, intervention, Meta-NAS, and evolutionary modules.
- Current interpretation: substantial research/engineering repository combining a novel attention architecture with an autonomous supervisory/control layer.
- Evidence note: repository contains explicit version/roadmap, deployment and structure artifacts; these establish intended implementation surface, not correctness of all claimed capabilities.
- Unknowns: actual implementation/test coverage, mathematical validity of spectral/entropy thresholds, and experimental comparison against conventional attention.
- Review state: `D2-deep-candidate`.

## 5. q-optimized-small-model
- Observed surface: README describes `src/model.py`, tokenizer, dataset, trainer, Kaggle training, evaluation, Hugging Face publishing, tests, and config files.
- Current interpretation: small-model training/deployment experiment centered on six custom vocabulary concepts and a Q-score framework.
- Evidence boundary: listed Q-scores >=0.9 are claims in the repository documentation; no independent validation is established by this inspection.
- Unknowns: actual model architecture, dataset construction, evaluation protocol, training artifacts, and reproducibility.
- Review state: `D2-candidate`; `claim-verification-needed`.

## 6. epistemic
- Observed surface: 4MB mathematical specification DOCX, 0.9MB PDF rendering, 26KB TXT rendering, multiple `epistem*.py` implementations including `epistem_rl.py`, and multiple test files.
- Current interpretation: multi-version epistemic-engine research artifact with both mathematical specification and implementation lineage; the multiple code copies are particularly relevant to internal evolution.
- Unknowns: exact differences among versions, which implementation is canonical, test execution history, and relationship to other repositories carrying epistemic/uncertainty terminology.
- Review state: `D2-lineage-candidate`.

## 7. Quantum-Arabic-
- Observed surface: multiple large skill-generation/research documents covering recursive sequences, algebraic resource control, metric tensors, temporal coherence, transfer learning, universal problem solving, interactive visual design, and metacognitive awareness, plus a large-scale validation report.
- Current interpretation: research/specification corpus focused on reusable skills and mathematical/AI reasoning procedures.
- Unknowns: which materials are executable, which are generated documents, implementation coverage, and empirical validation of the stated methods.
- Review state: `D2-document-deep-review-needed`.

## 8. dzd-rates
- Observed surface: `fetch_rates.py`, `dom_test.js`, `rates.json`, HTML calculator, and update workflow file; the repository also contains an older `README (19).md` alongside a minimal current README.
- Current interpretation: small self-hosted Algerian DZD official-vs-parallel exchange-rate calculator with automated data refresh and validation.
- Evidence note: the older README explicitly distinguishes DOM-tested behavior from live-site parsing that still required operator verification, which is useful provenance for the repository's epistemic state.
- Review state: `D2-implemented-small-tool`.

## Global note
No KEEP/MERGE/EXTRACT/FREEZE/ARCHIVE decision is assigned. The cards capture observed evidence, interpretation, unknowns, and review state only.
