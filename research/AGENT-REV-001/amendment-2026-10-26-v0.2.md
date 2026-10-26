# AGENT-REV-001 Amendment v0.2 — 2026-10-26

**Disposition:** `NOT VALIDATED — PILOT BLOCKED`  
**Prior protocol:** v0.1; **amended protocol:** v0.2  
**Prior evidence schema:** v0.2; **replacement evidence schema:** v0.3  
Protocol and schema versions are independent. This amendment records documentary and offline structural corrections only; it does not authorize or report a pilot.

## Reason and scope

This dated amendment responds to the schema-level finding on PR #19 and the 2026-10-26 technical-coherence review. It covers C1–C5 and customer-policy claim P1, their C0–T4 operational observations, evidence linkage, readiness, and deviations. No unrelated A-DAP methodology is amended.

The v0.2 schema source already expressed an intended non-empty-artifact condition for run-level positive classifications. This amendment does not characterize that intended rule as an omitted v0.2 requirement. The reported empty-evidence acceptance showed the old package contract was insufficient in practice; v0.3 repairs the invalid JSON, represents claim-level mixed findings, and moves evidence requirements to claim-specific package verification. A C1 gateway denial requires request/response evidence and may have no destination effect; an asserted destination effect requires the corresponding sink evidence.

## Changes

- Separate vendor conformance (C1–C4), observability limit (C5), and customer-policy conformance (P1); distinguish H0 from a policy-specific H1.
- Bound conclusions to a fully observed, fixed test set. Preserve a credible single counterexample as a candidate and document symmetric candidate support/defeaters; do not treat five conforming exploratory runs as global falsification.
- Define claim contracts and the C0–T4 controls, with runtime thresholds left unfilled/unapproved where they require owner review.
- Separate readiness, execution, per-claim classification, and deviations. Require owner approval and evidence-backed Gates 0–4 for readiness; do not permit `NOT_APPLICABLE` to bypass a required gate.
- Add local structural, reference, hash, evidence-role, and interval-order verification plus synthetic offline tests. The verifier does not authenticate source records, custody, or reviewer independence.

## Original and replacement hashes

SHA-256 values identify exact repository file bytes; they do not attest to evidence authenticity. “Original” values were computed from reviewed PR #19 HEAD `668fcf0e34bc1822d9e0b3ab79497574baaec471`; “replacement” values are the amended files in this amendment.

| File | Original SHA-256 | Replacement SHA-256 |
| --- | --- | --- |
| `protocol.md` | `6e840b3c58b0c3ef46a7e26caf6509659c7c4d08e4d188f6cf359faa35b36bb9` | `b2af0b62c98501d0915e0b9a0f2dd8dd71bdba056dcb98908639e1aac18f9679` |
| `test-matrix.md` | `791e0804f394a52529c1928ac827351a76d0721e81a750b9deb51b8286cd3389` | `3105c42fba326ce4770e8d6eb565b4f1fd458bd814847c5abf1de028471969b4` |
| `reviewer-checklist.md` | `2eacf7640af149dab9eef5b0d221f06734789d698b5278967b610d2305d0a3a0` | `8b1012207a72d945f0ee63ad7dd85ad348583820d1129378ee66ad1476fce769` |
| `evidence-manifest.schema.json` | `f81d60a09cd135caa693f21b8756fc3c987e84ee1cc80a7b8c140a65ca6556c0` | `50913a55930607a5d29e4669a85a0033772033657ef235e497b82ea2686e2768` |

## Source and validation provenance

The v0.1 registration records vendor-document access on 2026-10-22, but the cited source snapshots are not present in the reviewed package. This amendment does not claim that any new source snapshot was captured on that date. Current vendor pages are not historical snapshots; source capture, version/date, interpretation, and owner review remain prerequisites before a future authorized run. The supplied public pages could not be fetched from the editing environment.

The committed tests generate only explicitly synthetic package/artifact data. The valid mixed fixture retains pending authorization and gates; invalid-readiness cases use placeholder values only to verify rejection. Tests do not establish authorization, gate passage, execution, observation, independent reconstruction, external reproduction, or a vendor security failure. No historical sample counts are represented as new results. The verifier checks local schema shape, references, paths, hashes, and declared timing intervals only; it cannot authenticate underlying records or establish reviewer independence.

Run offline checks from the repository root:

```sh
python -m pip install -r research/AGENT-REV-001/requirements-test.txt
python -m unittest discover -s research/AGENT-REV-001 -p 'test_verify_package.py' -v
```

The package verifier can be run locally with:

```sh
python research/AGENT-REV-001/verify_package.py path/to/manifest.json
```

## Still outstanding

Owner authorization, frozen claim-specific source/policy and runtime parameters, calibration observations, Gates 0–4, independent review, named review, actual stop/recovery capability, source snapshots, and any experimental runs remain outstanding. T3/T4 require separate review. The exact research status remains **`NOT VALIDATED — PILOT BLOCKED`**.
