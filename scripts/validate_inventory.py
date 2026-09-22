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


def main() -> int:
    repositories = load_json("inventory/repositories.json")
    triage = load_json("inventory/triage.json")
    assessments = load_json("inventory/assessments.json")
    review_log = load_json("inventory/review-log.json")
    relationships = load_json("inventory/relationships.json")
    legacy_relationships = load_json("inventory/relationships.v0.1-legacy.json")
    clusters = load_json("inventory/cluster-candidates.json")
    deep_review = load_json("inventory/deep_reviews/2026-09-18-machine.json")
    machine_revalidation = load_json("inventory/deep_reviews/2026-09-22-machine-revalidation.json")
    decisions = load_json("records/DECISION_LEDGER_2026-09-22.json")
    census = load_json("records/CENSUS_SNAPSHOTS_2026-09-22.json")
    current_census = load_json("inventory/current-census-2026-09-22.json")
    current_triage = load_json("inventory/current-triage-2026-09-22.json")

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
    validate(deep_review, "schema/repository-review.schema.json", "Machine historical deep review")
    validate(machine_revalidation, "schema/repository-review.schema.json", "Machine revalidation")
    validate(decisions, "schema/decision.schema.json", "decision ledger")
    validate(census, "schema/census-snapshot.schema.json", "census snapshots")
    validate(current_census, "schema/current-census.schema.json", "current census overlay")
    validate(current_triage, "schema/current-triage.schema.json", "current structural triage")

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
    assert_true(current_census["reconciliation"]["exact_set_match"], "current census methods must reconcile exactly")
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
    print("Durable provenance marker gate: PASS")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Portfolio inventory validation: FAIL\n{exc}", file=sys.stderr)
        raise
