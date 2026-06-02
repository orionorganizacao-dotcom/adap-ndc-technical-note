# Public-Interest Verifier Maintenance

## Why A-DAP needs maintainable public verification infrastructure

## Abstract

A-DAP creates reconstructible evidentiary objects for high-impact automated decisions.

However, reconstructible evidence does not become practically contestable merely because a technical envelope exists.

Someone must be able to verify it.

If the only usable verifier is controlled by the same institution that made the decision, then practical contestability may collapse even when the decision envelope is technically well-formed.

This note argues that A-DAP requires not only reconstructible evidence, but also exercisable verification infrastructure.

A public-interest verifier should be independently maintained, openly inspectable, reproducible, and not controlled by the decision-making institution.

In short:

A-DAP evidence must be reconstructible.

A-DAP verification must be exercisable.

And the tools that exercise verification should not silently become new trust authorities.

## 1. Problem Statement

A-DAP separates the decision from the evidence of what happened.

But a new problem appears immediately:

Who maintains the verifier?

A decision envelope may be available.

A hash may be valid.

A reconstruction script may exist.

A receipt may give the affected person a reference code.

But if the affected person, lawyer, regulator, journalist, public defender, court, or civil society organization cannot practically run or access a verifier, then the evidentiary object remains underused.

This creates a gap between structural verifiability and practical verification.

A-DAP may succeed architecturally while still failing socially if verification depends on inaccessible tools, captured maintainers, expensive experts, or institution-controlled interfaces.

## 2. Core Claim

A-DAP requires public-interest verification infrastructure.

A decision-making institution may provide its own verifier.

But that verifier should not be treated as the only verification path.

A verifier controlled by the same institution that made the decision may be useful as a convenience interface.

It should not be treated as independent verification.

The core claim is:

A-DAP requires not only reconstructible evidence, but exercisable verification infrastructure capable of being maintained, inspected, reproduced, and challenged outside the decision-making institution.

## 3. Why Institution-Controlled Verification Is Not Enough

A company or agency may say:

“Our system is auditable because we provide a verification portal.”

That is not sufficient by itself.

A verification portal may still be controlled by the same institution that:

- made the decision;
- generated the envelope;
- stores the envelope;
- controls user access;
- controls the verification interface;
- controls the explanation;
- controls the logs;
- controls whether verification succeeds or fails;
- controls what the affected person sees.

In that case, the user may be moved from:

“Trust our decision.”

to:

“Trust our verifier.”

That does not solve the structural problem.

It relocates it.

## 4. The Verifier as a New Control Point

A verifier can become a new authority.

This is dangerous because users may treat verifier output as final.

Examples:

- “Hash verified” may be misread as “decision correct.”
- “Record found” may be misread as “lawful process.”
- “Envelope valid” may be misread as “input data was true.”
- “No mismatch found” may be misread as “no further contest is possible.”
- “Green result” may be misread as “case closed.”

A-DAP must prevent the verifier from becoming a new black box.

A verifier should expose:

- what it checked;
- what it did not check;
- what evidence it used;
- what assumptions it applied;
- what remained outside scope;
- what may still be contested.

The verifier should help people inspect evidence.

It should not become the evidence.

## 5. Public-Interest Verifier

A public-interest verifier is a verification implementation designed to serve contestability rather than institutional self-protection.

It may be maintained by:

- a university;
- a public defender office;
- a regulator;
- an ombuds office;
- a civil society organization;
- a standards body;
- a court technology lab;
- an independent audit cooperative;
- an open-source community with transparent governance.

The key issue is not merely organizational separation.

The key issue is dependency structure.

The verifier should not depend materially on the decision-making institution for its operation, interpretation, or result.

## 6. Minimum Properties

A public-interest verifier should satisfy several minimum properties.

### 6.1 Open Inspectability

The verifier’s source code, rules, schemas, assumptions, and verification logic should be inspectable.

If the verifier cannot be inspected, users are asked to trust another black box.

Open inspectability does not automatically guarantee independence.

But without inspectability, independence becomes much harder to evaluate.

### 6.2 Reproducibility

The verifier should allow others to reproduce the verification result using the same receipt, envelope, committed materials, and reconstruction rules.

The goal is not:

Trust this verifier.

The goal is:

Run the same procedure and obtain the same result, or detect divergence.

### 6.3 Independent Maintainability

The verifier should be maintainable without permission from the decision-making institution.

A public-interest verifier should not require the original operator to approve updates, suppress findings, revoke access, or control interpretation.

### 6.4 Versioned Verification Logic

Verifier logic should be versioned.

A verification result should identify which verifier version, schema version, reconstruction rule, and assumptions were used.

Otherwise, later parties may be unable to reconstruct what the verifier actually checked.

### 6.5 Exportable Results

The verifier should produce exportable results for:

