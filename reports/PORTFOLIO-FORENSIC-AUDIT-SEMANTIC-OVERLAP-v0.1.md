# Portfolio Forensic Audit — Semantic Overlap & Architecture Closure
## v0.1 — 2026-09-20

## Scope

This record consolidates the conclusions and findings established during the portfolio forensic audit conversation.

Audit rule:

repository inventory
→ actual implementation
→ tests
→ verification artifacts
→ current branch/commit
→ known failures/open defects
→ gap analysis
→ implementation only after the gap is proven

A capability is not treated as missing merely because another repository's README does not mention it.

Status vocabulary:
ESTABLISHED, EXPERIMENTALLY_SUPPORTED, USER_REPORTED, INFERENCE, HYPOTHESIS, CONTRADICTED, UNKNOWN, OPEN.

# 1. Portfolio-level conclusion

## ESTABLISHED

The original implementation gap was overstated.

The portfolio already contains most of the primitives that had previously been proposed as new implementation work. The remaining work is primarily:

1. semantic consolidation;
2. authority-boundary enforcement;
3. defect correction;
4. integration contracts;
5. removal of duplicated or unsupported claims;
6. authoritative-source selection.

The correct next gate is not another generic agent framework or universal trust engine.

The next implementation gate is:

existing implementation
→ exact source path
→ tested behavior
→ semantic owner
→ duplicate implementations
→ remaining defect
→ integration boundary

Only capabilities still classified as MISSING after this matrix should become new implementation work.

# 2. Architectural ownership

## Core execution authority — canonical-capability-core

Owns the semantics of:

- canonical state/lifecycle;
- authority;
- action preflight;
- durable execution;
- evidence validity/sufficiency primitives;
- reconciliation;
- recovery boundaries.

The audited primitive registry includes:

- primitive:state_transition
- primitive:relation
- primitive:evidence_validity
- primitive:authority
- primitive:action_preflight
- primitive:durable_execution
- primitive:evidence_sufficiency
- primitive:reconciliation

The registry declares invariants and failure modes. Durable execution explicitly preserves UNKNOWN outcomes, blocks blind retry, and requires restart safety.

Audited release/snapshot paths included:

- releases/v0.22/package/canonical_capability/primitive_contracts.py
- extracted/v15_release/primitive_contracts.py
- verification_strength/v0_23_expanded/source/canonical_capability/primitive_contracts.py
- releases/v0.22/extracted/canonical_capability_v0_22_release/canonical_capability/primitive_contracts.py

### Status

EXISTS + OPEN DEFECTS

Important unresolved verification boundaries remain around:

- post-approval policy enforcement;
- RESERVED-before-execution runtime durability;
- UNKNOWN vs EXECUTED semantics;
- reconciliation authority;
- idempotency across restart/concurrency;
- declared effects vs observed/reconciled effects;
- evidence validity vs evidence sufficiency;
- production vs controlled-staging claims.

Audited commit previously identified:
6396327425e7f5e6c23456579ebc286ca69f771f

Branch metadata has previously appeared inconsistent between main and master; branch identity must be revalidated before using it as current-state provenance.

# 3. Semantic overlap matrix

