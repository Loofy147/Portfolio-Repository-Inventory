
# Decision Lineage Semantics — Research Thread Record 2026-09-21

Status: OPEN / DURABLE REASONING RECORD
Repository: Loofy147/Portfolio-Repository-Inventory
Research branch: research/decision-lineage-semantics-v0.1

## Purpose

Preserve the reasoning frontier so future work does not repeat already-resolved objections or revive rejected designs without a triggering change.

This is not a transcript.

## Thread

Question:

Can a decision-lineage system provide verifiable direct and indirect support, preserve historical decision reasoning, revalidate after evidence changes, and keep decision authority local without conflating support with truth?

## Current direction

ATMS-derived support/environment semantics + versioned Gate + immutable Evaluation + immutable DecisionRevision + event-sourced provenance.

## Durable rejected designs

D1. Evidence -> Claim as truth-entailing relation.
Disposition: rejected.
Reason: direct evidence is a support/provenance relation, not a truth assignment.
Surviving boundary: support and counter relations are explicit.

D2. Evidence retraction -> Claim INVALIDATED.
Disposition: rejected.
Reason: another independent support environment may survive.
Surviving boundary: support state changes; truth is not represented as a mutable global status.

D3. Environment has an independent id/status.
Disposition: rejected.
Reason: minimality/dominance require extensional set identity.
Surviving boundary: Environment = frozenset of Assumption ids.

D4. DIRECT_SUPPORT and DERIVED are Environment identity.
Disposition: rejected.
Reason: one Environment may have multiple derivation/provenance certificates.
Surviving boundary: Origin/DerivationInstance is parallel provenance.

D5. HeuristicCandidate is an Environment.
Disposition: rejected.
Reason: heuristic candidates do not participate in assumption-set algebra.
Surviving boundary: disjoint type, Gate-local and ephemeral.

D6. Gate controls Label formation.
Disposition: rejected.
Reason: inference must be shared across decision contexts.
Surviving boundary: Gate consumes Label + Origins.

D7. Any support invalidation makes the Decision RE_EVALUATING.
Disposition: rejected.
Reason: alternative support environments can survive.
Surviving boundary: revalidation is impact-sensitive.

D8. RetractEvidence is globally SHRINK_ONLY.
Disposition: rejected.
Reason: defeater support can disappear, removing a Nogood and reopening an environment.
Surviving boundary: EffectCapability is conservative; unknown/mixed requires full recomputation.

D9. Historical Justification/Evaluation is mutable.
Disposition: rejected.
Reason: historical evaluation must remain auditable.
Surviving boundary: Evaluation is immutable; current justification is a projection.

D10. Evaluation lineage and Decision lineage are one mutable record.
Disposition: rejected.
Reason: warrant changes and chosen-alternative changes are distinct transitions.
Surviving boundary: Evaluation.supersedes and DecisionRevision.revises are separate.

D11. created_at defines current revision.
Disposition: rejected.
Reason: wall-clock time is not causal order.
Surviving boundary: LogSeq + revision ancestry.

D12. Defeater recursion can be left implicit.
Disposition: rejected.
Reason: cyclic nonmonotonic dependencies require explicit semantics.
v1 boundary: defeater dependency cycles are rejected at registration.

D13. Derived defeater Nogood is always the singleton default assumption.
Disposition: rejected.
Reason: if the exception needs environment E, the inconsistent set is default assumption union E.
Surviving boundary:
derived_nogood = {default_assumption} union exception_environment.
Singleton occurs only when exception environment is empty.

D14. Environment.semantics_class is the provenance class.
Disposition: rejected.
Reason: the same extensional Environment may have multiple Origins with different support classes.
Surviving boundary: support class belongs to Origin.

## Important correction to earlier reasoning

The earlier trace that treated a nonempty exception Label as automatically producing singleton {NoException_r} is invalid.

Correct contextual form:

If Label(Exception_r) contains E, then the derived structural Nogood candidate is:

{NoException_r} union E.

This correction is itself part of the durable negative knowledge base and must not be reintroduced later.

## Current open questions

O1. Is partitioned SupportLabel complete while remaining Gate-independent?

O2. Which evidence statuses can generate structural derived Nogoods?

O3. Can SHRINK_ONLY effect capability be defined as a sound conservative property?

O4. Is RawSupport complete under acyclic derivation constraints?

O5. Are MUTUALLY_EXCLUSIVE relations permanent or versioned/revisable?

O6. How does selection policy compare multiple admissible Origins/support classes?

O7. Can incremental state be shown equivalent to full replay?

## Re-open conditions

Reopen this thread when:
1. a formal result contradicts the current semantic boundary;
2. a minimal counterexample violates a surviving invariant;
3. cyclic defeasible reasoning becomes a required use case;
4. a Gate requirement proves Origin-aware partitioning insufficient;
5. differential verification finds incremental/full mismatch;
6. historical evaluation cannot be reconstructed from pinned context.

## Next discriminating actions

1. Prove/test partitioned SupportLabel completeness.
2. Define structural evidence eligibility.
3. Formalize derived contextual Nogoods.
4. Define EffectCapability soundness.
5. Build semantic tests.
6. Build full replay oracle before incremental optimization.

## Status boundary

This record is durable reasoning provenance and negative knowledge.

It is not implementation evidence.
Implementation evidence must reference actual repository/ref/commit and executed artifacts.
