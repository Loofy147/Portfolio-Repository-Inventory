# Decision Lineage Semantic Audit v0.1

Status: OPEN / VERIFICATION RECORD

This audit records the semantic reasoning frontier. It is not proof of implementation or verification.

## 1. Confirmed invariants

I1 — Environment identity:
~~~text
Environment ≡ frozenset[AssumptionId]
~~~

I2 — Origin separation:
~~~text
Environment = algebraic support context
Origin       = explanatory derivation witness
~~~

I3 — Heuristic separation:
~~~text
HeuristicCandidate ∉ Environment algebra
HeuristicCandidate ∉ Label
HeuristicCandidate ∉ NogoodSet
~~~

I4 — Consistency separation:
~~~text
Nogood ≠ Evidence retraction
Nogood ≠ Gate rejection
Nogood ≠ Claim false
~~~

I5 — Conservative local repair:
unknown effect => MIXED; MIXED => full recomputation.

I6 — Evaluation immutability:
Every evaluation attempt, including rejection, is append-only.

I7 — Decision revision immutability:
Decision revisions are immutable; current state is a projection.

I8 — Causal ordering:
LogSeq replaces wall-clock time for provenance-sensitive ordering.

I9 — Full selection:
Full reevaluation must apply the Gate selection policy across all relevant accepted alternatives.

I10 — Differential correctness:
Incremental state must equal full replay under the same pinned semantic context.

## 2. Rejected designs

### R1 — Claim status as truth

Rejected:
~~~text
ACTIVE / INVALIDATED
~~~
as a global truth judgment.

### R2 — Evidence retraction = claim invalidation

Rejected. Losing one support route is not evidence that the proposition is false.

### R3 — One invalidated environment = decision revalidation

Rejected when alternative current supports remain valid.

### R4 — RetractEvidence globally SHRINK_ONLY

Rejected in defeasible systems.

### R5 — Gate inside Label computation

Rejected. Gate is downstream of inference and consistency.

### R6 — Heuristic as Environment

Rejected. HeuristicCandidate is a disjoint type.

### R7 — Derived Nogood = {default assumption}

Rejected except when exception environment is empty.

General form:
~~~text
{default_assumption} ∪ exception_environment
~~~

### R8 — current revision = max(created_at)

Rejected. Use causal log order and revision ancestry.

### R9 — Environment.semantics_class as provenance

Rejected. Support class belongs to Origin because the same Environment can have different Origins.

### R10 — Label → Nogood → Label without stratification

Rejected for v1. Cyclic defeater dependencies require separate nonmonotonic semantics.

## 3. Critical semantic tests

### T1 — Independent supports

~~~text
E1 → C
E2 → C
~~~

Retracting E1 must leave E2.

### T2 — Conjunctive derivation

~~~text
E1 → A
E2 → B
A,B → C
~~~

Expected:
~~~text
{E1,E2}
~~~

### T3 — Same Environment, different Origins

One Environment has both DEDUCTIVE and DEFEASIBLE Origins.

Environment identity must remain unchanged.

### T4 — Gate divergence without Label mutation

Different Gates may accept/reject different Origins while SupportLabel and NogoodSet remain unchanged.

### T5 — Contextual derived Nogood

If:
~~~text
Label(Exception_r) = {{E}}
~~~
then:
~~~text
Nogood = {{NoException_r,E}}
~~~
not:
~~~text
{NoException_r}
~~~

### T6 — Defeater retraction

Removing the sole support for Exception_r removes its derived Nogood. Previously blocked defaults may become live. Generic local repair is therefore forbidden unless shrink-only is proven.

### T7 — Multiple Origins

Invalidate O1. If O2 still derives the same Environment, the Environment remains derivable. Only provenance changes.

### T8 — Dominance

For the same SupportClass:
~~~text
E1 ⊂ E2
~~~
E2 is dominated. Cross-class dominance is not applied.

### T9 — Provisional evidence

Unverified evidence must not change structural consistency unless the pinned SemanticModel explicitly permits it. Gate-local provisional acceptance cannot make NogoodSet Gate-dependent.

### T10 — Defeater cycle

Attempt to register a cyclic default/exception dependency. Expected: registration rejected in v1.

### T11 — Derivation cycle

Attempt C1 → C2 → C1. Expected: registration rejected in v1.

### T12 — Full reevaluation

If multiple alternatives are accepted, selection_policy sees all results. The previously selected alternative is not privileged because it survived.

## 4. Differential oracle

Reference:
~~~text
full_replay(event_log, pinned_context)
~~~

Optimized:
~~~text
incremental_apply(event, cached_state)
~~~

Compare:
- RawSupport
- SupportLabel
- NogoodSet
- Label
- Origin frontier
- AdmissionResult
- Evaluation outcome
- Current Decision

Mismatch is an optimization defect until a semantic-version change is explicitly declared.

## 5. Open blockers

B1. Prove partitioned SupportLabel completeness.
B2. Define structural evidence eligibility for derived Nogoods.
B3. Formalize effect-capability soundness.
B4. Prove RawSupport completeness under acyclic derivations.
B5. Define whether MUTUALLY_EXCLUSIVE is permanent or versioned.
B6. Specify selection policy across support classes and Origins.
B7. Implement differential oracle.

## 6. Status discipline

This document records design reasoning and unresolved verification obligations. It must not be cited as implementation evidence.

Implementation claims must point to repository/ref/commit and executed test artifacts.
