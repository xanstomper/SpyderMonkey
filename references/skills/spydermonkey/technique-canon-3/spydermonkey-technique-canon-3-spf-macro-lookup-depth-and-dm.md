# SPF macro/lookup-depth and DMARC report-only

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## The technique

SPF +all/?all, macro abuse, lookup>10 failures; DMARC p=none with no rua = spoofable-posture. Decisive test: record parse arithmetic — the record IS the evidence (no spoofed mail sent).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
