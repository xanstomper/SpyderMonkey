# SRI/CSP posture on third-party integrations

- source canon: `spydermonkey/technique-canon-5.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- generated: 2026-11-06

## The technique

Script integrations without SRI + CSP none = the injection amplifier (SPY-056 class). Decisive test: header posture + script-tag audit of the live page — the posture row is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
