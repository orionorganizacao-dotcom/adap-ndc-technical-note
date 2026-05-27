# A-DAP Reconstruction Challenge

This directory contains public reconstruction challenges for A-DAP.

A-DAP does not ask reviewers to trust the author.

It asks reviewers to reconstruct decision evidence, test custody claims, identify oracle boundaries, and determine whether tampering, ambiguity, or incorrect claims can be detected.

This directory separates two different types of challenge:

1. **Synthetic Case**
2. **GCD-001 Adversarial Reconstruction**

They must not be treated as the same thing.

---

## Why This Separation Matters

The synthetic case is a controlled demonstration.

GCD-001 is the adversarial reconstruction target.

Mixing the two would weaken the project, because a synthetic case is designed by the author and cannot serve as adversarial validation.

The correct distinction is:

```text
Synthetic Case = executable demonstration
GCD-001 = adversarial reconstruction target
