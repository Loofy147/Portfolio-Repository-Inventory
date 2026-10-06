# Ecosystem Friction Product Program v0.1

Status vocabulary: ESTABLISHED / EXPERIMENTALLY_SUPPORTED / INFERENCE / HYPOTHESIS / OPEN.

## Decision

Build the full identified ecosystem-friction portfolio rather than selecting a single product based on a market forecast.

Market demand remains an external unknown. The engineering response is portfolio optionality: one shared control-plane kernel, multiple independently deployable product packs, and provider-specific adapters isolated from the core.

## Shared architecture

Friction Contract -> Product Pack -> Environment Adapter -> Evidence Collector -> Verification / Gate -> Recovery Action -> Durable Artifact

Every product pack must cover:
1. Direct friction
2. Infrastructure friction
3. Indirect / second-order friction

Every product pack must provide:
- explicit invariants
- evidence requirements
- fail-closed decision behavior
- recovery path
- durable artifact / report

## Initial portfolio

### Vibe-coding
- ai-app-production-gate
- llm-cost-guard
- ai-architecture-debt

### AI discovery / GEO
- ai-visibility-audit
- llm-knowledge-pack
- review-integrity

### Cloud economics
- cloud-spend-guard
- cloud-migration-blueprint
- offsite-backup-recovery

### RAG / data quality
- rag-evaluation-gate
- rag-ingestion-pipeline
- pii-leakage-guard

### Platform resilience
- platform-shadow-export
- payment-migration-readiness
- payment-failover

## Reuse

`Software-res` is the evidence/verification research substrate and currently provides fail-closed evidence contracts, JSON Schemas, a deterministic policy engine, and Verification State / provenance work.

`m0-durable-run` is the candidate durable execution substrate and is provider-agnostic by design.

The new product suite must depend on capabilities/contracts, not on repository identity.

## Current implementation artifact

A local implementation at `/mnt/data/ecosystem-friction-suite` contains:
- shared kernel models
- evidence-state and gate semantics
- PackRegistry
- all 15 initial product pack contracts
- architecture documentation
- TDD suite: 7/7 passing
- compileall validation passing

The local environment could not perform editable installation because external package retrieval is unavailable. This is an environment limitation, not a project test failure.

## Next engineering frontier

Replace pack-only catalog entries with real adapters and collectors, beginning with the capability boundaries that can be shared across multiple packs:
- repository/schema inspection
- evidence collection
- policy evaluation
- execution and recovery
- durable artifact generation
- provider adapter interfaces