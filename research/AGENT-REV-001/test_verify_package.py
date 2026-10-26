import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from verify_package import SCHEMA_PATH, _strict_object, verify_package


CLAIM_IDS = ["C1", "C2", "C3", "C4", "C5", "P1"]
TIMES = {
    "deny": "2026-10-26T10:00:00Z",
    "request": "2026-10-26T10:00:01Z",
    "response": "2026-10-26T10:00:02Z",
    "session": "2026-10-26T10:00:03Z",
}


def empty_claim(claim_id):
    return {
        "claim_id": claim_id,
        "classification": "NOT_EVALUATED",
        "basis": "NONE",
        "supporting_artifact_refs": [],
        "defeating_artifact_refs": [],
        "candidate_falsifiers": [
            "Synthetic fixture only: identity, timing, permission, allowed-exception, "
            "or collection evidence could defeat this candidate."
        ],
        "identity_pseudonym": None,
        "events": [],
        "required_order": [],
        "uncertainty": "Synthetic unexecuted fixture; no observations."
    }


def empty_contract(claim_id):
    return {
        "claim_id": claim_id,
        "claim_type": "VENDOR_CONFORMANCE" if claim_id != "P1" else "CUSTOMER_POLICY_CONFORMANCE",
        "status": "UNFILLED",
        "source_url": None,
        "source_version": None,
        "source_artifact_ref": None,
        "enforcement_point": None,
        "exceptions": [],
        "eligibility": None,
        "observation_window_start": None,
        "observation_window_end": None,
        "maximum_wait_seconds": None,
        "repeatability_criterion": None,
        "inconclusive_conditions": [
            "Synthetic fixture only; parameters and observations are unfilled."
        ]
    }


def blocked_fixture():
    return {
        "protocol_id": "AGENT-REV-001",
        "protocol_version": "v0.2",
        "schema_version": "v0.3",
        "validation_status": "NOT VALIDATED",
        "protocol_readiness": "PILOT_BLOCKED",
        "run_state": "NOT_EXECUTED",
        "run_compliance": "NOT_APPLICABLE_UNEXECUTED",
        "run_id": "synthetic-blocked-run",
        "arm": "C0",
        "fixture_label": "SYNTHETIC TEST FIXTURE",
        "authorization": {
            "status": "PENDING",
            "scope": "Synthetic test fixture only; no owner permission is asserted.",
            "approval_record": None,
            "approved_by": None
        },
        "gates": {
            f"gate_{index}": {"status": "PENDING", "evidence_ref": None}
            for index in range(5)
        },
        "configuration": {"version": None, "artifact_ref": None, "sha256": None},
        "context": {
            "project_pseudonym": "SYNTHETIC-PROJECT",
            "workspace_pseudonym": "SYNTHETIC-WORKSPACE",
            "resource_pseudonym": None,
            "route": None,
            "permission": None,
            "api_version": None,
            "software_versions": {"fixture": "synthetic"},
            "model_environment": "SYNTHETIC ONLY; NOT A LIVE ENVIRONMENT",
            "thread_id": None,
            "session_id": None,
            "workflow_id": None,
            "deployment_id": None
        },
        "identity_map": {
            "creator_challenge_identity": "SYNTHETIC-A",
            "observer_recovery_identity": "SYNTHETIC-B",
            "distinct_identities": True,
            "observer_controls_available_after_creator_revocation": False
        },
        "counts": {
            "attempted": 0,
            "completed": 0,
            "excluded": 0,
            "deviations": 0,
            "request_attempts": 0,
            "destination_effects": 0
        },
        "collection_controls": {
            "source_to_field_mapping": [],
            "ingestion_bound_seconds": None,
            "clock_uncertainty_ms": None,
            "retention": "UNFILLED",
            "records_controller": "UNFILLED",
            "alter_or_delete_authority": "UNFILLED"
        },
        "claim_contracts": [empty_contract(claim_id) for claim_id in CLAIM_IDS],
        "claims": [empty_claim(claim_id) for claim_id in CLAIM_IDS],
        "artifacts": [],
        "limitations": ["Synthetic test fixture; no underlying evidence."]
    }