| Capability | Existing implementation | Status | Semantic owner | Boundary |
|---|---|---|---|---|
| State / lifecycle | canonical-capability-core / primitive:state_transition | EXISTS | Core | PIF/TOL must not redefine lifecycle semantics |
| Evidence validity | canonical-capability-core / primitive:evidence_validity | EXISTS | Core evidence semantics | Not equivalent to sufficiency |
| Evidence sufficiency | canonical-capability-core / primitive:evidence_sufficiency | EXISTS | Core evidence semantics | Requires explicit claim/context/policy |
| Claims / truth maintenance | recursive-audit claim graph + TMS | EXISTS + LIMITS | Evidence/Knowledge Plane | Does not grant action authority |
| Decision / context | ledger-system-source-of-truth | EXISTS + SINGLE-WRITER LIMIT | Decision/Context Plane | Not evidence validation |
| Authority | canonical-capability-core / primitive:authority | EXISTS | Core | Cannot be derived from LLM output or consensus |
| Action preflight | canonical-capability-core / primitive:action_preflight | EXISTS | Core | PIF composes procedures; it does not own action authority |
| Procedure schema | Ai-taxonomy/PIF models | EXISTS structurally | PIF | Declared DAG/proof is not execution proof |
| Procedure execution | PIF executor/orchestration | PARTIAL | PIF | Must remain subordinate to Core authority/execution semantics |
| Durable execution | canonical-capability-core | EXISTS + OPEN DEFECTS | Core | Do not duplicate inside PIF |
| Reconciliation | canonical-capability-core + external-staging-authority | EXISTS | Core + independent staging authority | Staging authority is not production authority |
| Tool communication | TOL | EXISTS | Communication Plane | Communication fabric is not execution authority |
| Software assurance | Software-res | EXISTS + VERTICAL | Domain Assurance | Do not promote into universal kernel |
| Experiment/evaluation | Research-framwork + historical research repos | REFERENCE / HISTORICAL | Evaluation/Research Plane | Evaluation is not verification or authority |
| Resilience/chaos | LibraNexus | REFERENCE | Resilience experiment layer | Best-effort recovery is not general transaction semantics |
| Optimization | Orvio | EXISTS | Optimization/Search | Optimization is not verification |
| Consensus | epistemic | EXISTS | Decision-support / research | Consensus is not truth |
| Context crystallization | Singularity | HISTORICAL | Reference | UQS is heuristic prioritization, not truth |
| Strategic experiment selection | Intellectual-intelligence.- | HISTORICAL | Reference | Automation is not intelligence |
| Agent/resource work queue | agent-hub | REFERENCE / ARCHIVE | Work/Resource Plane | No execution authority |
| Agent/plugin/failure patterns | The-new-era | HISTORICAL | Reference | Do not recreate broad AI OS |

# 4. Repository findings

## 4.1 canonical-capability-core

ESTABLISHED: a canonical capability lifecycle and execution authority implementation exists.

Core concepts include:

- capability lifecycle;
- contextual qualification;
- authority;
- action specifications and requests;
- preflight;
- durable execution;
- reconciliation;
- recovery;
- promotion identity invariants.

Durable execution distinguishes:
PREPARED, DISPATCHED, RUNNING, SUCCEEDED, FAILED, UNKNOWN_OUTCOME, RECONCILING, RECONCILED, COMPENSATED.

Critical invariant:
timeout / UNKNOWN is not equivalent to failure and must not permit blind retry.

Verification evidence exercised:

- real subprocess execution;
- malformed-result rejection;
- subprocess timeout → UNKNOWN_OUTCOME;
- restart;
- retry blocked before reconciliation;
- reconciliation → RECONCILED;
- successful execution → SUCCEEDED.

OPEN:
- APPROVAL_REQUIRED post-approval handling;
- RESERVED-before-execution persistence;
- crash/restart between reserve and external effect;
- UNKNOWN outcome persistence;
- replay blocking;
- reconciliation authority;
- idempotency-key scope;
- observed effect vs declared effect;
- evidence validity vs sufficiency.

Status: EXISTS + OPEN DEFECTS.

## 4.2 external-staging-authority

ESTABLISHED: independent non-destructive staging authority exists.

It provides durable effect identity and failure-injection scenarios:

- NORMAL;
- DELAYED;
- TIMEOUT_AFTER_ACCEPT;
- TIMEOUT_BEFORE_COMMIT;
- UNAVAILABLE.

It persists effect/command evidence using SQLite WAL and supports reconciliation without redispatch.

Boundary:
INDEPENDENT_STAGING_AUTHORITATIVE is not production/external-system authority.

Status: EXISTS.

## 4.3 PIF / Ai-taxonomy

Relevant model path:
pif/models.py

Actual structures include:

- ToolContract;
- DAGStep;
- dependencies;
- compensating procedures;
- VerificationProof;
- weakest-precondition text;
- certified-safe flag;
- step reviews.

ESTABLISHED: the data model for procedure contracts and DAG-style execution exists.

PARTIAL / OPEN:

- dependencies are declared but do not by themselves establish real dependency-aware execution;
- verification_proof is not equivalent to formal proof;
- weakest-precondition handling is textual/restricted rather than SMT-backed proof;
- router selection is lexical/heuristic;
- MCP integration is limited;
- duplicate paths exist under pif/ and src/procedure_intelligence/;
- authoritative implementation path is not fully established.

Status: PARTIAL.

Correct boundary:
PIF = procedure/composition layer above Core.
It must not duplicate authority, canonical state semantics, durable execution, or reconciliation authority.

## 4.4 TOL

ESTABLISHED: TOL provides a tool/service communication fabric with:

- peer registration/discovery;
- capability/schema publication;
- heartbeat/stale cleanup;
- invocation/result relay;
- pub/sub;
- JSON Schema validation;
- structured logging;
- API key handling;
- optional TLS.

Limits:

- cost approximates latency rather than monetary cost;
- prediction is skill selection rather than general sequence prediction;
- hit/miss does not mean execution success;
- skill instances are local objects;
- prefetch confidence/waste is not rigorously modeled;
- registry is in-memory;
- default secret-key is insecure;
- TLS configuration can disable verification;
- complete per-capability authorization/tenant identity is absent;
- replay/signing/rotation guarantees are absent;
- demonstrations are not sufficient as production evidence.

Status: EXISTS.

Boundary:
TOL = communication/tool-service fabric.
TOL != execution authority.

## 4.5 recursive-audit

ESTABLISHED: REAS / recursive evidence-audit infrastructure exists.

Capabilities include:

- claim/evidence graph;
- bi-temporal representation;
- dependency audits;
- causal-level checks;
- defeater/contradiction handling;
- truth-maintenance propagation;
- retraction;
- branch isolation;
- structured trace parsing;
- graph realignment;
- asynchronous event flow;
- query routing;
- sandbox/signature sweeping.

Status: EXISTS + LIMITS.

Boundary:
evidence/knowledge infrastructure does not grant action authority.

## 4.6 ledger-system-source-of-truth

ESTABLISHED: a file-based logical ledger exists for:

- decisions;
- constants;
- goals;
- constraints;
- findings;
- scope changes.

It supports:

- contradiction detection;
- supersession;
- comparators;
- digest;
- health;
- stale detection;
- history inspection.

The comparator mechanism is explicitly mechanical and does not infer semantic equivalence.

OPEN:

- comparator registry is not versioned per entry;
- changing a comparator can retroactively change historical judgment;
- logical append-only is not tamper-proof storage;
- single-file storage is not a distributed event store;
- multi-writer semantics are not supported.

Status: EXISTS + SINGLE-WRITER LIMIT.

Boundary:
Decision/context state != evidence validity.

## 4.7 Research-framwork

ESTABLISHED: early experiment orchestration exists through MetaOrchestrator, agent variants, standard experiments, adversarial benchmark execution, and shared contexts.

Limits:

- loose any types;
- weak experiment provenance;
- no robust statistical methodology;
- no stable effect-size/confidence/power treatment;
- insufficient seed/environment/model provenance;
- adversarial score is not itself scientific evidence.

A performance.ts utility was found to be web-vitals monitoring rather than experiment-science infrastructure.

Status: REFERENCE / HISTORICAL.

## 4.8 Software-res

ESTABLISHED: a tested software evidence/assurance vertical exists.

Includes:

- evidence contracts;
- schema validation;
- fail-closed collection/validation;
- non-compensatory reliability vector;
- deterministic policy;
- local Ed25519/DSSE P-256 proof-of-concept;
- controlled fixtures;
- real-GIL experiment harness;
- mutation/policy tests.

Non-goals:

- production SLSA builder trust/key management;
- real external ground-truth corpus;
- calibrated thresholds;
- general proof of software reliability.

Status: EXISTS + VERTICAL.

Boundary:
domain assurance adapter above Core, not universal kernel.

## 4.9 Orvio

ESTABLISHED: multi-phase numeric optimization/search exists with probing, exploration, surrogates, parallel evaluation, adaptive budget, and phase statistics.

Limits:

- README/roadmap count mismatch (14 vs actual 15 phases);
- budget is checked between rounds rather than as a strict evaluation bound;
- shared mutable surrogate risk under concurrent instances;
- ruggedness heuristic is heuristic;
- no strong statistical superiority evidence.

Status: EXISTS.

Boundary:
Optimization/search != verification/evaluation authority.

## 4.10 LibraNexus

ESTABLISHED: chaos/resilience experiment patterns exist:

steady state → intervention → observation → rollback → final validation.

Experiment objects include hypothesis, steady state, method, rollback, validation, duration, blast radius, metrics, and assertions.

Limits:

- final assertions do not establish full-window invariants;
- compensation is best effort;
- MTTR is simplified;
- blast radius is modeled more strongly than it is enforced.

Status: REFERENCE.

Reusable contract:
ExperimentSpec =
preconditions
+ baseline
+ intervention
+ expected invariants
+ observation
+ recovery
+ postconditions
+ evidence.

## 4.11 Do-it-

ESTABLISHED: portfolio/decision intelligence exists with idea objects, tests, scoring, ROI, graph relationships, duplicate detection, domain affinity, PageRank/communities/bridges, and proposal generation.

CRITICAL LIMIT:
knowledge_status maps executed → EXPERT and test-pass/research-note states to KNOWLEDGEABLE/EXPLORING. These are not justified truth-status labels.

Correct use:
portfolio state
→ candidate idea
→ explicit risky assumption
→ discriminating test
→ evidence
→ decision/context update.

Status: EXISTS.

## 4.12 Singularity

ESTABLISHED: realization objects, scoring, layering, lineage, and typed relations exist.

CONTRADICTED / UNSUPPORTED:
README claims O(log n) retrieval, while actual retrieval performs a full collection scan and sorting.

Evidence references exist but are not governed as authoritative evidence semantics.

Correct interpretation:
UQS = heuristic prioritization.
UQS != truth/confidence.

Status: HISTORICAL.

## 4.13 Intellectual-intelligence.-

ESTABLISHED:
Strategic Question → Riskiest Assumption → Cheapest Effective Test → Quantifiable Signal → Evidence → Decision → Updated Context.

LIMIT:
automation does not constitute general intelligence. Session analysis can reduce to counting filled sections and updating a tracking file.

Status: HISTORICAL.

## 4.14 The-new-era

ESTABLISHED: historical agent-platform concepts exist for role/manifest, plugin discovery, failure taxonomy, dependency topology, and self-healing patterns.

LIMIT:
latest architecture blueprint left modernization/infrastructure work unfinished.

Status: HISTORICAL.

## 4.15 agent-hub

ESTABLISHED: resource/work graph and Kubernetes-oriented deployment specification exists.

Patterns include:
discovery → issue → execution → PR → learning.

LIMIT:
deployment configuration is not production proof; example secrets were placeholders/insecure examples.

Status: REFERENCE / ARCHIVE.

Boundary:
work/resource management != execution authority.

## 4.16 epistemic

ESTABLISHED: mathematical decision-support research primitives exist for TF-IDF/SVD representation, convex-hull maximin consensus, worst/best bounds, fragility, Dirichlet stress scenarios, sensitivity/isomorphism, and PPO research code.

CRITICAL BOUNDARY:
consensus quality depends on representation quality. Profile collisions can occur and are warned about.

Therefore:
mathematical consensus != truth != evidence validity != authority.

Status: EXISTS.

# 5. Hard architectural non-merges

Optimization ≠ Evaluation.

Finding a high-scoring configuration does not establish that the metric is valid or that the result proves correctness.

Evaluation ≠ Verification.

Evaluation can measure behavior without establishing an invariant or proof obligation.

Verification ≠ Authority.

A verified condition does not itself grant permission to act.

Consensus ≠ Truth.

Agreement among proposals is not evidence that the agreed proposition is true.

Decision record ≠ Evidence.

The ledger records what was decided/contextualized; it does not turn a decision into evidence.

Communication fabric ≠ Execution authority.

TOL can carry an invocation without being the authority that permits the side effect.

