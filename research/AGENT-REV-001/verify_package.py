#!/usr/bin/env python3
"""Validate local AGENT-REV-001 package structure and file hashes only."""

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

from jsonschema import Draft202012Validator, FormatChecker


SCHEMA_PATH = Path(__file__).with_name("evidence-manifest.schema.json")
POSITIVE_FINDINGS = {
    "DOCUMENTED_REPRODUCED",
    "CONTRADICTION_CANDIDATE",
    "CONTRADICTION_REPRODUCED",
    "POLICY_VIOLATION_CANDIDATE",
    "POLICY_VIOLATION_TESTED",
}
REPRODUCED_FINDINGS = {
    "DOCUMENTED_REPRODUCED",
    "CONTRADICTION_REPRODUCED",
    "POLICY_VIOLATION_TESTED",
}


def _strict_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _load_json(path):
    with path.open(encoding="utf-8") as stream:
        return json.load(stream, object_pairs_hook=_strict_object)


def _parse_utc(value):
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None or parsed.utcoffset() != timezone.utc.utcoffset(parsed):
        raise ValueError(f"timestamp is not explicit UTC: {value}")
    return parsed


def _validate_temporal_order(claim, errors):
    events = claim["events"]
    by_id = {}
    for event in events:
        event_id = event["event_id"]
        if event_id in by_id:
            errors.append(f"claim {claim['claim_id']}: duplicate event id {event_id}")
            continue
        by_id[event_id] = event
        try:
            earliest = _parse_utc(event["earliest_utc"])
            latest = _parse_utc(event["latest_utc"])
        except (TypeError, ValueError) as error:
            errors.append(f"claim {claim['claim_id']}: {error}")
            continue
        if earliest > latest:
            errors.append(f"claim {claim['claim_id']}: reversed interval for {event_id}")

    for before_id, after_id in claim["required_order"]:
        before = by_id.get(before_id)
        after = by_id.get(after_id)
        if before is None or after is None:
            errors.append(
                f"claim {claim['claim_id']}: required order references unknown event "
                f"{before_id!r} or {after_id!r}"
            )
            continue
        try:
            before_end = _parse_utc(before["latest_utc"])
            after_start = _parse_utc(after["earliest_utc"])
        except (TypeError, ValueError):
            continue
        if before_end >= after_start:
            errors.append(
                f"claim {claim['claim_id']}: event intervals overlap or do not establish "
                f"{before_id} before {after_id}"
            )


def _required_roles(claim):
    finding = claim["classification"]
    basis = claim["basis"]
    if finding not in POSITIVE_FINDINGS:
        return set()
    if finding.startswith("POLICY_VIOLATION"):
        return {"CUSTOMER_POLICY", "DESTINATION_EFFECT"}
    if basis == "GATEWAY_DECISION":
        return {"SOURCE_PROMISE", "GATEWAY_RESPONSE"}
    if basis in {
        "SESSION_EFFECT",
        "INTERRUPT_EFFECT",
        "WORKFLOW_EFFECT",
        "DEPLOYMENT_EFFECT",
        "POLICY_EFFECT",
        "BOUNDED_OBSERVATION",
    }:
        return {"SOURCE_PROMISE", "DESTINATION_EFFECT"}
    return set()


def _artifact_index(package, package_dir, errors):
    artifacts = package["artifacts"]
    by_id = {}
    paths = set()

    for artifact in artifacts:
        artifact_id = artifact["artifact_id"]
        if artifact_id in by_id:
            errors.append(f"duplicate artifact id: {artifact_id}")
            continue
        by_id[artifact_id] = artifact

        raw_path = artifact["path"]
        relative = PurePosixPath(raw_path)
        if relative.is_absolute() or "\\" in raw_path or ".." in relative.parts:
            errors.append(f"artifact path is not a safe relative path: {raw_path}")
            continue
        normalized = relative.as_posix()
        if normalized in paths:
            errors.append(f"duplicate artifact path: {normalized}")
            continue
        paths.add(normalized)

        resolved = (package_dir / Path(*relative.parts)).resolve()
        if not resolved.is_relative_to(package_dir.resolve()):
            errors.append(f"artifact path escapes package directory: {raw_path}")
            continue
        if not resolved.is_file():
            errors.append(f"artifact file is missing or not a regular file: {raw_path}")
            continue
        actual_hash = hashlib.sha256(resolved.read_bytes()).hexdigest()
        if actual_hash != artifact["sha256"]:
            errors.append(f"artifact SHA-256 mismatch: {raw_path}")

    return by_id


