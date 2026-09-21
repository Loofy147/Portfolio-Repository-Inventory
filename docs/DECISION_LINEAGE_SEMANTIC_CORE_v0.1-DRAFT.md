# Decision Lineage Semantic Core v0.1-DRAFT

Status: DRAFT / SEMANTIC REVIEW

This document records the current semantic boundary for a decision-lineage and support-maintenance model derived from ATMS concepts and extended with decision-scoped gates, immutable evaluations, and decision revisions.

This is a design specification, not an implementation claim. Anything marked OPEN/REQUIRED remains unresolved until verified.

## 1. Scope

The system separates four layers:

~~~text
Inference
    ↓
Consistency
    ↓
Decision Admission
    ↓
Decision History
~~~

These meanings are deliberately distinct:

- derivable ≠ true
- consistent ≠ true
- admissible ≠ true
- selected ≠ true
- active decision ≠ true

The system records what can be derived, which environments are structurally inconsistent, what a versioned Gate permits for a decision, and which immutable decision revision was recorded.

The Environment/Label/Nogood portion is ATMS-derived. Gate, Evaluation, DecisionRevision, versioned evaluator semantics, heuristic candidates, and local-repair policy are project-specific extensions.

## 2. Canonical entities

### 2.1 Evidence

~~~text
Evidence:
  id
  immutable_content_ref
  status: UNVERIFIED | VERIFIED | RETRACTED
  status_history
~~~

Evidence retraction does not mean that the underlying proposition is false.

### 2.2 Assumption

~~~text
Assumption:
  id
  kind: BASE | DEFEASIBLE_DEFAULT
  default_rule_ref: RuleRef | None
  exception_claim: ClaimId | None
  stratum: Stratum | None
~~~

Invariants:

- BASE has no default_rule_ref, exception_claim, or stratum.
- DEFEASIBLE_DEFAULT has all three.
- default_rule_ref is versioned.
- stratum belongs to the versioned inference semantics.

### 2.3 Environment

~~~text
Environment = frozenset[AssumptionId]
~~~

Identity is extensional:

~~~text
E1 == E2 iff assumptions(E1) == assumptions(E2)
~~~

Environment has no independent identity, status, Gate, rule, or Origin field.

Subset relations are purely algebraic:

~~~text
E1 ⊆ E2
E1 ⊂ E2
~~~

They are never evaluated from provenance.

### 2.4 Origin

Origin is a parallel provenance layer:

~~~text
Origin:
  id
  claim_id
  environment: Environment
  support_class: DIRECT | DEDUCTIVE | DEFEASIBLE
  via:
    DirectSupport(evidence_id, relation)
    |
    DerivationStep(rule_id, rule_version, premise_origins[])
  produced_at: LogSeq
~~~

Multiple Origins may explain the same Environment.

Origin count and provenance do not change Environment identity or subset ordering.

A crucial invariant is:

> support_class belongs to the Origin, not to Environment.

The same extensional Environment may have multiple Origins with different inference provenance.

### 2.5 HeuristicCandidate

~~~text
HeuristicCandidate:
  rule_id
  score
  provenance: tuple[ClaimId, ...]
~~~

HeuristicCandidate is disjoint from Environment.

It has no assumption set, no subset relation, no minimality, and no membership in Label or NogoodSet. It may be evaluated only through Gate-local admission.

## 3. Inference

### 3.1 Rule

~~~text
Rule:
  id
  version
  premises_pattern
  conclusion_pattern
  class: DEDUCTIVE | DEFEASIBLE
  semantic_stratum
~~~

Rules are immutable per (id, version). Historical evaluations refer to exact Rule versions.

### 3.2 DerivationInstance

~~~text
DerivationInstance:
  id
  claim_id
  rule_id
  rule_version
  antecedent_claims[]
  premise_origins[]
  produced_environment
~~~

DerivationInstance explains how an Environment was generated. It is not the Environment's identity.

### 3.3 RawSupport

~~~text
RawSupport(claim, inference_context)
~~~

is the set of environments that can be generated before structural consistency filtering.

RawSupport is Gate-independent.

In v1, the transitive derivation dependency graph is acyclic. Registration that introduces a derivation cycle is rejected.

