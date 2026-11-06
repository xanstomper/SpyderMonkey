# Cache and temp leakage

- source canon: `spydermonkey/technique-canon-10.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

Sensitive responses cached to disk caches surviving app close. Decisive test: cache dump after one authenticated action on your build — the response body on disk = the row.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
