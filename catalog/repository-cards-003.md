# Repository Cards — Batch 003

Date: 2026-08-30
Inspection level: D1/D2 depending on repository.
Rule: summaries describe only inspected evidence; they are not final strategic decisions.

## Batch

### System-manifi
- **Observed:** README contains only the repository title.
- **Current understanding:** purpose cannot be established from the inspected surface.
- **Type signal:** unknown.
- **Next evidence:** root tree and any non-README artifacts.
- **Status:** UNKNOWN.

### Ket-apk
- **Observed:** README contains only the repository title.
- **Current understanding:** purpose cannot be established from the inspected surface.
- **Type signal:** unknown / possibly Android artifact based on repository name only, not established.
- **Status:** UNKNOWN.

### v0-crypto-dashboard
- **Observed:** v0-generated crypto dashboard repository synchronized with v0.app deployments and Vercel.
- **Current understanding:** deployment/UI surface for a cryptocurrency dashboard rather than an independently described research core.
- **Type signal:** product/UI prototype or generated app surface.
- **Relations:** possible relation to trading repositories, but not established from this README alone.
- **Status:** STRUCTURALLY IDENTIFIED.

### Marchants
- **Observed:** root contains React Native/Expo client, Express/TypeScript server, Drizzle configuration, package manifests, design guidelines and Replit project notes. Replit notes describe an app called El-marchi: Tinder-like swipe discovery for shopping, wishlist, categories, profiles and authentication.
- **Current understanding:** concrete mobile commerce MVP with client/server/shared schema separation.
- **Type signal:** MVP application.
- **Potential relations:** e-commerce/marketplace family; relation to Shop-one or other marketplace repositories not yet established.
- **Status:** STRUCTURALLY IDENTIFIED.

### Twin-ai
- **Observed:** digital-twin system using real-world integrations, adaptive question selection, 5,000+ question bank, Supabase RLS and local SQLite; documentation includes architecture, database schema, algorithms, integrations, setup and launch material.
- **Current understanding:** substantive personal digital-twin product/research implementation.
- **Type signal:** AI application + adaptive learning system.
- **Potential relations:** agent/adaptive-learning family; no repository lineage established yet.
- **Status:** D2 TARGET.

### general-engine
- **Observed:** README contains only the repository title.
- **Current understanding:** purpose cannot be established from the inspected surface.
- **Type signal:** unknown.
- **Status:** UNKNOWN.

### NeuroGolf
- **Observed:** README contains only the repository title.
- **Current understanding:** purpose cannot be established from the inspected surface.
- **Type signal:** unknown.
- **Status:** UNKNOWN.

### screal
- **Observed:** AI Studio-generated Android application surface. README instructs opening in Android Studio, configuring GEMINI_API_KEY and running on an emulator/device.
- **Current understanding:** Gemini-powered Android app; exact product purpose is not established by README.
- **Type signal:** mobile AI application / generated starter.
- **Status:** STRUCTURALLY IDENTIFIED.

### NeuraGrid
- **Observed:** README contains only the repository title.
- **Current understanding:** purpose cannot be established from the inspected surface.
- **Type signal:** unknown.
- **Status:** UNKNOWN.

### Gemini-app
- **Observed:** web application integrating `gemini-cli` with GitHub. Uses WebSockets for real-time terminal output, server-side sessions for credentials, and a `gemini-cli` git submodule.
- **Current understanding:** web wrapper/control surface around Gemini CLI with GitHub workflow integration.
- **Type signal:** integration application.
- **Potential relation:** strong candidate relation to `gemini-cli`; exact fork/submodule relationship needs git/tree verification.
- **Status:** D2 RELATIONSHIP TARGET.

### Exchange
- **Observed:** repository is a collection of Python self-portraits/reflections (`being.py`, `kairos.py`, `jules.py`, `this.py`, `arriving.py`, `meta.py`) focused on identity, agency, presence and self-programming.
- **Current understanding:** conceptual/creative software artifact rather than conventional product implementation.
- **Type signal:** conceptual/research/creative artifact.
- **Status:** IDENTIFIED.

