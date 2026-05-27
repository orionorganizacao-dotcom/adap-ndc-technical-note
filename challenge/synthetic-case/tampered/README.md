# Tampered Examples

This folder contains intentionally modified versions of the synthetic challenge files.

These examples are not valid A-DAP evidence.

They exist to show how small modifications can alter the evidence state and should be detected by a verifier.

## Included tampering examples

### 1. Modified input risk score

File:

`input-risk-score-modified.json`

Modification:

The original `risk_score` is changed from `0.12` to `0.82`.

Expected issue:

The original decision was `approved`, but a risk score of `0.82` is above the threshold of `0.50`.

### 2. Modified output decision

File:

`output-decision-modified.json`

Modification:

The original decision is changed from `approved` to `rejected`.

Expected issue:

The original input still has `risk_score = 0.12`, which is below the threshold of `0.50`.

### 3. Modified envelope file reference

File:

`envelope-file-reference-modified.json`

Modification:

The envelope reference is changed from `input.json` to `input-modified.json`.

Expected issue:

The declared evidence path no longer matches the original custody set.

### 4. Modified custody file list

File:

`custody-file-list-modified.json`

Modification:

The custody list removes `envelope.json`.

Expected issue:

The custody trail no longer includes the full evidence set required for reconstruction.

## Purpose

These examples prepare the ground for automated verification.

A future verifier should return a failure result for each tampered case.

## Principle

Tampering is not defined only as changing a decision.

Tampering may also occur through changes to inputs, outputs, envelope references, custody declarations, or claimed reconstruction scope.
