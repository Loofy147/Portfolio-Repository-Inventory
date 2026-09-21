
# Research Reasoning & Frontier Protocol v0.1

Status: PROPOSED / OPERATIONAL FOR RESEARCH BRANCH

## 1. Purpose

The portfolio must preserve not only conclusions and positive evidence, but also the reasoning that materially changed the research frontier.

A durable record must prevent:
1. repeating a previously killed hypothesis because the reason for rejection was forgotten;
2. reopening an already-settled discussion without identifying the new evidence or requirement that justifies reopening.

This is not transcript archiving. It is compact, provenance-preserving reasoning memory.

## 2. Governing rule

A discussion becomes durable when it materially changes any of:

- claim status;
- hypothesis status;
- decision;
- architecture/specification boundary;
- experiment design;
- evidence interpretation;
- relationship between repositories;
- known failure mode;
- open question;
- revalidation obligation;
- future re-opening condition.

Transient wording and redundant exploration do not need to be stored.

## 3. Durable research thread

Each material thread should preserve:

Question
Current hypothesis/claim
Candidate alternatives
Evidence and arguments
Objections/counterexamples
Disposition
Decision or rejection
Residual uncertainty
Re-open condition
Next discriminating action

This is the minimum anti-repetition unit.

## 4. Statuses

OPEN
ESTABLISHED
EXPERIMENTALLY_SUPPORTED
REJECTED
SUPERSEDED
CONDITIONAL
UNKNOWN

REJECTED is durable negative knowledge. It does not mean impossible in every context.

A rejection must retain:
- proposition;
- scope;
- decisive basis;
- rejection boundary;
- what the result does not establish;
- re-open condition.

## 5. Re-opening

A rejected candidate is not mutated.

A new re-opening event/evaluation is created only when a recorded ReopenCondition is satisfied, for example:

- decisive evidence is retracted;
- a material assumption changes;
- scope changes;
- semantic context/version changes;
- a new counterexample attacks the rejection;
- the mechanism under rejection changes materially;
- previously unavailable evidence becomes available.

The historical rejection remains intact.

## 6. Killed discussion versus killed hypothesis

Not every discussion kills a hypothesis.

A discussion may reject:
- implementation shortcut;
- schema shape;
- optimization;
- interpretation;
- causal explanation;
- architecture;
- modeling assumption.

Record the durable candidate and why it was rejected. The invariant is:

candidate -> decisive basis -> boundary -> re-open condition.

## 7. Counterexamples

A counterexample that materially changes the frontier is a first-class evidence/Artifact reference.

Record:
- setup;
- candidate tested;
- expected result;
- actual result;
- discrepancy;
- interpretation;
- limitation.

A counterexample may kill a strong claim without killing a weaker claim. Preserve the distinction.

## 8. Argument structure

Reasoning relations should be typed:

SUPPORTS
COUNTERS
REFINES
CONSTRAINS
DEPENDS_ON
MOTIVATES
REJECTS
SUPERSEDES
REOPENS

A rejection should point to its decisive counterargument/evidence.

A decision should point to the claims/evidence/arguments that justify it.

## 9. Validity envelope

Every durable rejection or conditional result carries a validity envelope:

- scope;
- assumptions;
- semantic context;
- evidence cutoff.

A later environment change does not silently revive the candidate. It creates a revalidation question.

## 10. Anti-repetition key

Research threads need stable identity independent of wording.

For v0.1 use an explicit thread_id.

A future normalization algorithm may derive stable keys from normalized subject + question type + scope, but this is OPEN and must not be invented implicitly.

Before starting a new thread:
1. search existing questions and rejected candidates;
2. inspect linked evidence and re-open conditions;
3. classify the new thread as identical, refinement, contradiction, reopening, or new;
4. record the relationship.

## 11. Research frontier

The durable frontier is the materialized set of:
- OPEN questions;
- active hypotheses;
- unresolved contradictions;
- pending revalidation;
- recently rejected items with unsatisfied re-open conditions;
- next discriminating actions.

The frontier must not depend on the latest conversation being available.

## 12. Conversation sync

A conversation sync records:
1. durable findings;
2. rejected candidates;
3. decisions;
4. contradictions;
5. new questions;
6. re-open conditions;
7. next discriminating actions.

It does not copy the full transcript.

A sync is complete when every reasoning change that would alter future work is represented durably.

## 13. Provenance

Repository-backed reasoning:
repository + branch/ref + commit

Execution:
repository/ref + experiment/test identity + inputs/fixture + result artifact

External source:
source + version/date when relevant + access date + exact referenced claim

Pure derivation:
premises + rule/argument identifier

Rejected hypothesis:
candidate + decisive basis + scope + validity envelope + re-open condition

## 14. Interaction with the portfolio ontology

Do not create a parallel domain ontology.

Use the existing:
- Claim;
- Evidence;
- Experiment;
- Decision;
- Gap/Unknown;
- Contradiction;
- Relationship.

The reasoning frontier is a control/evidence layer linking those records.

## 15. Bidirectional reasoning lineage

Forward:

Question
-> Candidate
-> Evidence/Argument
-> Objection/Counterexample
-> Disposition
-> Decision/Rejected Candidate
-> Re-open Condition / Next Test

Backward:

Decision
-> why?
-> claims/evidence/arguments
-> which alternatives were rejected?
-> why were they rejected?
-> what would reopen them?

## 16. Negative knowledge

Do not record only "we decided not to do X."

Record why X was rejected and under what boundary.

This distinguishes:
- already killed;
- not yet investigated;
- temporarily deferred;
- rejected only under an old scope.

## 17. Revalidation triggers

Re-open or revalidate prior reasoning when:
- decisive evidence changes;
- assumptions change;
- scope changes;
- semantic model/version changes;
- relevant implementation/dependency changes;
- a new mechanism changes the causal boundary;
- new evidence becomes available.

Otherwise a REJECTED item remains part of the negative knowledge base.

## 18. Stopping rule

A reasoning thread should terminate in or remain explicitly at:
ESTABLISHED, EXPERIMENTALLY_SUPPORTED, REJECTED, SUPERSEDED, CONDITIONAL, UNKNOWN, or OPEN.

If unresolved, record the next discriminating action.

## 19. Core invariant

Do not make future work rediscover a past reasoning step when that step materially changed the research frontier.

The durable record must answer:
- what did we consider?
- why?
- what evidence/argument changed it?
- what was rejected?
- what survived?
- what remains unknown?
- what would reopen the rejection?
- what must be tested next?
