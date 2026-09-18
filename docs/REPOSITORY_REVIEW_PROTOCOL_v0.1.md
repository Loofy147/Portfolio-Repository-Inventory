
# Repository Review & Evidence Handling Protocol v0.1

Status: OPERATIONAL
Date: 2026-09-18

## 1. Purpose

This repository is not only a list of repositories. It is the portfolio-level control and evidence layer for inspecting, comparing, relating, and reasoning about other repositories without collapsing distinct projects, branches, experiments, or assumptions into one narrative.

This protocol defines the minimum professional handling standard for any repository reviewed through this inventory.

The protocol is designed to prevent recurring failure modes:

- identifying the wrong repository as the active project;
- treating a default branch as the whole project;
- treating documentation as implementation evidence;
- treating terminology similarity as lineage;
- transferring claims from one repository to another without evidence;
- mixing historical implementations with current research;
- confusing observations, interpretations, assumptions, suggestions, and conclusions;
- losing the exact branch/commit provenance behind an assessment;
- turning an incomplete inspection into a false negative.

## 2. Repository identity is contextual

A repository must never be identified by name or semantic resemblance alone.

The minimum provenance tuple for a material claim is:

`repository + branch/ref + commit`

The repository-level identity additionally records:

- repository full name;
- stable repository id when available;
- default branch;
- visibility/access context when relevant;
- observation timestamp;
- inspected ref/commit.

A project may have several simultaneously meaningful branches. Therefore:

`repository != branch != project state`

The current state of a project is a claim that requires evidence.

## 3. Active-project identification

When a user refers to a project ambiguously, use this sequence:

1. Identify candidate repositories by exact name, URL, distinctive terminology, or repository description.
2. Inspect repository metadata.
3. Enumerate relevant branches.
4. Identify branches that appear to contain the current research or implementation frontier.
5. Inspect recent commits on candidate branches.
6. Read branch-specific source, tests, experiments, and documentation.
7. Compare the candidate branch with the default branch before calling anything "current", "merged", or "canonical".
8. Label older related repositories as historical/reference rather than current implementation unless evidence shows otherwise.

Do not use semantic similarity as a substitute for this procedure.

## 4. Inspection order

Default inspection order:

`METADATA -> BRANCHES/REFS -> ROOT TREE -> BUILD/MANIFEST -> SOURCE -> TESTS/CI -> DATA/ARTIFACTS -> README/DOCS -> HISTORY`

Adjust the order when the repository type requires it, but do not skip evidence-bearing surfaces merely because the README appears informative.

### 4.1 Metadata

Record:

- repository name/full name;
- stable repository id when available;
- default branch;
- repository URL;
- visibility;
- archived state;
- observed date/time.

### 4.2 Branch and ref surface

Record:

- relevant branches;
- research branches;
- release/tag refs when relevant;
- branch tip commits;
- whether the inspected work is ahead/behind default branch;
- whether a research branch is merged, unmerged, or unknown.

### 4.3 Structural surface

Inspect enough of the root tree to identify:

- language/toolchain;
- package/build manifests;
- entry points;
- tests;
- workflows;
- deployment/runtime descriptors;
- research fixtures;
- generated or vendored material;
- documentation structure.

### 4.4 Behavioral surface

For each important claim, distinguish:

- documented intent;
- implemented mechanism;
- executable test/experiment;
- observed result;
- causal interpretation.

Do not collapse these into one statement.

### 4.5 History surface

Use history to establish:

- evolution;
- replacement;
- regression/fix;
- branch lineage;
- possible successor relationships;
- introduction/removal of mechanisms.

History is evidence of change, not automatically evidence of conceptual lineage.

## 5. Evidence layers

Every material finding should be classified by evidence layer:

### OBSERVED

Directly visible in inspected repository state.

Examples:
- a file exists;
- a branch exists;
- a function contains a given mechanism;
- a commit changed a file.

### EXPERIMENTALLY_SUPPORTED

Observed through an executed or otherwise reproducible experiment/test with enough information to identify the tested setup.

### DERIVED

A deterministic conclusion from established observations.

### INFERRED

A plausible interpretation that is not directly established.

### USER_REPORTED

A fact supplied by the user but not independently verified in the inspected source.

### UNKNOWN

The inspected evidence is insufficient.

### CONTRADICTED

The claim conflicts with stronger or more direct evidence.

Do not silently upgrade a lower-evidence claim.

## 6. Claims, assumptions, and suggestions are different objects

### Claim

A statement about what is true.

Claims require provenance and an evidence status.

### Assumption

A working premise used to proceed despite incomplete evidence.

Assumptions must be visible and must not be written as established facts.

### Suggestion

A proposed action, architecture, experiment, or interpretation.

A suggestion is not evidence and must not be used later as though it were a project fact.

### Decision

A selected action or policy.

A decision may be based on evidence plus explicit assumptions, but its status must remain separate from the evidence itself.

## 7. Experiments and mechanisms must remain separated

For an experiment, keep these layers distinct:

