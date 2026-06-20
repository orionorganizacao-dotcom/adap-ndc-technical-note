# PL2338-EXP-001
## Custody Graph Analysis of AI Oversight and Contestability in Brazil

### Status
Draft

### Objective

Evaluate whether the oversight, contestability, and accountability mechanisms proposed in PL 2338/2023 create structurally independent verification paths or merely declaratory supervision mechanisms.

### Research Question

What is the theoretical NDC (Non-Dependency Count) implied by the oversight and contestability mechanisms described in PL 2338/2023?

### Scope

Included:

- Contestability
- Accountability
- Oversight
- Recordkeeping
- Reconstruction of decisions

Excluded:

- Fairness
- Bias
- Constitutional analysis
- Economic impact
- Regulatory desirability

### Methodology

1. Extract relevant articles from PL 2338/2023.
2. Map legal actors to custody domains.
3. Construct custody graphs.
4. Collapse domains sharing material control.
5. Compute theoretical NDC.
6. Classify mechanisms as:
   - Structural supervision
   - Declaratory supervision

### Material Control Collapse Criterion

Two domains are collapsed whenever they share any critical dependency required for reconstruction or contestation of a decision.

Examples include:

- Log control
- Evidence control
- Funding dependency
- Infrastructure dependency
- Governance dependency

### Falsification Criteria

This experiment is falsified if:

1. Independent custody paths remain after collapse and are not reflected in NDC.
2. Different graph constructions from the same legal text consistently produce incompatible NDC values.
3. Material control dependencies cannot be operationally defined.

### Expected Outcomes

A. NDC > 1
B. NDC = 1
C. NDC not computable from legal text

All outcomes are considered informative.
