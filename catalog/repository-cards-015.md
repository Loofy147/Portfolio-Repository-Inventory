# Repository Cards — Batch 015

Inspection date: 2026-08-30
Purpose: descriptive census only. No strategic decision is assigned here.

## 1. Cashier
- Observed surface: root contains only `README.md` (9 bytes) in the inspected `main` tree.
- Current interpretation: extremely small repository surface; no implementation inferred from the root.
- Unknowns: hidden/non-default refs or later history are not assessed here.
- Review state: `D1-root-only`.

## 2. agent-hub
- Observed surface: `agents/`, `app/`, `src/`, `config/`, `docs/`, `prisma/`, `scripts/`, package/tsconfig plus `AGENTS.md` and a 13.8KB `SETUP.md`.
- README describes seven specialized autonomous AI identities (Tuber, Bolt, Sentinel, Sun Tzu, Palette, Midas, Oracle) and a SaaS foundation with authentication, database, orchestration and landing page.
- Current interpretation: full-stack agent-hub product/system rather than a prompt-only repository.
- Unknowns: actual runtime/test status and depth of each agent implementation.
- Review state: `structurally-identified`.

## 3. Agents-next-tokens
- Observed surface: extensive strategy/implementation/QA documentation, `SKILL_REGISTRY_JSON.json`, `hiro_agent.py` (~16.4KB), `competition_skill.py`, `kaggle_manager.py`, and additional Python tooling.
- Current interpretation: agent/skill framework with explicit documentation, quality, business/data strategy and implementation surfaces.
- Lineage signal: naming and artifacts suggest possible relationship to other HIRO/skill repositories, but no relationship is asserted here.
- Unknowns: executable coverage and historical evolution.
- Review state: `D2-candidate`.

## 4. synapse-platform
- Observed surface: React/TypeScript client, server, shared layer, Drizzle schema/migrations, tRPC routers, package/lockfile, patches and todo.
- README describes a founder/freelancer/investor/collaborator ecosystem with project marketplace, validation, matching algorithm, analytics, team-cost calculation, financial projections and role-specific workflows.
- Current interpretation: substantial full-stack startup ecosystem platform; matching and financial calculation logic are explicit technical surfaces.
- Unknowns: actual runtime behavior, test results and production deployment evidence are not established by this inspection.
- Review state: `D2-candidate`.

## 5. Founders-
- Observed surface: root README is 11 bytes plus an `autodeploy-engine/` directory whose inspected listing returned no child entries.
- Current interpretation: repository appears to be a container for an autodeploy-engine effort, but implementation contents were not exposed in this inspection.
- Unknowns: contents of non-default refs/history and whether the directory is populated elsewhere.
- Review state: `D1-root-plus-child-check`.

## 6. CRMEB
- Observed surface: very large repository (metadata ~302MB) with `crmeb/`, `docker-compose/`, `template/`, `readme/`, a 12.9KB README and a 1.2MB installation DOCX.
- Current interpretation: substantial pre-existing e-commerce/CRM-style system or imported platform; provenance must be separated from local modifications before portfolio attribution.
- Unknowns: exact upstream origin, local changes, modules and test/deployment state require deeper source/history audit.
- Review state: `provenance-review`.

## 7. One-handed
- Observed surface: README plus large operational/design documentation (`ASSET_CATALOG.md` ~16.7KB, `OPPORTUNITIES.md`, `VISION.md`, contributing guide) and directories for `agents`, `ai-automation`, `arabic-ai`, `computer-vision`, `dataset-businesses`, `hidden-value-discovery`, `high-leverage-research`, etc.
- Current interpretation: broad umbrella/portfolio workspace containing multiple technical/research tracks rather than one narrow application.
- Unknowns: depth of each child module and whether these are implementations, plans, or curated assets.
- Review state: `D2-candidate`.

## 8. Exchange
- Observed surface: `MANIFEST.md`, `exchange.py`, multiple substantial Python modules including `aion_full.py`, `arriving.py`, `being.py`, `jules.py` (~47.7KB), `kairos.py`, `meta.py`, `this.py`, plus an `auditor.py`.
- Current interpretation: multi-module experimental/agent system with several named execution identities/components; not a trivial exchange application despite the repository name.
- Unknowns: central architecture, tests and semantic relationships among modules require source-level inspection.
- Review state: `D2-candidate`.

## 9. cwc-Loofy-strategie
- Observed surface: `SKILL_v2.md` (~22.3KB), `benchmark_v2.py` (~13.4KB), `bot.py` (~26.7KB), `regime_adaptive.py`, `sim_data.py`, chart tooling and optimized configuration.
- Current interpretation: executable strategy/trading research workspace with benchmarking, simulation and regime-adaptive logic.
- Unknowns: exact strategy target and empirical validation status need direct source/results inspection.
- Review state: `D2-candidate`.

## 10. the-rainer-system
- Observed surface: Go project with `backend/`, `cmd/`, `go.mod`, `go.sum`, `main.go`, plus a tracked binary/file named `the-rainer-system` of ~4.57MB.
- Current interpretation: compiled/application system with Go source and a committed executable artifact.
- Unknowns: binary provenance, runtime purpose, tests and relation to any other Rainer repositories.
- Review state: `D2-candidate`; `artifact-provenance-review`.

## 11. STRATOS_OMEGA_ULTIMATE_V4
- Observed surface: repository metadata ~122MB; root contains multiple large STRATOS archives, including ~32.7MB comprehensive, ~20.1MB final 2048D and ~72.9MB upgraded 2048D ZIPs, plus `STRATOS_OMEGA_SUPREME.py` and technical spec.
- Current interpretation: artifact-heavy V4 STRATOS distribution/research repository; versioned archives are first-class evidence for lineage and release evolution.
- Unknowns: correspondence between archives and checked-in Python/specification, generation dates, and whether the archives contain code absent from the tree.
- Review state: `D2-deep-artifact-review`.

## 12. Global note for this batch
No KEEP/MERGE/EXTRACT/FREEZE/ARCHIVE decision is made. Relationship hints remain non-decisional until cross-repository comparison and provenance analysis are complete.
