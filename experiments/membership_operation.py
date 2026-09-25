"""Second-system integration probe for Membership Primitive.

Real workload:
    current census repositories - historical inventory repositories

This is the exact invariant already enforced by scripts/validate_inventory.py:
    new_triage_expected = current_census_names - historical_names
    triage_names == new_triage_expected

No production validator is modified by this experiment.

The candidate primitive is deliberately operation-level:
    anti_join(left, membership, key=None)

When key is omitted, the hot loop performs direct membership. When a key is
actually needed, the projection is paid explicitly. This avoids making a
projection callback part of every identity-key lookup.
"""

from __future__ import annotations

import json
import platform
import random
import time
from statistics import median
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(relative: str):
    with (ROOT / relative).open(encoding="utf-8") as fh:
        return json.load(fh)


def direct_anti_join(left, membership):
    out = []
    for value in left:
        if value not in membership:
            out.append(value)
    return out


def anti_join(left, membership, key=None):
    out = []
    if key is None:
        for value in left:
            if value not in membership:
                out.append(value)
    else:
        for value in left:
            if key(value) not in membership:
                out.append(value)
    return out


def median_ms(fn, repeats=7):
    samples = []
    result = None
    for _ in range(repeats):
        start = time.perf_counter_ns()
        result = fn()
        samples.append((time.perf_counter_ns() - start) / 1_000_000)
    return result, median(samples)


def main():
    historical = {
        record["repository_full_name"]
        for record in load("inventory/repositories.json")["repositories"]
    }
    current = [
        record["repository_full_name"]
        for record in load("inventory/current-census-2026-09-22.json")["repositories"]
    ]
    triage = {
        record["repository_full_name"]
        for record in load("inventory/current-triage-2026-09-22.json")["records"]
    }

    expected = direct_anti_join(current, historical)
    actual = anti_join(current, historical)
    assert actual == expected
    assert set(actual) == triage
    assert len(actual) == 20

    # The real dataset is intentionally small; amplify only the same real
    # values to measure execution shape without inventing repository IDs.
    amplified = current * 10_000

    for _ in range(2):
        direct_anti_join(amplified, historical)
        anti_join(amplified, historical)

    direct_result, direct_ms = median_ms(
        lambda: direct_anti_join(amplified, historical)
    )
    generic_result, generic_ms = median_ms(
        lambda: anti_join(amplified, historical)
    )

    # Confirm that a projection is semantically available, but do not make
    # its cost part of the identity-key benchmark.
    projected_left = [{"name": x} for x in current]
    projected_result = anti_join(
        projected_left,
        historical,
        key=lambda item: item["name"],
    )
    assert [x["name"] for x in projected_result] == expected

    print(json.dumps({
        "experiment": "membership-operation-v0.1",
        "repository": "Loofy147/Portfolio-Repository-Inventory",
        "source": {
            "repositories": "main@37d8a0b2003d528818889ed6da801649c98b7579",
            "current_census": "main@364893c31e645e87bf11cab50567e8e1c01a6aea",
            "current_triage": "main@94ff9a1c01e53842a809a0697efb1ea542f0bd94",
            "validator": "main@fba524c0859f906f02a3440db197951fe8935959",
        },
        "fixture": {
            "historical_repositories": len(historical),
            "current_census": len(current),
            "expected_new_repositories": len(expected),
            "triage_records": len(triage),
            "amplification_factor": 10_000,
            "amplified_membership_checks": len(amplified),
        },
        "correctness": {
            "validator_set_invariant": True,
            "generic_equals_direct": True,
            "generic_key_projection_equals_direct": True,
        },
        "timing_ms_median": {
            "direct_identity_membership": direct_ms,
            "generic_identity_membership": generic_ms,
        },
        "overhead_pct": (generic_ms / direct_ms - 1.0) * 100.0,
        "runtime": {
            "python": platform.python_version(),
            "platform": platform.platform(),
        },
        "decision": {
            "identity_path_within_15pct": generic_ms <= direct_ms * 1.15,
            "promote_to_core": False,
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
