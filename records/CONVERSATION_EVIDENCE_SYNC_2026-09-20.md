# Conversation Evidence Sync — 2026-09-20

Status: DURABLE PORTFOLIO RECORD
Repository: Loofy147/Portfolio-Repository-Inventory
Branch: main

Purpose
-------
Record the durable cross-repository findings from the September 19–20, 2026 engineering discussion and point to the authoritative project records.

## Loofy147/Machine

Authoritative sync:
- Branch: research/evidence-disposition-v0
- Commit: 8f16e5dcc57c59025e3cc9ec5607d294a1c8b8e3
- File: docs/research/CONVERSATION_FINDINGS_2026-09-20.md

Durable findings:
- One-shot ddmin can under-repair a bundled failure containing an independent bug plus an AND-interaction pair.
- Repair must iterate: diagnosis -> minimal repair -> correctness/replay/generalization/preservation gates -> re-diagnosis until the full acceptance suite is clear.
- S2 post-repair conformance evidence is suite-scoped and tied to repair commit d768ffdea4472ea4c88351f5bd680b8f30bc9152 and Actions run 35466392638.
- Target-oblivious frontier remains OPEN and requires explicit B/W/accuracy measurements before architectural conclusions.
- Repository/branch/ref/commit is the minimum evidence identity; conversation-only work is not repository evidence.

## Loofy147/Llms-mcp-android

Authoritative sync:
- Branch: main
- Commit: 7a7e1c67d1dce15457b62cf173d159a7be15f9ce
- File: docs/architecture/CONVERSATION_FINDINGS_2026-09-20.md

Durable findings:
- Model/reasoning, policy, approval, risk signals, execution authority, and evidence remain distinct.
- Meta Muse and Anthropic research reinforce credential isolation, provenance-aware egress, bounded containment, and separation of durable semantic state from execution machinery.
- T2 cases B2/B3 are experimentally supported at case level; B4/B5/B6/B7 and caller-side UNKNOWN_OUTCOME remain open.
- Next proving sequence is caller recovery -> concurrent recovery -> stale ordering -> credential-use isolation -> provenance-aware egress -> event sufficiency -> MCP re-audit -> high-power containment.
- No general exactly-once claim and no speculative VM/eBPF/browser/multi-agent/event-bus layer should be promoted ahead of evidence.

## Cross-repository operating invariant

Every important engineering action must preserve:
repository + branch + exact ref/commit + changed files + executed action/experiment + actual result + claim/status + interpretation boundary + next discriminating action.

External reference material may change research priorities, but never upgrades local implementation claims without local evidence.
