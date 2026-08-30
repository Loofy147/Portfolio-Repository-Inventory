# Repository Cards — Batch 029

## Scope
Additional repositories inspected from the current owner inventory. This batch records observed structure and identity signals only; no merge/archive/priority decisions.

## Cards

### Learning-agent
- Default branch: `main`.
- Repository metadata name suggests a learning agent, but README identifies it as a **BTC Trading Simulator**.
- README describes FastAPI, JWT authentication, wallets, BTC buy/sell, limit orders, Celery background processing, Docker/Compose, and pytest.
- Root tree contains `app/`, `alembic/`, Dockerfile, docker-compose, `data/`, `images/`, learning materials, a ~1.54 MB dataset text file, and CI-related files.
- `app/` includes API client, auth, config, database, models, routers, schemas, security and Celery worker.
- Identity mismatch is explicit: repo name != stated product identity.
- Status: substantial implementation surface; business/product identity requires provenance/history review.

### Hbo
- Default branch: `main`.
- Root contains Dockerfile, pre-commit configuration, `.github`, `advanced_optimizers.py` (~50 KB), HPO patch-generation tooling, configs, examples, `hpo_production_system/`, and an HPO database artifact.
- `.coverage` is committed, indicating test/coverage artifacts are part of the repository state.
- Status: optimization/HPO-oriented engineering workspace; exact research scope requires deeper source review.

### v0-spokecosystem
- Default branch: `main`.
- Root contains `automl`, `benchmarks`, `config`, `core_engine`, `docs`, `ensemble`, `examples`, `experiments`, `infrastructure`, `interpretability`, `patterns`, `performance`, `production`, and a pnpm lockfile (~121 KB).
- This is a broad AI/ML system surface with explicit experiment, benchmark, interpretability and production areas.
- Status: substantial multi-layer workspace; likely ecosystem/platform rather than a single feature.

### Quantum-market-analyzer-
- Default branch: `main`.
- README is only 26 bytes.
- Root contains ~23.9 KB mobile-app documentation, `quantum-crypto-analyzer/`, and a ~27.4 KB TSX source snapshot stored as `.tsx.txt`.
- `server.log` exists but is empty.
- Status: mixed documentation + implementation snapshot; needs nested review to determine runnable depth.

### LAA
- Default branch: `main`.
- Root includes `api/`, `app.py`, `laa_core/`, `laa_tools/`, SDK surface, multiple large technical/business/methodology documents, requirements, and a ~115.8 KB project overview.
- Also includes a ~45 KB TSX strategy artifact and a ~29 KB learning-augmented-algorithms document.
- Status: research + implementation repository with significant documentation density; likely related to LAA/learning-augmented algorithm work elsewhere in the portfolio, but relationship is not established here.

### Unified-ai
- Default branch: `main`.
- Root includes `agents`, `algorithms`, `configs`, `core`, `docs`, `environments`, `experiments`, `intelligence`, `orchestration`, and `main.py`.
- Two major French reports are committed: integration report (~18.7 KB) and final implementation report (~14.4 KB).
- README is ~7.3 KB; architecture is explicitly multi-domain and unified.
- Status: substantial unified AI framework; claims in reports remain separate from runtime verification.

### Personal-ai
- Default branch: `main`.
- Observed root contains only `README.md` (13 bytes) on `main`.
- Status: current observed surface is minimal; no inference about historical branches/artifacts.

### Just-asystem
- Default branch: `main`.
- Root contains only `README.md` (14 bytes).
- Status: minimal observed surface.

### Gemini-app
- Default branch: `main`.
- README describes a web application wrapping `gemini-cli` with GitHub integration, WebSockets, session-backed credential storage, and a `gemini-cli` git submodule.
- README names `index.js`, `src/routes.js`, `src/websocket.js`, `public/`, and `gemini-cli/` as structural components.
- Status: application/integration surface; provenance of embedded `gemini-cli` and exact committed submodule state should be recorded separately.

### Ai-evaluation-system
- Default branch: `main`.
- README identifies this repository as **Software Resilience PoC — Phase A**, specifically a real GIL causality experiment for free-threaded CPython.
- It specifies independent Control/Treatment runs on CPython 3.13t/3.14t, runtime-before/import/runtime-after evidence, fail-closed behavior, and an acceptance target of 5 control + 5 treatment runs.
- README names `artifacts/real-gil/phase-a-summary.json` as the expected result artifact and states CI real-runtime execution is authoritative.
- Status: direct high-confidence relationship candidate with the Software Resilience work; this is strong enough to trigger later lineage/source comparison, but not a merge decision.

### NeuroGolf
- Default branch: `main`.
- README is 11 bytes.
- Root contains `core/`, `kernels/`, `registry/`, `tests/`, `produce_submission.py`, and committed `__pycache__/`.
- Status: non-empty experimental/ML surface hidden behind a minimal README.

### Vipers-
- Default branch: `main`.
- README is 9 bytes.
- Root contains `backend/` and `frontend/`.
- Status: full-stack scaffold/implementation surface; exact product identity remains unresolved.

### Symmetric-HAG
- Default branch: `main`.
- README points directly to `Global-theorem-` and `HAG` repositories.
- Status: explicit cross-repository linkage marker; likely a coordination/reference repository, but its role should be determined from commit/history and tree evidence.

### v0-crypto-dashboard
- Default branch: `main`.
- Current inventory metadata shows a small repository (~122 KB in GitHub size units) and it is already tracked as a portfolio candidate.
- Status: needs dedicated tree inspection before assigning implementation depth.

### Learning-agent identity correction
- Important: the repository's public-facing README says **BTC Trading Simulator**, while the repository name is `Learning-agent`.
- This is another confirmed case where repository name, README identity, and likely historical intent can diverge.

### Supporting observations from the same census
- `The-matching-engine-`: README remains tiny, but tree has `matching_logic.md`, `matching_query.sql`, `matching_service.py`, `cache_client.py`, schema SQL, and tests.
- `Marchants`: root tree shows client/server/shared plus Drizzle and Expo/Replit configuration, confirming a substantial application surface.
- `NeuraGrid`: README is minimal, but root contains a 7.9 KB pitch deck and `neurogrid-demo/`.
- `openclaw`: very large public repository; future review must separate upstream source from any local modifications before attributing capabilities to the owner's work.

## Batch interpretation
This batch reinforces four inventory rules:
1. repository name and product identity can differ;
2. tiny README is not evidence of a tiny repository;
3. reports/artifacts are evidence objects, not proof of claims;
4. explicit cross-repository links are lineage signals, not merge decisions.
