# Machine-native Primitives ↔ Log-Os Reference Audit
Date: 2026-09-18
Status: EVIDENCE NOTE / NOT A LINEAGE DECISION

## Scope

This note records the current evidence boundary between the active `Machine` research line and the older `log-os` interpreter. It does not establish code lineage or repository equivalence.

## Current Machine position

The active research specification is present on `research/machine-native-primitives-v0`.

The branch defines the reflection frontier as a stronger property than ordinary executable hot-swap:

reify/expose execution machinery
-> modify
-> modified representation participates in later transitions
-> observable behavior changes

The candidate minimal state is `Q = <R, S, K, rho, H>`, with `rho` required to be causally consulted by future execution.

The online experiment specification explicitly states that the existing prime-stream result is limited: it demonstrates same-process executable replacement, but the current reification reads an external source representation, Python evaluation semantics remain fixed, and candidate validation occurs outside the live execution path.

Therefore the current target is stronger than existing hot-swap evidence.

## Log-Os evidence

The inspected `log-os` snapshot contains:

- a Lisp-like object language with `lambda`, lexical environments, macros and multimethods;
- a Python-hosted `lambda` implementation that creates a Python callable and captures the current `Environment`;
- a CPS/trampoline execution model with explicit `Value`, `TailCall`, `Effect`, and `Thunk` computation objects;
- language-level `defmulti` / `defmethod` machinery implemented in L0;
- multiple meta-level uses of `eval`, including constructing functions from AST data.

These establish useful historical substrate capabilities, but they do not by themselves establish online causal reflection.

## Critical boundary

The current `log-os` closure implementation is host-defined:

object-language lambda
-> Python function closure
-> captured Python Environment

That is different from the current Machine target:

object-language closure
-> reifiable object-language value
-> mutable/replaceable dispatch semantics
-> same live continuation continues under modified rule

Likewise, the inspected `log-os` surface does not provide sufficient evidence that the prime-stream hot-swap harness described by the current Machine documents is implemented there. The experiment should therefore not be attributed to `log-os` without locating the actual harness/history artifact.

## Reusable evidence from Log-Os

The old project remains relevant as an implementation reference for:

1. explicit continuation/trampoline representation;
2. lexical environment structure;
3. object-language functions and dynamic dispatch;
4. AST-level `eval` and program construction;
5. failure modes caused by leaking host-language semantics into language semantics.

It is not sufficient as evidence for the stronger Machine reflection claim.

## Discriminating test for Machine

The decisive test should be:

single live run
-> execute ordinary object-language code
-> reify actual closure / dispatch state
-> transform it in the object language
-> install modified rule
-> continue the SAME continuation
-> observe changed later transition

A test that terminates the run and starts a second invocation is insufficient.

A test that mutates an external Python object while the interpreter keeps using a hidden Python callback is also insufficient.

The strongest minimal pair keeps ordinary state, input, continuation, and target operation fixed while changing only the installed object-language execution rule.

## Status

- Machine repository identity: OBSERVED
- `research/machine-native-primitives-v0` as the active documented research line: OBSERVED
- Online same-process hot-swap as documented experimental evidence: EXPERIMENTALLY_SUPPORTED / LIMITED
- Genuine object-language closure with no Python special case: OPEN / current implementation target
- Causal online evaluator/dispatch replacement in one unbroken run: OPEN
- `log-os` as historical implementation reference: OBSERVED
- `log-os` as proven source of the current Machine hot-swap experiment: UNKNOWN
- Direct code lineage Machine -> Log-Os: UNKNOWN