- affected persons;
- legal representatives;
- regulators;
- courts;
- public defenders;
- ombuds offices;
- auditors;
- journalists;
- civil society organizations.

The output should include both a technical result and a plain-language explanation.

### 6.6 Scope Disclosure

The verifier should clearly say what it did not verify.

For example:

- It did not prove the decision was correct.
- It did not prove the input data was true.
- It did not prove the policy was lawful.
- It did not prove fairness.
- It did not prove that the affected person received proper notice.
- It did not prove that the person had meaningful appeal rights.

### 6.7 Privacy Preservation

The verifier should avoid exposing sensitive personal data unnecessarily.

It should support controlled disclosure, redaction, authorization, and privacy-preserving reconstruction where appropriate.

Public verification should not become public exposure of protected data.

### 6.8 Accessibility

The verifier should be usable by non-engineers or their representatives.

A public-interest verifier should support:

- receipt lookup;
- file upload;
- plain-language result display;
- exportable evidence package;
- mobile access;
- screen reader compatibility;
- low-bandwidth access;
- multilingual explanations where appropriate.

### 6.9 Non-Authority Design

The verifier should not present itself as a final authority.

It should present itself as a reconstruction tool.

The output should avoid language such as:

- “Decision valid.”
- “Decision lawful.”
- “Case verified.”
- “No further action needed.”

Safer language:

- “The checked record matches the committed evidence within the declared verification scope.”
- “This result does not determine correctness, fairness, legality, input truth, remedy, or procedural finality.”
- “This result may be used as evidence for further review.”

## 7. Verifier Governance Risks

A public-interest verifier can still be captured.

Independence is not guaranteed by nonprofit status, academic status, public status, or open-source labeling.

Relevant risks include:

- funding capture;
- access dependency;
- hosting dependency;
- update dependency;
- governance capture;
- scope limitation;
- political pressure;
- legal intimidation;
- silent deprecation;
- selective maintenance;
- unequal access;
- institutional partnership bias;
- interface manipulation;
- overclaiming in public-facing outputs.

Therefore, the verifier itself should be subject to A-DAP-style scrutiny.

The verifier should not escape verification merely because it verifies others.

## 8. Custody Questions for Verifier Maintenance

A-DAP should ask the following questions about any verifier:

- Who maintains the verifier?
- Who funds it?
- Who can update it?
- Who can shut it down?
- Who controls hosting?
- Who controls access to envelopes?
- Who controls the schema registry?
- Who controls public-facing language?
- Who signs releases?
- Who audits the verifier?
- Who can reproduce verifier results independently?
- Who can challenge the verifier’s assumptions?
- Who can fork or mirror the verifier?
- Who can preserve old versions?
- Who benefits if verification becomes difficult?
- Who benefits if verification is overtrusted?

If the answers collapse into the same institution that made the decision, practical independence is weak.

## 9. Institution-Provided Verifiers

A-DAP does not prohibit institutions from providing their own verification portals.

Institution-provided verifiers may be useful for:

- convenience;
- first-pass review;
- receipt lookup;
- envelope delivery;
- authentication;
- user support;
- administrative workflow;
- accessibility.

But they should be labeled correctly.

An institution-provided verifier is not independent merely because it verifies a record.

It should be treated as an operator-provided verification interface unless the custody and governance structure demonstrate otherwise.

A safer label:

Operator-provided verification interface.

Not:

Independent verifier.

## 10. Public Verifier vs Independent Verifier

A public verifier is not automatically independent.

A verifier may be public but still controlled by one actor.

A verifier may be open-source but still practically dependent on one maintainer.

A verifier may be maintained by a university but still funded by the decision-making institution.

A verifier may be run by a regulator but still depend on operator-provided data access.

Therefore, A-DAP should distinguish:

- public availability;
- open inspectability;
- operational independence;
- funding independence;
- access independence;
- reconstruction independence;
- interpretive independence.

These are not the same.

## 11. Public-Interest Verifier Topology

A stronger topology includes multiple layers:

1. Operator-provided interface  
   For convenience and authenticated envelope access.

2. Public-interest verifier  
   Maintained outside the operator for independent reconstruction.

3. Open reconstruction specification  
   Allows any competent party to reproduce the result.

4. Versioned test vectors  
   Allow verifier correctness to be tested.

5. Public issue tracker  
   Allows defects, overclaims, and edge cases to be reported.

6. Archival mirrors  
   Preserve verifier versions and schemas over time.

7. Institutional interpretation layer  
   Courts, regulators, auditors, or agencies interpret the evidence.

The verifier should not replace the institutional interpretation layer.

## 12. Relation to NDC

Verifier maintenance directly affects NDC.

If the decision system, envelope repository, verifier, and result interface are all controlled by the same institution, apparent verification may collapse to NDC = 1.

