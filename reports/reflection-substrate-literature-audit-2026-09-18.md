
# Reflection Literature Mapping — Portfolio Finding

Date: 2026-09-18
Status: RESEARCH ALIGNMENT

The first reflective-interpreter candidate was reconciled with Machine's current reflection frontier and external literature.

The closest direct precedent is Friedman & Wand (1984), "Reification: Reflection without Metaphysics": interpreter data structures can be exposed to running code and altered, including form/expression, environment, and continuation, without requiring an infinite reflective tower.

Wand & Friedman (1986), "The Mystery of the Tower Revealed", is better mapped as a semantic/reference framework for reflective towers.

Smith/des Rivières work is relevant to causal connection, vantage point, and level-shifting.

The candidate therefore maps:

CEK substrate
-> tower-independent reification/reflection
-> procedural-reflection / causal-vantage precedent
-> Machine narrow reflective seam (rho_dispatch = *applier*)

Durable gaps identified:

- reify currently uses control=0 instead of current control;
- environment/continuation remain host objects;
- *applier* still has a host-recognized bootstrap role;
- reflective mutation has not yet been shown to alter future rho_dispatch;
- continuation transport is present but continuation transformation is not;
- clone isolation is not established for arbitrary aliases;
- probe/rollback is not integrated;
- minimum substrate is not established.

A prior over-strong interpretation was corrected: literal use of one host while-loop is not the core requirement. The stronger requirement is uninterrupted causal execution with correct continuation/meta-level semantics.

This is an audit finding, not a claim that tier-3 has been demonstrated.
