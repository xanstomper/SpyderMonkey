# XXE → SSRF pivot (metadata)

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-INPV-10** · **CWE-918** · **ATT&CK T1190**
- generated: 2026-11-06

## The technique

External entity aimed at 169.254.169.254 = the cloud-pivot class. Decisive test: entity response carrying instance metadata — the pivot is characterized read-only.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
