## Repository Structure

```text
.
├── README.md
├── NOTICE.md
├── THREAT_MODEL.md
├── CONTRIBUTING.md
├── QUICKSTART.md
├── RELEASE_NOTES.md
├── ADAP-EXP-003.md
├── GCD-002_BENCHMARK_CUSTODY_COLLAPSE.md
├── 90-DAY-GO-NO-GO.md
├── architecture/
│   ├── adoption-capture-risk.md
│   ├── automated-ndc-v2.md
│   ├── citizen-facing-evidence-language.md
│   ├── citizen-verifier-ui-spec.md
│   ├── cryptographic-habeas-data.md
│   ├── disjoint-anchoring-for-contestability.md
│   ├── envelope-bottleneck.md
│   ├── example-verification-topology.md
│   ├── exercisable-citizen-verification.md
│   ├── exercisable-verification-interface.md
│   ├── independent-verification-topology.md
│   ├── input-provenance-envelope.md
│   ├── input-truth-boundary.md
│   ├── ip-priority-and-authorized-execution.md
│   ├── ndc-comparative-positioning.md
│   ├── ndc-separability-criterion.md
│   ├── non-self-attested-materiality.md
│   ├── non-terminal-verification.md
│   ├── objective-indexed-ndc.md
│   ├── omega-plus-plus-reconstructible-verdicts.md
│   ├── random-audit-sampling.md
│   ├── scope-completeness-boundary.md
│   ├── sdk-vs-external-audit-service.md
│   ├── self-validating-limitation-claims.md
│   ├── signer-custody-boundary.md
│   └── verifier-funding-capture.md
├── challenge/
│   ├── gcd-001/
│   ├── gcd-002-verifier-funding/
│   └── gcd-003-internal-integrity-sensor/
├── experiments/
│   ├── adec-001.md
│   ├── gcd-002-solver-validation.md
│   └── second-order-entity-ndc/
├── proofs/
│   └── README.md
└── solver/
    └── README.md
```

The exact structure may evolve.

The important distinction is conceptual:

- `architecture/` explains the theory;
- `challenge/` tests reconstruction;
- `experiments/` tests immature or falsifiable concepts before they become claims;
- `proofs/` separates evidentiary categories;
- `solver/` contains experimental tooling;
- `THREAT_MODEL.md` defines limits.
