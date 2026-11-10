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
| Knowledge-work coordination | [unified-knowledge-work-system](https://github.com/Loofy147/unified-knowledge-work-system) `main@683c38fdc3c921c1d7977786d5b5ed8617969476`; conformance PR #21 head `dc4a4a1dbfb1420b287c4d3eac2c061bac329d54` | Module registry and relationship ledger; task routing; specialist composition; evaluation, context/trust/review/adjudication; MySQL/Drizzle project, plan revision, event, evidence, assumption and validation persistence; PR #21 adds a separate JSONL effect recovery primitive. | **SOURCE-OBSERVED / PARTIAL:** the PR #21 syntax defects were repaired and both modules passed local compilation and smoke checks. Its earlier Actions run #331 failed on the pre-fix source; no new Actions run was observed at the corrected PR head. The JSONL effect ledger has no cross-process writer lock; concurrent-writer safety remains OPEN. HGSB database activation remains separately verification-pending. | Coordination, knowledge-work, project/plan and claim-adjudication owner. |
| Goal/search/boundary continuity | [UWS HGSB PR #23](https://github.com/Loofy147/unified-knowledge-work-system/pull/23), branch `feat/hgsb-durable-state-v0.1` | Versioned state schema, persistence contract and bootstrap artifact for hierarchical goals, search state, capability boundaries and continuation. | **DRAFT / VERIFICATION-PENDING:** Git bootstrap is retrievable; database-backed HGSB activation awaits MySQL migration, ownership, CAS/idempotency and restart/recovery proof. Keep separate from UWS project persistence. | Long-horizon goal/search/boundary continuity; not action authority. |
| Conversation continuity | [Conversational](https://github.com/Loofy147/Conversational) `main@9da36fcd99f49b9f859751f39d1a4f4393c1d1de` | Repository-native event history, canonical-state reduction, projection, lineage and restore policy. | **CANDIDATE / RESTORE UNVERIFIED:** first fresh-boundary restore is reported, not independently attested; authenticity is self-integrity only. Restore is CONTEXT_ONLY and cannot authorize actions. | Conversation frontier recovery, not project truth or global memory. |
| Durable Run and local effect ledger | [m0-durable-run](https://github.com/Loofy147/m0-durable-run) `main@69b07a54e4b2f8421532b78b8abffca308bbe3da`; [PR #4](https://github.com/Loofy147/m0-durable-run/pull/4) head `fc283c7c18a30be52d464894bed3a337b89aefa3` | Small SQLite append-only Run/evidence store; idempotent stable Run identity; two-process restart demonstration; draft append-only effect ledger with UNKNOWN/reconciliation; SQLite `BEGIN IMMEDIATE` serialization for effect reservation and state transitions; cache artifact provenance/reuse contracts. | **EXPERIMENTALLY_SUPPORTED IN LOCAL SQLITE SCOPE:** deterministic 16-worker test gives one `RESERVED` and 15 `REPLAY_BLOCKED`; core, router, effect lifecycle/concurrency and two-process restart checks passed on Python 3.11/3.12/3.13 in Actions run [#42860970422](https://github.com/Loofy147/m0-durable-run/actions/runs/42860970422), exact PR head. The effect ledger remains a draft PR, no provider adapter or external-authority integration; no distributed/multi-host or exactly-once guarantee. Agent executor remains a stub. | Minimal Run durability plus a candidate local effect-state primitive; keep both narrowly scoped. |
| Device effect authority | [Llms-mcp-android](https://github.com/Loofy147/Llms-mcp-android) `main@78afd5d3d7716fe31a5f109a5796eb3db7f99970` | Action/Capability separation, policy engine, approval store, egress policy, CapabilityExecutor, runtime store and tests for UNKNOWN effect enumeration/reconciliation across journal restart. | **SOURCE-OBSERVED / ANDROID-LOCAL:** tests cover unknown/completed/not-executed states and restart. Cross-platform semantics and current-device CI must be revalidated before portability claims. | Candidate authority/effect implementation for Android; conformance reference, not universal owner. |
| Machine habits and persistent flows | [HabitRoute](https://github.com/Loofy147/HabitRoute) `main@e57e86afa12757223b9dada4ff191b496ece6c1f`; checkpoint PR #12 head `c505d96fe011f94af8eae90fab84f6ebcf317c81` | Versioned machine habits, harness contracts, side-effect classes, local event-sourced flow journal and worker; PR #12 adds per-operation intent/result, attempt accounting, resume cursor and fail-closed pending intent. | **DRAFT PR / CI PASS:** PR #12 run #42703942809 passed 93/93 tests on Python 3.11–3.13. It remains local single-writer JSONL; unknown provider outcomes still need reconciliation. | Procedural machine habits and local flow/step progress; not human intent, global state or provider authority. |
| Capability repertoire and read-only Git inspector | [HabitRoute PR #10](https://github.com/Loofy147/HabitRoute/pull/10), branch `feat/habit-repertoire-composition-v0.3`, head `dd9d88e45b2bfd2dfeaa0130439838181ccc8c15` | SituationFrame, exact host capability snapshot, bounded dry-run capability-chain planner and read-only immutable Git commit-range inspector. | **DRAFT / PLANNING + NARROW EXECUTION:** reference repo-verification path exists; it does not run project tests/scripts or persist a HabitEpisode through the flow worker. | Candidate read-only capability discovery/execution path for a first vertical slice. |
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
- HabitRoute's pending-intent guard prevents blind local replay, but does not query a provider or determine whether an external effect occurred.
- Android's UNKNOWN journal tests are a real local implementation candidate, but not proof that its state model is portable or identical to the canonical-capability contract.
- My_browser's evidence IDs and hashes provide integrity/lineage references, not external-source authenticity or semantic truth.
- The canonical-capability rc2 failure is a useful killed assumption: successful adapter transport is not enough; the runtime must consume UNKNOWN at the state-transition boundary.
- Personal digital-twin products are not the human-machine control plane; their data requires a separate privacy/consent boundary.


## 3A. Evidence update — 2026-11-10

- **M0 concurrency:** a forced two-reader reproduction showed the old read-then-append race could produce two `RESERVED` outcomes for one `effect_id`. The draft repair moves state read/validation/append inside a SQLite `BEGIN IMMEDIATE` transaction. The 16-worker regression passes with one reservation and 15 blocked replays. Actions run #42860970422 passed all three Python versions and all core/router/effect/restart steps on M0 PR #4 head `fc283c7c18a30be52d464894bed3a337b89aefa3`. The qualification is local to workers sharing the same SQLite file.
- **UWS effect recovery:** PR #21's malformed newline and backslash literals were fixed. Local compilation, state-machine smoke and path-traversal guards pass. The historical CI failure was on the earlier broken source; CI at corrected head was not observed. The JSONL append path has no cross-process writer lock; do not call it concurrency-safe.
- **Architecture implication:** M0 and UWS now both carry candidate local UNKNOWN/reconciliation primitives, but with different stores and limitations. They have not passed a current-head, clean-clone shared conformance campaign. The Open-System-One G-02/G-04 cross-runtime gaps remain OPEN.

## 3B. Shared-fixture coverage audit — 2026-11-10

A source-level comparison of the two repository adapters reveals an important asymmetry that should drive the next implementation step:

| Fixture assertion | M0 adapter at `conformance/cache-contract-v0.1` | UWS adapter at same branch family |
|---|---|---|
| K-IDENTITY-01 | Executes same Run ID / different request rejection; reports PASS only on observed rejection. | Reports NOT_PROVEN. |
| K-VERIFY-01 | Executes completed Run, records Observation and independent verifier rejection; checks execution remains completed while verification is failed. | Executes same separation and rejection pattern; checks persisted Verification. |
| K-EVIDENCE-01 | Links Run, Observation, Verification and Evidence; checks references. | Links Run, Observation, Verification and Evidence; checks references. |
| K-UNKNOWN-01 | Loads the vendored Open-System-One v0.2 fixture, verifies its Git blob SHA, executes each vector step against the SQLite effect ledger, and checks result, state and event-count delta. | Reports NOT_REPRESENTED in `conformance_adapter.py`. Separate UWS `effect_recovery.py` tests cover UNKNOWN blocking/reconciliation/recovery, but the shared conformance adapter does not invoke them. |
| K-AUTHORITY-01 | NOT_REPRESENTED. | NOT_REPRESENTED. |
| K-FRONTIER-01 | NOT_REPRESENTED. | NOT_REPRESENTED. |

**Interpretation:** M0 has stronger coverage of the current shared UNKNOWN fixture, while UWS has a separate local UNKNOWN helper/test suite that has not yet been wired into its conformance adapter. It would be incorrect to report the two adapters as equivalent on K-UNKNOWN-01. It would also be incorrect to infer that UWS lacks all UNKNOWN behavior: its separate helper implements RESERVED → UNKNOWN → COMPLETED / CONFIRMED_NOT_EXECUTED and tests replay blocking and recovery.

**Next discriminating implementation:** add a UWS adapter path that executes the exact same vendored K-UNKNOWN-01 vector against the UWS effect helper, with source-blob pinning and per-step state/event assertions. First resolve the topology difference: UWS currently appends JSONL without a cross-process writer lock, while M0 uses SQLite `BEGIN IMMEDIATE`. The adapter should report concurrency as NOT_TESTED until a separate concurrent-writer test exists; do not make the UWS JSONL helper appear equivalent to M0's transaction semantics.

**Evidence boundary:** the 2026-10-05 Open-System-One experiment records are source-reconstructed experiment artifacts. They provide useful test-design and result evidence, but their own provenance/limits say they were not a clean-clone CI campaign. The present adapter source comparison is direct code inspection, not a fresh execution of either adapter in this review.

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
