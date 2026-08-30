# Repository Cards — Batch 026

Inspection date: 2026-08-30
Purpose: descriptive census only. No strategic decision is assigned here.

## 1. openclaw
- Observed surface: very large public repository; current README describes a personal AI assistant with a local-first Gateway control plane, multi-channel messaging, multi-agent routing, tools/automation, companion apps, skills, browser control, Canvas/A2UI, CLI and operational tooling.
- Runtime/build: Node >=22; npm/pnpm/bun; source build via pnpm; explicit stable/beta/dev release channels.
- Security surface: explicit pairing/allowlist defaults for inbound DMs, doctor diagnostics, remote access, OAuth/API-key model failover, browser and node control.
- Current interpretation: substantial assistant/platform codebase and likely a major upstream-derived or upstream-tracking surface; provenance and local divergence must be checked before treating it as original local work.
- Unknowns: exact fork relationship/remote provenance, local modifications, commit lineage, test/CI state on the user's fork, and which subsystems were authored or changed locally.
- Review state: `D2-deep-candidate`; `provenance-required`.

## 2. operator
- Observed surface: current main contents exposed only a 7-byte README on the inspected public surface.
- Current interpretation: minimal observed surface; insufficient evidence to classify the project.
- Unknowns: historical commits, branches, hidden/unindexed content, intended role.
- Review state: `D1-minimal-observed-surface`.

## 3. Founders-
- Observed surface: root README is only 11 bytes, but `autodeploy-engine/` is a nested project with README/deployment docs, `.env.example`, GitHub configuration, CLI, docs, HTML entrypoint, package.json/package-lock, Playwright config, PostCSS and `src/`.
- Current interpretation: nested autonomous deployment/automation engine; root repository is a container for a substantial implementation surface.
- Evidence boundary: existence of package/test configuration does not by itself prove successful execution.
- Unknowns: nested source internals, CI results, deployment target, relationship to other autodeploy/agent repositories.
- Review state: `D2-nested-implementation`.

## 4. Baddel
- Observed surface: Flutter/Dart mobile marketplace with Supabase/PostgreSQL/PostGIS/Realtime/Storage; README describes phone auth, geolocation feed, item upload, cash/swap/hybrid offers, deal management, chat, reputation/gamification and admin analytics.
- Additional claims: README also describes a 9-factor recommendation engine, 30+ achievements and RLS-backed security.
- Current interpretation: substantial product implementation candidate for an Algerian local marketplace; README combines v1 beta and later premium-feature descriptions, so version boundaries need reconciliation.
- Unknowns: actual Flutter source structure, SQL migration completeness, recommendation implementation, test/CI evidence, production behavior, and exact chronology between beta and premium-feature claims.
- Review state: `D2-product-candidate`; `version-boundary-review-needed`.

## 5. -Highly-Symmetric-HAG
- Observed surface: README only 23 bytes, but root tree contains `main.py` (~9KB), `minimal_bench.py`, `G-HAG/`, binary/model artifacts including `adapter_config.json`, an empty `adapter_model.bin`, requirements, `solve_nemotron.py`, `nvidia-nemotron-model-reasoning-challenge.zip`, and `submission.zip`.
- Current interpretation: mixed research/competition workspace combining code, HAG materials, model adapter metadata and challenge artifacts.
- Evidence boundary: presence of an empty adapter binary is not evidence of a trained model; ZIP names do not establish contents without extraction.
- Unknowns: contents of G-HAG, exact relationship to `HAG`, model provenance, benchmark results, and whether challenge artifacts are original submissions or imported materials.
- Review state: `D2-artifact-research-candidate`; `lineage-review-needed`.

## 6. Solver
- Observed surface: substantial symmetry-focused mathematical/combinatorial solver project. README specifies `src/core.py`, `engine.py`, `theorems.py`, `domains.py`, `frontiers.py`, `benchmark.py`, unified `main.py`, multiple domain extensions and five research papers.
- Research surface: claims 10 theorem verifications, exact W4/H¹ formula, closure lemma work, symmetry reductions, impossibility proofs and benchmark comparisons across multiple solvers.
- Current interpretation: mathematical research + computational verification system; potentially highly relevant to the mathematical lineage across other symmetry/theorem repositories.
- Evidence boundary: README reports theorem/benchmark results, but independent verification requires source inspection and execution; claims are not promoted to established results by documentation alone.
- Unknowns: source contents of theorem proofs, test suite, exact datasets/instances, statistical benchmark protocol, and relation to `Global-theorem-`, `-Highly-Symmetric-HAG`, `SIE`/discovery systems, or other mathematical repositories.
- Review state: `D3-math-deep-review-candidate`.

## 7. HAG
- Observed surface: README/docs plus `.claude`, `.github`, `.jules`, research paper, HF README, Makefile, runtime `app.py`, benchmarks/configs/data/dist and other implementation surfaces.
- Current interpretation: research/runtime HAG system with packaging and benchmark surfaces; requires source-level inspection.
- Unknowns: exact algorithm, model dependencies, benchmark definitions, relationship to `-Highly-Symmetric-HAG` and whether artifacts are shared.
- Review state: `D2-deep-candidate`.

## 8. MARL-Pro
- Observed surface: repository metadata indicates a small (20KB) repository; detailed contents not yet inspected in this batch.
- Current interpretation: candidate multi-agent reinforcement-learning project based on repository name only; no stronger claim made.
- Unknowns: all substantive implementation, research, data and evidence surfaces.
- Review state: `D1-pending-deep-inspection`.

## 9. Regular
- Observed surface: repository metadata indicates ~160KB on main; substantive contents not yet inspected in this batch.
- Current interpretation: unresolved project identity; no inference from name.
- Unknowns: purpose, implementation, artifacts, tests, history.
- Review state: `D1-pending-deep-inspection`.

## 10. SIE
- Observed surface: repository metadata indicates a small public repository; prior inspection identifies an ingest → sandbox execution → vetting gate → registry architecture with SQLite, tests and an MCP adapter.
- Current interpretation: AI/system ingestion and verification infrastructure candidate.
- Unknowns: exact implementation depth, test execution evidence, and relation to other verification/evidence repositories.
- Review state: `D2-identified`; `cross-lineage-review-needed`.

## Census integrity note
The authenticated repository listing is currently returning a bounded subset rather than a complete all-pages inventory, while `user:Loofy147` search also returns only a bounded result set. Therefore the repository count in older snapshots must remain labeled as a search snapshot, not the authoritative total portfolio count. Discovery and inspection continue until we can establish a reliable census boundary.

No KEEP/MERGE/EXTRACT/FREEZE/ARCHIVE decision is assigned here.
