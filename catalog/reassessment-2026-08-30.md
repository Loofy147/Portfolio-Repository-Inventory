# Reassessment — README is not a repository-state oracle

**Date:** 2026-08-30

This record corrects an earlier inspection assumption: a short or uninformative README does **not** imply an empty or low-content repository. Repository state must be assessed from metadata, root tree, source/build surfaces, tests, CI, data, documentation, and history as available.

## Corrections / stronger observations

### Rationale-agent
Earlier: classified primarily from README.
Now: root tree confirms `.github`, benchmark and planning documents, Dockerfile, `enhanced_agent.py`, `mas/`, `openapi.yaml`, `pyproject.toml`, `pytest.ini`, `tests/`, scripts, and docs. It is structurally substantial even before source-level execution verification.

### TGI-Market-Engine
Earlier: README was only 19 bytes, which is insufficient for classification.
Now: root tree confirms implementation/documentation/data surfaces including `README_IMPLEMENTATION.md`, BTC and gold historical Parquet datasets, `src/`, `tgi_engine/`, `scripts/`, `tests/`, and `.github`. Therefore the README must not be used as a proxy for repository content.

### STRATOS
Root metadata and tree confirm a TypeScript monorepo with `apps/`, `packages/`, `services/`, `infrastructure/`, `docs/`, `scripts/`, `pnpm-workspace.yaml`, Turbo configuration, package lock, GitHub configuration and Husky. This is a system architecture repository, not a README-only artifact.

### OMNIS 2.0 NODE
The repository contains a substantial documentation/protocol and implementation surface: `AGENTS.md`, `CODEX.md`, `CONTRIBUTING.md`, `ERROR_FIXES_SUMMARY.md`, `KEY_WORDS.md`, `OMNIS_API_SOURCE_OF_TRUTH.md`, `README.md`, application/service/package/infrastructure directories and an admin-console artifact. Treat as a full-system candidate for later verification, not as a lightweight concept.

### NeuraSynth
Root tree contains a PDF plus text architecture artifact, business model, implementation plan, executive summary, expansion proposals, launch/relations, legal templates, optimization/gap analysis, SWOT, CSS and application files. The repository therefore carries both product-design artifacts and implementation/UI material.

### Hbo
Root tree exposes Python implementation and operational surfaces: `advanced_optimizers.py` (~50KB), HPO patch tooling, configuration, Docker/compose, examples, production-system directory, coverage artifact and requirements. It requires source/test analysis before determining its actual scientific/engineering state.

### Learning-agent
Root tree exposes Docker, Alembic, app/data directories, a ~1.5MB dataset file, image/learning-material directories, pytest configuration and database migration configuration. It is demonstrably more than a README-level project.

### Trading-app
Root tree exposes a Vite/TypeScript application with `App.tsx`, components, services, metadata, package/package-lock, types, config and an npm output log. It should be treated as an implemented UI/application surface pending deeper source inspection.

### SpotUp-gg
Root tree includes Android/Gradle application structure (`app/`, Gradle build files, source directory) plus `metadata.json`. The metadata explicitly describes SpotUp as a spontaneous local-activity coordination app using a server-side Gemini capability. This is an Android application surface, not an empty concept.

### Agentdit
Root tree contains architecture, roadmap, agent registry, benchmark report, large market data, Playwright tests, package manifests and a public dashboard/index. The README specifies a financial execution layer combining double-entry accounting, SAC and programmatic evaluation. Performance and invariant claims remain claims until independently checked.

### Swarm-AGI
Root tree contains staged directories (`1_foundations`, `2_moonshot`, `3_deep_vision`, `4_the_legion`, `5_experimental`), a `Legion` artifact, `main.py`, outputs and dependencies. The staged topology is itself evidence of a multi-phase research/experimentation repository and warrants deeper inspection.

### TNN-ARC-AGI-2026
Root tree contains `src/`, `data/`, `docs/`, and README. It is not justified to call it trivial merely because the README is short.

## New operating rule

`README_STATUS` and `REPOSITORY_CONTENT_STATUS` are separate fields.

A short README can coexist with:
- substantial implementation;
- large datasets;
- research artifacts;
- generated code;
- deployment configuration;
- tests and CI;
- historical branches.

A repository is considered **empty** only when the accessible repository surface establishes emptiness, not when the README is empty or missing.

No strategic decisions are made by this reassessment.
