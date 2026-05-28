# A-DAP — Auditable Decision Accountability Protocol

A-DAP is a contestability architecture for high-impact automated decisions.

Its core claim is intentionally narrow:

A-DAP makes later alteration of committed decision records detectable.

It does not prove that the original decision was true.

It does not prove that the decision was fair.

It does not eliminate trust in the operator at origin.

It does not guarantee detection.

Its value is stricter:

high-impact automated decisions should be born with a reconstructible evidentiary object, so that affected parties, auditors, regulators, or courts can later contest the specific decision against a pre-committed record.

A-DAP turns automated decisions from post-hoc explanations into contestable records.

---

## Executive Summary

A-DAP — Auditable Decision Accountability Protocol — proposes that high-impact automated decisions be committed before or at the moment of action through reconstructible decision envelopes.

A decision envelope is not a truth oracle.

It is a pre-committed evidentiary object that can later be reconstructed, examined, and compared against explanations, notices, logs, or operator claims.

A-DAP uses cryptographic commitments, canonicalization, timestamps, signatures, and optional independent anchoring to strengthen temporal integrity.

But cryptography does not prove truth.

A content-blind anchor can make retrospective rewriting detectable, but it cannot prove that the operator told the truth when the envelope was created.

Therefore, A-DAP’s defensible claim is not:

“the system proves the decision was correct.”

The defensible claim is:

“the system preserves a contestable record of what was committed at decision time.”

This project favors claims that survive adversarial review over claims that sound stronger but collapse under scrutiny.
