
# Reflection Substrate Re-Audit — Portfolio Finding

Date: 2026-09-18
Status: DURABLE RESEARCH AUDIT

The second audit reconciled the first reflective-interpreter candidate with the current Machine repository and external literature.

Key findings:

1. The closest direct precedent is Friedman & Wand 1984. Their reflection construction exposes interpreter structures including form/expression, environment, and continuation to running code and allows them to be altered without requiring an infinite reflective tower. cite-reference:FW84
2. Wand & Friedman 1986/1988 provide the stronger semantic account of reflective towers, including metacontinuation and the relation between reified environment/continuation and their reinstallation. cite-reference:WF8688
3. des Rivières/Smith show an implementation strategy based on a level-shifting processor, so a literal single host-language loop is not the core invariant. cite-reference:DRS84
4. CEK remains a suitable structural substrate for the candidate's control/environment/continuation decomposition. cite-reference:CEK

Decision consequences:

- Narrow the first reflection target to `rho_dispatch`.
- Treat the supplied candidate as unverified until committed and tested.
- Keep confirmatory-fault-transfer governance separate.
- Do not add more reflective features before the minimal causal-dispatch test.
- Treat ordinary `set!` as a matched control.
- Require an explicit representation/install contract for environment and continuation.
- Treat continuation replacement during install as a semantic choice requiring an explicit jump/tail/resume/level interpretation.
- Keep the bootstrap hook explicit and minimal.
- Keep reachable-space expansion, reusable structure, modifier self-change, and substrate portability outside the first proof obligation.

Immediate claim:

"A running machine can causally replace an object-language-defined compound-procedure dispatch rule through reified state and same-run installation, producing a later observable dispatch difference under matched controls."

No stronger claim is promoted.
