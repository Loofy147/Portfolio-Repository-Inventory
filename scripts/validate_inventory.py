#!/usr/bin/env python3
"""Validate Portfolio-Repository-Inventory machine-readable contracts and invariants."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]


def load_json(relative: str) -> object:
    with (ROOT / relative).open("r", encoding="utf-8") as fh:
        return json.load(fh)


def validate(instance: object, schema_path: str, label: str) -> None:
    schema = load_json(schema_path)
    Draft202012Validator.check_schema(schema)
    errors = sorted(
        Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(instance),
        key=lambda e: list(e.path),
    )
    if errors:
        details = "\n".join(
            f"- {label}: {'/'.join(map(str, error.path))}: {error.message}"
            for error in errors[:20]
        )
        raise AssertionError(details)


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validate_incremental_triage(previous_census: dict, current_census: dict, triage: dict) -> set[str]:
    """Require triage to cover exactly the identities added by an immutable census."""
    previous_names = [record["repository_full_name"] for record in previous_census["repositories"]]
    current_names = [record["repository_full_name"] for record in current_census["repositories"]]
    triage_names = [record["repository_full_name"] for record in triage["records"]]

    assert_true(len(previous_names) == len(set(previous_names)), "duplicate previous census identity")
    assert_true(len(current_names) == len(set(current_names)), "duplicate current census identity")
    assert_true(
        set(previous_names).issubset(set(current_names)),
        "historical census identity missing from current census",
    )
    assert_true(len(triage_names) == len(set(triage_names)), "duplicate triage identity")

    expected = set(current_names) - set(previous_names)
    assert_true(
        set(triage_names) == expected,
        "current triage must cover exactly the newly observed repository identities",
    )
    assert_true(len(triage_names) == len(expected), "triage count mismatch")
    return expected


def main() -> int:
    repositories = load_json("inventory/repositories.json")
    triage = load_json("inventory/triage.json")
    assessments = load_json("inventory/assessments.json")
    review_log = load_json("inventory/review-log.json")
    relationships = load_json("inventory/relationships.json")
    legacy_relationships = load_json("inventory/relationships.v0.1-legacy.json")
    clusters = load_json("inventory/cluster-candidates.json")
    deep_review_dir = ROOT / "inventory/deep_reviews"
    deep_review_files = sorted(deep_review_dir.glob("*.json"))
    current_deep_review_files = []
    legacy_deep_review_files = []
    for path in deep_review_files:
        payload = load_json(str(path.relative_to(ROOT)))
        if isinstance(payload, dict) and payload.get("schema_version") == "0.2.0":
            current_deep_review_files.append(path)
        else:
            legacy_deep_review_files.append(path)
    decisions = load_json("records/DECISION_LEDGER_2026-09-22.json")
    census = load_json("records/CENSUS_SNAPSHOTS_2026-09-22.json")
    current_census = load_json("inventory/current-census-2026-09-22.json")
    current_triage = load_json("inventory/current-triage-2026-09-22.json")
    current_census_1031 = load_json("inventory/current-census-2026-10-31.json")
    current_triage_1031 = load_json("inventory/current-triage-2026-10-31.json")

    repository_schema = load_json("schema/repository.schema.json")
    Draft202012Validator.check_schema(repository_schema)
    for index, record in enumerate(repositories["repositories"]):
        validate(record, "schema/repository.schema.json", f"repositories[{index}]")
    triage_schema = load_json("schema/triage.schema.json")
    Draft202012Validator.check_schema(triage_schema)
    for index, record in enumerate(triage["records"]):
        validate(record, "schema/triage.schema.json", f"triage[{index}]")

    assessment_schema = load_json("schema/assessment.schema.json")
    Draft202012Validator.check_schema(assessment_schema)
    for index, record in enumerate(assessments["assessments"]):
        validate(record, "schema/assessment.schema.json", f"assessments[{index}]")

    validate(review_log, "schema/review-log.schema.json", "review-log")

    validate(relationships, "schema/relationship-inventory.v0.2.schema.json", "relationships v0.2")
    relationship_schema = load_json("schema/relationship.schema.json")
    Draft202012Validator.check_schema(relationship_schema)
    for index, record in enumerate(legacy_relationships["relationships"]):
        validate(record, "schema/relationship.schema.json", f"legacy relationships[{index}]")
    validate(clusters, "schema/cluster.schema.json", "cluster candidates")
    assert_true(bool(current_deep_review_files), "at least one v0.2 deep-review record is required")
    for path in current_deep_review_files:
        validate(
            load_json(str(path.relative_to(ROOT))),
            "schema/repository-review.schema.json",
            f"deep review {path.name}",
        )
    # Legacy batch review artifacts remain historical records and are not silently
    # coerced into the v0.2 repository-review schema.
    validate(decisions, "schema/decision.schema.json", "decision ledger")
    validate(census, "schema/census-snapshot.schema.json", "census snapshots")
    validate(current_census, "schema/current-census.schema.json", "2026-09-22 current census overlay")
    validate(current_triage, "schema/current-triage.schema.json", "2026-09-22 current structural triage")
    validate(current_census_1031, "schema/current-census.schema.json", "2026-10-31 current census overlay")
    validate(current_triage_1031, "schema/current-triage.schema.json", "2026-10-31 current structural triage")

    repo_records = repositories["repositories"]
    repo_names = [record["repository_full_name"] for record in repo_records]
    assert_true(len(repo_names) == len(set(repo_names)), "duplicate repository full_name detected")
    repo_set = set(repo_names)

    for cluster in clusters["clusters"]:
        missing = sorted(set(cluster["repositories"]) - repo_set)
        assert_true(
            not missing,
            f"cluster {cluster['cluster_id']} references missing repositories: {missing}",
        )

    for relation in relationships["relationships"]:
        assert_true(
            relation["source"] in repo_set,
            f"relationship source missing: {relation['source']}",
        )
        assert_true(
            relation["target"] in repo_set,
            f"relationship target missing: {relation['target']}",
        )

    review_names = [record["repository"] for record in review_log["records"]]
    missing_reviews = sorted(set(review_names) - repo_set)
    assert_true(not missing_reviews, f"review-log references missing repositories: {missing_reviews}")

    active_target = [
        decision
        for decision in decisions["decisions"]
        if decision["decision_type"] == "current_target" and decision["status"] == "active"
    ]
    assert_true(len(active_target) == 1, "exactly one active current_target decision is required")

    active_working_sets = [
        decision
        for decision in decisions["decisions"]
        if decision["decision_type"] == "core_working_set" and decision["status"] == "active"
    ]
    assert_true(
        len(active_working_sets) == 1,
        "exactly one active core_working_set decision is required",
    )

    target = active_target[0]["subject"]
    current_census_names = {record["repository_full_name"] for record in current_census["repositories"]}
    historical_names = set(repo_names)
    triage_names = {record["repository_full_name"] for record in current_triage["records"]}
    new_triage_expected = current_census_names - historical_names
    assert_true(triage_names == new_triage_expected, "current triage must cover exactly the newly observed repository identities")
    assert_true(historical_names.issubset(current_census_names), "current census must contain every historical inventory identity")
    assert_true(current_census["search_method"]["total"] == len(current_census_names), "current census search total must equal unique repository records")
    assert_true(current_census["installed_search_method"]["total"] == len(current_census_names), "installed search total must equal unique repository records")
    assert_true(current_census["reconciliation"]["exact_set_match"], "2026-09-22 current census methods must reconcile exactly")

    # The 2026-10-31 census is a new immutable observation, not a replacement
    # for the 2026-09-22 baseline. Its triage must cover exactly the 54 added IDs.
    current_census_1031_names = {
        record["repository_full_name"] for record in current_census_1031["repositories"]
    }
    new_triage_expected = validate_incremental_triage(
        current_census, current_census_1031, current_triage_1031
    )
    assert_true(len(current_census["repositories"]) == 339, "2026-09-22 census must retain 339 identities")
    assert_true(len(current_census_1031_names) == 393, "2026-10-31 census must contain 393 identities")
    assert_true(len(new_triage_expected) == 54, "2026-10-31 census must add exactly 54 identities")
    assert_true(
        current_census_1031["search_method"]["total"] == 393,
        "2026-10-31 GitHub search total must equal 393",
    )
    assert_true(
        current_census_1031["installed_search_method"]["total"] == 393,
        "2026-10-31 installed search total must equal 393",
    )
    assert_true(
        current_census_1031["reconciliation"]["exact_set_match"],
        "2026-10-31 census methods must reconcile exactly",
    )
    assert_true(
        current_census_1031["reconciliation"]["newly_observed_count"] == 54,
        "2026-10-31 census reconciliation must record 54 new identities",
    )
    census_1031_by_name = {
        record["repository_full_name"]: record
        for record in current_census_1031["repositories"]
    }
    for record in current_triage_1031["records"]:
        census_record = census_1031_by_name[record["repository_full_name"]]
        assert_true(
            record["ref"] == census_record["identity"]["default_branch"],
            f"default branch ref mismatch for {record['repository_full_name']}",
        )
        if record["commit"] is None:
            assert_true(
                census_record["identity"]["size_kb"] == 0
                and record["triage"]["maturity_signal"] == "empty"
                and record["observations"]["tests"] == "absent_verified"
                and record["observations"]["ci"] == "absent_verified",
                f"missing commit is only permitted for an evidenced empty repository: {record['repository_full_name']}",
            )
        if record["provenance"]["status"] == "external_fork":
            assert_true(
                record["provenance"]["fork"] is True,
                f"external fork status requires fork=true: {record['repository_full_name']}",
            )
    core_set = set(active_working_sets[0]["subject"])
    assessed_repos = {record["repository_full_name"] for record in assessments["assessments"]}
    assert_true(assessed_repos.issubset(core_set), "assessments must be limited to current core working set")
    assert_true(len(assessed_repos) == len(assessments["assessments"]), "duplicate assessment repository detected")
    working_set = set(active_working_sets[0]["subject"])
    assert_true(target in working_set, "current target must be a member of the active core working set")

    marker = "\ue080filecite\ue080"
    bad_markers: list[str] = []
    for base in ("catalog", "inventory", "records", "reports", "docs", "schema"):
        directory = ROOT / base
        if not directory.exists():
            continue
        for path in directory.rglob("*"):
            if (
                not path.is_file()
                or path.suffix.lower() not in {".md", ".json", ".yaml", ".yml", ".py", ".txt"}
            ):
                continue
            content = path.read_text(encoding="utf-8", errors="ignore")
            if marker in content:
                bad_markers.append(str(path.relative_to(ROOT)))

    assert_true(not bad_markers, f"conversation-scoped citation markers remain: {bad_markers}")

    print("Portfolio inventory validation: PASS")
    print(f"Repositories: {len(repo_records)}")
    print(f"Review records: {len(review_log['records'])}")
    print(f"Relationships (v0.2): {len(relationships['relationships'])}")
    print(f"Clusters: {len(clusters['clusters'])}")
    print("Current target decision: PASS")
    print("2026-10-31 census transition: PASS (393 total; 339 retained; 54 triaged)")
    print("Durable provenance marker gate: PASS")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Portfolio inventory validation: FAIL\n{exc}", file=sys.stderr)
        raise
