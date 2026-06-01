## v0.4.4 — Non-Terminal Verification and Perpetual Refutability

This release formalizes the principle that no A-DAP verification event should be treated as final.

### Added

- Added `architecture/non-terminal-verification.md`.
- Added the concept of non-terminal verification.
- Added the principle of perpetual refutability.
- Added explicit distinction between:
  - open-but-dormant verification;
  - friendly-executed verification;
  - adversarially-reexecuted verification;
  - terminal verification.

### Changed

- Updated `README.md` to clarify that external execution increases evidentiary confidence but does not close the record.
- Clarified that A-DAP does not require trusted adversaries.
- Clarified that A-DAP requires unclosable verification.
- Added design discipline language: do not treat any verification event as final.
- Added an open problem about preserving perpetual refutability under friendly, captured, non-adversarial, or adversarial-looking review.

### Rationale

This release narrows the protocol’s claims and reduces audit-theater risk.

A public, deterministic, signed, timestamped, and externally executable repository should not be described as externally verified unless verification has actually been exercised.

Even after execution, the result should remain reproducible, contestable, and refutable by future structurally disjoint verifiers.

### Safe Claim

A-DAP does not convert trust in the operator into trust in a verifier.

It preserves the conditions under which later structurally disjoint verifiers can rerun the same committed procedure and detect divergence.
