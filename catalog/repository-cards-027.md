# Repository Cards — Batch 027

Inspection date: 2026-08-30
Purpose: descriptive census only. No strategic decision is assigned here.

## 1. Scraper
- Observed surface on default branch `feat/developer-resources-explorer`: `index.html` (~18.7KB) and `CardSkeleton.js`; the attempted README lookup returned 404, so the README cannot be treated as the description of this branch.
- Current interpretation: active branch contains a web UI/prototype surface, apparently a developer-resources explorer based on the branch name; exact product behavior remains source-level work.
- Unknowns: other files/branches, data sources, execution state, tests, and lineage.
- Review state: `D2-partially-inspected`; branch-aware review required.

## 2. Drogon
- Observed branch: `feature/autorevenue-agent`.
- README identifies `AutoRevenue Pro`: AI-assisted revenue-generation dashboard with market-trend analysis, opportunity identification, strategy management, integrations, and realtime revenue tracking. Backend is described as Express/Mongoose/MongoDB; frontend as React.
- `package.json` identifies the package as `autorevenue-agent` v0.1.0 and includes Express, Mongoose, Redis, JWT, Helmet, Supertest, Jest, React, and concurrent frontend/backend development scripts.
- Current interpretation: full-stack autonomous/revenue automation application surface with explicit security middleware and test tooling.
- Unknowns: actual strategy logic, integrations, database schema, test execution status, and safety/business validity of automated revenue actions.
- Review state: `D2-implemented-candidate`; branch/provenance review needed.

## 3. ai-meta-orchestrator
- Observed surface: Flask backend + vanilla-JS frontend layout, `.github`, pre-commit, changelog, agent documentation, Docker Compose, Jest/ESLint configs, package-lock, package.json, and `src/`.
- README is generic/template-like and still contains placeholder authors/repository URLs.
- Changelog records v1.0.0 on 2024-07-18 with initial Python backend, JavaScript frontend, linting and basic GitHub Actions CI.
- Current interpretation: early Meta Orchestrator scaffold with real project structure but generic/template documentation remains.
- Unknowns: actual orchestrator behavior, agent implementation depth, test results, and relationship to other Meta Orchestrator repositories.
- Review state: `D2-scaffold-with-history`.

## 4. training-home
- Observed surface: `dataset.jsonl` ~1.54MB, `learning-materials/`, `process_files.py`, and GitHub Actions.
- No README was available on the inspected default branch surface.
- Current interpretation: training-data/learning-material preparation repository; the large JSONL is a substantive dataset artifact rather than only project documentation.
- Unknowns: dataset schema, provenance/licensing, intended model/task, transformation pipeline details, and validation/split methodology.
- Review state: `D2-data-artifact-candidate`.

## 5. Slack-bot
- README identifies a Meta Orchestrator AI integrated with Slack Bolt; described components include `orchestrator.py`, `slack_app.py`, prompts, examples, config/utils, retry handling, async Slack processing, and validation.
- Root tree confirms `.env.example`, `.gitignore`, `.bolt`, `api/`, `base_orchestrator.py`, `code_analysis_agent.py`, `config.py`, `data_creator_agent.py`, `deployment/`, `docker-compose.production.yml`, `docs/`, `documentation_analysis_agent.py`, `embedding_agent.py`, and `enhanced_orchestrator.py`.
- Current interpretation: substantial multi-agent/orchestration implementation, significantly richer than a simple Slack bot.
- Security note: repository documents use of secrets via environment variables; only `.env.example` was observed at the root in this inspection. No secret values were read.
- Unknowns: complete agent graph, runtime behavior, tests/CI results, canonical orchestrator version, and lineage to `ai-meta-orchestrator` or other orchestrator repositories.
- Review state: `D2-deep-candidate`; `lineage-review-needed`.

## 6. Doha-platform
- README identifies “Lamsa Doha / لمسة ضحى”, an Algerian/Arab marketplace focused on women entrepreneurs and creators, supporting stores, products/services, rentals, orders, analytics, marketing, community and support.
- `package.json` identifies Next.js 15 + React 18 + TypeScript with Firebase Genkit/Google AI, Zod, Tailwind/ShadCN, Framer Motion, Pexels and Firebase. Scripts include build, typecheck, product-image download, and Genkit development/watch.
- README explicitly states that backend behavior is currently simulated/mock and that production backend/auth/storage choices remain future/configuration work.
- Current interpretation: substantial frontend/product prototype with AI-enabled content-generation hooks, but not evidence of a complete production backend.
- Unknowns: actual source coverage, database/auth implementation, tests, deployment state, and comparison with other Algerian marketplace/delivery repositories.
- Review state: `D2-implemented-frontend-prototype`.

## 7. The-matching-engine-
- README is 22 bytes, but root tree contains `matching_service.py` (~9.7KB), `matching_logic.md` (~8.6KB), `matching_query.sql` (~4.9KB), `schema_extensions.sql` (~4.4KB), `cache_client.py`, and `tests/`.
- Current interpretation: concrete matching/recommendation service with Python logic plus SQL/query/schema layer and tests; exact domain is not yet established from the inspected surface.
- Unknowns: domain model, ranking/scoring algorithm, test results, persistence/cache contract, and relationships to `synapse-platform`, `The-industry-`, and other matching systems.
- Review state: `D2-source-candidate`.

## Global note
This batch deliberately records branch/ref identity where it materially changes interpretation. No KEEP/MERGE/EXTRACT/FREEZE/ARCHIVE decision is assigned.