If the verifier is independently maintained, reproducible, and able to reconstruct committed records without depending on the operator’s interpretation, NDC may increase.

However, NDC does not increase merely because a verifier exists.

The question is whether the verifier creates a materially independent verification path after dependency collapse.

## 13. Relation to Citizen Verification

Citizen verification requires more than a receipt.

A person may receive a receipt and still be unable to exercise verification if:

- the verifier is unavailable;
- the verifier is too technical;
- the envelope is inaccessible;
- the verification link is operator-controlled;
- the person lacks legal or technical support;
- the result cannot be exported;
- the result is written in misleading language;
- the verifier overclaims;
- the verifier cannot be inspected.

A public-interest verifier helps convert receipt possession into exercisable contestability.

## 14. Relation to Courts and Regulators

Courts and regulators may use public-interest verifiers to separate technical reconstruction from legal judgment.

A verifier can help answer:

- Does a committed decision record exist?
- Does the receipt point to a real envelope?
- Does the later explanation match the committed record?
- Was the envelope altered, missing, or inconsistent?
- Was the verification process reproducible?
- What did the verifier not check?

A verifier should not answer:

- Was the decision legally valid?
- Was the policy lawful?
- Was the input true?
- Was the decision fair?
- What remedy is required?
- Should the case be reopened?
- Has procedural finality been overcome?

Those are institutional questions.

## 15. Safe Claims

A safe claim:

A-DAP verification should be exercisable through tools that are inspectable, reproducible, and not materially controlled by the decision-making institution.

Another safe claim:

A public-interest verifier can improve practical contestability, but it does not by itself prove correctness, fairness, legality, or accountability.

Another safe claim:

A verifier result is evidence about reconstruction within scope, not a final legal conclusion.

## 16. Unsafe Claims

Unsafe claim:

Because a verifier exists, the system is independently auditable.

Safer statement:

A verifier may support auditability if its maintenance, access, governance, and reconstruction path do not collapse into the same control domain as the decision-making system.

Unsafe claim:

The operator’s verification portal proves the decision was valid.

Safer statement:

The operator’s verification portal may provide a convenience interface, but independent verification requires a structurally disjoint reconstruction path.

Unsafe claim:

The public-interest verifier is trusted, so its output is final.

Safer statement:

The public-interest verifier should expose its procedure, assumptions, version, evidence, and limits so that future verifiers can reproduce or challenge its result.

Unsafe claim:

A green result means the citizen has no further claim.

Safer statement:

A green result may show consistency within the declared verification scope. It does not resolve input truth, fairness, legality, remedy, or procedural rights.

## 17. Minimum Public-Interest Verifier Output

A verifier output should include at least:

- receipt identifier;
- envelope identifier;
- verifier name;
- verifier version;
- schema version;
- reconstruction rule version;
- verification date;
- input materials checked;
- hash comparison result;
- signature or timestamp result if applicable;
- mismatch status;
- missing evidence status;
- custody assumptions;
- scope limits;
- plain-language summary;
- exportable evidence package;
- statement of what remains contestable.

The output should avoid presenting itself as a final judgment.

## 18. Open Problems

Several questions remain open:

- Who should maintain public-interest verifiers?
- How should they be funded without capture?
- Should regulators certify verifier maintainers?
- Should courts accept verifier outputs as technical evidence?
- How should verifier defects be disclosed?
- How should old verifier versions be preserved?
- How should verifier outputs be cited in legal proceedings?
- How should public-interest verifiers handle sensitive personal data?
- How should verifier access work when the envelope is restricted?
- How should competing verifier outputs be reconciled?
- How should verifier forks be governed?
- How should public-interest verifiers avoid becoming new authorities?
- How should funding dependency be disclosed?
- How should verifier maintenance be audited?
- How should a citizen know which verifier to use?
- How should public defenders, ombuds offices, and civil society organizations access verifier infrastructure?
- How should verification be made available in low-resource environments?
- How should verification remain usable after procedural closure?
- How should institutional refusal to provide envelopes be handled?
- How should a verifier report that the envelope is missing, inaccessible, or non-reconstructible?

These are not secondary implementation details.

They determine whether A-DAP can be exercised in practice.

## 19. Conclusion

A-DAP should not stop at creating reconstructible envelopes.

It must also address who can exercise reconstruction.

A verifier controlled by the same institution that made the decision may provide convenience, but it should not be mistaken for independent verification.

Public-interest verifier maintenance is necessary to prevent A-DAP from becoming technically correct but practically inaccessible.

The verifier must not become a new authority.

It must remain inspectable, reproducible, limited, contestable, and open to future contradiction.

## Final Principle

A-DAP evidence must be reconstructible.

A-DAP verification must be exercisable.

A verifier should help people test the record.

It should not become the record.
