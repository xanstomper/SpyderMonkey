# WebAuthn/FIDO classes

- source canon: `spydermonkey/technique-canon-6.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

Origin/RP-ID scoping gaps, challenge entropy, credential-id enumeration, the SPY-101 allowCredentials:[] mint class. Decisive test: ceremony parameters observed on your own enrollment — the scoping delta is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
