# Human–Machine Twin: Existing System-of-Systems Crosswalk

**Originally recorded:** 2026-11-09  
**Evidence update:** 2026-11-10  
**Portfolio source:** `Loofy147/Portfolio-Repository-Inventory`  
**Purpose:** Reconcile the Human–Machine Twin initiative with existing architecture, runtime, evidence, memory, decision and product work.  
**Status:** Evidence-bounded crosswalk; not a merge plan, integration approval, production certification or assertion that all systems are currently interoperable.

## 1. Architecture decision

The Human–Machine Twin (HMT) is not a new universal agent runtime and is not synonymous with a single assistant, model, repository or product.

Use three nested levels:

1. **MIRA — Machine Intelligence Reference Architecture:** the provisional parent reference architecture for a heterogeneous system of machine capabilities, coordination, grounding, memory, agency, authorization, execution and verification. It is proposed in Open-System-One PR #11.
2. **Architecture Convergence Contract:** the cross-repository semantic agreement for ownership and the operational, execution and epistemic record spines. It is maintained in Open-System-One; the envelope, authority and evidence schemas remain drafts, and cross-runtime conformance is open.
3. **Human–Machine Twin:** the operating relationship between a human principal and that system: intent, mandate, goal adoption, authority, continuity, trust, privacy, feedback, adaptation and final acceptance.

HMT must reuse the existing owners and contracts. It must not replace their state stores, re-authorize their effects, or copy whole implementations into a new orchestration repository.

## 2. System ownership and evidence crosswalk

Refs below are the exact observed branch/commit surfaces used for this review. Some are draft PR heads rather than default-branch releases. Review depth is limited to the cited source files, READMEs, schemas, tests and qualification records; no complete local test suites were rerun as part of this crosswalk.

