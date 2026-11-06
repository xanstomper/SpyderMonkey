# DKIM key length and selector hygiene

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-06

## The technique

DKIM RSA key < 1024 bits or stale selectors pointing at dead infra. Decisive test: selector DNS lookup + published key size parse = the posture finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
