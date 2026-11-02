"""Mutation tests for the 2026-09-22 -> 2026-10-31 census transition."""
from __future__ import annotations

import unittest

from scripts.validate_inventory import validate_incremental_triage


def census(*names: str) -> dict:
    return {"repositories": [{"repository_full_name": name} for name in names]}


def triage(*names: str) -> dict:
    return {"records": [{"repository_full_name": name} for name in names]}


class IncrementalCensusTests(unittest.TestCase):
    def setUp(self) -> None:
        self.previous = census("Loofy147/a", "Loofy147/b")
        self.current = census("Loofy147/a", "Loofy147/b", "Loofy147/c", "Loofy147/d")

    def test_exact_new_identity_set_passes(self) -> None:
        self.assertEqual(
            validate_incremental_triage(
                self.previous, self.current, triage("Loofy147/c", "Loofy147/d")
            ),
            {"Loofy147/c", "Loofy147/d"},
        )

    def test_missing_triage_record_is_rejected(self) -> None:
        with self.assertRaisesRegex(AssertionError, "cover exactly"):
            validate_incremental_triage(
                self.previous, self.current, triage("Loofy147/c")
            )

    def test_extra_triage_record_is_rejected(self) -> None:
        with self.assertRaisesRegex(AssertionError, "cover exactly"):
            validate_incremental_triage(
                self.previous,
                self.current,
                triage("Loofy147/c", "Loofy147/d", "Loofy147/x"),
            )

    def test_duplicate_current_identity_is_rejected(self) -> None:
        with self.assertRaisesRegex(AssertionError, "duplicate current"):
            validate_incremental_triage(
                self.previous,
                census("Loofy147/a", "Loofy147/b", "Loofy147/c", "Loofy147/c"),
                triage("Loofy147/c"),
            )

    def test_duplicate_triage_identity_is_rejected(self) -> None:
        with self.assertRaisesRegex(AssertionError, "duplicate triage"):
            validate_incremental_triage(
                self.previous,
                self.current,
                triage("Loofy147/c", "Loofy147/c"),
            )

    def test_removing_historical_identity_is_rejected(self) -> None:
        with self.assertRaisesRegex(AssertionError, "historical census identity missing"):
            validate_incremental_triage(
                self.previous,
                census("Loofy147/a", "Loofy147/c", "Loofy147/d"),
                triage("Loofy147/c", "Loofy147/d"),
            )


if __name__ == "__main__":
    unittest.main()
