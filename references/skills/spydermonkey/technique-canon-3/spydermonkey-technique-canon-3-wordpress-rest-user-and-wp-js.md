# WordPress REST user and wp-json exposure

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-06

## The technique

/api/wp/v2/users leaking identity; wp-json route exposure beyond default. Decisive test: REST users GET anonymous — the enumeration is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
