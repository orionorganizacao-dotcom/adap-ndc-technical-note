import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


CASE_DIR = Path(__file__).parent


class SyntheticCaseVerifierLimitationTest(unittest.TestCase):
    def run_case(self, replacement=None):
        with tempfile.TemporaryDirectory() as temporary_directory:
            case_copy = Path(temporary_directory) / "synthetic-case"
            shutil.copytree(CASE_DIR, case_copy)

            if replacement:
                original_name, tampered_name = replacement
                shutil.copyfile(
                    case_copy / "tampered" / tampered_name,
                    case_copy / original_name,
                )

            return subprocess.run(
                [sys.executable, "-B", str(case_copy / "verify_synthetic_case.py")],
                check=False,
                capture_output=True,
                text=True,
            )

    def test_original_fixture_passes(self):
        result = self.run_case()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Original fixture consistency: PASS", result.stdout)
        self.assertIn("VERDICT: PASS", result.stdout)

    def assert_single_file_replacement_fails(self, original_name, tampered_name):
        result = self.run_case((original_name, tampered_name))
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Original fixture consistency: FAIL", result.stdout)
        self.assertIn("VERDICT: FAIL", result.stdout)

    def test_tampered_input_replacement_fails(self):
        self.assert_single_file_replacement_fails(
            "input.json", "input-risk-score-modified.json"
        )

    def test_tampered_output_replacement_fails(self):
        self.assert_single_file_replacement_fails(
            "output.json", "output-decision-modified.json"
        )

    def test_tampered_envelope_replacement_fails(self):
        self.assert_single_file_replacement_fails(
            "envelope.json", "envelope-file-reference-modified.json"
        )

    def test_tampered_custody_replacement_fails(self):
        self.assert_single_file_replacement_fails(
            "custody.json", "custody-file-list-modified.json"
        )

    def test_known_limitation_coordinated_input_output_changes_pass(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            case_copy = Path(temporary_directory) / "synthetic-case"
            shutil.copytree(CASE_DIR, case_copy)

            for filename in ("input.json", "output.json"):
                path = case_copy / filename
                data = json.loads(path.read_text(encoding="utf-8"))
                data["risk_score"] = 0.42
                path.write_text(json.dumps(data), encoding="utf-8")

            result = subprocess.run(
                [sys.executable, "-B", str(case_copy / "verify_synthetic_case.py")],
                check=False,
                capture_output=True,
                text=True,
            )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Original fixture consistency: PASS", result.stdout)
        self.assertIn("VERDICT: PASS", result.stdout)


if __name__ == "__main__":
    unittest.main()
