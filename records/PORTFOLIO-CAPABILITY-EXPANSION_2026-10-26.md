# Portfolio Capability Expansion — 2026-10-26

**Purpose:** Record newly inspected capability relationships, their evidence limits and the next useful discrimination test.
**Observed portfolio ref:** main at 33e66462b9f48b796e78da1c9b214737d8808ac3.
**Review depth:** selective D1/D2 — README, architecture indexes and selected qualification records. No full test suites were executed in this pass.

## Main finding

Several repositories address related but distinct parts of the capability-execution lifecycle. They should be compared through a narrow interface experiment rather than merged into a single runtime.

| Repository | Observed ref / commit | Directly inspected evidence | Limitation |
|---|---|---|---|
| [canonical-capability-core](https://github.com/Loofy147/canonical-capability-core) | master / 6396327425e7f5e6c23456579ebc286ca69f771f | README and referenced versioned release records describe capability qualification, action, observation, reconciliation and a candidate v0.22 conformance release. | Release lineage and current executable behavior need a deeper inspection; reported test counts were not rerun here. |
| [external-staging-authority](https://github.com/Loofy147/external-staging-authority) | main / 5e313c05245dfa5b646d3b80713b74d443b8c528 | README, independent qualification record and precision audit describe synthetic timeout, restart and reconciliation cases against a pinned candidate image and a separate durable effect ledger. | The recorded qualification is for the named canonical-capability-core image in controlled CI—not Deter-agent or production authority. A separate physical failure domain is not established. |
| [m0-durable-run](https://github.com/Loofy147/m0-durable-run) | main / 69b07a54e4b2f8421532b78b8abffca308bbe3da | README describes an intentionally minimal SQLite run/evidence store and a separate-process restart/idempotency demonstration. | Claims were documented, not rerun in this review; remote-provider behavior remains unverified. |
| [Llms-mcp-android](https://github.com/Loofy147/Llms-mcp-android) | main / 78afd5d3d7716fe31a5f109a5796eb3db7f99970 | README and architecture index describe a user-owned mobile runtime with action, policy, approval, egress, run, verification and evidence boundaries. | Its cited CI result is from an older commit; current-head and real-device behavior were not independently verified. |
| [unified-knowledge-work-system](https://github.com/Loofy147/unified-knowledge-work-system) | main / 683c38fdc3c921c1d7977786d5b5ed8617969476 | README describes relationship-aware task/module routing, evaluation suites and evidence-bearing handoffs. | Planning and routing outputs are not evidence that external actions succeeded and do not authorize them. |
| [Open-System-One](https://github.com/Loofy147/Open-System-One) | main / fb21d176d0ed1b083df889cf747ac562d449ceef | README and research index describe a typed decision contract, deterministic composition, abstention and replaceable model backends. | The README marks some model advantages as open; a model score must not become permission to act. |
| [All-time-](https://github.com/Loofy147/All-time-) | main / c9f8662acde83808b64ad75ac8bef4ee67edd5da | README describes browser-local inference, pinned model revisions, WebGPU with WASM/CPU fallback and a PWA shell. | The README says current-main production verification remains open. |
| [outonomos-system](https://github.com/Loofy147/outonomos-system) | main / 71f4f46156507a6741a4cf55b6f222c8274af643 | README describes contribution intake, security/license checks, risk tiers and human review escalation. | Scanner coverage, bypass paths and actual tests require source-level review. |
| [Agora-32Bit](https://github.com/Loofy147/Agora-32Bit) | master / f16485b19a5a74628469eb08d9fcbec4d0b6f822 | README describes an Android BYOK multi-provider client with local history, MCP and remote shell tooling; README identifies an MIT license. | Provider isolation, secret handling, runtime permissions and remote-tool security were not audited. |
| [METATRON](https://github.com/Loofy147/METATRON) | main / 9dd2ee3daa33397453c76e9fcba446f117d22cb6 | README describes a local-LLM-assisted security assessment workflow with saved scan history. | Use only in owned or explicitly authorized test environments. Findings need verification against tool evidence. |

## Relationship status

- **canonical-capability-core → external-staging-authority:** established in the staging repository's qualification record for its named image; not an established Deter-agent integration.
- **m0-durable-run ↔ Deter-agent:** shared-primitive candidate for restart and idempotency tests; implementation compatibility remains unknown.
- **Llms-mcp-android ↔ Deter-agent:** independent similarity around action/policy/approval/execution/evidence boundaries; no code lineage is asserted.
- **unified-knowledge-work-system ↔ Deter-agent:** candidate for evidence-bearing handoffs and task routing only; keep authorization separate.
- **Open-System-One ↔ Deter-agent:** candidate for testing the boundary between model-derived recommendations and deterministic action permission.
- **outonomos-system ↔ Loofy-Extensions:** adjacent contribution/extension governance; compare actual implementations before declaring overlap or choosing one canonical owner.

## Recommended next experiment

Run a small synthetic, provider-neutral conformance matrix before writing any new adapter:

1. Confirm the command identity, idempotency key, attempt and evidence-binding contract.
2. Test pre-dispatch rejection, timeout before commit, timeout after commit, restart and reconciliation.
3. Count effects at the target-side ledger rather than inferring them from the caller's local log.
4. Compare results at each repository's current observed ref. Preserve each project's output as evidence belonging to that project.
5. Implement an adapter only if the contracts match and the experiment demonstrates a concrete gap that the adapter solves.

The staging record's reported result is useful source evidence, but it does not prove Deter-agent passes the same cases. This record does not update the census, current target, Core Working Set or relationship inventory. It is discovery—not an integration approval, production-readiness finding or lineage claim.

## Next review depth

For the first controlled experiment, inspect the current source/tests in canonical-capability-core, m0-durable-run and external-staging-authority at the refs above, then execute only synthetic cases. Current-head tests for Llms-mcp-android and unified-knowledge-work-system should be revalidated before adopting any runtime contract.
