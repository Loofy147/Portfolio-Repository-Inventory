
# Portfolio Operating Manual v0.2

Status: OPERATIONAL
Date: 2026-09-18
Scope: Portfolio-Repository-Inventory and all repository reviews recorded through it

## 1. Mission

Portfolio-Repository-Inventory is the portfolio control and evidence layer.

It is not a forced common codebase, not a universal framework, and not a replacement for project-local architecture.

Its job is to make a heterogeneous repository portfolio understandable enough to:

- identify what each repository actually contains;
- identify which state is current;
- preserve branch and commit provenance;
- distinguish evidence from interpretation;
- detect genuine relationships without inventing lineage;
- retain useful historical work;
- expose contradictions and gaps;
- support active projects without making the portfolio audit a blocking gate;
- accumulate durable primitives and evidence that may later support integration.

## 2. System boundary

The portfolio contains several distinct object types.

Repository
: Git storage and collaboration boundary.

Ref
: Branch, tag, or commit selecting a repository state.

Project
: An interpreted work identity that may span several refs or repositories.

Observation
: Something directly inspected at a specific repository/ref state.

Evidence
: An observation, execution result, artifact, test, benchmark, history fact, or explicit owner statement that supports a claim.

Claim
: A statement about what is true.

Experiment
: A controlled procedure intended to discriminate between claims.

Artifact
: A durable source, result, trace, benchmark output, fixture, or other inspectable object.

Relationship
: A typed relation between repositories/projects/primitives with explicit evidence status.

Assessment
: A bounded evaluation of a repository against stated dimensions.

Decision
: A selected portfolio action, kept separate from the evidence that motivated it.

Unknown / Gap
: Something material that has not been established.

Contradiction
: Two materially incompatible observations or claims whose provenance must both remain visible.

These objects must not be collapsed into one narrative.

## 3. Minimum provenance

The minimum location for a material technical claim is:

repository + branch/ref + commit

For an evidence observation, also preserve:

observed_at + inspected surface

For an executed result, preserve:

repository/ref + experiment or test identity + inputs/fixture + result artifact

A repository name alone is never sufficient provenance when branches differ materially.

## 4. Repository, branch, and project state

Treat these as different dimensions:

repository identity
branch/ref identity
documented specification
implemented behavior
executed behavior
portfolio interpretation

Use the following state vocabulary:

- CURRENT: supported by evidence from the active research/implementation frontier.
- DEFAULT-BRANCH: present on the default branch.
- RESEARCH-FRONTIER: materially advanced research/implementation on a non-default branch.
- HISTORICAL: useful older implementation or state.
- UNMERGED: work exists on another ref but is not shown on the inspected default branch.
- UNKNOWN: current state cannot be established.

Do not promote a branch to canonical merely because it contains more documentation.

Do not demote a branch merely because it is not the default branch.

When branch state matters, compare refs explicitly.

## 5. Active-project identification

When a project is referred to by a goal, phrase, experiment, or idea instead of an exact repository name:

1. Identify candidate repositories.
2. Inspect metadata and default branch.
3. Enumerate relevant branches.
4. Search for distinctive phrases from the current task.
5. Inspect branch-specific documentation and source.
6. Inspect recent commits.
7. Compare candidate branch against default branch.
8. Identify the actual current research/implementation frontier.
9. Only then name the active repository.
10. Label older related repositories explicitly as historical/reference unless lineage is evidenced.

Never select the active project from semantic resemblance alone.

## 6. Inspection depth

Use progressive inspection depth.

D0 — Metadata census
- repository identity and metadata only.

D1 — Structural triage
- root tree;
- primary README;
- manifests;
- obvious tests/CI/deployment signals.

D2 — Selected implementation review
- relevant source;
- architecture/specification documents;
- selected tests/fixtures;
- history where needed to answer the current question.

D3 — Deep comparison
- implementation details;
- tests/CI;
- relevant history;
- branch comparison;
- relationship/lineage analysis;
- competing explanations.

D4 — Executed/reproduced verification
- run the relevant test/experiment;
- inspect generated artifacts/results;
- verify the claimed behavior under declared conditions;
- record limitations and falsifiers.

Do not claim D4-level evidence from documentation alone.

A review may stop earlier when the actual question is answered. The stopping point and uninspected surfaces must be explicit when they could affect the conclusion.

## 7. Default inspection order

Use:

METADATA
-> BRANCHES/REFS
-> ROOT TREE
-> BUILD/MANIFEST
-> SOURCE
-> TESTS/CI
-> DATA/ARTIFACTS
-> README/DOCS
-> HISTORY
-> EXECUTION/REPRODUCTION when required

Adjust for repository type, but never let a polished README replace source or execution evidence.

## 8. Evidence model

Use two compatible vocabularies.

### Portfolio evidence class

OBSERVED
DERIVED
INFERRED
USER_REPORTED
UNKNOWN
CONTRADICTED

### Project claim status