## 4. Support labels and minimality

Classical ATMS labels are sets of minimal environments supporting a node, with soundness, consistency, completeness, and minimality as distinct properties.

This design adds a project-specific partition because Gate semantics can distinguish provenance classes.

~~~text
SupportLabel(C):
  DIRECT:     antichain[Environment]
  DEDUCTIVE:  antichain[Environment]
  DEFEASIBLE: antichain[Environment]
~~~

Heuristic candidates are not part of any partition.

Dominance is applied only inside the same SupportClass:

~~~text
E1 dominates E2 iff E1 ⊂ E2
~~~

Minimality does not imply completeness.

For each partition:

- Soundness: every stored environment genuinely supports the claim under the inference context.
- Consistency: no stored environment contains a current Nogood.
- Completeness: every derivable consistent environment of the same support class is covered by a stored environment in that partition.
- Minimality: no environment strictly dominates another in the same partition.

Whether this partitioned form preserves full classical ATMS completeness is OPEN and must be demonstrated before schema freeze.

## 5. Consistency and Nogoods

~~~text
Nogood = Environment
NogoodSet = minimal_antichain(Set[Nogood])
~~~

An environment E is inconsistent iff:

~~~text
∃ N ∈ NogoodSet : N ⊆ E
~~~

Nogood does not mean false claim, retracted evidence, or Gate rejection.

### 5.1 Explicit structural Nogoods

A domain-declared MUTUALLY_EXCLUSIVE relation may produce explicit Nogoods.

This relation is a consistency-layer primitive and is not inferred merely because two claims have opposing names.

### 5.2 Defeasible defaults

A defeasible rule introduces an explicit default assumption:

~~~text
δr = NoException(r)
~~~

with exception_claim(r).

If an exception environment E supports exception_claim(r), the derived Nogood is:

~~~text
{δr} ∪ E
~~~

not {δr} in the general case.

Only when E = ∅ does the derived Nogood reduce to {δr}.

Derived defeater Nogoods are recomputed from current support state; they are not independently mutated through a Retraction event.

### 5.3 Stratification

v1 forbids cycles in defeater dependencies.

For each defeasible default δr:

~~~text
Every dependency used to establish exception_claim(r)
must come from a strictly lower semantic stratum.
~~~

Registration rejects a rule set whose defeater dependency graph is cyclic.

The purpose is to avoid introducing well-founded/stable-model semantics into v1.

## 6. Label computation

~~~text
RawSupport(C, inference_context)
      ↓
minimal support frontier
      ↓
current structural Nogood filtering
      ↓
Label(C, inference_context)
~~~

Gate is absent from these operations.

Gate cannot alter RawSupport, SupportLabel, NogoodSet, or Environment identity.

Historical queries are evaluated against pinned semantics:

~~~text
InferenceContext:
  semantic_model_version
  rule_pack_version
  evaluator_semantics_version
  stratum_schema_version
~~~

Thus Label_at(C,t) means the label under the historical inference context at t, not today's semantics applied to yesterday's events.

## 7. Gate and admission

~~~text
Gate:
  id
  version
  allowed_relations
  allowed_rules: Set[(rule_id, version)]
  accepts_provisional
  accepts_heuristic
  defeasible_priority
  contradiction_policy
  selection_policy
~~~

Gate is local decision authority.

It is evaluated only after inference and consistency.

Because Environment does not carry derivation provenance, Gate admissibility is evaluated against Origins:

~~~text
gate_accepts(claim, environment, origin, gate)
~~~

The same Environment may have multiple Origins; at least one Gate-admissible Origin may suffice according to the Gate's relation policy.

### 7.1 Heuristic fallback

A HeuristicCandidate can be generated ephemerally during admission.

It is never written into Label or RawSupport.

The result is a tagged union:

~~~text
Witness =
  EnvironmentWitness
  |
  HeuristicWitness
~~~

The precedence between admissible environments and heuristic candidates is part of Gate/selection policy, not accidental branch ordering.

## 8. Evaluation

~~~text
Evaluation:
  id
  decision_key
  alternative_id

  gate_id
  gate_version

  semantic_model_version
  rule_pack_version
  evaluator_semantics_version

  candidates_checked
  outcome:
    Accepted(witness, full_valid_set)
    | Rejected(reason)

  triggered_by: EventId | None
  supersedes: EvaluationId | None
  log_seq
