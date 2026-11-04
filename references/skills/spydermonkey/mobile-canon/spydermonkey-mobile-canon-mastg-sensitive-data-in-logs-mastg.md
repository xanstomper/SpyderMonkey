# MASTG Sensitive Data in Logs (MASTG-STORAGE-01)

- source canon: `spydermonkey/mobile-canon.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-04

## The technique

- class: app logging credentials, tokens, PII to logcat
- probe: read the app's own logs on a LAB device; grep for the test account's markers
- wall: lab devices only; no third-party apps touched

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
