# IMDS classes (v1 vs v2)

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-06

## The technique

IMDSv1 (tokenless GET) reachable via SSRF = the class; IMDSv2-required = mitigated negative (bank it). Decisive test: SSRF response carrying instance-id/iam-info, or the 401 token-gate — either is a ledger row.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