~~~

Evaluation records are immutable and append-only. Rejected evaluations are retained.

## 9. Decision revisions

~~~text
DecisionRevision:
  id
  key
  chosen
  current_evaluation_id
  status:
    ACTIVE
    RE_EVALUATING
    SUPERSEDED
    UNSUPPORTED
  revises: RevisionId | None
  log_seq
~~~

DecisionRevision is immutable.

Current decision state is a projection over the revision chain.

A new revision must revise the current head for that key.

Causal log position, not wall-clock time, determines history order.

Evaluation lineage answers how the warrant/evaluation changed. DecisionRevision lineage answers how the selected alternative/status changed.

## 10. Revalidation

The system never converts "not currently verified" directly into "false".

Generic flow:

~~~text
Event
  ↓
impact analysis
  ↓
revalidation obligation
  ↓
local repair only if soundly shrink-only
  else full recomputation
  ↓
new Evaluation
  ↓
new DecisionRevision if required
~~~

### 10.1 Effect capability

~~~text
EffectCapability:
  SHRINK_ONLY
  MIXED
  NONE
~~~

This is a conservative over-approximation.

Unknown or unproven impact is treated as MIXED.

Local witness repair is allowed only when the affected decision closure is proven shrink-only and no new candidate can become admissible.

Evidence retraction is not globally shrink-only in a defeasible system because it may remove exception support, remove a derived Nogood, and reopen previously blocked environments.

DeclareNogood can be intrinsically shrink-only when it changes only the consistency layer by adding a Nogood.

## 11. Differential correctness

The incremental implementation is not a second semantics.

For a fixed semantic context:

~~~text
incremental_state == full_replay_state
~~~

must hold for at least:

- RawSupport;
- SupportLabel;
- NogoodSet;
- Label;
- Origin frontier;
- AdmissionResult;
- Evaluation outcome;
- Current Decision.

Full replay is the oracle for incremental optimization.

## 12. Historical queries

Derivability:

~~~text
SupportLabel(claim, inference_context_at(t))
~~~

Current consistent supports:

~~~text
Label(claim, context_at(t))
~~~

Why was an Environment obtained?

~~~text
origins_for(claim, environment)
~~~

What blocks an excluded environment?

~~~text
blocking_nogoods(environment)
~~~

This is separate from:

~~~text
dominating_environments(environment)
~~~

because an environment can be excluded by minimality without containing a Nogood.

For changes, compute separate SupportDiff, AdmissionDiff, WarrantDiff, and DecisionDiff.

## 13. Remaining OPEN items

1. Prove or disprove completeness of partitioned SupportLabel under Gate-sensitive provenance.
2. Define the exact structural evidence policy for generating structural exception Nogoods.
3. Formalize soundness of effect-capability SHRINK_ONLY.
4. Prove RawSupport completeness under acyclic derivations.
5. Decide whether MUTUALLY_EXCLUSIVE declarations are permanent or versioned/revisable.
6. Fully specify selection policy when multiple support classes or Origins are admissible.
7. Build the executable differential oracle.

No schema freeze until these blockers are either resolved or explicitly accepted as bounded limitations.

## 14. External semantic boundary

ATMS foundation:

- de Kleer, "A General Labeling Algorithm for Assumption-Based Truth Maintenance", AAAI 1988: https://cdn.aaai.org/AAAI/1988/AAAI88-034.pdf
- Reiter & de Kleer, "Foundations of Assumption-Based Truth Maintenance Systems", AAAI 1987: https://cdn.aaai.org/AAAI/1987/AAAI87-033.pdf

Recursive nonmonotonic semantics:

- Van Gelder, Ross, Schlipf, "The Well-Founded Semantics for General Logic Programs", JACM 1991: https://doi.org/10.1145/115234.115290

Event history:

- Martin Fowler, "Event Sourcing": https://martinfowler.com/eaaDev/EventSourcing.html

These sources justify external foundations only. Gate, Evaluation, DecisionRevision, heuristic separation, versioned evaluator contexts, and local-repair contracts are project-specific design decisions.