def validate_package(package, package_dir, schema):
    errors = []
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors.extend(
        f"schema: {error.message} at {list(error.absolute_path)}"
        for error in validator.iter_errors(package)
    )
    if errors:
        return errors

    artifacts = _artifact_index(package, package_dir, errors)
    references = []

    for gate_name, gate in package["gates"].items():
        if gate["evidence_ref"] is not None:
            references.append((f"{gate_name} evidence", gate["evidence_ref"]))

    configuration = package["configuration"]
    if configuration["artifact_ref"] is not None:
        references.append(("configuration", configuration["artifact_ref"]))
        config_artifact = artifacts.get(configuration["artifact_ref"])
        if config_artifact is not None:
            if config_artifact["role"] != "CONFIGURATION":
                errors.append("configuration reference does not have CONFIGURATION role")
            if config_artifact["sha256"] != configuration["sha256"]:
                errors.append("configuration hash does not match its artifact hash")

    contracts = {}
    for contract in package["claim_contracts"]:
        claim_id = contract["claim_id"]
        if claim_id in contracts:
            errors.append(f"duplicate claim contract: {claim_id}")
        contracts[claim_id] = contract
        if contract["source_artifact_ref"] is not None:
            references.append((f"{claim_id} source", contract["source_artifact_ref"]))
            source_artifact = artifacts.get(contract["source_artifact_ref"])
            required_role = (
                "CUSTOMER_POLICY"
                if contract["claim_type"] == "CUSTOMER_POLICY_CONFORMANCE"
                else "SOURCE_PROMISE"
            )
            if source_artifact is not None and source_artifact["role"] != required_role:
                errors.append(
                    f"{claim_id} source artifact must have role {required_role}"
                )
        if contract["status"] == "FROZEN":
            required_values = (
                "source_url",
                "source_version",
                "source_artifact_ref",
                "enforcement_point",
                "eligibility",
                "observation_window_start",
                "observation_window_end",
                "maximum_wait_seconds",
                "repeatability_criterion",
            )
            if any(contract[field] is None for field in required_values):
                errors.append(f"{claim_id} frozen contract has unfilled parameters")
            start = contract["observation_window_start"]
            end = contract["observation_window_end"]
            if start and end:
                try:
                    if _parse_utc(start) >= _parse_utc(end):
                        errors.append(f"{claim_id} observation window is empty or reversed")
                except ValueError as error:
                    errors.append(f"{claim_id} {error}")

    claims = {}
    for claim in package["claims"]:
        claim_id = claim["claim_id"]
        if claim_id in claims:
            errors.append(f"duplicate claim outcome: {claim_id}")
        claims[claim_id] = claim
        contract = contracts.get(claim_id)
        if contract is None:
            errors.append(f"claim outcome has no contract: {claim_id}")

        for reference in claim["supporting_artifact_refs"] + claim["defeating_artifact_refs"]:
            references.append((f"{claim_id} claim evidence", reference))
        for event in claim["events"]:
            for reference in event["artifact_refs"]:
                references.append((f"{claim_id} event evidence", reference))
        _validate_temporal_order(claim, errors)

        finding = claim["classification"]
        if finding in POSITIVE_FINDINGS:
            if contract is None:
                continue
            if contract["status"] != "FROZEN":
                errors.append(f"{claim_id} positive finding requires a frozen claim contract")
            if not claim["identity_pseudonym"]:
                errors.append(f"{claim_id} positive finding requires an identity pseudonym")
            if not claim["events"]:
                errors.append(f"{claim_id} positive finding requires timed evidence events")
            if any(not event["artifact_refs"] for event in claim["events"]):
                errors.append(f"{claim_id} positive finding has an event without evidence")
            if finding in {
                "CONTRADICTION_CANDIDATE",
                "CONTRADICTION_REPRODUCED",
                "POLICY_VIOLATION_CANDIDATE",
                "POLICY_VIOLATION_TESTED",
            } and not claim["supporting_artifact_refs"]:
                errors.append(f"{claim_id} finding lacks supporting evidence")
            roles = _required_roles(claim)
            if not roles:
                errors.append(f"{claim_id} positive finding requires a supported evidence basis")
            referenced = {
                artifacts[ref]["role"]
                for ref in claim["supporting_artifact_refs"]
                if ref in artifacts
            }
            missing_roles = roles - referenced
            if missing_roles:
                errors.append(
                    f"{claim_id} finding lacks required evidence roles: "
                    + ", ".join(sorted(missing_roles))
                )
            if finding.startswith("POLICY_VIOLATION") and (
                contract["claim_type"] != "CUSTOMER_POLICY_CONFORMANCE"
            ):
                errors.append(f"{claim_id} policy finding lacks a customer-policy contract")
            if finding.startswith("CONTRADICTION") and (
                contract["claim_type"] != "VENDOR_CONFORMANCE"
            ):
                errors.append(f"{claim_id} contradiction finding lacks a vendor contract")
            if finding in REPRODUCED_FINDINGS and (
                package["run_state"] != "COMPLETED"
                or package["run_compliance"] != "COMPLIANT"
            ):
                errors.append(
                    f"{claim_id} reproduced/tested finding requires a completed compliant run"
                )

    for referrer, reference in references:
        if reference not in artifacts:
            errors.append(f"{referrer} has unresolved artifact reference: {reference}")

    if set(claims) != set(contracts):
        errors.append("claim outcomes and claim contracts must have identical claim IDs")

    counts = package["counts"]
    for field in ("completed", "excluded", "deviations"):
        if counts[field] > counts["attempted"]:
            errors.append(f"count {field} exceeds attempted count")

    if package["run_state"] != "NOT_EXECUTED":
        context = package["context"]
        for field in ("api_version", "resource_pseudonym", "route", "permission"):
            if not context[field]:
                errors.append(f"executed package lacks context field: {field}")
        if any(not version for version in context["software_versions"].values()):
            errors.append("executed package has an unfilled software version")
        if package["arm"] in {"C0", "T1", "T2"} and not (
            context["thread_id"] and context["session_id"]
        ):
            errors.append("executed arm requires thread and session IDs")
        if package["arm"] == "T3" and not (
            context["thread_id"] and context["session_id"] and context["workflow_id"]
        ):
            errors.append("executed T3 requires thread, session, and workflow IDs")
        if package["arm"] == "T4" and not (
            context["session_id"] and context["workflow_id"] and context["deployment_id"]
        ):
            errors.append("executed T4 requires session, workflow, and deployment IDs")

    if package["run_compliance"] == "DEVIATION":
        if package["run_state"] not in {"ATTEMPTED", "COMPLETED", "ABORTED"}:
            errors.append("deviation must be associated with an attempted execution")
        if any(
            claim["classification"] in REPRODUCED_FINDINGS
            for claim in package["claims"]
        ):
            errors.append("a deviation cannot be admitted as a reproduced compliant result")

    return errors


def verify_package(manifest_path, schema_path=SCHEMA_PATH):
    manifest_path = Path(manifest_path).resolve()
    schema_path = Path(schema_path).resolve()
    try:
        package = _load_json(manifest_path)
        schema = _load_json(schema_path)
        Draft202012Validator.check_schema(schema)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as error:
        return [f"cannot load strict JSON/schema: {error}"]

    return validate_package(package, manifest_path.parent, schema)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--schema", type=Path, default=SCHEMA_PATH)
    args = parser.parse_args(argv)
    errors = verify_package(args.manifest, args.schema)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(
        "Package structure and local SHA-256 references are consistent. "
        "This does not authenticate evidence or establish independent review."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
