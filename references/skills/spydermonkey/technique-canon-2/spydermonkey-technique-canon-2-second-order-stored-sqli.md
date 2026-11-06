# Second-order stored SQLi

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-INPV-05** · **CWE-89** · **ATT&CK T1190**
- generated: 2026-11-06

## The technique

Payload stored in profile/asset fields, executed by a LATER query (admin render, export job). Decisive test: your own stored payload flipping an error class in a downstream render you can read — the downstream context is the proof.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
