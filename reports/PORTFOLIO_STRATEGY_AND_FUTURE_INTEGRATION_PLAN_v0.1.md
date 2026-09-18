# Portfolio Strategy & Future Integration Plan v0.1

Status: PROVISIONAL STRATEGY / NOT A CURRENT MERGE PLAN
Date: 2026-09-18

## 1. Purpose

This document records the current portfolio-level direction without prematurely selecting a final universal architecture, product, or North Star.

The portfolio contains a large and heterogeneous set of repositories spanning experiments, research, reusable primitives, applications, platforms, infrastructure, datasets, mathematical work, agent systems, Android/Linux work, commerce, trading, security, and other domains.

> Eventually derive a coherent infrastructure from the accumulated repositories and private files, reconnecting reusable projects, ideas, applications, primitives, evidence, and missing capabilities while preserving provenance and discarding unsupported assumptions.

This is not the current execution target.

## 2. Current operating mode

1. Existing projects continue on their own tracks.
2. Project-local architecture remains authoritative for implementation work.
3. Cross-project reuse is introduced only when a concrete shared boundary is evidenced.
4. The portfolio repository acts as the coordination and analysis layer, not as a forced common codebase.
5. No large-scale repository merge, extraction, framework consolidation, or universal ontology is required merely because related projects exist.
6. Research, experiments, implementation, and product work may continue before the final portfolio architecture is known.

The portfolio is therefore treated as a collection of evolving assets, not yet as one software system.

## 3. Strategic direction

The future integration target is broader than any single current project.

The eventual infrastructure may need to connect:

- projects;
- reusable capabilities and primitives;
- claims and decisions;
- experiments and runs;
- evidence and artifacts;
- dependencies and provenance;
- execution/runtime implementations;
- applications and product surfaces;
- datasets and research;
- private files and durable knowledge;
- external protocols and replaceable service implementations.

The final architecture is OPEN until sufficient portfolio evidence exists.

Candidate architectural interpretations discussed so far remain HYPOTHESES, not portfolio decisions.

## 4. What the portfolio audit must establish before future integration

Before a future consolidation phase, the portfolio must be understood along at least these dimensions:

### Identity
What each repository actually is, independently of its repository name.

### Provenance
Whether the implementation is original, derived, forked, copied, generated, imported, experimental, or an external/template artifact.

### Lineage
Which repositories represent evolution, successors, experiments, branches, or independent implementations of a related idea.

### Semantic primitives
Which concepts or invariants recur across otherwise different projects.

### Architectural boundaries
Which recurring structures are real shared interfaces versus superficial vocabulary.

### Evidence
Which claims, tests, benchmarks, demonstrations, and execution results have actually been established.

### Maturity
Which repositories are prototypes, research baselines, working applications, validated components, abandoned experiments, or unresolved artifacts.

### Composition opportunities
Which existing components can be combined without forcing premature abstractions.

### Gaps
Which capabilities or infrastructure pieces are repeatedly missing across otherwise viable projects.

### Contradictions
Where projects make incompatible assumptions, define the same concept differently, or carry mutually exclusive architectural commitments.

## 5. Portfolio analysis pipeline

The portfolio-wide method remains:

CENSUS -> STRUCTURAL TRIAGE -> CLUSTERING -> DEEP REVIEW -> DECISION -> REVALIDATION

Future integration adds a later phase:

... -> PORTFOLIO SYNTHESIS -> GAP ANALYSIS -> ARCHITECTURE CANDIDATES -> CONSTRAINED INTEGRATION

The final architecture is therefore an output of evidence, not an input assumption.

## 6.1 Repository handling standard

The portfolio coordination layer now has an explicit operational model for reviewing other repositories:

- repository identity is contextualized by branch/ref and commit;
- current research branches are not assumed to be the default branch;
- documentation, implementation, experiment, causal interpretation, and architecture are separate evidence layers;
- historical repositories can supply references without establishing lineage;
- durable discoveries are recorded incrementally;
- existing inventory records remain valid and are not destructively rewritten.

See `docs/PORTFOLIO_OPERATING_MANUAL_v0.2.md`.

## 6. Immediate work policy

The immediate goal is not to audit all repositories to completion before doing anything else.

Instead:

- Continue active project work where the project has a valid local objective.
- Update the portfolio inventory when an important durable relationship, decision, contradiction, lineage finding, or reusable primitive is established.
- Deep-review portfolio clusters when the result can affect an active project or materially reduce future integration risk.
- Keep unresolved relationships explicitly unresolved.
- Prefer small, reversible extraction/reuse experiments over global refactors.
- Do not create general abstractions solely because multiple repositories appear similar by name.

## 7. Future integration gates

A repository or primitive should become a candidate for shared infrastructure only when the relevant boundary has evidence such as:

1. at least two real implementations or workloads requiring the same semantic contract;
2. stable behavior that is independently testable;
3. clear ownership/provenance;
4. explicit compatibility and migration boundaries;
5. a demonstrated reduction in duplicated complexity;
6. acceptable failure and rollback behavior;
7. no unresolved contradiction with a higher-priority invariant.

A theoretical commonality is not enough.

## 8. Private-file integration

The future infrastructure is expected to use a substantial private-file corpus as additional evidence and source material.

Private files must not be treated as automatically authoritative.

They will eventually be incorporated through the same provenance/evidence discipline:

source -> identity -> extraction -> claim/artifact -> verification -> integration candidate

The future corpus may contain stronger historical context than the repositories, but missing verification remains UNKNOWN.

## 9. Current portfolio census boundary

The portfolio inventory repository records a 2026-08-30 search snapshot of 313 repositories.

A direct current GitHub installation census on 2026-09-18 observed 331 repositories accessible through the current connection.

These are different snapshots and must not be silently mixed.

The 331-repository observation is an operational freshness signal, not yet the new canonical inventory snapshot. The inventory should be deliberately re-censused and reconciled before its stored census is promoted.

## 10. Non-goals for the current phase

Do not currently:

- merge the portfolio into one repository;
- extract a universal framework;
- declare a final North Star architecture;
- force all projects onto one domain model;
- replace valid project-local architectures with a portfolio abstraction;
- treat repository similarity as proof of lineage;
- treat model/vendor/protocol trends as proof of portfolio strategy;
- erase or archive work merely because it is old, duplicated-looking, or incomplete.

## 11. Success condition for this phase

This phase succeeds when the portfolio can answer, with evidence:

> What do we actually have, what is genuinely related, what is reusable, what is proven, what is missing, and what should remain separate?

Only then should the portfolio move from collection + evolution into intentional infrastructure synthesis.

## 12. Current status

- Portfolio-wide final architecture: UNKNOWN
- Future integration objective: ACCEPTED AS STRATEGIC DIRECTION
- Immediate requirement for global consolidation: NO
- Current project autonomy: PRESERVED
- Portfolio census: STALE RELATIVE TO CURRENT OBSERVED ACCESS; RECONCILIATION OPEN
- Cross-repository lineage: PARTIALLY MAPPED
- Deep portfolio synthesis: OPEN
- Private-file integration design: FUTURE WORK
- Universal infrastructure implementation: NOT STARTED

## 13. Governing principle

> Do not force today's projects to become tomorrow's infrastructure before the evidence shows what the infrastructure actually is.

The portfolio should accumulate validated primitives, relationships, evidence, and successful implementations now so that a future infrastructure can be derived from reality rather than imposed on it.