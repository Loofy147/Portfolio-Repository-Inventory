# Integrated System Research — 2026-09-27

Status: DURABLE CROSS-REPOSITORY RESEARCH SYNTHESIS

Canonical full artifact SHA-256:
18ae8211976e5f4eb1443794db53304797ad1dda1261f9f67633407243999f2d

This record anchors the complete self-contained research paper generated in the 2026-09-27 research session:
INTEGRATED_SYSTEM_RESEARCH_2026-09-27.md

## Scope

Integrated:
- Loofy147/Machine: substrate contracts, mechanism/frontier experiments, target-oblivious precomputation, representation closure, black-box insufficiency, error localization, transfer-contract validation, bundled-failure repair, evidence/branch canonicalization.
- Loofy147/Llms-mcp-android: authority model, Action/Capability execution, policy/approval/egress, credential protection, Binder/process failure recovery, Operation identity, MCP, Android lifecycle, containment.
- Loofy147/Portfolio-Repository-Inventory: cross-repository provenance and evidence indexing.
- External related work: distributed systems, data-structure preprocessing/query tradeoffs, information-flow security, least privilege/reference monitoring, delta debugging, Android platform lifecycle, MCP Tasks/auth, Anthropic containment, Meta Muse security architecture.

## Central finding

The common failure mode is boundary contamination: a layer intended to expose, transport, represent, advise, observe, or schedule silently acquires authority, information, durable-state meaning, or uncharged resource semantics.

Therefore capability and safety claims require an explicit contract covering information, timing, representation, primitive operations, authority, identity, resource accounting, correctness, failure model, and evidence semantics.

## Machine status

EXPERIMENTALLY_SUPPORTED, bounded:
- Direct predecessor access shifts the sampled online frontier under B_off=0 and R=0 with unified edge accounting.
- Successor-only exhaustive predecessor emulation fails to recover the native frontier at tight budgets in the tested finite graph family.
- A target-oblivious reverse adjacency representation reproduces the native bidirectional frontier exactly for tested M in {30,100,300}, at B_off=R=3M.
- Richer all-pairs policy state reduces online work further at approximately quadratic offline/state cost.
- Strict-heldout controls show target-specific cached state that cannot contain the realized target does not alter the tested behavior.
- Finite black-box persistent failure does not justify global expressive-insufficiency claims without regularity/certificate assumptions.

REFINED:
- “Direct predecessor is inherently more powerful” became “resource-bounded frontier shift under an explicit substrate/resource contract.”
- “Minimal failing subset explains the failure” became “minimal subset isolates one failure witness; bundled repair requires iteration.”

OPEN:
- stronger successor-only baselines;
- independent graph families;
- normalized predecessor-access cost;
- compact representation closure;
- causal evaluator reflection;
- nontrivial transfer learning without supplied context labels;
- complete research-branch canonicalization.

## Android status

ESTABLISHED / PROVISIONALLY VERIFIED:
- Model reasoning, Tool exposure, Policy, Approval, Risk signals, Capability execution, Observation, Verification, and Evidence are distinct.
- Model output cannot authorize an effect.
- Durable effect reservation/replay blocking exists.
- Provider-side Binder recovery cases B2/B3 are experimentally supported in the tested API 35 topology.

OPEN:
- caller-side UNKNOWN_OUTCOME;
- concurrent recovery;
- stale callbacks/results;
- reboot, force-stop, package-update and power-loss matrices;
- credential-use isolation;
- provenance-aware egress;
- native MCP auth/lifecycle;
- high-power capability containment;
- durable event/audit sufficiency.

NOT CLAIMED:
- general exactly-once external execution.

## Formal framework

Substrate:
Sigma = (X,Q,S,Pi,Delta,Omega,kappa,Lambda)

Offline representation:
phi(x) -> S before target/query-dependent information is available.

Feasible frontier:
F_Sigma = {(B_off,R,B_on): an admissible representation and online algorithm satisfy the declared correctness predicate}

Authority context:
Gamma = (principal, action, version, input, scope, invocations, policy_context, credential_refs, egress_context, freshness)

Policy:
P(Gamma) -> {DENY, APPROVAL_REQUIRED, ALLOW}

Effect state:
NEW -> RESERVED -> DISPATCHED -> {COMPLETED, UNKNOWN_OUTCOME, CONFIRMED_NOT_EXECUTED}

