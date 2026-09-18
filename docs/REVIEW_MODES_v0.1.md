# Repository Review Modes v0.1

Status: OPERATIONAL
Date: 2026-09-18

The portfolio does not use one review shape for every repository. Select the smallest review mode that can answer the current question, then increase depth only when evidence or decision cost requires it.

## 1. Identity / Current-State Review

Question:
"What repository/branch actually represents the current work?"

Minimum:
D1-D2

Focus:
- metadata;
- default branch;
- relevant branches;
- recent commits;
- branch comparison;
- branch-specific README/source.

Primary failure prevented:
choosing an older or wrong repository because of semantic similarity.

## 2. Structural Triage

Question:
"What is materially present in this repository?"

Minimum:
D1

Focus:
- root tree;
- manifests;
- source/test/CI/deployment signals;
- documentation structure.

Primary failure prevented:
calling a sparse README a sparse project.

## 3. Implementation Review

Question:
"How is a claimed mechanism actually implemented?"

Minimum:
D2-D3

Focus:
- relevant source;
- data/control flow;
- host-language versus object-language boundary;
- tests/fixtures;
- relevant history.

Primary failure prevented:
treating documentation or API names as proof of mechanism.

## 4. Experiment Audit

Question:
"What exactly did the experiment establish?"

Minimum:
D3; D4 when execution/reproduction is required.

Focus:
- intervention;
- control;
- observation boundary;
- fixture;
- execution;
- artifact;
- result;
- confounds;
- falsifiers.

Primary failure prevented:
expanding a narrow experimental result into a broader capability claim.

## 5. Lineage / Relationship Review

Question:
"Are these repositories related, and how?"

Minimum:
D2-D3

Focus:
- explicit cross-links;
- copied/shared content;
- commit ancestry where available;
- chronology;
- implementation overlap;
- semantic overlap separately from lineage.

Primary failure prevented:
turning similar names or concepts into false lineage.

## 6. Historical Reference Review

Question:
"What useful techniques or failure modes can be recovered from an older repository?"

Minimum:
D2

Focus:
- implementation mechanisms;
- tests;
- fixes;
- design precedents;
- limitations.

Output:
HISTORICAL_REFERENCE, not automatic lineage.

## 7. Integration Review

Question:
"Can a primitive or component become shared infrastructure?"

Minimum:
D3-D4 for high-impact integration.

Focus:
- at least two real workloads/implementations;
- stable semantic boundary;
- provenance;
- compatibility;
- failure/rollback;
- duplicated-complexity reduction;
- contradictions.

Gate:

observe
-> compare
-> reproduce
-> isolate boundary
-> small reuse experiment
-> verify
-> integrate

No global abstraction is justified by naming similarity alone.

## 8. Revalidation Review

Question:
"Is an older portfolio conclusion still true?"

Minimum:
match the depth that supported the old conclusion.

Focus:
- current branch state;
- current implementation;
- changed history;
- changed dependencies;
- newly discovered successor/reference.

Do not rewrite old evidence as current. Add a new observation.

## 9. Review-mode selection rule

Choose review mode from:

question
+ evidence risk
+ architecture maturity
+ reversibility of the decision

not from repository size alone.

A large repository can be safely triaged at D1.
A tiny repository can require D4 when its claim controls a critical integration decision.

## 10. Trust gate

Before reusing a repository result, primitive, or implementation, ask:

1. Is the source state identified?
2. Is the mechanism actually evidenced?
3. Is the boundary stable enough to reuse?
4. Are important assumptions explicit?
5. Are failure and rollback known?
6. Is provenance preserved?

Reuse should be evidence-gated, not similarity-gated.
