import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


CASE_DIR = Path(__file__).parent


class SyntheticCaseVerifierLimitationTest(unittest.TestCase):
    def test_coordinated_input_output_changes_are_not_authenticated(self):
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
        self.assertIn("Original case: PASS", result.stdout)
        self.assertIn("VERDICT: PASS", result.stdout)


if __name__ == "__main__":
    unittest.main()
