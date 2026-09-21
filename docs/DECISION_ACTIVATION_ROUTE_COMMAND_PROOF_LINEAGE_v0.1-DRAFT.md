
# Decision Activation, Routes, Commands & Proof Lineage v0.1-DRAFT

Status: DRAFT / SEMANTIC REVIEW

## 1. Purpose

The decision-lineage model needs one additional boundary between "a decision is selected" and "something is activated".

A decision is not an execution command.

A route is not evidence.

A command is not proof.

A warrant/proof is not execution success.

The intended chain is:

DecisionRevision
  ↓
RouteRevision
  ↓
ActivationRequest / Command
  ↓
ActivationWarrant
  ↓
Issued Command
  ↓
Execution Run
  ↓
Execution Evidence

This preserves the distinction between authority, planned path, activation, execution, and observed outcome.

## 2. Decision

A DecisionRevision records a selected alternative under a pinned evaluation context.

It answers:

> What was selected?

It does not itself authorize execution.

A selected DecisionRevision may be informational, planning-only, or executable under an explicit activation policy. Whether execution is permitted is a separate Gate/policy decision.

## 3. Route

A Route is a versioned execution/planning path associated with a decision alternative.

RouteRevision:
  id
  route_key
  version
  decision_key
  decision_revision_id
  steps[]
  preconditions[]
  postconditions[]
  dependencies[]
  rollback_policy
  resource_limits
  semantic_context
  log_seq

RouteRevision is immutable.

A Route is a description of intended traversal/operations.

It is not evidence that the route is valid in the external world.

It is not proof that execution will succeed.

## 4. Path semantics

A route can have structural properties:

- well-formed;
- dependency-complete;
- acyclic, when required by the route type;
- internally consistent;
- compatible with its RoutePolicy.

These are route properties.

They must not be confused with:
- decision warrant;
- external-world truth;
- execution success.

## 5. Activation request

An ActivationRequest asks the system to make a specific DecisionRevision + RouteRevision executable.

ActivationRequest:
  id
  decision_revision_id
  route_revision_id
  requested_by
  requested_at_log_seq
  requested_capability
  requested_scope

The request does not itself grant authority.

## 6. ActivationWarrant

ActivationWarrant is a decision-scoped admissibility result for activating one exact route under one exact decision revision.

ActivationWarrant:
  id
  activation_request_id
  decision_revision_id
  route_revision_id
  gate_id
  gate_version
  evaluation_id
  inference_context
  witness
  proof_kind:
    DEDUCTIVE_PROOF
    DEFEASIBLE_WARRANT
    HEURISTIC_WARRANT
    POLICY_WARRANT
  valid_for:
    decision_revision
    route_revision
  issued_at_log_seq
  expires_or_revalidate_on

The warrant is immutable.

It is derived from Evaluation/Gate state; it is not a replacement for them.

### Important distinction

- DEDUCTIVE_PROOF: only when the relevant derivation is deductive under the declared semantics.
- DEFEASIBLE_WARRANT: defeasible admissibility; not deductive proof.
- HEURISTIC_WARRANT: heuristic acceptance; never silently promoted to deductive proof.
- POLICY_WARRANT: authorization based on an explicit policy Gate rather than proposition derivation.

The word "proof" must not be used as a generic synonym for "accepted".

## 7. Command

A Command is an instruction to activate or execute a specific route.

Command:
  id
  activation_request_id
  activation_warrant_id
  decision_revision_id
  route_revision_id
  command_type
  payload_ref
  status
  issued_at_log_seq

The Command must reference the exact DecisionRevision, RouteRevision, and ActivationWarrant.

No command may refer only to a logical decision key and current route, because both may have changed.

## 8. Command status

Command status is execution lifecycle, not decision truth.

Suggested states:

ELIGIBLE
AUTHORIZED
ISSUED
STARTED
COMPLETED
FAILED
ABORTED
UNKNOWN_OUTCOME

These are not Claim statuses and must not be reused for inference.

Every transition is append-only.

## 9. Proof/warrant linkage

A command can expose a complete justification chain:

Command
  ↓
ActivationWarrant
  ↓
Evaluation
  ↓
DecisionRevision
  ↓
EnvironmentWitness / HeuristicWitness
  ↓
Origin(s)
  ↓
Assumptions
  ↓
Evidence

For deductive support, the chain may additionally expose the full derivation DAG.

For defeasible support, it exposes the default assumptions and applicable Nogoods/defeater context.

