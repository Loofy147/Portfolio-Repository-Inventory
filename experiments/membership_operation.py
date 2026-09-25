"""Second-system integration probe for Membership Primitive.

Real workload:
    current census repositories - historical inventory repositories

This is the exact invariant already enforced by scripts/validate_inventory.py:
    new_triage_expected = current_census_names - historical_names
    triage_names == new_triage_expected

No production validator is modified by this experiment.

Candidate operation:
    anti_join(left, membership, key=None)

The identity path intentionally avoids a per-item projection callback.
Projection is explicit when the real key differs from the item itself.
"""
from __future__ import annotations

import json
import platform
import time
from pathlib import Path
from statistics import median

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
    samples.sort()
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

    projected_left = [{"name": x} for x in current]
    projected_result = anti_join(
        projected_left,
        historical,
        key=lambda item: item["name"],
    )
    assert [x["name"] for x in projected_result] == expected

    amplified = current * 10_000

    for _ in range(3):
        direct_anti_join(amplified, historical)
        anti_join(amplified, historical)

    direct_result, direct_ms = median_ms(
        lambda: direct_anti_join(amplified, historical)
    )
    generic_result, generic_ms = median_ms(
        lambda: anti_join(amplified, historical)
    )

    assert generic_result == direct_result

    overhead_pct = (generic_ms / direct_ms - 1.0) * 100.0

    print(json.dumps({
        "experiment": "membership-operation-v0.1",
        "repository": "Loofy147/Portfolio-Repository-Inventory",
        "provenance": {
            "base_commit": "fba524c0859f906f02a3440db197951fe8935959",
            "repositories_blob_sha": "37d8a0b2003d528818889ed6da801649c98b7579",
            "current_census_blob_sha": "364893c31e645e87bf11cab50567e8e1c01a6aea",
            "current_triage_blob_sha": "94ff9a1c01e53842a809a0697efb1ea542f0bd94",
        },
        "dataset": {
            "historical_repositories": len(historical),
            "current_census": len(current),
            "triage_records": len(triage),
            "expected_new_repositories": len(expected),
            "amplification_factor": 10_000,
            "amplified_checks": len(amplified),
        },
        "correctness": {
            "census_minus_historical_equals_triage": True,
            "generic_identity_equals_direct": True,
            "projection_path_equals_direct": True,
            "orphan_count": len(expected),
        },
        "timing_ms_median": {
            "direct_identity": direct_ms,
            "generic_identity": generic_ms,
        },
        "overhead_pct": overhead_pct,
        "runtime": {
            "python": platform.python_version(),
            "repeats": 7,
            "warmup_rounds": 3,
        },
        "promotion_gate": {
            "identity_path_max_overhead_pct": 15.0,
            "passed": overhead_pct <= 15.0,
            "promote_to_core": False,
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
