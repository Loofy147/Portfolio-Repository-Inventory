# PORP-Guided Discovery Wave — 2026-09-28

## Discovery basis

The user-supplied Portable Orchestration Protocols — Enhanced Durable Baseline v1.0 defines a portable orchestration loop and a minimal core containing:

- Capability Registry
- Task Graph
- State Machine
- Event Log
- Claim Store
- Authority Gate
- Verification Engine
- Recovery Engine
- Artifact Registry

This wave uses those mechanisms as a search taxonomy, not as evidence that any candidate implements them completely.

## Inventory boundary

The latest exact census remains 342 repositories.

Two identities have been observed after that census:

1. Loofy147/Digital-twin
2. Loofy147/MORPHS

Therefore the recorded identity frontier is 344 observed identities, but this is not a replacement full census.

## New identity

### Loofy147/MORPHS

Main HEAD: 31543069e9a42a81be476bccf40776dc7a6b2411

GitHub Actions run #133 completed successfully on the same HEAD.

MORPHS exposes a mechanism-level overlap with the portable orchestration boundary:

- capability discovery/classification;
- epistemic-state discipline;
- authority separation;
- dependency-aware task execution;
- evidence and verification;
- recovery and unknown external outcomes;
- durable event/provenance concepts;
- external-world reconciliation.

Experiment 041 is currently EXPERIMENTALLY_SUPPORTED, but only within a deterministic external-world simulator.

The experiment explicitly tests dependency ordering, fresh observation, authorization blocks, unknown mutation outcomes, and drift/re-observation.

Its current limitations remain:

- arbitrary external APIs;
- irreversible effects;
- network partitions;
- adversarial state reporting;
- unrestricted root-cause automation.

No portability or production equivalence is inferred from this experiment.

## Already-known repositories surfaced again

The PORP search also repeatedly rediscovered:

- canonical-capability-core
- My_browser
- Llms-mcp-android
- unified-knowledge-work-system
- m0-durable-run
- Conversational
- Open-System-One
- atlas-lifehacks

Their reappearance is useful as convergence evidence for the capability taxonomy, but it does not create new identity records.

## Next discriminating experiment

The next useful test is not another broad repository audit.

Use one portable run contract to compare:

MORPHS external reconciliation
→ canonical-capability-core authority/reconciliation
→ m0-durable-run durability/replay
→ UWS orchestration/persistence

The objective is to determine which mechanisms are actually portable across implementations, while preserving simulator-only and repository-specific limitations.