| Boundary | Repository / observed ref | Existing capability | Evidence status and limits | HMT role |
|---|---|---|---|---|
| Portfolio identity and provenance | [Portfolio-Repository-Inventory](https://github.com/Loofy147/Portfolio-Repository-Inventory) `main@cd65ed81a4013849d017750d85925cc8ca51acda` | Repository census, review records, relationships, lineage and evidence references. A new connected census reconciliation is in PR #18. | **OBSERVED:** schemas and records exist. The new census is connected-search identity evidence, not activity/maturity evidence. | Governance and provenance index; not runtime authority. |
| Parent architecture and decision semantics | [Open-System-One](https://github.com/Loofy147/Open-System-One) `main@fb21d176d0ed1b083df889cf747ac562d449ceef`; MIRA PR #11 head `6ab16f44dc4df050590f8738f416ce1976baf2a7`; kernel PR #10 head `ddb11f1ff31b24ea9dc58d809e33394b082fb0f9` | Typed decision contract; deterministic scoring, abstention and policy separation; MIRA foundation; canonical record envelope; draft authority/evidence schemas and kernel conformance fixtures. | **PROVISIONAL / DRAFT:** MIRA PR #11 and kernel PR #10 are unmerged. G-01/G-02 remain open; current main contains documentation/schema/fixture surfaces, not a complete universal runtime. | Parent reference architecture and shared semantic/conformance authority. |
| Machine-native substrate research | [Machine](https://github.com/Loofy147/Machine) `main@2d5f6bd0513ecd2d9f29f395d4d95c90849b2648`; research branch `research/machine-native-primitives-v0@f752aac015d9f837bc6a89d44eed50e0325b60a6` | State/operation/transition/control model, substrate/interpreter research, adaptation/reflection and memory-under-uncertainty experiments. | **RESEARCH / BRANCH-BOUND:** research frontier is not equivalent to a production substrate. Claims need branch-specific reproduction; some memory results are explicitly user-reported or open. | Mechanistic research source; not a deployed agent runtime. |
| Knowledge-work coordination | [unified-knowledge-work-system](https://github.com/Loofy147/unified-knowledge-work-system) `main@683c38fdc3c921c1d7977786d5b5ed8617969476`; conformance PR #21 head `ceecd35c7fb4770255c0fab8f5552671ed86908c` | Module registry and relationship ledger; task routing; specialist composition; evaluation, context/trust/review/adjudication; MySQL/Drizzle project, plan revision, event, evidence, assumption and validation persistence; PR #21 adds a JSONL effect recovery primitive and executes the shared nine-step K-UNKNOWN vector in its conformance adapter. | **EXPERIMENTALLY SUPPORTED / PR DRAFT:** PR #21's sequential K-UNKNOWN adapter passed in Actions run [#42864208807](https://github.com/Loofy147/unified-knowledge-work-system/actions/runs/42864208807). The branch now adds an OS-lock-protected local multi-process JSONL transition and deterministic race/process-termination tests. Exact current head `ceecd35c7fb4770255c0fab8f5552671ed86908c` is being checked in Actions run [#42895590793](https://github.com/Loofy147/unified-knowledge-work-system/actions/runs/42895590793); the control-plane job passed, while system validation was still running at the last inspection. Supported scope is one host/local filesystem; network and multi-host coordination are unsupported. HGSB database activation remains separately verification-pending. | Coordination, knowledge-work, project/plan and claim-adjudication owner. |
| Goal/search/boundary continuity | [UWS HGSB PR #23](https://github.com/Loofy147/unified-knowledge-work-system/pull/23), branch `feat/hgsb-durable-state-v0.1` | Versioned state schema, persistence contract and bootstrap artifact for hierarchical goals, search state, capability boundaries and continuation. | **DRAFT / VERIFICATION-PENDING:** Git bootstrap is retrievable; database-backed HGSB activation awaits MySQL migration, ownership, CAS/idempotency and restart/recovery proof. Keep separate from UWS project persistence. | Long-horizon goal/search/boundary continuity; not action authority. |
| Conversation continuity | [Conversational](https://github.com/Loofy147/Conversational) `main@9da36fcd99f49b9f859751f39d1a4f4393c1d1de` | Repository-native event history, canonical-state reduction, projection, lineage and restore policy. | **CANDIDATE / RESTORE UNVERIFIED:** first fresh-boundary restore is reported, not independently attested; authenticity is self-integrity only. Restore is CONTEXT_ONLY and cannot authorize actions. | Conversation frontier recovery, not project truth or global memory. |
| Durable Run and local effect ledger | [m0-durable-run](https://github.com/Loofy147/m0-durable-run) `main@69b07a54e4b2f8421532b78b8abffca308bbe3da`; [PR #4](https://github.com/Loofy147/m0-durable-run/pull/4) head `92b7f8b1d0b3c8729f607627e443d6d71e6bb2d2` | Small SQLite append-only Run/evidence store; idempotent stable Run identity; two-process restart demonstration; draft append-only effect ledger with UNKNOWN/reconciliation; SQLite `BEGIN IMMEDIATE` serialization for effect reservation and state transitions; cache artifact provenance/reuse contracts. | **EXPERIMENTALLY_SUPPORTED IN LOCAL SQLITE SCOPE:** deterministic 16-worker test gives one `RESERVED` and 15 `REPLAY_BLOCKED`; core, router, effect lifecycle/concurrency and two-process restart checks passed on Python 3.11/3.12/3.13 in Actions run [#42860970422](https://github.com/Loofy147/m0-durable-run/actions/runs/42860970422), exact PR head. The effect ledger remains a draft PR, no provider adapter or external-authority integration; no distributed/multi-host or exactly-once guarantee. Agent executor remains a stub. | Minimal Run durability plus a candidate local effect-state primitive; keep both narrowly scoped. |
| Device effect authority | [Llms-mcp-android](https://github.com/Loofy147/Llms-mcp-android) `main@78afd5d3d7716fe31a5f109a5796eb3db7f99970` | Action/Capability separation, policy engine, approval store, egress policy, CapabilityExecutor, runtime store and tests for UNKNOWN effect enumeration/reconciliation across journal restart. | **SOURCE-OBSERVED / ANDROID-LOCAL:** tests cover unknown/completed/not-executed states and restart. Cross-platform semantics and current-device CI must be revalidated before portability claims. | Candidate authority/effect implementation for Android; conformance reference, not universal owner. |
| Machine habits and persistent flows | [HabitRoute](https://github.com/Loofy147/HabitRoute) `main@e57e86afa12757223b9dada4ff191b496ece6c1f`; checkpoint PR #12 head `c505d96fe011f94af8eae90fab84f6ebcf317c81`; integration PR #14 head `e7cee372be5ed702266fbfb76b2987442f7d0bdd` | Versioned machine habits, harness contracts, side-effect classes, local event-sourced flow journal and worker; PR #12 adds per-operation intent/result, attempt accounting, resume cursor and fail-closed pending intent; PR #14 composes this with the repertoire planner, cross-process per-run journal locking and an executable read-only repository-review flow. | **EXPERIMENTALLY SUPPORTED / DRAFT:** PR #14 Actions run [#42897875221](https://github.com/Loofy147/HabitRoute/actions/runs/42897875221) passed Python 3.11/3.12/3.13, including multi-process journal tests and M3 review tests. Local filesystem/one-host only; no distributed journal. Machine-habit UNKNOWN blocks blind replay, but explicit provider reconciliation is not yet implemented. | Procedural machine habits and local flow/step progress; not human intent, global state or provider authority. |
| Capability repertoire and read-only Git inspector | [HabitRoute PR #10](https://github.com/Loofy147/HabitRoute/pull/10), branch `feat/habit-repertoire-composition-v0.3`, head `dd9d88e45b2bfd2dfeaa0130439838181ccc8c15`, composed in [PR #14](https://github.com/Loofy147/HabitRoute/pull/14) | SituationFrame, exact host capability snapshot, bounded capability-chain planner, immutable Git commit-range adapter, persistent flow invocation, content-addressed evidence and a separate inventory/blob verifier. | **EXPERIMENTALLY SUPPORTED / DRAFT:** PR #14 run [#42897875221](https://github.com/Loofy147/HabitRoute/actions/runs/42897875221) passed Python 3.11/3.12/3.13. It is a read-only local repository inventory, not semantic review, test execution, source authenticity or live UWS integration. | First M3 executable review slice. Task/goal refs are provenance pointers only; no live UWS task/evidence API connection. |
| Capability lifecycle / effect semantics | [canonical-capability-core](https://github.com/Loofy147/canonical-capability-core) `master@6396327425e7f5e6c23456579ebc286ca69f771f` | Versioned capability qualification, authorization, action, observation, reconciliation and conformance artifacts; frozen v0.22 reference and rc2 staging candidate. | **NEGATIVE EVIDENCE MUST BE PRESERVED:** rc2 runtime evidence-consumption gate failed; adapter UNKNOWN was transported but runtime returned EXECUTED, not UNKNOWN_OUTCOME. Production is blocked; rc2 must not be patched or promoted as safe. | Semantic reference and qualification research; not an approved production effect runtime. |
| Independent synthetic effect ledger | [external-staging-authority](https://github.com/Loofy147/external-staging-authority) `main@5e313c05245dfa5b646d3b80713b74d443b8c528` | Local/VM SQLite effect identity, status query, disposition, reconciliation and provenance for synthetic non-destructive effects. | **QUALIFICATION-ONLY:** separate process/storage boundary, but not a separate physical failure domain or third-party production authority. | Sandbox oracle for adapter qualification; never production truth. |
| Evidence acquisition and provenance | [My_browser](https://github.com/Loofy147/My_browser) `main@402121c0e6cf9294d8e71feecd5752eade859807` | Canonical JSON identities, SHA-256 artifacts, Execution→Observation→Evidence→Verification→Provenance, raw artifact retention, deterministic transforms/replay and SQLite. | **EXPERIMENTALLY SUPPORTED FOR TESTED PROBES:** 19/19 CI tests on Node 22/24 at run #33679026934; jsdom is not a real browser, PDF input is pre-extracted text, GitHub probe is already-fetched JSON, hashes do not prove source authenticity. | Evidence/provenance primitive; no general browser or network transport claim. |
| Browser-local model execution | [All-time-](https://github.com/Loofy147/All-time-) `main@c9f8662acde83808b64ad75ac8bef4ee67edd5da` | Transformers.js local inference, WebGPU with WASM/CPU fallback, pinned model revisions, PWA shell. | **IMPLEMENTATION SIGNAL / PRODUCTION VERIFY OPEN:** main contains cleanup beyond last known READY deployment; no current-HEAD production verification. | Optional local inference capability adapter; not a continuity or authority layer. |
| Exact-key contradiction ledger | [ledger-system-source-of-truth](https://github.com/Loofy147/ledger-system-source-of-truth) `main@e63a92171f6c5b3a4958157be979347857f6a809` | Append-only JSON ledger, registered exact-key comparators, deterministic contradiction detection, MCP and optional WebSocket surfaces. | **NARROW GUARANTEE:** same registered key/comparator only; does not infer semantic equivalence or decide which value is true; local ledger must be configured/persisted explicitly. | Optional decision/context ledger for exact-key facts; not epistemic adjudication or action authority. |
| Personal decision-support products | [Digital-twin](https://github.com/Loofy147/Digital-twin) `main@7f1806dd2976a3233207ab6bf7e65d7026d473d3`; [Twin-ai](https://github.com/Loofy147/Twin-ai) `main@70284e86b4ac4a0449dad3fdec5eed28b8464e2f` | Distinct product experiments around personal assessment, inferred profile, scenario simulation, consent, audit and adaptive questioning. | **PRODUCT SURFACES, NOT HMT BACKPLANE:** Digital-twin uses dev auth and has production privacy/security hardening gates; Twin-ai README claims need fresh source/test validation. These products can contain sensitive personal data. | Keep isolated behind explicit consented integrations; never import their personal data into general HMT context by default. |

## 3. The existing work is not one merged system

The repositories represent different authorities and maturity levels. Similar names, adjacent concepts or common owners do not establish shared implementation or compatibility.

In particular:

- UWS project/evidence persistence is not the same authority as HGSB goal/search continuation.
- Conversational conversation restore is not the same as HGSB project continuity.
- m0 durable Run identity is not equivalent to Android effect reconciliation or HabitRoute flow orchestration. M0 PR #4 now contains a separate local SQLite effect ledger; its atomic reservation fix is experimentally supported on the same-file SQLite topology, not distributed or provider-authoritative.
- HabitRoute's machine-habit event model keeps an UNKNOWN pending operation and prevents blind replay after restore, but it does not yet implement explicit CONFIRMED_COMPLETED / CONFIRMED_NOT_EXECUTED reconciliation transitions. Its plain FlowNode.OPERATION path has no pre-invocation intent event and is used in PR #14 only for bounded READ_ONLY Git inspection, where deterministic replay is a safe, narrow property. Do not generalize this retry property to external effects.
- Android's UNKNOWN journal tests are a real local implementation candidate, but not proof that its state model is portable or identical to the canonical-capability contract.
- My_browser's evidence IDs and hashes provide integrity/lineage references, not external-source authenticity or semantic truth.
- The canonical-capability rc2 failure is a useful killed assumption: successful adapter transport is not enough; the runtime must consume UNKNOWN at the state-transition boundary.
- Personal digital-twin products are not the human-machine control plane; their data requires a separate privacy/consent boundary.


## 3A. Evidence update — 2026-11-10

- **M0 concurrency:** a forced two-reader reproduction showed the old read-then-append race could produce two `RESERVED` outcomes for one `effect_id`. The draft repair moves state read/validation/append inside a SQLite `BEGIN IMMEDIATE` transaction. The 16-worker regression passes with one reservation and 15 blocked replays. Actions run #42860970422 passed all three Python versions and all core/router/effect/restart steps on M0 PR #4 head `fc283c7c18a30be52d464894bed3a337b89aefa3`. The qualification is local to workers sharing the same SQLite file.
- **UWS effect recovery:** PR #21 adds a stable OS lock file around compound JSONL state transitions and ledger snapshots. Local focused suite: 6/6 pass on Python 3.13.5; the lock-free RED reproduction fails the forced two-process race test, and the locked version passes it. Actions run [#42895590793](https://github.com/Loofy147/unified-knowledge-work-system/actions/runs/42895590793) has passed `verify-control-plane`; `validate-system` had passed system tests, system validator, research refresh integration, SAR, eval harness, routing regression and capability suites at the last refresh, but the job had not yet completed. Exact head `ceecd35c7fb4770255c0fab8f5552671ed86908c`. Scope is local processes/one host; no network filesystem, multi-host or exactly-once guarantee.
- **Architecture implication:** M0 and UWS now both carry candidate local UNKNOWN/reconciliation primitives, but with different stores and limitations. They have not passed a current-head, clean-clone shared conformance campaign. The Open-System-One G-02/G-04 cross-runtime gaps remain OPEN.

## 3B. Shared-fixture coverage audit — 2026-11-10

The initial source comparison was superseded by the PR #21 adapter update. The current inspected head is `ceecd35c7fb4770255c0fab8f5552671ed86908c`; it wires the exact shared UNKNOWN vector into the UWS adapter and adds local-process ledger locking.

| Fixture assertion | M0 adapter at `conformance/cache-contract-v0.1` | UWS adapter at PR #21 head |
|---|---|---|
| K-IDENTITY-01 | Executes same Run ID / different request rejection; reports PASS only on observed rejection. | NOT_PROVEN. |
| K-VERIFY-01 | Executes completed Run, records Observation and independent verifier rejection; checks execution remains completed while verification is failed. | Executes same separation and rejection pattern; checks persisted Verification. |
| K-EVIDENCE-01 | Links Run, Observation, Verification and Evidence; checks references. | Links Run, Observation, Verification and Evidence; checks references. |
| K-UNKNOWN-01 | Pins the vendored Open-System-One fixture by Git blob SHA, executes all nine vector steps against SQLite, and checks result, state and event-count delta. | Now does the same against the UWS JSONL helper: pins the same fixture blob, executes all nine vector steps, and checks result, state and event-count delta. |
| K-AUTHORITY-01 | NOT_REPRESENTED. | NOT_REPRESENTED. |
| K-FRONTIER-01 | NOT_REPRESENTED. | NOT_REPRESENTED. |

**Current experimental evidence:** UWS PR #21's current head was included in GitHub Actions run [#42864208807](https://github.com/Loofy147/unified-knowledge-work-system/actions/runs/42864208807), which completed successfully. The `validate-system` job ran `test_kernel_fixture_subset` successfully, plus the four focused effect recovery tests; the `verify-control-plane` job also passed typecheck, persistence migrations (including idempotency rerun), integration tests and production build. The Actions workflow checked out merge ref `476b2ae7cc5156301aa1bc9b1ac330886274d9e5`, combining PR head `27962fe...` with the then-current main base. PR #21 remains OPEN and DRAFT.

**Important topology difference remains:** M0's effect ledger uses SQLite `BEGIN IMMEDIATE`; UWS retains append-only JSONL and adds OS-level locking around read/check/append and public snapshots. UWS has deterministic two-process race and process-termination lock-release tests; exact-head Actions run [#42895590793](https://github.com/Loofy147/unified-knowledge-work-system/actions/runs/42895590793) had the control-plane and all inspected validation suites passing, but the validation job had not yet reported a terminal conclusion at last refresh. Both stores are local, same-host topologies; neither implies multi-host safety or provider-authoritative truth.

**Interpretation:** M0 and UWS now both pass the same sequential K-UNKNOWN-01 fixture, which is stronger cross-runtime evidence than their earlier standalone helper tests. This is still not full kernel conformance: identity semantics differ, Authority and Frontier remain unrepresented, the local storage/concurrency models differ, and no clean-clone independent campaign has been established across all target runtimes.

**Next discriminating implementation:** complete the exact-head CI and independent review tracked in [UWS issue #25](https://github.com/Loofy147/unified-knowledge-work-system/issues/25). After that, extend shared fixtures to Android and HabitRoute and preserve the canonical-capability-core rc2 UNKNOWN-consumption failure as a negative control.

## 3C. M3 read-only repository-review vertical slice

**Current implementation:** HabitRoute [PR #14](https://github.com/Loofy147/HabitRoute/pull/14), head `e7cee372be5ed702266fbfb76b2987442f7d0bdd`, stacked on repertoire [PR #10](https://github.com/Loofy147/HabitRoute/pull/10) at `dd9d88e45b2bfd2dfeaa0130439838181ccc8c15`. Actions run [#42897875221](https://github.com/Loofy147/HabitRoute/actions/runs/42897875221) passed Python 3.11, 3.12 and 3.13.

The flow performs a pre-execution plan check against the current SituationFrame and host-supplied capability snapshot; selects one exact-version READ_ONLY Git capability; persists the flow; inventories an immutable base/target commit range; independently re-resolves both commits, re-computes the raw diff inventory, checks Git object metadata and blob-content digests, and checks a before/after worktree marker. It atomically stores a content-addressed evidence package. A crash after evidence publication but before the flow-success event is replayed as the same read-only inspection and resolves to the same evidence digest.

**Evidence meaning:** verification PASS means the recorded inventory and observed blob states passed integrity checks. It does not imply semantic correctness. `review_status=incomplete` remains incomplete even when the integrity verifier passes. Project tests/scripts/hooks are not executed. This is not a source-authenticity attestation.

**Authority and integration limits:** task/goal references are caller-supplied opaque UWS pointers; no UWS API/database is read or written. The host snapshot is not cryptographically authenticated by this local module. FlowNode.OPERATION has no pre-invocation operation-intent event; this slice uses it only because immutable Git inspection is READ_ONLY and deterministically re-runnable. Side-effecting operations must not inherit this replay behavior. Journal locks support local processes on one host/local filesystem only.

**Remaining integration gate:** live UWS task/evidence registration with authenticated principal/authorization context; explicit cross-runtime conformance for HabitRoute and Android; reconciliation semantics for HabitRoute's pending UNKNOWN habit operation; supported multi-host coordination if required; project test execution as a separate, explicit capability; independent source/provenance verification.

## 4. Conformance priorities already present in Open-System-One

The existing convergence gap register should remain the master gap set. This crosswalk does not create duplicate gaps.

| Priority | Existing gap | Best candidate owners to exercise | First discriminating test |
|---|---|---|---|
| P0 | G-01 canonical kernel intersection | Open-System-One, UWS, m0, My_browser | Map Run, Observation, Verification, Evidence and provenance to the draft envelope without forcing local payload schemas to match. |
| P0 | G-02 cross-repository conformance | UWS + m0 or My_browser; then Android | Run identical fixtures for identity, linkage, verification, replay and authority through two independent implementations. |
| P0 | G-03 Capability/Verification boundary | HabitRoute, Android, My_browser, UWS | Show that a pinned capability produces an attributable observation, that an independent verifier checks it, and that the resulting evidence is linked to the run. |
| P0 | G-04 UNKNOWN effect/reconciliation | Android, canonical-capability-core, external-staging-authority, HabitRoute | Query/reconcile an induced unknown effect; assert no blind retry; preserve command/effect identity and evidence after restart. Include canonical-capability rc2 as a negative control, not a passing implementation. |
| P1 | G-05 provenance-aware egress | Android, UWS, My_browser | Preserve source, data class/taint, destination, purpose, minimization and authorization reference at a remote boundary. |
| P1 | G-07 evidence integrity | My_browser, Portfolio Inventory, Open-System-One | Pin exact repo/ref/commit, command, input, raw receipt, normalizer/verifier versions and digest; detect drift. |
| P1 | G-09 product adapter boundary | Taskora, TwiYo, Wedgettok/la-rouine-platform after fresh review | Consume stable semantic IDs and contracts without importing UWS/MIRA internals. |
| Parallel | G-06 Machine substrate contract | Machine | Audit actual interpreter/state-access implementation and reproduce cost claims; do not promote the abstract substrate model by naming alone. |

## 5. Recommended first implementation sequence

1. Resolve the current review/merge chain for MIRA PR #11, Open-System-One kernel PR #10 and UWS HGSB PR #23; do not assume any are merged.
2. Turn the Open-System-One draft kernel fixtures into executable adapters and run them through two existing, materially different implementations (recommended initial pair: m0 + My_browser, or UWS + m0).
3. Extend the same conformance suite to Android's effect journal and HabitRoute's operation-level flow events.
4. Add the synthetic external-staging authority only as a qualification oracle. Preserve canonical-capability-core rc2's UNKNOWN-consumption failure as a failed negative control.
5. Compose one read-only repository-review flow across HabitRoute's planner/inspector, My_browser-style evidence identity, an independent verifier and UWS evidence reference.
6. Only after read-only evidence and recovery work: evaluate local inference, additional model providers, product adapters and bounded write actions.
7. Keep the personal data of Digital-twin/Twin-ai products separate unless the human principal explicitly consents to a defined purpose and data flow.

## 6. Stop rules

- Do not create a new universal runtime until existing implementations have failed a shared conformance test in a specific way.
- Do not merge specialist repositories to obtain superficial architectural uniformity.
- Do not copy a capability implementation without its version, license, provenance, tests and failure modes.
- Do not treat CI-green as proof of an architecture claim unless CI tests that exact claim independently.
- Do not promote external-action safety from a synthetic ledger or a local journal alone.
- Do not let memory restore, tool availability or previous approvals expand authorization.
- Do not import personal assessment, contact, calendar or communication data into general machine context without explicit purpose, consent, minimization and retention rules.

This crosswalk is a dated map of existing assets and candidate tests. It is not a ranking of all 397 connected repository identities and does not imply that every listed repository is active, production-ready or interoperable.


## 7. Evidence update — 2026-11-11

This update supersedes stale PR heads and CI claims in earlier sections. Refs below were refreshed during this review.

### UWS effect ledger — cross-platform local-process qualification

- UWS conformance PR #21 current head: `c36962321775e65ac4abecc3915718c26ab98c4a`.
- Exact-head Actions run [#43075043272](https://github.com/Loofy147/unified-knowledge-work-system/actions/runs/43075043272): `validate-system`, `windows-effect-ledger` and `verify-control-plane` all completed successfully.
- The Windows job ran the focused effect recovery suite on Windows / Python 3.12: 7/7 tests passed, including cross-process reservation, state transitions, and lock release after process termination.
- The Linux system-validation job passed. The MySQL-backed control-plane job also passed on the same exact PR head.
- The PR now exercises POSIX `fcntl.flock` and Windows `msvcrt.locking`; the complete read/check/append transition and snapshots are serialized.
- [Issue #25](https://github.com/Loofy147/unified-knowledge-work-system/issues/25) records remaining final source review gates.

**Limit:** local processes on one host/local filesystem only. No network-filesystem or multi-host guarantee; no exactly-once external delivery or provider-authoritative truth. PR #21 remains draft/unmerged.

### M0 effect ledger — transaction semantics versus proof coverage

- M0 conformance PR #4 current head: `92b7f8b1d0b3c8729f607627e443d6d71e6bb2d2`.
- Exact-head Actions run [#42864164588](https://github.com/Loofy147/m0-durable-run/actions/runs/42864164588) passed Python 3.11, 3.12 and 3.13.
- Reservation and individual transitions use SQLite `BEGIN IMMEDIATE`; the current 16-contender regression is thread-based (`ThreadPoolExecutor`), not a multi-process test.
- Source review found `recover_interrupted_effects()` reads the RESERVED set, closes that connection, then transitions effects one by one. A stale recovery scan could race with a completion/reconciliation/re-reservation and mark a newer attempt UNKNOWN.
- [Issue #5](https://github.com/Loofy147/m0-durable-run/issues/5) now tracks process-level contention and atomic/attempt-guarded recovery.

**Limit:** local processes sharing one SQLite database file are the intended scope. No multi-host claim or exactly-once external delivery. PR #4 remains draft/unmerged.

### HabitRoute — M3 integration and flow-journal coordination

- HabitRoute M3 integration PR #14 current head: `fdcad291213f90bf03c84cf1362e1d622dcb9cb2`, stacked on PR #10's capability-repertoire branch.
- Exact-head Actions run [#42898530500](https://github.com/Loofy147/HabitRoute/actions/runs/42898530500) passed all three Python versions (3.11, 3.12, 3.13).
- PR #14 ports the per-operation checkpoint/recovery work onto the PR #10 lineage and adds per-run OS-lock serialization for JSONL load/snapshot and read/check/append. Deterministic tests cover two-process same-sequence contention and process-termination lock release.
- It implements the local read-only repository-review vertical slice: exact-version READ_ONLY planning/invocation, immutable Git-object inventory, content-addressed evidence, separate inventory/blob verification, stale-context/permission/root checks and fail-closed incomplete evidence.
- [Issue #13](https://github.com/Loofy147/HabitRoute/issues/13) now accurately distinguishes the local slice from live UWS integration.
- [Issue #16](https://github.com/Loofy147/HabitRoute/issues/16) tracks Windows locking qualification and interrupted/short-write journal integrity. PR #14's current matrix is Ubuntu-only.
- PR #12 is a separate standalone branch based on main; PR #14 intentionally ports its checkpoint logic onto the PR #10 lineage. Do not blindly merge or cherry-pick the divergent branches.

**Limits:** local processes on one host/local filesystem only. No multi-host journal coordination, authenticated host attestation, live UWS task/evidence API, semantic code review, source authenticity proof or project test execution. The flow is safely re-runnable because its inspected capability is READ_ONLY; do not generalize to side-effecting operations. PR #14 remains draft/unmerged.

### Cross-runtime conformance status

| Semantic area | UWS PR #21 | M0 PR #4 | HabitRoute PR #14 |
|---|---|---|---|
| UNKNOWN / reconciliation fixture | PASS — nine-step shared K-UNKNOWN vector | PASS — same nine-step vector | Local pending-intent recovery tests; shared vector not yet demonstrated |
| Identity fixture | NOT_PROVEN | PASS — rejects same run ID with a different request | Exact version/run pinning exists; shared identity fixture not yet demonstrated |
| Authority | NOT_REPRESENTED | NOT_REPRESENTED | Host snapshot is not cryptographically authenticated; no shared authority fixture |
| Continuation frontier | NOT_REPRESENTED | NOT_REPRESENTED | Local flow restore exists; shared frontier fixture not yet demonstrated |
| Cross-host coordination | NOT_SUPPORTED | NOT_PROVEN / NOT_CLAIMED | NOT_SUPPORTED |

The conformance fixture remains draft. PASS means the repository adapter executed the represented local semantics; it does not prove the whole architecture interoperable or production-ready. Preserve canonical-capability-core rc2's prior UNKNOWN-consumption failure as a negative control.

### Current engineering order

1. Finish UWS PR #21 exact-head source review; its Linux, Windows and MySQL-backed CI jobs now pass.
2. Fix M0 recovery atomicity and add a true multi-process SQLite test under issue #5.
3. Add Windows and torn-write qualification to HabitRoute PR #14 under issue #16.
4. Extend the shared conformance fixture to HabitRoute and Android; keep Authority and Frontier explicitly NOT_REPRESENTED until exercised.
5. Continue live UWS↔HabitRoute goal/task/evidence integration only after the local read-only boundary, authenticated host authority and durable flow semantics are clear.
6. Keep HGSB database activation, provider reconciliation and any bounded write workflow as separate gates.

No PR was merged during this review. All cited implementation PRs remain draft/unmerged at this update.


## 8. M0 follow-up implementation — 2026-11-11

This supersedes the M0 PR #4 head and issue status recorded in section 7.

- Current M0 PR #4 head: `772b26fdbe379b86524f14e8de741f11b78b304c`.
- Exact-head Actions run [#43075855209](https://github.com/Loofy147/m0-durable-run/actions/runs/43075855209) passed Python 3.11, 3.12 and 3.13.
- Added an eight-process race against one shared SQLite file: one `RESERVED`, seven `REPLAY_BLOCKED`.
- Changed `recover_interrupted_effects()` so the latest-RESERVED scan and UNKNOWN event appends occur inside one `BEGIN IMMEDIATE` transaction.
- Added a SQL trace regression asserting BEGIN → SELECT → INSERT → COMMIT.
- M0 issue #5 remains open only for deterministic interleaving/fault-injection coverage of recovery racing with a newer reservation. The implementation and current CI do not claim multi-host coordination or exactly-once external delivery.

The conformance PR remains draft/unmerged.


## 9. Shared effect-identity and reconciliation contract gap — 2026-11-11

Open-System-One issue [#12](https://github.com/Loofy147/Open-System-One/issues/12) now tracks a cross-runtime semantic gap found while comparing the shared K-UNKNOWN fixture with M0 and UWS implementations.

The fixture supplies `scope`, `attributed_to` and `parameters_digest`, and both implementations compare these fields when present, but their reservation APIs currently require only `effect_id`, `run_id`, `capability_id`, `action_id` and `action_version`. Missing identity fields can therefore be absent on both sides of an identity comparison.

Additionally, local `reconcile(effect_id, decision)` APIs accept a bare decision string. This is a useful synthetic state transition, but it is not evidence that a trusted provider/authority established the external outcome.

The shared contract must define complete immutable effect identity, attempt/generation semantics, and evidence-backed reconciliation attestation. M0/UWS local primitives may store trusted attestation references without becoming provider authorities themselves. This issue is a contract/fixture gate, not a reason to promote any local ledger as production effect truth.


## 10. Android effect-journal audit — 2026-11-11

Android main remains at `78afd5d3d7716fe31a5f109a5796eb3db7f99970`. The existing UNKNOWN tests establish basic enumeration, reconciliation calls and journal restart. The separate T2 provider service runs in Android process `:provider`; its Binder process-death experiments must remain distinct from the main-process `JournalRuntimeStore` semantics.

A source audit found additional main-process effect-journal gaps, tracked in [Android issue #18](https://github.com/Loofy147/Llms-mcp-android/issues/18):

- `StoredEffect.compatibleWith()` omits `runId` from the identity comparison.
- `completeEffect()` and `markEffectUnknown()` append status changes without checking that the prior state is RESERVED; journal replay accepts syntactically valid status records without enforcing legal predecessor/successor transitions.
- Replay silently skips malformed R/E/X records at any position, not only a demonstrably torn final record. A skipped reservation could make the projection appear absent.
- The append path makes one FileChannel write call without looping/checking for a complete write.
- Per-instance synchronization and cross-instance/process coordination remain separately tracked by Android issue #8.
- Attempt/generation identity and evidence-backed reconciliation belong to the shared contract in Open-System-One issue #12; the shared Android fixture execution is tracked in Android issue #17.

These are source-review findings, not claims that an exploit or production duplicate action has been observed. Android issue #18 requires transition guards, fail-closed replay, torn-tail handling and fault-injection tests before this journal can be treated as a robust effect-state authority.