ESTABLISHED
EXPERIMENTALLY_SUPPORTED
USER_REPORTED
INFERENCE
HYPOTHESIS
CONTRADICTED
UNKNOWN
OPEN

The first describes the evidence object. The second describes the status of the project claim being discussed.

Never silently upgrade one into another.

## 9. Claims, assumptions, suggestions, decisions

Claim
: says what is true; requires provenance and status.

Assumption
: working premise used because evidence is incomplete; must remain visible.

Suggestion
: proposed action, experiment, architecture, or interpretation; not evidence.

Decision
: selected action/policy; not evidence and not a substitute for evidence.

Hypothesis
: testable explanation or proposition that is not established.

Gap
: missing capability or missing evidence that materially affects reasoning.

Contradiction
: incompatible evidence or claims that require preservation and, when necessary, discrimination.

## 10. Behavioral evidence layers

For any important experiment or implementation claim, separate:

1. documented intent;
2. implementation mechanism;
3. test/experiment procedure;
4. observed result;
5. causal interpretation;
6. architectural implication.

A result can establish a capability without establishing the claimed internal mechanism.

A host-language callback is not automatically an object-language primitive.

A successful output is not proof of causal reflection.

A hot-swap between separate invocations is not automatically online continuity.

## 11. Historical/reference handling

An older repository can be valuable even when it is not the active project.

Historical/reference evidence can supply:

- implementation precedents;
- techniques;
- failure modes;
- tests;
- design patterns;
- counterexamples;
- migration clues;
- terminology.

It does not automatically establish:

- current ownership;
- current project identity;
- code lineage;
- conceptual inheritance;
- provenance of a newer experiment;
- semantic equivalence.

Use explicit relation labels such as:

HISTORICAL_REFERENCE
POSSIBLE_LINEAGE
ESTABLISHED_LINEAGE
SHARED_PRIMITIVE_CANDIDATE
DUPLICATE_CANDIDATE
INDEPENDENT_SIMILARITY
SUCCESSOR_CANDIDATE
DEPENDENCY

Similarity is a discovery signal, not lineage.

## 12. Relationship analysis

When comparing two repositories, answer these independently:

Identity
: same project, distinct project, or unresolved?

Lineage
: did one evolve from the other?

Semantic overlap
: do they implement related functions or primitives?

Implementation reuse
: is code/data/protocol/infrastructure actually reused?

Evidence transfer
: does evidence in one legitimately support a claim in the other?

Architectural compatibility
: can they share a stable boundary without forcing premature abstraction?

Do not infer one dimension from another.

Examples:

shared terminology -> possible similarity, not lineage

same domain -> possible same idea, not code reuse

explicit cross-link -> stronger lineage signal, but still verify content/history

copied code or preserved commit ancestry -> strong implementation lineage evidence

## 13. Evidence transfer across repositories

Evidence belongs first to the source repository/ref.

A portfolio-level conclusion should preserve:

source repository/ref
-> observation
-> relationship or derivation
-> portfolio claim

Evidence must not be copied into another repository record without retaining this provenance chain.

If a claim appears in multiple repositories, distinguish:

- independently evidenced in both;
- inherited/derived from one;
- merely repeated;
- currently unresolved.

## 14. Negative findings

Never record an absolute absence unless the relevant surface was inspected sufficiently.

Prefer:

"X was not found in inspected surfaces A/B/C at ref R."

Do not infer missing implementation from:

- missing README text;
- sparse root tree inspection;
- absent search hit on one branch;
- documentation omission.

## 15. Assumption discipline

Material assumptions must be written down.

Typical review assumptions include:

- this branch is the active research branch;
- this repository is the successor of another;
- the documented experiment is implemented;
- a representation is causally consulted by the runtime;
- a result reflects the mechanism claimed rather than a hidden confound.

An assumption can guide the next action. It cannot silently become evidence.

## 16. Suggestion discipline

Suggestions are action candidates.

Examples:

- inspect a specific branch;
- compare a historical implementation;
- run a minimal pair;
- extract a stable boundary;
- preserve a fixture;
- create a compatibility adapter.

A suggestion must not later be cited as though it were a fact about the repository.

## 17. Review packet

Every material repository review should be able to produce:

- repository identity;
- observed ref/commit;
- relevant branches;
- current-state interpretation;
- inspection depth;
- inspected surfaces;
- established observations;
- experimentally supported claims;
- assumptions;
- suggestions;
- relationships;
- unknowns;
- contradictions;
- verification status;
- next discriminating test or inspection.

Use the reusable template in docs/REVIEW_PACKET_TEMPLATE_v0.1.md.

## 18. Durable portfolio updates

Update this repository as soon as a durable finding is sufficiently evidenced.

Record at least these classes:

- repository identity correction;
- active-branch correction;
- branch/default divergence;
- established lineage;
- meaningful historical reference;
- reusable primitive;
- evidence result;
- contradiction;
- important assumption;
- unresolved gap;
- dependency;
- cross-repository decision.

Do not wait for full portfolio coverage.

Do not persist transient conversation speculation.

## 19. Active work is non-blocking

