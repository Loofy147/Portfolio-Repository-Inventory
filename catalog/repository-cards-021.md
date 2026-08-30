# Repository Cards — Batch 021

Date: 2026-08-30
Scope: continued structural/source inspection. Descriptive only; no strategic decisions.

## Loofy147/Ai-hichem
- Observed: on-premise AI coding assistant monorepo on `feature/initial-project-setup`.
- Surface: FastAPI backend for local inference and semantic search; VS Code TypeScript extension; Docker Compose; Prometheus/Grafana; model update tooling; agent extension path; release workflow for on-prem registry.
- Current understanding: concrete local coding-assistant system with generation, test generation, semantic search and model switching surfaces.
- Unknowns: actual model backend, test results, security isolation, source completeness and runtime proof.
- State: D2-identified.

## Loofy147/DernAi
- Observed: README is only the title `DernAi`; conventional `package.json` path was not found.
- Current understanding: insufficient evidence to characterize purpose.
- Unknowns: tree, implementation, history and non-default refs.
- State: UNKNOWN.

## Loofy147/Research-framwork
- Observed: TypeScript/Node AI Agent Meta-Orchestrator Framework with dist, docs, src/orchestrator, variants, registry, config and CLI.
- Source evidence: `MetaOrchestrator` registers agent variants, runs standard experiments concurrently, and supports adversarial benchmarks by generating a challenging context before running target variants.
- Current understanding: executable benchmark/orchestration framework, not merely a research document.
- Important implementation detail: failures are converted into returned metrics objects for standard/target runs; adversarial top-level failure returns an empty Map. This behavior should be considered when assessing evaluation semantics later.
- Unknowns: actual experiment results, test execution and completeness of concrete variants.
- State: D2-source-verified.

## Loofy147/Free-ai
- Observed: Python "Project Free-AI / Project Sentience" with source package, tests, Docker, CI, Kaggle notebook and RAG/memory/agent components.
- Architecture described: `Director`, `ExecutorBody`, `CognitiveEngine`, `VectorMemory`, `Agora`, `SentientOracle`.
- Source evidence: `CognitiveEngine.think()` queries vector memory, asks the Oracle for a plan, validates actions/tools against a fixed action set and returns the next queued action; invalid plans are converted to an error action.
- Current understanding: concrete agent framework with RAG-backed planning and plan validation, presented as a synthesis/final incarnation of previous work.
- Unknowns: actual consciousness/sentience claims are not established by implementation; LLM behavior, tests and runtime results need verification.
- State: D2-source-verified.

## Loofy147/No-limites
- Observed: detailed Python Epigenetic Genetic Algorithm framework with EGA and AdaptiveEGA, component registry, experiment runner, parallel execution, checkpoint/resume, YAML configuration, CI and hardening notes.
- Current understanding: substantive evolutionary-algorithm research/engineering framework.
- Important implementation/evidence distinction: README claims security hardening around JSON checkpoints, configuration validation and registry validation; these remain claims until source/tests are checked.
- State: D2-identified; implementation verification pending.

## Loofy147/Multi-layer
- Observed: README only contains the title `Multi-layer`; `package.json` was not found at the conventional root path.
- Current understanding: unknown.
- State: UNKNOWN; tree/history still required.

## Loofy147/Leak-detecteur
- Observed: Next.js SaaS for detecting recurring financial waste from transaction data; integrates Plaid, Stripe, Supabase, Anthropic and Resend.
- Architecture: API routes, business logic/services, security middleware, circuit breakers, email/reporting and database schema.
- Current understanding: concrete fintech SaaS application/prototype.
- Unknowns: actual credential handling, test results, webhook correctness and production security require source-level review.
- State: D2-identified.

## Loofy147/Signals-generator-
- Observed: React Native/Expo trading-signal PoC supporting multi-timeframe Binance data, pluggable LLM providers, consensus aggregation, RAG playbook, circuit breaker and secure provider-secret storage.
- Current understanding: mobile LLM-assisted crypto signal research/application; README explicitly leaves outcome tracking and more advanced indicators for future work.
- Unknowns: actual signal logic, provider isolation, security implementation and test coverage.
- State: D2-identified.

## Loofy147/LAA
- Observed: Hugging Face Gradio Space for Learning-Augmented Algorithms; README states a Rust `laa_core` library is built during setup.
- Current understanding: interactive/demo surface for LAA algorithms rather than necessarily the canonical algorithm library.
- Unknowns: contents of `laa_core`, algorithms exposed by the Space, tests and relationship to `Crispo`/other LAA work.
- State: D1/D2; relationship target.

## Loofy147/Shop-one
- Observed: root contains `.github`, `workflows`, and a 345KB `README (2).md` specification.
- Source evidence: the specification is actually a broad Smart Delivery Platform design covering lifecycle, architecture, user management, API, authentication/authorization, database, payments, transaction processing, refunds/disputes and security.
- Current understanding: design/specification repository for a delivery/commerce platform, not a simple shop repository.
- Unknowns: workflow contents and any hidden implementation/history.
- State: D2-document-verified.

## Loofy147/Shop-grocery-
- Observed: non-empty static web surface: `index.html`, `script.js`, `style.css`.
- Current understanding: small grocery/shop web prototype.
- Unknowns: functional behavior, backend/persistence and history.
- State: D2-static-surface.

## Loofy147/Work
- Observed: root contains `client/`, `ml/`, `.gitignore`, README and `package.json`.
- Source evidence: `package.json` is minimal CommonJS scaffolding and its test script intentionally exits with "no test specified".
- Current understanding: early workspace containing client and ML areas, with no established application identity from current root evidence.
- State: D1/D2-partial.

## Loofy147/Block-chain-
- Observed: Rust crate `pow-mvp-rust` with serde, sha2, sled, rand, chrono and `src/main.rs`.
- Source evidence: defines transactions, block headers, blocks, SHA-256 block/header hashing and a simple Merkle-like aggregation.
- Current understanding: proof-of-work/blockchain MVP implementation, not empty despite a minimal README.
- Unknowns: consensus correctness, persistence behavior, transaction validation, tests and security.
- State: D2-source-verified-partial.

## Loofy147/The-industry-
- Observed: Node.js DDD example with frontend, `src`, `schemas`, Docker, production docs, GAP reports and package files.
- Source surface includes API gateway, auth, circuit breakers, configuration, CSV parser, data transformation/validation, event store and report generation.
- Current understanding: substantial software-architecture example/system implementing DDD/CQRS/event-sourcing-oriented patterns.
- Provenance signal: README clone URL points to `The-Awesome-App/the-industry.git`; local origin/modifications require explicit provenance verification.
- State: D2-source/provenance review.

## Batch findings
- `Ai-hichem` is materially more substantial than its repository name suggests.
- `Research-framwork` and `Free-ai` now have source-level evidence for actual orchestration/planning logic, while higher-level claims remain separate.
- `Shop-one` demonstrates that a huge specification may itself be the primary repository artifact.
- `Block-chain-` demonstrates again that a 14-byte README does not imply an empty project.
- `The-industry-` combines real implementation surfaces with a third-party-origin-looking clone URL, so implementation value and provenance must remain separate.

No strategic decision is assigned in this batch.