Domain assurance ≠ Universal execution kernel.

Software-res can qualify software evidence under its domain policy; this does not make it the universal assurance engine.

Declared contract ≠ Enforced semantics.

PIF DAG dependencies, proof fields, and compensation metadata cannot be treated as proof that the executor enforced those semantics.

# 6. Important duplication findings

Three forms of duplication were identified.

### A. Cross-repository duplication

Multiple repositories contain adjacent implementations of evidence/claims, decisions/context, procedures, experimentation, authority-like checks, and execution-adjacent behavior.

These require semantic ownership rather than blind merging.

### B. Within-repository duplication

canonical-capability-core contains release/extraction/verification-strength copies of primitive contracts.

The same durable-execution contract appears in multiple paths.

This creates a provenance hazard: snapshot paths can be mistaken for authoritative implementation.

### C. Historical conceptual duplication

Several older repositories contain their own versions of agent orchestration, intelligence, optimization, evidence, trust, or self-improvement.

Treat these as historical references unless explicitly promoted.

# 7. Integration model

AI / Agents
    ↓
Planning / PIF
    ↓
Canonical Capability Core
    ├── canonical state
    ├── authority
    ├── action preflight
    ├── durable execution
    ├── reconciliation
    └── evidence validity/sufficiency
    ↓
TOL / external adapters
    ↓
External world

Evidence / Knowledge Plane
    ├── recursive-audit / claim graph / TMS
    ├── ledger / decision-context state
    ├── consensus research
    └── crystallized context / lineage

The important architectural property is asymmetric responsibility:

- higher layers compose;
- Core enforces execution invariants;
- evidence systems inform but do not self-authorize;
- communication systems transport but do not authorize;
- domain assurance qualifies domain-specific artifacts;
- research systems generate measurements/experiments but do not silently become authority.

# 8. Remaining open questions

## OPEN — authoritative Core source

Which path inside canonical-capability-core is the single authoritative implementation after excluding release/extraction artifacts?

Required evidence:

repository
branch
commit
source path
test path
workflow/artifact.

## OPEN — PIF enforcement semantics

Do current executors actually enforce declared DAG dependencies, verification obligations, and compensation semantics, or merely carry those fields?

Required discriminating test:
execute a nontrivial dependency graph where serial execution and dependency-aware execution produce observably different behavior, including a dependency failure.

## OPEN — Core execution closure

Re-test:

- APPROVAL_REQUIRED post-approval handling;
- RESERVED-before-execution persistence;
- crash/restart between reserve and external effect;
- UNKNOWN outcome persistence;
- replay blocking;
- reconciliation authority;
- idempotency-key scope;
- observed effect vs declared effect;
- evidence validity vs sufficiency.

## OPEN — evidence authority boundary

Explicitly assign authority for:

- evidence identity;
- evidence validity;
- evidence sufficiency;
- claim relation;
- claim retraction;
- decision/context.

These should not be flattened into one generic trust state.

## OPEN — duplicate resolution

Every duplicate implementation needs a disposition:

- authoritative;
- adapter;
- historical;
- experimental;
- superseded.

# 9. Next gate

No new generic engine should be built before the following matrix is complete:

Capability
→ Repository
→ Exact source path
→ Commit
→ Tested behavior
→ Verification artifact
→ Semantic owner
→ Duplicate paths
→ Known defect
→ Integration boundary
→ Disposition

Allowed dispositions:
EXISTS, PARTIAL, MISSING, BROKEN, DUPLICATED, SUPERSEDED, HISTORICAL, REFERENCE.

Only MISSING after this audit qualifies as new implementation work.

# 10. Final synthesis

The portfolio is not missing a generic agent trust/execution concept.

It already contains the major pieces.

The actual engineering problem is semantic authority, verification strength, defect closure, provenance, and composition.

The most important design decision from this audit is:

Do not solve portfolio fragmentation by inventing another abstraction layer. Solve it by assigning semantic ownership to implementations that already exist, proving their enforced behavior, and making the boundaries between them executable.

This record is a portfolio-audit snapshot, not a claim that all listed repositories are current production-ready systems.