The portfolio audit is a parallel track.

Project-local execution continues when its local evidence is sufficient.

The inventory should not become a gate that requires every repository to be understood before any individual project can progress.

The correct operating pattern is:

active project work
+
incremental portfolio review
+
durable cross-project recording

## 20. Integration gate

A repository or primitive becomes an integration candidate only when the boundary is evidenced.

Preferred progression:

observe
-> compare
-> reproduce
-> isolate boundary
-> small reuse experiment
-> verify
-> integrate

Evidence for integration should normally include:

- at least two real implementations/workloads;
- stable semantic contract;
- provenance/ownership;
- compatibility constraints;
- failure/rollback behavior;
- measurable reduction in duplicated complexity;
- no unresolved contradiction with a higher-priority invariant.

Conceptual resemblance is not enough.

## 21. Architecture restraint

Do not create a universal abstraction merely because several repositories use the same nouns.

Delay extraction until the common behavior is observed at the interface that matters.

Prefer:

small reversible extraction
over
large speculative framework

Prefer:

capabilities and interfaces
over
provider-specific coupling

Preserve independent implementations until the shared contract is real.

## 22. Experiment discipline

For experimental claims:

- define the tested substrate;
- define the intervention;
- define the control;
- define the observation boundary;
- preserve reproducible artifacts;
- state the confounds;
- state the falsifiers;
- distinguish the tested mechanism from the broader architectural interpretation.

A narrow positive result should remain narrow.

## 23. Branch-aware evidence transfer

When a repository has multiple meaningful branches, the evidence chain includes the ref:

repository/ref/commit
-> observed mechanism
-> result
-> interpretation

A claim from a research branch must not silently appear as a default-branch capability.

A claim from an old commit must not silently become a current capability.

## 24. Revalidation

Portfolio conclusions are time-bounded observations.

Revalidate when:

- the relevant branch moves substantially;
- the default branch changes;
- the project is renamed or split;
- a suspected successor appears;
- a previously unknown relationship gains evidence;
- a critical implementation changes;
- an integration decision depends on current behavior.

Do not rewrite old evidence to look current. Add a newer observation.

## 25. Compatibility with existing inventory

Existing inventory schemas remain valid historical records.

The v0.2 operating model is an overlay that improves interpretation and future records without requiring destructive migration.

Legacy fields should be preserved.

When a new concept has no legacy field:

- add a new review/relationship record;
- preserve the old record;
- link the two by provenance.

Do not silently rewrite history.

## 26. Case learned from Machine and Log-Os

The 2026-09-18 review established a concrete operating lesson.

Machine is the active repository for the current machine-native-primitives research.

Its documented research frontier is on:

research/machine-native-primitives-v0

The comparison of that branch against Machine/main showed that the research branch is materially divergent from main. The branch is therefore evidence of a research frontier, not evidence of default-branch state.

Log-Os is an older interpreter repository and a useful historical reference for:

- CPS/trampoline execution;
- explicit continuation objects;
- lexical environments;
- object-language procedures/macros;
- L0 multimethod dispatch;
- AST-level loading/evaluation.

However, the inspected Log-Os surface does not establish that the current Machine prime-stream hot-swap experiment originated there.

Therefore:

Machine -> Log-Os lineage = UNKNOWN

and:

Log-Os as historical interpreter reference = OBSERVED / supported by inspected source

This example is now the default pattern for similar future cases.

## 27. Portfolio update rule derived from the case

When a repository review changes the interpretation of another repository, update the portfolio immediately with:

- the corrected active repository;
- the exact branch/ref evidence;
- the historical repository classification;
- the relationship status;
- the remaining unknown;
- the next discriminating inspection.

This prevents a local correction from being lost in conversation.

## 28. Professional stopping rule

Stop when the current question is answered with sufficient evidence.

Increase depth when the decision has high cost, high irreversibility, or cross-repository implications.

Do not replace weak evidence with stronger language.

The correct endpoint is sometimes:

UNKNOWN

or:

OPEN

That is a valid portfolio result.

## 29. Governing rule

Identify the repository and exact ref first.

Then separate:

implementation
experiment
evidence
assumption
suggestion
historical reference
interpretation

Only after those are separated should relationships, reuse, or architecture be inferred.

## 30. Review mode selection

Not every repository needs the same review.

Use `docs/REVIEW_MODES_v0.1.md` to select among:

- identity/current-state review;
- structural triage;
- implementation review;
- experiment audit;
- lineage/relationship review;
- historical reference review;
- integration review;
- revalidation review.

Select the mode from the question, evidence risk, architecture maturity, and decision reversibility.

## 31. Trust gate before reuse

Before reusing a result or primitive from another repository, verify:

1. source state is identified;
2. mechanism is actually evidenced;
3. boundary is stable enough to reuse;
4. assumptions are explicit;
5. failure/rollback behavior is understood;
6. provenance is retained.

This is the portfolio-level trust gate:

`evidence -> trust judgment -> reuse candidate`

not:

`similarity -> reuse`.
