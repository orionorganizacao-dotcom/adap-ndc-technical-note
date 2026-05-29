#!/usr/bin/env python3
"""
Decision Receipt PoC — scenarios/non_issuance.py

This adversarial scenario demonstrates non-issuance.

Scenario:
- A simulated automated decision is assumed to have occurred.
- No receipt is issued to the affected person.
- The verifier checks the expected receipt path.
- Because the receipt is missing, the process fails.

This does NOT prove unfairness, illegality, truth, or correctness.

It only demonstrates that the contestability object is missing.
"""

from __future__ import annotations

import sys
from pathlib import Path


SCENARIO_DIR = Path(__file__).resolve().parent
POC_DIR = SCENARIO_DIR.parent
RECEIPTS_DIR = POC_DIR / "receipts"

# Allow imports from the PoC root directory.
sys.path.insert(0, str(POC_DIR))

from verify_receipt import verify_non_issuance  # noqa: E402


def main() -> None:
    print("=" * 72)
    print("Scenario: Non-issuance")
    print("=" * 72)
    print()
    print("This scenario simulates a decision where no receipt was issued.")
    print("The expected outcome is a process failure.")
    print()

    expected_receipt_path = RECEIPTS_DIR / "missing_required_receipt.json"

    # Ensure the scenario remains adversarial and deterministic:
    # if a previous run created this file somehow, remove it.
    if expected_receipt_path.exists():
        expected_receipt_path.unlink()

    print("Expected receipt path:")
    print(f"- {expected_receipt_path}")
    print()

    ok = verify_non_issuance(expected_receipt_path)

    if ok:
        print()
        print("UNEXPECTED RESULT:")
        print("A receipt exists, so non-issuance was not demonstrated.")
        sys.exit(1)

    print()
    print("=" * 72)
    print("EXPECTED RESULT")
    print("=" * 72)
    print("No decision receipt was issued.")
    print()
    print("Meaning:")
    print("- The affected person has no stable decision object to contest.")
    print("- The process failed to provide the required contestability object.")
    print("- The absence of the receipt is itself a procedural failure if issuance")
    print("  is required by law, policy, procurement rule, or system design.")
    print()
    print("Limit:")
    print("- This does not prove the decision was unfair, unlawful, or incorrect.")
    print("- This PoC cannot force a real operator or state institution to issue")
    print("  receipts. That requires institutional adoption or legal obligation.")
    print()
    print("Scenario completed successfully.")

    # Exit 0 because non-issuance detection is the expected result.
    sys.exit(0)


if __name__ == "__main__":
    main()
