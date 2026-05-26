# Signed Commit Verification Instructions

This file documents how an independent auditor can verify signed commits outside GitHub.

GitHub's "Verified" badge is a convenience layer, not the proof itself.

The independently verifiable proof is the cryptographic signature attached to the commit.

## Verification command

```bash
git verify-commit <commit_hash>
