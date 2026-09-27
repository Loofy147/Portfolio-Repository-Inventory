# Integrated System Research — 2026-09-27

Status: RESEARCH RELEASE / CONSERVATIVE INTEGRATED SYNTHESIS

## Released artifact

File: INTEGRATED_SYSTEM_RESEARCH_2026-09-27.md
SHA-256: b814b35dab3027336a2b447cde2b610f1e532387089e2039418eb17f9a4df2b3
Words: 9283

The artifact includes the integrated research paper plus Appendix C, the learned Research Review Protocol, and Appendix D, release disposition.

## Applied research-method improvements

- contract-first comparisons;
- result -> interpretation -> claim separation;
- iterative diagnosis/re-diagnosis after repair;
- mechanism vs representation vs computation-relocation controls;
- multi-resource Pareto accounting;
- finite-black-box INCONCLUSIVE_AT_RESOLUTION rule;
- hidden-assistance audit;
- stronger-baseline obligation;
- branch/ref/commit provenance;
- reproduction before promotion;
- cross-boundary security review;
- semantic identity independent of execution machinery;
- alternative-explanation/falsification gate;
- regression institutionalization;
- final epistemic-status audit.

Protocol: research/RESEARCH_REVIEW_PROTOCOL_v0.2.md
Protocol commit: b00baea17f94e8d438a5bce6a8008df5e7ba8b3a

## Current epistemic frontier

### Machine

EXPERIMENTALLY_SUPPORTED, bounded:
- direct predecessor resource-bounded frontier shift;
- successor-only inverse emulation lag at tight budgets;
- reverse-index representation closure in the tested finite graph;
- target-oblivious offline/online tradeoffs;
- strict-heldout protection against target leakage;
- black-box insufficiency methodological constraint;
- reproducible fixture/harness behavior.

REFINED:
- mechanism superiority -> resource-bounded frontier shift;
- minimal failure subset -> local witness, requiring iterative repair for bundled failure sets;
- transfer effect -> deterministic contract evidence rather than transferable learning.

OPEN:
- stronger successor-only baselines;
- independent graph families;
- normalized access cost;
- compact representation closure;
- causal evaluator reflection;
- nontrivial transfer without supplied labels;
- complete branch canonicalization.

### Android

ESTABLISHED / PROVISIONALLY VERIFIED:
- model is not authorization;
- Tool exposure is not authority;
- policy, approval, risk signal, credential possession/use, egress, execution, observation and verification are distinct;
- durable effect reservation/replay blocking;
- provider-side T2 B2/B3 case evidence.

OPEN:
- caller-side UNKNOWN_OUTCOME;
- concurrent recovery;
- stale-result ordering;
- reboot/force-stop/update/power-loss;
- credential-use isolation;
- provenance-aware egress;
- native MCP lifecycle/auth;
- containment for first genuinely high-power capability;
- durable audit/event sufficiency.

NOT CLAIMED:
- general exactly-once external execution.

## Formal core

Substrate: Sigma = (X,Q,S,Pi,Delta,Omega,kappa,Lambda)

Frontier: F_Sigma = {(B_off,R,B_on): an admissible representation and online algorithm satisfy the declared correctness predicate}

Authority context: Gamma = (principal, action, version, input, scope, invocations, policy_context, credential_refs, egress_context, freshness)

Policy: P(Gamma) -> {DENY, APPROVAL_REQUIRED, ALLOW}

Effect: NEW -> RESERVED -> DISPATCHED -> {COMPLETED, UNKNOWN_OUTCOME, CONFIRMED_NOT_EXECUTED}

## High-value unresolved questions

1. Caller/provider crash recovery and durable UNKNOWN_OUTCOME.
2. Concurrent recovery linearization.
3. Stale callback rejection.
4. End-to-end credential non-observability.
5. Payload-provenance-aware egress.
6. Minimum substrate for operational stored relations.
7. Mechanism frontier replication under stronger baselines and independent graph families.
8. Compact target-oblivious representation closure.
9. Causal evaluator reflection without experimenter-supplied action structure.
10. Nontrivial transfer across hidden source/target regimes.

## Primary local provenance

Machine: research/evidence-disposition-v0 @ 137f76bc7fb56138a40b3bc98ed2a3291fe7acf5
Android: main @ 4880767491d29a5f105765683c8224c82244d1a7
Portfolio: main @ 1e01edf79c705a44317847c216bcde71ff27eea4

## Release interpretation

This is a research release, not a claim that all engineering gates are closed. Open items remain explicitly OPEN or NOT CLAIMED.

The exact artifact is identified by the SHA-256 hash above.