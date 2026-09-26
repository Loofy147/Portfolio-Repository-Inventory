# Portfolio review state — 2026-09-26

## Source-of-truth status

- Inventory repository main HEAD after review/lineage merge: `624726c548ccb3a28b239681b83c77d26ff7b006`.
- Inventory Validation push run #39 passed on that exact HEAD.
- PR #7 (deep-review completion + Wedgettok lineage concern) is merged.
- The 2026-09-24 census delta recorded an exact connected-search surface of 342 repositories, up from 339 on 2026-09-22.
- The 342 count is the latest exact census currently recorded. A fresh exact 2026-09-26 full recount was not independently established, so no newer total is asserted.

## Completed review work

The previous two deep-review waves remain complete: 10 repositories were reviewed at claim/evidence level. The capability-discovery step then pivoted from repository-by-repository auditing to need-driven mechanism discovery.

Three repositories added in the 2026-09-24 census delta were inspected directly:

### All-time-
Browser-first local AI workspace. Current main contains WebGPU adapter detection, WASM/CPU fallback, pinned Hugging Face revisions, installable PWA architecture, run-level evidence identities/digests, and CI build provenance. Main quality run 36056291780 passed for typecheck/build/provenance.

Boundary: browser acceptance, installed Android/PWA update behavior, Android WebGPU benchmarking, deterministic acceptance, structured failure taxonomy, and product persistence remain open.

### Conversational
Repository-native durable conversation continuity. The entrypoint requires resolving the event log, canonical state, revision, lineage, provenance, projection and restore policy before producing a RestoreResult. Current protocol remains CANDIDATE / UNVERIFIED for fresh-conversation restore, with external action authorization explicitly separated from restored context.

### Open-System-One
Typed decision substrate with deterministic composition and replaceable runtime backends. Core decision contract is documented as ESTABLISHED; browser MiniLM ONNX execution is EXPERIMENTALLY_SUPPORTED; set-aware and conditional advantages remain OPEN.

## Mechanism families now visible

The current portfolio scan identifies reusable mechanism families around:

- evidence/provenance kernels;
- capability qualification and authorization;
- MCP ingestion and connector boundaries;
- durable execution/restart/reconciliation;
- typed decision contracts and deterministic ledgers;
- browser-local inference and PWA runtime;
- mobile agent execution;
- conversation continuity and episodic memory;
- adversarial/replay verification.

Important distinction: search hits and README claims are signals until checked against the implementation/ref/commit and, where material, executable evidence.

## Current directly actionable review paths

1. My_browser → All-time- → Llms-mcp-android: test whether the acquisition/evidence lifecycle can wrap a real browser-local model run.
2. Conversational → UWS → m0-durable-run: test which continuity/recovery mechanisms are genuinely composable after restart/replay.
3. canonical-capability-core → Llms-mcp-android → UWS: inspect capability qualification/authority boundaries as a portable mechanism.
4. Open-System-One → ledger-system-source-of-truth: test typed decision state plus deterministic contradiction handling without aggregate-truth semantics.

## Remaining portfolio concerns

- G10: historical D4 review-log records remain unconverted.
- P1: older catalog observations need revalidation when they materially affect a current decision.
- C1: Wedgettok roadmap baseline is stale relative to current HEAD.
- C2: Wedgettok-Next operational lineage classification remains OPEN.
- U1: UWS Projects UI has stale persistence wording.
- Portfolio-wide assessment remains intentionally OPEN outside the six Core Working Set repositories.
- The 2026-09-24 three-repository census delta has identity evidence, but its capability classification is now only partially advanced; the new capability map records the direct findings for the three and signal-only treatment for most secondary candidates.

## Operating rule for the next round

Do not audit more repositories merely because they exist. Start from a concrete capability gap or experiment, then inspect only the repository/ref/evidence needed to discriminate the mechanism. Reuse is promoted only after a measurable experiment or independent verification supports it.
