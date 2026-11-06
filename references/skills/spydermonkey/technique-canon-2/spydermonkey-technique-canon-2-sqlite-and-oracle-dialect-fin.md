# SQLite and Oracle dialect fingerprints

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-INPV-05** · **CWE-89** · **ATT&CK T1190**
- generated: 2026-11-06

## The technique

`sqlite_version()` inline and `dbms_random`/`utl_http` classes — dialect selection is the recon result itself. Decisive test: version-render or dialect-error delta.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
