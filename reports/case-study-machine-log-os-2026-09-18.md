
# Case Study: Machine vs Log-Os — Repository Identification and Evidence Boundary

Status: DURABLE PORTFOLIO FINDING
Date: 2026-09-18

## 1. Review question

Which repository is the active project for the current machine-native-primitives work, and what relationship does it have to the older Log-Os interpreter project?

## 2. Repository identities

### Active candidate

Repository: Loofy147/Machine

Default branch: main

Relevant research branch:
research/machine-native-primitives-v0

Main currently contains branch/evidence handling and experiment freeze/statistical-plan commits. The research branch contains the substantive machine-native research frontier.

### Historical candidate

Repository: Loofy147/log-os

Default branch: main

The repository is an older experimental Lisp/interpreter environment with a substantial Python implementation and Lisp standard library.

## 3. Branch evidence

Machine main and research/machine-native-primitives-v0 are not interchangeable.

A direct comparison of:

main
vs
research/machine-native-primitives-v0

reported:

- status: diverged;
- research branch ahead by 42 commits;
- main behind by 3 commits;
- merge base: 641517a26790c40295606f12fd6e4a87fcab7186.

The research branch contains substantive files such as:

- docs/ABSTRACT-MACHINE.md
- docs/EXPERIMENT-ONLINE-REFLECTIVE-LEARNING.md
- docs/EXPERIMENT-CONTEXTUAL-CREDIT.md
- docs/EXPERIMENT-ERROR-SOURCE-LOCALIZATION.md
- docs/REFLECTION-FRONTIER.md
- experiments/error-source-localization/

Therefore the research branch must be treated as a research frontier, not silently as default-branch state.

## 4. Machine research target

The inspected Machine research documentation defines the project around machine-native computation/adaptation and asks:

"What is the smallest fixed substrate that permits executable state to change its own future operating regime, while consequences and retained history can affect subsequent changes?"

The current documentation distinguishes:

reconfigurability
!= adaptation
!= learning
!= reusable learning
!= causal reflection

The online reflective-learning experiment reports continuous same-process evaluator hot-swap as experimentally supported in the tested harness, while the stronger causal-reflection target remains open.

## 5. Relevant Log-Os evidence

The inspected Log-Os main branch contains:

- a Python CPS/trampoline interpreter;
- explicit Computation, Value, TailCall, Effect, and Thunk objects;
- lexical Environment handling;
- object-language lambda/defun/macro machinery;
- a Log-Os multimethod system in stdlib/multimethods.l0;
- source loading and evaluation mechanisms.

These are useful historical implementation references.

They do not establish that Log-Os is the source repository for Machine's current prime-stream hot-swap experiment.

## 6. Critical distinction

The following statements are different:

1. Log-Os contains interpreter mechanisms useful to Machine research.
2. Machine may have conceptual similarity to Log-Os.
3. Machine may reuse code from Log-Os.
4. Machine's current experiment originated in Log-Os.
5. Machine and Log-Os are the same project or direct successor.

The inspection supports (1).

The inspection does not establish (3), (4), or (5).

Conceptual similarity alone is insufficient for lineage.

## 7. Durable portfolio classification

Machine
= CURRENT / RESEARCH-FRONTIER for the current machine-native-primitives line.

Log-Os
= HISTORICAL_REFERENCE for interpreter machinery.

Machine -> Log-Os direct lineage
= UNKNOWN.

This classification is tied to inspected repository/ref state on 2026-09-18 and must be revalidated after material repository movement.

## 8. Method lesson

This review exposed a general failure mode:

semantic resemblance can discover a useful reference while still identifying the wrong active project.

The professional correction is:

repository discovery
-> branch identification
-> recent-commit inspection
-> branch-specific source/doc inspection
-> default comparison
-> current-frontier classification
-> historical-reference classification
-> relationship inference only after evidence

## 9. Portfolio implication

The finding is not merely about Machine.

It becomes a general portfolio rule:

"Never identify the active project from semantic resemblance alone."

The exact branch/ref is part of technical identity.

## 10. Remaining open questions

- Does Machine intentionally reuse any implementation from Log-Os?
- Is there a historical commit/branch that demonstrates direct ancestry?
- Can genuine object-language closure be implemented without a Python special case?
- Can the Machine reflection target be achieved with causal continuity rather than source-file hot-swapping?

Until answered, retain UNKNOWN/OPEN rather than upgrading confidence.
