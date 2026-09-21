# Core Working Set — 2026-09-21

Status: **OWNER-SELECTED PRIMARY WORKING CORPUS**
Repository: `Loofy147/Portfolio-Repository-Inventory`
Branch: `main`

## Decision

The following six repositories are now registered together as the **Core Working Set** for primary work:

1. `Loofy147/Llms-mcp-android`
2. `Loofy147/Machine`
3. `Loofy147/unified-knowledge-work-system`
4. `Loofy147/m0-durable-run`
5. `Loofy147/la-rouine-platform`
6. `Loofy147/Wedgettok`

This is a portfolio working-set decision. It **does not** assert that these repositories are one project, that they share lineage, or that they should be merged.

## Revalidated state

| Repository | Ref used | Current head | Working role | Claim frontier |
|---|---|---|---|---|
| `Llms-mcp-android` | `main` | `7a7e1c67d1dce15457b62cf173d159a7be15f9ce` | Android agent runtime/control plane | T2 B2/B3 experimentally supported; B4/B5/B6/B7 and caller-side UNKNOWN_OUTCOME remain open |
| `Machine` | `main` + research refs | `1626bac2f5c478294afa4b9463f694608c322117` on main | Machine-native/interpreter/substrate research | research branches carry the executable frontier; claims remain branch/ref scoped |
| `unified-knowledge-work-system` | `main` | `4a39bfbbcc069492a6fbd3f7ddf4ae5e5b6196b9` | Durable knowledge/control plane | persistence, project continuity, plan revision and actor attribution implemented; broader real-world validation remains open |
| `m0-durable-run` | `main` | `9436841c77d5a1cb9d23051a3db69eb93ec6240d` | Minimal durable execution primitive | local durable/idempotent/restart evidence exists; real-provider variation and abstraction boundaries remain open |
| `la-rouine-platform` | `main` | `3f2a7f4d2cb16db7488afdb16f1610c27ae3d1ca` | Declarative Experience runtime | deterministic render, validation, editability, remix/lineage and outcome gates have executable evidence; feed/moderation/creation/offline-online remain open |
| `Wedgettok` | `main` | `0d4ac8958008b305f082b806387184ce548816c0` | Experience/feed product surface | Experience contracts and catalog are present; actual user/feed evidence remains separate from design/catalog evidence |

## Provenance rule

Each member is registered in `inventory/repositories.json` with its exact observed HEAD snapshot. The review depth and inspected focus are registered in `inventory/review-log.json`.

Evidence remains owned by the source repository/ref. A Core Working Set membership entry must never be treated as evidence that a claim in one member is true in another.

## Non-merges

No cross-repository lineage, code reuse, dependency, or semantic equivalence is promoted by this record.

Known historical/reference relations remain separately governed by `inventory/relationships.json`.

## Operating rule

Future work involving these repositories should begin from this Core Working Set unless a new review establishes that another repository/ref is the actual source of the relevant work.

The working set is not a stop gate for other valid projects; it is the current primary corpus for coordinated work.