Core derived results:
1. Mechanism attribution is invalid when substrate/resource/timing/representation contracts differ.
2. Computability equivalence does not imply resource equivalence.
3. Approval cannot substitute for current policy when context can change.
4. Durable local state does not imply exactly-once external effects without effect-boundary idempotency, transactional coupling, or authoritative reconciliation.
5. Credential non-observability is provable only under explicit isolation assumptions.
6. Finite black-box failure cannot prove global insufficiency without additional assumptions.

## Security convergence

Anthropic and Meta Muse reinforce:
- reasoning is not authorization;
- policy is distinct from human approval;
- risk classifiers are not final authority;
- CredentialRef must be separated from CredentialValue;
- provenance can influence egress;
- containment complements policy;
- browser access should be brokered;
- execution processes are not durable semantic identity.

MCP's current evolution reinforces explicit task handles, per-task authorization, and stateless lifecycle concepts. These are external signals, not local proof and not reasons to make MCP the canonical domain model.

## Highest-value next experiments

1. Caller crash after provider effect: durable checkpoint -> effect -> caller loss -> restart -> UNKNOWN_OUTCOME -> reconcile -> no duplicate effect.
2. Concurrent recovery with explicit linearization point.
3. Stale callback ordering with generation/attempt rejection.
4. Full credential-path instrumentation proving raw-secret non-observability.
5. Payload-provenance-aware egress tests.
6. Stronger Machine baselines and independent graph families.
7. Compact target-oblivious representation search.
8. Causal evaluator reification without experimenter-supplied intervention order.
9. Nontrivial source-to-target transfer with hidden regime structure.

## Evidence rule

A claim is not upgraded because it is repeated, elegant, vendor-implemented, or intuitively compelling. Promotion requires:
repository + branch + exact ref/commit + artifact + execution + conditions + result + status + interpretation boundary + next discriminating action.

## Primary local records

Machine:
research/evidence-disposition-v0 @ 8f16e5dcc57c59025e3cc9ec5607d294a1c8b8e3
docs/research/CONVERSATION_FINDINGS_2026-09-20.md

Android:
main @ 7a7e1c67d1dce15457b62cf173d159a7be15f9ce
docs/architecture/CONVERSATION_FINDINGS_2026-09-20.md
docs/architecture/ARCHITECTURE_STATE_SYNC_2026-09-17.md
docs/architecture/DECISION_REGISTER_v0.2.md

Portfolio:
main @ c6f441cb929b4b744c1f3a84cdce14c42cfff143
records/CONVERSATION_EVIDENCE_SYNC_2026-09-20.md

## External source anchors

Android lifecycle:
https://developer.android.com/guide/components/activities/activity-lifecycle

Android persistent WorkManager:
https://developer.android.com/develop/background-work/background-tasks/persistent

Android App Functions:
https://developer.android.com/reference/android/app/appfunctions/package-summary

Binder:
https://developer.android.com/reference/kotlin/android/os/IBinder

MCP 2025-11-25:
https://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/

MCP 2026-07-28:
https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/

MCP Tasks:
https://tasks.extensions.modelcontextprotocol.io/specification/draft/tasks

Anthropic containment:
https://www.anthropic.com/engineering/how-we-contain-claude

Meta Muse security:
https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse

Meta Muse launch:
https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/

NIST least privilege:
https://csrc.nist.gov/glossary/term/least_privilege

End-to-end arguments:
https://web.mit.edu/6.033/2002/wwwdocs/papers/endtoend.pdf

Computability and complexity:
https://plato.stanford.edu/entries/computability/

MIT cell-probe:
https://live.ocw.mit.edu/courses/18-405j-advanced-complexity-theory-spring-2016/f373ff7db6f99debba9256050d372980_MIT18_405JS16_Data_Struc.pdf

Delta debugging:
https://www.cs.umd.edu/class/spring2016/cmsc838G/DeltaDebug.pdf

## Scope warning

This record and the full paper intentionally do not claim:
- universal mechanism superiority;
- universal expressive-insufficiency detection;
- causal reflection;
- general exactly-once effects;
- production-grade autonomous mobile execution;
- vendor-independent proof from Meta/Anthropic/MCP documentation.

The complete paper remains the authoritative integrated handoff for this research pass.
