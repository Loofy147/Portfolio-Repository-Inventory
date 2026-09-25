# Membership Operation — Portfolio Inventory Integration Decision

## Experiment identity

- Repository: `Loofy147/Portfolio-Repository-Inventory`
- Branch: `experiment/membership-operation-v0.1`
- Base commit: `fba524c0859f906f02a3440db197951fe8935959`
- Workload: `current census - historical repository inventory`
- Existing validator: `scripts/validate_inventory.py`
- Production files changed: none.

## Why this workload qualifies

The repository already defines and enforces:

```
new_triage_expected = current_census_names - historical_names
triage_names == new_triage_expected
```

This is an actual set-difference invariant over repository identities, not a synthetic example.

Current data:

- historical inventory: 319 repositories
- current census: 339 repositories
- current triage: 20 repositories
- exact difference: 20 repositories

The twenty resulting identities exactly match the twenty current triage records.

## Controlled comparison

Candidates:

1. direct identity anti-join using a native set;
2. the operation-level `anti_join(left, membership, key=None)`;
3. the same operation with an explicit identity projection callback.

The third path is deliberately measured as a cost boundary: identity-key workloads should not pay for a projection callback they do not need.

Because the real dataset contains only 339 identities, the same exact values were repeated 10,000 times for timing. No repository identifiers were invented.

### Three repeated cycles

| Cycle | Direct ms | Generic identity ms | Identity overhead | Explicit identity-key overhead |
|---|---:|---:|---:|---:|
| 1 | 167 | 167 | 0.00% | 31.14% |
| 2 | 162 | 168 | 3.70% | 33.95% |
| 3 | 163 | 166 | 1.84% | 36.81% |

The amplified run contains 3,390,000 membership checks.

## Correctness

All checks passed:

```
census - historical == triage
generic identity anti-join == direct identity anti-join
projection path == direct identity result
orphan/new repository count = 20
```

## Decision

### KEEP

The operation-level primitive remains a credible shared operation:

```python
anti_join(items, membership, key=None)
```

For identity-key workloads, `key=None` is the fast path.

### REJECT

Do not require an explicit identity projection callback.

The measured cost was approximately 31–37% in this workload.

### DO NOT PROMOTE TO PORTFOLIO CORE YET

The experiment demonstrates a second real use of the operation, outside the M0 execution/evidence system. That is materially stronger evidence of portability.

However, the current portfolio validator already expresses this invariant clearly and efficiently. Replacing it now would add a dependency/abstraction without reducing current complexity enough to justify the change.

## Evidence status

**EXPERIMENTALLY_SUPPORTED**

- The operation matches a real cross-file invariant in the portfolio system.
- The result is exactly equivalent to the repository's current validator logic.
- The same operation remains within a small overhead envelope when the membership argument is native and the identity path avoids unnecessary projection.
- The invariant is therefore portable across at least two substantially different systems:
  - execution/evidence reconciliation in `m0-durable-run`;
  - repository-census/triage reconciliation in `Portfolio-Repository-Inventory`.

**NOT PROVEN**

This does not prove that a standalone membership library should be maintained.

## Promotion trigger

Promotion into a shared library or canonical package requires a concrete third workload OR a non-performance benefit that removes duplicated correctness logic, configuration, instrumentation, or backend selection.

Until that trigger occurs, keep the operation as a small research primitive and do not create a framework around it.
