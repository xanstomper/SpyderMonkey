# OTP multi-submit race

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-06

## The technique

The verify endpoint that accepts concurrent submits can validate one OTP across N sessions. Decisive test: same OTP payload fanned to 5 parallel requests with distinct session tokens — >1 success = the class. The race is measured in the lab replica first (dojo replica reproduces the semantics).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
