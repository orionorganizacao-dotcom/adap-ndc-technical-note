#!/usr/bin/env python3
"""
Decision Receipt PoC — generate_receipt.py

This script generates a minimal affected-party decision receipt.

It is intentionally simple and deterministic.

Purpose:
- Generate a citizen-held decision receipt at the moment of a simulated automated decision.
- Fix the contestable decision object.
- Demonstrate that explanation_hash fixes the operator's explanation, but does not validate it.

Non-goals:
- This does not prove fairness.
- This does not prove legality.
- This does not prove truth.
- This does not prove that the input was correct.
- This does not prove that the explanation is valid.
- This does not implement production-grade signatures.
- This does not implement RFC 3161 timestamping or public anchoring.
"""

from __future__ import annotations

import argparse
import hashlib
import hmac
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict


POC_VERSION = "0.1"
RECEIPT_TYPE = "adap_decision_receipt"

BASE_DIR = Path(__file__).resolve().parent
RECEIPTS_DIR = BASE_DIR / "receipts"

# Demo-only signing secret.
# In a real implementation, this must be replaced by proper asymmetric signatures,
# such as Ed25519, with key custody and verifier independence explicitly declared.
DEMO_SIGNING_SECRET = b"demo-only-not-production-secret"


def canonical_json(data: Dict[str, Any]) -> str:
    """
    Produce deterministic JSON for hashing.

    This is a simplified canonicalization approach for the PoC.
    Production systems should use a formal canonicalization scheme,
    such as RFC 8785 JSON Canonicalization Scheme, where appropriate.
    """
    return json.dumps(
        data,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )


def sha256_text(value: str) -> str:
    """Return sha256 hash of a string with sha256: prefix."""
    digest = hashlib.sha256(value.encode("utf-8")).hexdigest()
    return f"sha256:{digest}"


def sha256_json(data: Dict[str, Any]) -> str:
    """Return sha256 hash of deterministic JSON."""
    return sha256_text(canonical_json(data))


