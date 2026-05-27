import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
TAMPERED_DIR = BASE_DIR / "tampered"


def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def fail(message):
    return {
        "status": "fail",
        "message": message
    }


def pass_result(message):
    return {
        "status": "pass",
        "message": message
    }


def verify_original_case():
    input_data = load_json(BASE_DIR / "input.json")
    output_data = load_json(BASE_DIR / "output.json")
    envelope = load_json(BASE_DIR / "envelope.json")
    custody = load_json(BASE_DIR / "custody.json")
    expected = load_json(BASE_DIR / "expected-verdict.json")

    risk_score = input_data.get("risk_score")
    threshold = input_data.get("threshold")
    decision = output_data.get("decision")

    if risk_score is None or threshold is None:
        return fail("Missing risk_score or threshold in input.json")

    if risk_score < threshold and decision != "approved":
        return fail("Decision should be approved because risk_score is below threshold")

    if risk_score >= threshold and decision != "rejected":
        return fail("Decision should be rejected because risk_score is not below threshold")

    if envelope.get("input_file") != "input.json":
        return fail("Envelope input_file does not match input.json")

    if envelope.get("output_file") != "output.json":
        return fail("Envelope output_file does not match output.json")

    required_files = {
        "input.json",
        "output.json",
        "envelope.json",
        "custody.json"
    }

    custody_files = set(custody.get("files_under_custody", []))

    if not required_files.issubset(custody_files):
        return fail("Custody file list does not include the full required evidence set")

    if expected.get("expected_result") != "pass":
        return fail("Expected verdict does not declare pass")

    return pass_result("Original synthetic case verified successfully")


def verify_tampered_cases():
    results = []

    tampered_input = load_json(TAMPERED_DIR / "input-risk-score-modified.json")
    if tampered_input.get("risk_score", 0) >= tampered_input.get("threshold", 1):
        results.append(pass_result("Tampered input risk score detected"))
    else:
        results.append(fail("Tampered input risk score was not detected"))

    tampered_output = load_json(TAMPERED_DIR / "output-decision-modified.json")
    if tampered_output.get("risk_score") < tampered_output.get("threshold") and tampered_output.get("decision") != "approved":
        results.append(pass_result("Tampered output decision detected"))
    else:
        results.append(fail("Tampered output decision was not detected"))

    tampered_envelope = load_json(TAMPERED_DIR / "envelope-file-reference-modified.json")
    if tampered_envelope.get("input_file") != "input.json":
        results.append(pass_result("Tampered envelope file reference detected"))
    else:
        results.append(fail("Tampered envelope file reference was not detected"))

    tampered_custody = load_json(TAMPERED_DIR / "custody-file-list-modified.json")
    custody_files = set(tampered_custody.get("files_under_custody", []))
    if "envelope.json" not in custody_files:
        results.append(pass_result("Tampered custody file list detected"))
    else:
        results.append(fail("Tampered custody file list was not detected"))

    return results


def main():
    print("A-DAP Synthetic Challenge Verifier")
    print("---------------------------------")

    original_result = verify_original_case()
    print(f"Original case: {original_result['status'].upper()} — {original_result['message']}")

    tampered_results = verify_tampered_cases()

    for index, result in enumerate(tampered_results, start=1):
        print(f"Tampered case {index}: {result['status'].upper()} — {result['message']}")

    all_passed = original_result["status"] == "pass" and all(
        result["status"] == "pass" for result in tampered_results
    )

    print("---------------------------------")

    if all_passed:
        print("VERDICT: PASS")
        print("The original case was reconstructed and all documented tampering examples were detected.")
    else:
        print("VERDICT: FAIL")
        print("At least one verification check failed.")


if __name__ == "__main__":
    main()
