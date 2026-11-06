# ConfigMap/Secret exposure

- source canon: `spydermonkey/technique-canon-8.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## The technique

Sensitive material in ConfigMaps (not Secrets) readable cluster-wide. Decisive test: your own namespace's cm listing = the row.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
