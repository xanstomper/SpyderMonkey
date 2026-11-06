# MongoDB unauth (27017) — the classic

- source canon: `spydermonkey/technique-canon-4.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

No auth = full read exposure class. Decisive test: `mongosh --host` list-databases — inventory only; never write. A 200-ish auth-less listing = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