def demo_signature(message: str) -> str:
    """
    Return demo HMAC signature.

    This is NOT a production signature.

    It is used only so the PoC has a verifiable field.
    A real A-DAP implementation should use asymmetric signatures
    so the affected party and independent verifiers do not need the signing secret.
    """
    digest = hmac.new(
        DEMO_SIGNING_SECRET,
        message.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()
    return f"demo-hmac-sha256:{digest}"


def now_utc_iso() -> str:
    """Return current UTC timestamp in ISO-8601 format."""
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def build_demo_decision(scenario: str) -> Dict[str, Any]:
    """
    Build a simulated decision object.

    Scenario meanings:

    happy_path:
        A normal internally coherent decision.

    perfect_bad_decision:
        A structurally valid receipt for a decision that is intentionally questionable.
        This demonstrates the GIGO boundary:
        the receipt can verify while the merits remain contestable.
    """

    if scenario == "perfect_bad_decision":
        return {
            "decision_id": "D-003",
            "affected_party_ref": "subject:demo-citizen-003",
            "policy_ref": "eligibility-policy-v1",
            "model_ref": "demo-model-v1",
            "input": {
                "age": 42,
                "declared_income": 0,
                "risk_flag": "unverified-high-risk",
                "note": "This input may be false or unfairly generated. The receipt will still verify.",
            },
            "output": {
                "decision": "denied",
                "reason_code": "risk_flag_high",
            },
            "explanation": {
                "text": "The request was denied because the system marked the applicant as high risk.",
                "warning": (
                    "This explanation is fixed by explanation_hash, "
                    "but the hash does not prove the explanation is true, complete, or fair."
                ),
            },
        }

    return {
        "decision_id": "D-001",
        "affected_party_ref": "subject:demo-citizen-001",
        "policy_ref": "eligibility-policy-v1",
        "model_ref": "demo-model-v1",
        "input": {
            "age": 34,
            "declared_income": 1800,
            "risk_flag": "standard",
        },
        "output": {
            "decision": "approved",
            "reason_code": "basic_eligibility_met",
        },
        "explanation": {
            "text": "The request was approved because the declared criteria were met.",
            "warning": (
                "This explanation is fixed by explanation_hash, "
                "but the hash does not prove the explanation is true, complete, or fair."
            ),
        },
    }


def generate_receipt(decision: Dict[str, Any], receipt_label: str) -> Dict[str, Any]:
    """
    Generate a minimal decision receipt.

    The receipt fixes:
    - decision_id
    - issued_at
    - affected_party_ref
    - policy_ref
    - model_ref
    - input_hash
    - output_hash
    - explanation_hash
    - decision_hash
    - demo signature

    Important:
    explanation_hash fixes the explanation given at decision time.
    It does NOT validate the explanation.
    """

    input_hash = sha256_json(decision["input"])
    output_hash = sha256_json(decision["output"])
    explanation_hash = sha256_json(decision["explanation"])

    committed_decision = {
        "decision_id": decision["decision_id"],
        "affected_party_ref": decision["affected_party_ref"],
        "policy_ref": decision["policy_ref"],
        "model_ref": decision["model_ref"],
        "input_hash": input_hash,
        "output_hash": output_hash,
        "explanation_hash": explanation_hash,
    }

    decision_hash = sha256_json(committed_decision)

    receipt_unsigned = {
        "receipt_type": RECEIPT_TYPE,
        "receipt_version": POC_VERSION,
        "receipt_label": receipt_label,
        "issued_at": now_utc_iso(),
        **committed_decision,
        "decision_hash": decision_hash,
        "verification_method": "local-demo-verifier",
        "limits": {
            "does_not_prove_fairness": True,
            "does_not_prove_legality": True,
            "does_not_prove_truth": True,
            "does_not_prove_input_correctness": True,
            "does_not_validate_explanation": True,
            "explanation_hash_semantics": (
                "Fixes the explanation text/object given by the operator. "
                "Does not prove that the explanation is true, complete, or adequate."
            ),
        },
    }

    signature_payload = canonical_json(receipt_unsigned)

    receipt = {
        **receipt_unsigned,
        "signature": demo_signature(signature_payload),
        "signature_warning": (
            "Demo HMAC only. Not production security. "
            "Use Ed25519 or equivalent asymmetric signatures in real implementations."
        ),
    }

    return receipt


def write_json(path: Path, data: Dict[str, Any]) -> None:
    """Write pretty JSON to disk."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True),
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a minimal A-DAP decision receipt for the Decision Receipt PoC."
    )

    parser.add_argument(
        "--scenario",
        choices=["happy_path", "perfect_bad_decision"],
        default="happy_path",
        help="Decision scenario to generate.",
    )

    parser.add_argument(
        "--label",
        default="citizen-held",
        help="Receipt label, e.g. citizen-held or operator-held.",
    )

    parser.add_argument(
        "--output",
        default=None,
        help="Output JSON path. Defaults to receipts/citizen_receipt.json or receipts/perfect_bad_decision_receipt.json.",
    )

    args = parser.parse_args()

    decision = build_demo_decision(args.scenario)
    receipt = generate_receipt(decision, args.label)

    if args.output:
        output_path = Path(args.output)
        if not output_path.is_absolute():
            output_path = BASE_DIR / output_path
    else:
        if args.scenario == "perfect_bad_decision":
            output_path = RECEIPTS_DIR / "perfect_bad_decision_receipt.json"
        else:
            output_path = RECEIPTS_DIR / "citizen_receipt.json"

    write_json(output_path, receipt)

    print("Decision receipt generated.")
    print(f"Scenario: {args.scenario}")
    print(f"Receipt label: {args.label}")
    print(f"Decision ID: {receipt['decision_id']}")
    print(f"Decision hash: {receipt['decision_hash']}")
    print(f"Output: {output_path}")
    print()
    print("Important limit:")
    print("This receipt fixes the contestable decision object.")
    print("It does not prove fairness, legality, truth, input correctness, or explanation validity.")


if __name__ == "__main__":
    main()