def mixed_fixture(root):
    package = blocked_fixture()
    package.update({
        "run_state": "ATTEMPTED",
        "run_compliance": "DEVIATION",
        "run_id": "synthetic-mixed-run"
    })
    package["context"].update({
        "resource_pseudonym": "SYNTHETIC-RESOURCE",
        "route": "synthetic-route",
        "permission": "synthetic-permission",
        "api_version": "synthetic-api-v1",
        "thread_id": "SYNTHETIC-THREAD",
        "session_id": "SYNTHETIC-SESSION"
    })
    package["context"]["software_versions"] = {"fixture-tool": "synthetic-v1"}
    package["configuration"] = {"version": "synthetic-v1", "artifact_ref": "config", "sha256": None}
    package["counts"] = {
        "attempted": 1,
        "completed": 0,
        "excluded": 0,
        "deviations": 1,
        "request_attempts": 1,
        "destination_effects": 0
    }
    package["collection_controls"] = {
        "source_to_field_mapping": [{
            "source": "synthetic-gateway",
            "source_field": "decision",
            "manifest_field": "C1.gateway_decision"
        }],
        "ingestion_bound_seconds": 0,
        "clock_uncertainty_ms": 0,
        "retention": "SYNTHETIC FIXTURE ONLY",
        "records_controller": "SYNTHETIC FIXTURE ONLY",
        "alter_or_delete_authority": "SYNTHETIC FIXTURE ONLY"
    }
    package["deviation"] = {
        "actual_execution": True,
        "description": "Synthetic attempted/deviation record only.",
        "intervention": "Synthetic stop marker; no live system.",
        "intervention_time_utc": "2026-10-26T10:00:04Z",
        "compliant_result": False,
        "gates_marked_pass_by_deviation": False
    }

    def add_artifact(artifact_id, role, text):
        relative_path = Path("artifacts") / f"{artifact_id}.txt"
        target = root / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(f"SYNTHETIC TEST FIXTURE ONLY: {text}\n", encoding="utf-8")
        digest = hashlib.sha256(target.read_bytes()).hexdigest()
        package["artifacts"].append({
            "artifact_id": artifact_id,
            "path": relative_path.as_posix(),
            "sha256": digest,
            "role": role,
            "source_fields": ["synthetic-field"],
            "custody": {
                "collector_pseudonym": "SYNTHETIC-COLLECTOR",
                "collected_at_utc": "2026-10-26T10:00:04Z",
                "can_alter_or_delete": True,
                "retention": "SYNTHETIC FIXTURE ONLY"
            },
            "review": {
                "reviewer_pseudonym": None,
                "independence_status": "NOT_ASSESSED",
                "basis": "A fixture label is not evidence of independence."
            }
        })
        return digest

    config_hash = add_artifact("config", "CONFIGURATION", "synthetic configuration")
    package["configuration"]["sha256"] = config_hash
    source_c1 = add_artifact("source-c1", "SOURCE_PROMISE", "synthetic source contract")
    source_c2 = add_artifact("source-c2", "SOURCE_PROMISE", "synthetic source contract")
    add_artifact("iam-denial", "CLOUD_AUDIT", "synthetic effective-denial event")
    add_artifact("gateway-response", "GATEWAY_RESPONSE", "synthetic HTTP denial")
    add_artifact("session-event", "AGENT_EVENT", "synthetic unresolved session event")

    frozen_fields = {
        "status": "FROZEN",
        "source_url": "https://example.invalid/synthetic-source",
        "source_version": "synthetic-document-version",
        "enforcement_point": "synthetic gateway",
        "exceptions": ["Synthetic fixture exception; not a real vendor claim."],
        "eligibility": "synthetic principal A and protected operation",
        "observation_window_start": "2026-10-26T10:00:00Z",
        "observation_window_end": "2026-10-26T10:01:00Z",
        "maximum_wait_seconds": 60,
        "repeatability_criterion": "Synthetic shape only; not a calibrated threshold."
    }
    for claim_id, source_ref in (("C1", "source-c1"), ("C2", "source-c2")):
        contract = package["claim_contracts"][CLAIM_IDS.index(claim_id)]
        contract.update(frozen_fields)
        contract["source_artifact_ref"] = source_ref

    c1 = package["claims"][CLAIM_IDS.index("C1")]
    c1.update({
        "classification": "CONTRADICTION_CANDIDATE",
        "basis": "GATEWAY_DECISION",
        "supporting_artifact_refs": ["source-c1", "iam-denial", "gateway-response"],
        "identity_pseudonym": "SYNTHETIC-A",
        "events": [
            {
                "event_id": "effective-denial",
                "kind": "iam-denial",
                "earliest_utc": TIMES["deny"],
                "latest_utc": TIMES["deny"],
                "artifact_refs": ["iam-denial"]
            },
            {
                "event_id": "fresh-request",
                "kind": "fresh-request",
                "earliest_utc": TIMES["request"],
                "latest_utc": TIMES["request"],
                "artifact_refs": ["gateway-response"]
            },
            {
                "event_id": "gateway-denial",
                "kind": "gateway-denial",
                "earliest_utc": TIMES["response"],
                "latest_utc": TIMES["response"],
                "artifact_refs": ["gateway-response"]
            }
        ],
        "required_order": [
            ["effective-denial", "fresh-request"],
            ["fresh-request", "gateway-denial"]
        ],
        "uncertainty": "Synthetic candidate event; no real observation or reproduction."
    })
    c2 = package["claims"][CLAIM_IDS.index("C2")]
    c2.update({
        "classification": "INCONCLUSIVE",
        "basis": "SESSION_EFFECT",
        "supporting_artifact_refs": ["session-event"],
        "identity_pseudonym": "SYNTHETIC-A",
        "events": [{
            "event_id": "session-observation",
            "kind": "session-event",
            "earliest_utc": TIMES["session"],
            "latest_utc": TIMES["session"],
            "artifact_refs": ["session-event"]
        }],
        "uncertainty": "Synthetic event cannot establish continuation or destination effect."
    })
    return package


class VerifyPackageTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        self.root = Path(self.tempdir.name)

    def write_package(self, package, name="manifest.json"):
        path = self.root / name
        path.write_text(json.dumps(package, indent=2) + "\n", encoding="utf-8")
        return path

    def errors_for(self, package):
        return verify_package(self.write_package(package))

    def test_strict_json_and_draft_2020_12_schema(self):
        with SCHEMA_PATH.open(encoding="utf-8") as stream:
            schema = json.load(stream, object_pairs_hook=_strict_object)
        Draft202012Validator.check_schema(schema)
        with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
            json.loads('{"x":1,"x":2}', object_pairs_hook=_strict_object)

    def test_amendment_replacement_hashes_match_current_deliverables(self):
        package_dir = SCHEMA_PATH.parent
        amendment = (package_dir / "amendment-2026-10-26-v0.2.md").read_text(
            encoding="utf-8"
        )
        for filename in (
            "protocol.md",
            "test-matrix.md",
            "reviewer-checklist.md",
            "evidence-manifest.schema.json",
        ):
            digest = hashlib.sha256((package_dir / filename).read_bytes()).hexdigest()
            self.assertIn(f"| `{filename}` |", amendment)
            self.assertIn(digest, amendment)
        self.assertIn(
            "f81d60a09cd135caa693f21b8756fc3c987e84ee1cc80a7b8c140a65ca6556c0",
            amendment,
        )

    def test_valid_blocked_unexecuted_synthetic_fixture(self):
        fixture = blocked_fixture()
        self.assertEqual(fixture["fixture_label"], "SYNTHETIC TEST FIXTURE")
        self.assertEqual(verify_package(self.write_package(fixture)), [])

    def test_valid_mixed_per_claim_synthetic_fixture(self):
        fixture = mixed_fixture(self.root)
        self.assertEqual(fixture["fixture_label"], "SYNTHETIC TEST FIXTURE")
        self.assertEqual(fixture["claims"][0]["classification"], "CONTRADICTION_CANDIDATE")
        self.assertEqual(fixture["claims"][1]["classification"], "INCONCLUSIVE")
        self.assertEqual(fixture["protocol_readiness"], "PILOT_BLOCKED")
        self.assertEqual(fixture["authorization"]["status"], "PENDING")
        self.assertTrue(all(
            gate["status"] == "PENDING" for gate in fixture["gates"].values()
        ))
        self.assertEqual(fixture["counts"]["destination_effects"], 0)
        self.assertEqual(verify_package(self.write_package(fixture)), [])

    def test_authorized_readiness_rejects_pending_approval_or_gate(self):
        fixture = blocked_fixture()
        fixture["protocol_readiness"] = "PILOT_AUTHORIZED"
        self.assertTrue(self.errors_for(fixture))

        fixture = blocked_fixture()
        fixture["protocol_readiness"] = "PILOT_AUTHORIZED"
        fixture["authorization"].update({
            "status": "APPROVED",
            "approval_record": "SYNTHETIC INVALID-READINESS CASE",
            "approved_by": "SYNTHETIC INVALID-READINESS CASE"
        })
        self.assertTrue(self.errors_for(fixture))

    def test_positive_finding_requires_evidence_contract_identity_and_timing(self):
        fixture = mixed_fixture(self.root)
        fixture["claims"][0]["supporting_artifact_refs"] = []
        self.assertTrue(any("required evidence roles" in error for error in self.errors_for(fixture)))

        fixture = mixed_fixture(self.root)
        fixture["claims"][0]["basis"] = "NONE"
        self.assertTrue(any("supported evidence basis" in error for error in self.errors_for(fixture)))

        fixture = mixed_fixture(self.root)
        fixture["claims"][0]["identity_pseudonym"] = None
        errors = self.errors_for(fixture)
        self.assertTrue(any("identity pseudonym" in error for error in errors))

        fixture = mixed_fixture(self.root)
        fixture["claims"][0]["events"] = []
        errors = self.errors_for(fixture)
        self.assertTrue(any("timed evidence events" in error for error in errors))

        fixture = mixed_fixture(self.root)
        fixture["claim_contracts"][0]["maximum_wait_seconds"] = None
        errors = self.errors_for(fixture)
        self.assertTrue(any("unfilled parameters" in error for error in errors))

    def test_policy_positive_requires_claim_specific_policy_and_sink_evidence(self):
        fixture = mixed_fixture(self.root)
        policy = fixture["claims"][CLAIM_IDS.index("P1")]
        policy.update({
            "classification": "POLICY_VIOLATION_TESTED",
            "basis": "POLICY_EFFECT",
            "identity_pseudonym": "SYNTHETIC-A",
            "events": [{
                "event_id": "synthetic-policy-effect",
                "kind": "destination-effect",
                "earliest_utc": TIMES["response"],
                "latest_utc": TIMES["response"],
                "artifact_refs": []
            }]
        })
        errors = self.errors_for(fixture)
        self.assertTrue(any("frozen claim contract" in error for error in errors))
        self.assertTrue(any("CUSTOMER_POLICY" in error for error in errors))
        self.assertTrue(any("DESTINATION_EFFECT" in error for error in errors))

    def test_missing_and_mismatched_artifact_references_or_hashes_rejected(self):
        fixture = mixed_fixture(self.root)
        fixture["claims"][0]["supporting_artifact_refs"][0] = "missing-artifact"
        self.assertTrue(any("unresolved artifact reference" in error for error in self.errors_for(fixture)))

        fixture = mixed_fixture(self.root)
        fixture["artifacts"][0]["sha256"] = "0" * 64
        self.assertTrue(any("SHA-256 mismatch" in error for error in self.errors_for(fixture)))

    def test_duplicate_paths_and_uncertain_overlapping_intervals_rejected(self):
        fixture = mixed_fixture(self.root)
        duplicate = copy.deepcopy(fixture["artifacts"][0])
        duplicate["artifact_id"] = "duplicate-path"
        fixture["artifacts"].append(duplicate)
        self.assertTrue(any("duplicate artifact path" in error for error in self.errors_for(fixture)))

        fixture = mixed_fixture(self.root)
        fixture["claims"][0]["events"][1]["earliest_utc"] = TIMES["deny"]
        errors = self.errors_for(fixture)
        self.assertTrue(any("intervals overlap" in error for error in errors))

    def test_gateway_denial_needs_no_fabricated_sink_effect(self):
        fixture = mixed_fixture(self.root)
        fixture["claims"][0]["classification"] = "INCONCLUSIVE"
        fixture["claims"][0]["supporting_artifact_refs"] = [
            "source-c1",
            "gateway-response"
        ]
        roles = {item["role"] for item in fixture["artifacts"]}
        self.assertNotIn("DESTINATION_EFFECT", roles)
        self.assertEqual(fixture["counts"]["destination_effects"], 0)
        self.assertEqual(self.errors_for(fixture), [])

    def test_aborted_deviation_is_preserved_without_false_gate_pass(self):
        fixture = blocked_fixture()
        fixture["run_state"] = "ABORTED"
        fixture["run_compliance"] = "DEVIATION"
        fixture["counts"].update({"attempted": 1, "deviations": 1})
        fixture["context"].update({
            "resource_pseudonym": "SYNTHETIC-RESOURCE",
            "route": "synthetic-route",
            "permission": "synthetic-permission",
            "api_version": "synthetic-api-v1",
            "thread_id": "SYNTHETIC-THREAD",
            "session_id": "SYNTHETIC-SESSION"
        })
        fixture["deviation"] = {
            "actual_execution": True,
            "description": "Synthetic aborted/deviation fixture only.",
            "intervention": "Synthetic stop marker; no live system.",
            "intervention_time_utc": "2026-10-26T10:00:00Z",
            "compliant_result": False,
            "gates_marked_pass_by_deviation": False
        }
        self.assertEqual(self.errors_for(fixture), [])
        self.assertTrue(all(
            gate["status"] == "PENDING" for gate in fixture["gates"].values()
        ))
        self.assertEqual(fixture["run_compliance"], "DEVIATION")

        fixture["gates"]["gate_0"] = {"status": "PASS", "evidence_ref": None}
        self.assertTrue(self.errors_for(fixture))


if __name__ == "__main__":
    unittest.main()
