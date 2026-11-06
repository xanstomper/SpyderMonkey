# Local storage classes (files, prefs, caches)

- source canon: `spydermonkey/technique-canon-7.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-06

## The technique

Secrets/PII in app files, sqlite dbs, shared prefs, caches readable from your own build (the SPY-013 id-adopted-session family is the session twin). Decisive test: your build's data dump — live secret/PII material = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
