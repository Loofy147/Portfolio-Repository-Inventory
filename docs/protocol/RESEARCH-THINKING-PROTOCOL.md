# Research Thinking & Context Preservation Protocol

**Status:** Working meta-protocol
**Purpose:** Preserve and continuously improve the reasoning discipline used while reconstructing the portfolio and its history. This document records method, not a final product thesis.

## 1. Core Principle

The conversation is a temporary working surface. Durable knowledge must be externalized into versioned records with provenance.

Do not treat the latest interpretation as truth merely because it is newer. Treat the research state as evolutionary:

`Observation → Hypothesis → Test → Evidence → Counterevidence → Correction → Decision → Consequence`

Every transition should remain inspectable.

## 2. Context First, Conclusions Later

When a large documentation corpus is supplied (Markdown, PDF, notes, specifications, reports, diagrams, repository artifacts), the first objective is **context reconstruction**, not product ideation.

Process:

`Collect → Read → Extract → Link → Reconcile → Identify contradictions → Build global context → Evaluate`

Do not force documents into premature consistency. Contradictions, obsolete assumptions, abandoned branches, and changed definitions are research assets.

## 3. Evidence Layers

Keep these states distinct:

`DOCUMENTED`

A document states or proposes something.

`IMPLEMENTED`

Repository/source evidence shows an implementation exists.

`TESTED`

A bounded test exercised the implementation.

`REPRODUCED`

An independent or separately controlled run reproduced the relevant result.

`EXTERNALLY_VALIDATED`

Evidence outside the originating project supports the claim.

`USEFUL`

Observed use or measurable internal value exists.

`VIABLE`

Technical/economic viability has been demonstrated for the stated context.

`COMMERCIAL`

There is direct market evidence sufficient for a commercial claim.

Never silently promote one level into another.

## 4. Epistemic Vocabulary

Use explicit epistemic labels:

- `OBSERVED`
- `DERIVED`
- `INFERRED`
- `USER_REPORTED`
- `UNKNOWN`
- `CONTRADICTED`
- `OPEN`

A missing observation is not proof of absence. An inference is not an observation. A user-reported result is not independent validation.

## 5. Assumption Discipline

Every consequential design or strategic statement should be traceable to one or more assumptions.

Record:

- the original assumption;
- why it appeared reasonable at the time;
- evidence supporting it;
- evidence opposing it;
- falsification attempt;
- what changed;
- whether the assumption survived, weakened, or was killed;
- downstream decisions affected by the change.

Never delete a disproven assumption simply because it is wrong. Its failure is part of the research history.

## 6. Historical Reconstruction

For evolving ideas and systems, reconstruct state over time rather than summarizing only the latest state.

Preferred form:

`T0 assumption → T1 design → T2 implementation → T3 evidence → T4 correction → T5 current state`

When evaluating an old decision, apply **information cutoff**: use only evidence that was available at the decision date unless explicitly performing hindsight analysis.

## 7. Portfolio Interpretation

Treat:

`Repository ≠ Project ≠ Idea ≠ Capability ≠ Asset ≠ Product ≠ Venture`

A repository can be:

- an implementation;
- a fork/upstream copy;
- a wrapper;
- a research artifact;
- a specification archive;
- a generated surface;
- shared infrastructure;
- a historical branch of another idea;
- an unknown requiring further inspection.

Do not count repository quantity as project quantity.

## 8. Relationship Discipline

Candidate relationships require evidence. Distinguish:

`SAME_VOCABULARY`
`CONCEPTUALLY_RELATED`
`SAME_IDEA`
`LINEAGE_CANDIDATE`
`SUCCESSOR_CANDIDATE`
`DUPLICATE_CANDIDATE`
`SAME_IMPLEMENTATION`
`SHARED_CAPABILITY`
`DEPENDENCY`
`UPSTREAM_DERIVED`
`UNKNOWN`

Do not promote a candidate relationship into a fact solely from naming similarity.

## 9. Build-vs-Buy-vs-Compose

For internal systems, usefulness does not imply a new product should be built from scratch.

Evaluate:

`Existing OSS → Existing tooling → Existing SaaS → Internal build → Composition`

Consider total cost of ownership:

`engineering + maintenance + security + upgrades + operations + opportunity cost`

against:

`subscription + integration + lock-in + usage + migration risk`.

Prefer ownership only where ownership creates strategic leverage or unique institutional value.

## 10. Venture Filter

A technically excellent artifact is not automatically a venture.

A venture hypothesis must survive at least:

1. pain validation;
2. identifiable buyer and budget;
3. measurable economic value;
4. market-gap / platform-absorption attack;
5. internal-build / substitute attack;
6. defensibility assessment;
7. technical feasibility;
8. direct WTP evidence;
9. adversarial falsification.

Failure of a product thesis does not imply failure of the underlying technology as an internal capability or research asset.

## 11. Decision Separation

Keep these decisions distinct:

`VENTURE_GO / VENTURE_PIVOT / VENTURE_KILL`

from:

`INTERNAL_BUILD / KEEP / MERGE / EXTRACT / FREEZE / ARCHIVE / KILL`

A project may be killed as a venture while its capabilities are retained internally.

## 12. Anti-Excitement Rule

When an idea becomes more technically attractive, increase falsification effort rather than implementation speed.

Do not infer opportunity from:

- technical elegance;
- novelty;
- repository size;
- number of related projects;
- investor funding;
- large TAM claims;
- availability of implementation tools;
- apparent complexity.

Ask instead:

`What would make this unnecessary?`
`Who already solves it?`
`Why would an organization not build it internally?`
`Why would a platform not absorb it?`
`What evidence would kill our thesis?`

## 13. Conversation-to-Record Rule

When a conversation changes an important assumption, definition, architecture, or decision, record the change in a durable artifact before relying on it later.

The record should identify:

- date/context;
- previous position;
- new position;
- evidence or reasoning that caused the update;
- confidence/state;
- affected projects or documents;
- whether implementation is authorized.

The conversation remains a discovery surface; the repository becomes the durable research memory.

## 14. Continuous Improvement of the Protocol

This protocol is itself subject to falsification.

When a real case exposes a blind spot:

`Case failure → identify protocol failure → propose change → adversarial test → update versioned protocol`

Do not modify rules only because they produce an inconvenient answer. A change must have an explicit rationale and regression cases.

## 15. Current Use in This Portfolio Investigation

For the current documentation/archive effort:

1. ingest Markdown and PDF material;
2. reconstruct ideas and their chronology;
3. link concepts to repositories and repository lineage;
4. preserve obsolete and corrected assumptions;
5. distinguish documented claims from implementation and verification;
6. build a global context model only after adequate corpus coverage;
7. evaluate surviving capabilities and opportunities only after context reconstruction;
8. use separate internal-value and external-venture filters.

No product architecture should be inferred merely from the existence of this protocol.

## 16. Canonical Rule

> **Preserve the history of what we thought, why we thought it, what evidence changed it, and what survived. Then make decisions from the reconstructed evidence state—not from the latest conversation.**
