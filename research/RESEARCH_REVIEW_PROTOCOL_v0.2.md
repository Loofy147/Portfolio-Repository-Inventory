# Research Review Protocol v0.2

Status: ACTIVE RESEARCH METHOD
Effective: 2026-09-27

Purpose
-------
This protocol captures methodological findings learned from the research program itself and makes them reusable in future reviews and revisions.

## 1. Contract-first analysis

Before attributing an observation to a mechanism, freeze:
- information available;
- information timing;
- representation/state;
- primitive operations;
- authority/identity;
- resource accounting;
- correctness criterion;
- failure model;
- observation/evidence semantics.

A comparison that changes an uncharged contract dimension is not a clean mechanism comparison.

## 2. Result -> interpretation -> claim

Keep three layers separate:

result/observation
  -> interpretation
  -> claim

The interpretation is itself a hypothesis that must be audited for:
- evaluator validity;
- hidden assumptions;
- alternative explanations;
- causal identifiability;
- scope.

## 3. Iterative diagnosis closure

A minimal failure-inducing subset explains one witness, not necessarily the complete failure set.

Required loop:
failure set -> diagnosis -> minimal repair -> correctness/replay/generalization/preservation gates -> residual-failure search -> repeat -> global closure.

A repair process is not closed until the full acceptance suite has no unresolved failure.

## 4. Mechanism vs representation vs computation relocation

Every apparent mechanism improvement must be decomposed into at least:
1. primitive mechanism change;
2. richer representation/state;
3. computation relocation or altered cost model.

If a representation can reproduce the effect under the fixed substrate, do not call the effect an absolute capability increase.

## 5. Multi-resource frontiers

Avoid scalar 'power' claims when offline work, stored state, online work, latency, authority, reversibility, or consequence can trade off.

Report the relevant resource vector and Pareto frontier.

## 6. Black-box negative-result rule

Finite persistent failure is not sufficient evidence of expressive insufficiency.

Default:
INCONCLUSIVE_AT_RESOLUTION(delta)

A stronger negative statement requires an independently justified certificate or regularity assumption, with its scope explicitly recorded.

## 7. Hidden-assistance audit

Before accepting experimental evidence, test whether the controller received:
- labels;
- action vocabulary;
- fixed intervention order;
- regime identifiers;
- target information;
- structural priors;
- privileged observables.

Removing such assistance is a new experimental condition, not a cleanup detail.

## 8. Stronger-baseline obligation

For every positive result, identify the strongest credible alternative explanation and add a baseline/control targeted at that explanation.

## 9. Branch/ref provenance

Evidence identity is:
repository + branch + exact commit/ref + artifact + execution.

Branch-local results are not repository-wide truth until reconciled.

## 10. Reproduction before promotion

Historical numbers must be re-run from the current committed executable artifact. If reproduction changes a result, preserve the old value as historical/stale and promote only the reproduced value.

## 11. Cross-boundary security review

Review the entire flow:

reasoning -> proposal -> policy -> approval -> credential resolution -> egress -> effect -> observation -> verification -> evidence -> recovery

Do not treat one boundary control as proof of the complete flow.

## 12. Semantic identity survives execution replacement

Process, thread, Activity, Worker, Binder handle, provider instance, browser session, model session, scheduler, and sandbox are replaceable execution machinery.

Durable operation/run identity must exist independently for recovery and reconciliation.

## 13. Alternative explanation and falsification gate

Every material conclusion records:
- current explanation;
- credible alternatives;
- discriminating observation;
- falsifier.

A conclusion without a discriminating next action is incomplete.

## 14. Regression institutionalization

Important properties should become:
- executable tests;
- reproducible experiments;
- machine-readable claims;
- CI gates;
- canonicalization/reconciliation rules.

Prose-only invariants remain specification debt.

## 15. Epistemic status discipline

Use:
ESTABLISHED
FORMALLY_DERIVED
EXPERIMENTALLY_SUPPORTED
USER_REPORTED
INFERENCE
HYPOTHESIS
REFINED
CONTRADICTED
INCONCLUSIVE
OPEN

Repetition does not upgrade status.

## 16. Required final review

Before release, audit:
- definitions and notation;
- contract completeness;
- hidden assumptions;
- alternative explanations;
- unsupported assertions;
- causal interpretation;
- duplicate concepts;
- contradiction;
- evidence provenance;
- experiment reproducibility;
- implementation/formal-model gaps;
- unresolved gates.

Then produce:
- consolidated claims;
- explicit limitations;
- open questions;
- next discriminating experiments;
- exact release provenance.

## Applied to the 2026-09-27 revision

Applied changes:
- narrowed mechanism-frontier language;
- separated representation closure from mechanism change;
- retained multi-resource accounting;
- retained INCONCLUSIVE_AT_RESOLUTION for black-box insufficiency;
- classified transfer pilot as contract evidence only;
- treated ddmin as local diagnosis rather than global repair;
- kept Android T2 claims at B2/B3 case scope;
- retained exactly-once, credential isolation, provenance-aware egress, causal reflection, compact representation closure, and complete branch canonicalization as open;
- verified release branch heads and commit provenance.

This protocol is now part of the research method and must be used in subsequent reviews/revisions.