# Dangling client versions

- source canon: `spydermonkey/technique-canon-10.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

Retired app versions/chunks still served exposing old auth shapes. Decisive test: old-version bundle diff vs live = the drift row.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
