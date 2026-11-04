# Operator note

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

Free-AI/bill-drain and cross-user poisoning were the prior session's highest-scoring items
(scores 85/95), already reported. This pass adds supply-chain recon + data-plane leak surface.
No host RCE, no admin panel, no secrets — target remains hardened on the data plane; the "holy
shit" is unauthorized resource usage + full infrastructure disclosure, not root.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