For heuristic support, it exposes the heuristic candidate and its provenance, but does not fabricate an Environment.

This is the desired direct and indirect verifiable linkage.

## 10. Proof graph versus execution graph

These must remain separate.

Proof / warrant graph:
why activation was admissible.

Execution graph:
what commands were issued, what steps ran, what artifacts/results were produced, and what actually happened.

The two graphs are linked at Command/ActivationWarrant, but neither is substituted for the other.

A successful execution does not retroactively prove the original warrant.

A valid warrant does not prove successful execution.

## 11. Activation validity

An ActivationWarrant is valid only for the exact pinned context.

Conceptually:

valid_warrant iff:
- referenced DecisionRevision is the intended revision;
- referenced RouteRevision is the intended version;
- referenced Evaluation remains the relevant admissibility record;
- Gate/version is unchanged;
- required inference semantic context is unchanged;
- route preconditions required at activation are satisfied;
- no explicit revocation/revalidation condition has fired.

The warrant may become stale without becoming historically false.

Historical warrant remains immutable.

## 12. Revalidation and stale commands

A later evidence change does not rewrite a prior Command.

Instead:

Evidence/Event change
  ↓
impact analysis
  ↓
ActivationWarrant may become STALE / REVALIDATION_REQUIRED
  ↓
new ActivationWarrant if revalidated

Already-issued execution remains a historical fact.

If a command has not started, policy may block execution after warrant staleness.

If execution already started, the response is an execution-control problem, not a retroactive truth change.

## 13. Route changes

A RouteRevision change must not silently modify an existing ActivationWarrant.

New RouteRevision:

Route_v1
  ↓ supersedes
Route_v2

requires a new ActivationRequest/Warrant if Route_v2 is to be activated.

This preserves exact decision-to-path provenance.

## 14. Decision changes

If DecisionRevision D1 selected A and D2 selects B:

D1 + RouteA + WarrantA

must not be reused as the authorization chain for:

D2 + RouteB.

A new activation chain is required.

The old chain remains historical.

## 15. Direct and indirect proof queries

Why was this command authorized?

Command
-> ActivationWarrant
-> Evaluation
-> Gate
-> witness/origins
-> evidence

Which decision authorized this command?

Command
-> DecisionRevision

Which evidence directly supported the authorization?

Warrant
-> witness/origins
-> DirectSupport evidence

Which indirect derivations were involved?

Warrant
-> Environment
-> Origins
-> DerivationInstances
-> premise Origins

What execution evidence resulted?

Command
-> Run
-> Artifact/Evidence

These paths are typed and traceable.

## 16. No authority leakage

The following are deliberately distinct:

Decision:
  selected policy choice

Gate:
  local admissibility/authorization semantics

ActivationWarrant:
  recorded authorization result

Command:
  issued instruction

Run:
  execution instance

Evidence:
  observed result

None of these implies truth by name alone.

## 17. Failure boundaries

Failure at any layer should remain local:

Decision rejected
  !=
Route invalid

Route invalid
  !=
Warrant rejected

Warrant rejected
  !=
Decision false

Command failed
  !=
Warrant invalid

Execution evidence contradicts expected postcondition
  !=
historical command erased

Each transition creates new evidence/state rather than rewriting previous layers.

## 18. Open semantic questions

A1. Does every executable Decision require a RouteRevision, or can some decisions execute directly?

A2. Which Gate authorizes activation: the decision Gate, a separate ActivationGate, or both?

A3. Can an ActivationWarrant survive a RouteRevision change when the changed route is observationally equivalent? If yes, the equivalence relation must be versioned and proven.

A4. Which route preconditions are structural and which require live external evidence?

A5. What is the exact revocation model for not-yet-started Commands?

A6. Can one ActivationWarrant authorize multiple Commands, or must authorization be single-use?

A7. Which execution outcomes can trigger automatic revalidation of the originating Decision?

A8. What constitutes a POLICY_WARRANT, and how is it distinguished from a derivational warrant?

No execution schema should be frozen until these are resolved.

## 19. Design invariant

The complete trace must always be traversable:

Question
→ Candidate
→ Decision
→ Route
→ ActivationRequest
→ ActivationWarrant
→ Command
→ Run
→ Evidence

and in reverse:

Evidence
→ Run
→ Command
→ Warrant
→ Decision
→ Candidate
→ Question

This is the operational form of verifiable decision/path linkage.
