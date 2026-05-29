#!/usr/bin/env python3
"""
Decision Receipt PoC — run_all_scenarios.py

Run all adversarial scenarios for the Decision Receipt PoC.

Scenarios:
1. Non-issuance
2. Split-view receipt
3. Perfect bad decision

This runner is intentionally simple.

It does not prove fairness, legality, truth, input correctness, or institutional legitimacy.

It only executes the PoC scenarios that demonstrate:
- missing receipt as process failure;
- split-view conflict detection;
- structurally valid receipt for a bad decision.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import List, Tuple


POC_DIR = Path(__file__).resolve().parent
SCENARIOS_DIR = POC_DIR / "scenarios"


SCENARIOS = [
    ("non-issuance", SCENARIOS_DIR / "non_issuance.py"),
    ("split-view", SCENARIOS_DIR / "split_view.py"),
    ("perfect-bad-decision", SCENARIOS_DIR / "perfect_bad_decision.py"),
]


def run_scenario(name: str, script_path: Path) -> Tuple[str, int]:
    """
    Run a single scenario script.

    Returns:
    - scenario name
    - process return code
    """
    print("=" * 80)
    print(f"Running scenario: {name}")
    print(f"Script: {script_path}")
    print("=" * 80)
    print()

    if not script_path.exists():
        print(f"FAIL: scenario script not found: {script_path}")
        print()
        return name, 1

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=str(POC_DIR),
        text=True,
    )

    print()
    print("=" * 80)
    print(f"Scenario finished: {name}")
    print(f"Exit code: {result.returncode}")
    print("=" * 80)
    print()

    return name, result.returncode


def main() -> None:
    print("=" * 80)
    print("Decision Receipt PoC — Run All Scenarios")
    print("=" * 80)
    print()
    print("This runner executes the three adversarial scenarios.")
    print()
    print("Important limits:")
    print("- This PoC does not prove fairness.")
    print("- This PoC does not prove legality.")
    print("- This PoC does not prove truth.")
    print("- This PoC does not prove input correctness.")
    print("- This PoC fixes and tests the contestable decision object only.")
    print()

    results: List[Tuple[str, int]] = []

    for name, script_path in SCENARIOS:
        results.append(run_scenario(name, script_path))

    print("=" * 80)
    print("Summary")
    print("=" * 80)

    failed = []

    for name, code in results:
        status = "PASS" if code == 0 else "FAIL"
        print(f"{status}: {name}")
        if code != 0:
            failed.append(name)

    print()

    if failed:
        print("Some scenarios failed:")
        for name in failed:
            print(f"- {name}")
        print()
        print("The PoC is not passing all adversarial scenarios.")
        sys.exit(1)

    print("All scenarios completed successfully.")
    print()
    print("Interpretation:")
    print("- Non-issuance is represented as a process failure.")
    print("- Split-view reconstruction is detected when receipts diverge.")
    print("- A structurally valid receipt can still represent a bad decision.")
    print()
    print("Final limit:")
    print("The receipt fixes the object of contestation.")
    print("It does not decide the merits.")

    sys.exit(0)


if __name__ == "__main__":
    main()
