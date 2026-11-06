# API scope confusion

- source canon: `spydermonkey/technique-canon-8.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-06

## The technique

Token scopes checked per-endpoint inconsistently. Decisive test: narrow-scope token accepted on a wider endpoint = the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
