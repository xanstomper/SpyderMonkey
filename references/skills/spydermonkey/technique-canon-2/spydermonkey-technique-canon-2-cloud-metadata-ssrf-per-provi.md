# Cloud metadata SSRF per-provider

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-06

## The technique

169.254.169.254 (AWS/Azure/GCP), `metadata.google.internal` — IMDSv2/azure-token enforcement = mitigated negative (bank it). Decisive test: SSRF response carrying instance-id/subscription-id, or the documented refusal.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