### Vipers-
- **Observed:** README contains only the repository title.
- **Current understanding:** purpose cannot be established from the inspected surface.
- **Type signal:** unknown.
- **Status:** UNKNOWN.

### Grok-supreme
- **Observed:** SSO-TS cryptocurrency strategy simulator/dashboard using Next.js/React/TypeScript and Python training, with xAI Grok integration, OMEGA framework terminology, Kaggle dataset/training orchestration, backtesting and performance metrics. README reports numerical performance targets/results, but these are repository claims.
- **Current understanding:** substantial trading simulation + AI-analysis application; explicitly simulation-only.
- **Type signal:** product/research prototype.
- **Potential relations:** trading family; possible OMEGA lineage with other AI framework repositories needs verification.
- **Status:** D2 TARGET; CLAIM-VERIFICATION TARGET.

### Jules-orchestrator-
- **Observed:** README title is `Gemini-Head-`.
- **Current understanding:** repository naming and README naming diverge; purpose cannot be established reliably from this surface.
- **Type signal:** unknown / possible Gemini orchestration surface.
- **Next evidence:** root tree and recent commits.
- **Status:** UNKNOWN.

### RE-UP
- **Observed:** blueprint/scaffold for relational hierarchy learning stack `CRSS → BITRS → ETRP → HRCO → ARASS → MFP → EVREP`, including mathematical specification, architecture, repository architecture and minimal implementation scaffold.
- **Current understanding:** research scaffold focused on relational hierarchy learning, intended to expand into a PyTorch implementation.
- **Type signal:** research artifact / prototype scaffold.
- **Potential relations:** RL/representation-learning family; should be compared with `training-home`, `Unified-ai`, `Herarchecal-agent`, and related research repositories.
- **Status:** D2 TARGET.

### Orvio
- **Observed:** high-performance hierarchical numeric optimization framework with solver orchestrator, adaptive meta-controller, 14-phase search/refine engine, task typing, pluggable surrogates, uncertainty-aware LCB search and structured optimization reports.
- **Current understanding:** concrete optimization engine abstraction, with examples and benchmark harness.
- **Type signal:** algorithmic research/engineering library.
- **Potential relations:** optimization family; possible connection to FSO/other optimization work requires implementation comparison.
- **Status:** D2 TARGET.

### Algorithms-
- **Observed:** README describes a monorepo/library implementing time-aware computing, resource/carbon-aware scheduling, uncertainty quantification, adversarial-first primitives, self-modifying systems, causal reasoning, algebraic/transactional composability and resilience. Workspace includes web/mobile/shared algorithms/tests/docs.
- **Current understanding:** broad computational-principles platform/library rather than a single-domain app.
- **Type signal:** research/engineering monorepo.
- **Potential relations:** likely candidate for comparison with `Twin-ai`, `canonical-capability-core`, `Software-res`, `Orvio`, and other foundational work; no lineage promoted yet.
- **Status:** D2 TARGET.

### LightRAG
- **Observed:** README is the upstream HKUDS LightRAG project, with explicit links to `HKUDS/LightRAG`, arXiv paper, PyPI package, server/core installation and RAG-related documentation.
- **Current understanding:** external/open-source upstream mirror or copy in the portfolio, not an original Loofy147 project based on inspected provenance signals.
- **Type signal:** upstream/open-source dependency or mirror artifact.
- **Provenance note:** must be treated separately from original work when assessing portfolio ownership/value.
- **Status:** PROVENANCE REVIEW.

## Batch conclusions

1. Repository size alone is not predictive: `Twin-ai`, `Marchants`, `Grok-supreme`, `Orvio`, and `Algorithms-` have substantive surfaces, while several similarly sized repositories expose almost no identifying documentation.
2. Some repositories are clearly **wrappers/surfaces** around another system (`Gemini-app` around `gemini-cli`, `v0-crypto-dashboard` around a v0 deployment), which must be represented as relationships rather than counted as independent ideas automatically.
3. Some repositories are **research scaffolds** rather than unfinished products (`RE-UP`). They must not be judged by product-MVP criteria.
4. External-source repositories such as `LightRAG` require provenance classification before any strategic value is assigned.
5. The catalog should continue until every accessible repository has at least one card, even when the correct answer is UNKNOWN.