1. observed behavior;
2. experimental mechanism;
3. host-language/runtime mechanism;
4. object-language mechanism;
5. causal interpretation;
6. architectural implication.

A successful output does not prove the internal mechanism that produced it.

A host-language implementation detail does not prove that the object language has the claimed primitive.

A reusable mechanism must be demonstrated at the layer where the claim is made.

## 8. Historical/reference repositories

A related older repository may provide:

- implementation precedents;
- failure modes;
- design patterns;
- tests;
- counterexamples;
- terminology;
- migration clues.

It does not automatically establish:

- current implementation ownership;
- current project identity;
- direct lineage;
- preservation of the same semantics;
- provenance of a newer experiment.

Use explicit relationship labels:

- `HISTORICAL_REFERENCE`
- `POSSIBLE_LINEAGE`
- `ESTABLISHED_LINEAGE`
- `SHARED_PRIMITIVE_CANDIDATE`
- `DUPLICATE_CANDIDATE`
- `INDEPENDENT_SIMILARITY`
- `SUCCESSOR_CANDIDATE`
- `DEPENDENCY`

Only promote a relationship when the evidence supports the stronger label.

## 9. Repository relationships

When comparing repositories, answer these questions independently:

### Identity

Are they actually the same project, different projects, or unresolved?

### Lineage

Is there evidence that one evolved from the other?

### Semantic overlap

Do they implement the same function or primitive without implying lineage?

### Implementation reuse

Is code, data, protocol, or infrastructure actually reused?

### Evidence transfer

Does an experiment in one repository legitimately support a claim in another?

### Architectural compatibility

Could they share a boundary without forcing a premature abstraction?

Similarity is not lineage. Shared terminology is not reuse. Historical proximity is not causation.

## 10. Current-state vocabulary

Use precise state language:

- `CURRENT`: supported by the inspected current frontier.
- `DEFAULT-BRANCH`: present on default branch.
- `RESEARCH-FRONTIER`: documented or implemented on a research branch that is not necessarily merged.
- `HISTORICAL`: older state/reference.
- `UNMERGED`: branch contains work not shown on default branch.
- `UNKNOWN`: current status cannot be established.

Do not call a research branch "canonical" merely because it is the most detailed branch.

## 11. Review packet

A professional review should produce, at minimum:

`Repository identity
Observed ref/commit
Relevant branches
Project/current-state interpretation
Inspected surfaces
Established claims
Experimentally supported claims
Assumptions
Suggestions
Unknowns
Contradictions
Relationships to other repositories
Historical references
Tests/verification status
Next discriminating test or inspection`

The packet may be stored as Markdown, JSON, or both.

## 12. Negative findings

Never record:

> "X does not exist."

unless the relevant repository surface was inspected deeply enough to justify absence.

Prefer:

> "X was not found in the inspected surfaces A/B/C at ref R."

A missing README statement is not proof of a missing implementation.

## 13. Cross-repository evidence discipline

Evidence belongs first to the repository/ref where it was observed.

When a portfolio-level conclusion is derived:

`source repository/ref -> observation -> relation/derivation -> portfolio claim`

Do not copy a claim into another repository record without retaining this provenance chain.

When evidence conflicts:

1. keep both observations;
2. retain their source refs;
3. describe the contradiction;
4. prefer neither solely because it is newer or more convenient;
5. run a discriminating inspection/experiment when needed.

## 14. Durable portfolio updates

The portfolio inventory should be updated whenever a review establishes a durable:

- repository identity correction;
- branch/state distinction;
- lineage finding;
- reusable primitive;
- evidence result;
- contradiction;
- important assumption;
- unresolved gap;
- dependency/relationship;
- decision that affects multiple repositories.

Do not wait for the full portfolio audit before recording durable discoveries.

At the same time, do not persist transient conversation speculation as portfolio fact.

## 15. Professional stopping rule

A repository review may stop when the current question is answered with sufficient evidence.

It does not need exhaustive inspection unless the decision requires it.

The reviewer should explicitly state what was not inspected when that limitation could affect the conclusion.

For high-impact integration or lineage decisions, increase inspection depth rather than increasing confidence from weak evidence.

## 16. Integration gate

A repository or primitive becomes an integration candidate only when the relevant boundary is evidenced by real workloads, reproducible behavior, provenance, and compatibility constraints.

A common name, similar README, or conceptual resemblance is not enough.

Preferred progression:

`observe -> compare -> reproduce -> isolate boundary -> small reuse experiment -> verify -> integrate`

not:

`similarity -> abstraction -> merge`

## 17. Protocol maintenance

This protocol itself is versioned.

Changes to the protocol should preserve historical review provenance. When a later version changes the meaning of a field or status, existing records should not be silently rewritten as though the old protocol had the new semantics.

## 18. Governing rule

> Identify the repository and exact ref first. Then separate implementation, experiment, assumption, suggestion, and historical reference. Only after that infer relationships or architecture.

This is the default handling standard for all future repository work recorded in Portfolio-Repository-Inventory.
