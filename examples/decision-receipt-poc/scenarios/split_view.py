#!/usr/bin/env python3
"""
Decision Receipt PoC — scenarios/perfect_bad_decision.py

This adversarial scenario demonstrates a perfect bad decision.

Scenario:
- The operator issues a structurally valid decision receipt.
- The receipt verifies successfully.
- However, the underlying decision scenario is intentionally questionable.
- This demonstrates the GIGO boundary: a valid receipt can preserve a bad decision.

This does NOT prove fairness, legality, truth, or correctness.

It demonstrates that the receipt fixes the contestable object,
but the merits remain contestable.
"""

from __future__ import annotations

import sys
from pathlib import Path


SCENARIO_DIR = Path(__file__).resolve().parent
POC_DIR = SCENARIO_DIR.parent
RECEIPTS_DIR = POC_DIR / "receipts"

# Allow imports from the PoC root directory.
sys.path.insert(0, str(POC_DIR))

from generate_receipt import build_demo_decision, generate_receipt, write_json  # noqa: E402
from verify_receipt import verify_receipt  # noqa: E402


def main() -> None:
    print("=" * 72)
    print("Scenario: Perfect bad decision")
    print("=" * 72)
    print()
    print("This scenario creates a structurally valid receipt for a decision")
    print("that is intentionally questionable at the input/criterion level.")
    print()
    print("Expected outcome:")
    print("- The receipt verifies structurally.")
    print("- The verifier still warns that verification does not prove fairness,")
    print("  legality, truth, input correctness, or explanation validity.")
    print()

    RECEIPTS_DIR.mkdir(parents=True, exist_ok=True)

    decision = build_demo_decision("perfect_bad_decision")

    receipt = generate_receipt(
        decision=decision,
        receipt_label="citizen-held-perfect-bad-decision",
    )

    receipt_path = RECEIPTS_DIR / "perfect_bad_decision_receipt.json"

    write_json(receipt_path, receipt)

    print("Generated receipt:")
    print(f"- {receipt_path}")
    print()

    print("Step 1 — Verify the receipt structurally")
    print()

    ok = verify_receipt(receipt_path)

    if not ok:
        print()
        print("UNEXPECTED RESULT:")
        print("The receipt failed structural verification.")
        print("This scenario requires the receipt to verify successfully.")
        sys.exit(1)

    print()
    print("=" * 72)
    print("EXPECTED RESULT")
    print("=" * 72)
    print("The receipt verified successfully.")
    print()
    print("Meaning:")
    print("- The decision object was fixed.")
    print("- The input_hash, output_hash, explanation_hash, and decision_hash")
    print("  are structurally consistent.")
    print("- The demo signature matches the receipt payload.")
    print()
    print("But this does NOT mean:")
    print("- the input was true;")
    print("- the criterion was legitimate;")
    print("- the policy was lawful;")
    print("- the explanation was adequate;")
    print("- the decision was fair;")
    print("- the affected person should lose the dispute.")
    print()
    print("This is the GIGO boundary.")
    print()
    print("A-DAP and Cryptographic Habeas Data can fix the object of contestation.")
    print("They do not automatically prove the merits.")
    print()
    print("Scenario completed successfully.")

    sys.exit(0)


if __name__ == "__main__":
    main()
