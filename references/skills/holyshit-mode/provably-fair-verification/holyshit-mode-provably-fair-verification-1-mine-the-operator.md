# 1. Mine the operator's documented scheme first

- source canon: `holyshit-mode/provably-fair-verification.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-04

## The technique

Search their blog/help-center for the PF explainer. Extract: seed model (server/client
seed, nonce), commitment pattern (commit-and-reveal, hash chain), consumption order
(forward chain vs reverse chain), and the published anchor ("final hash published before
play"). This defines exactly what the public wire must show for the claim to hold.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
