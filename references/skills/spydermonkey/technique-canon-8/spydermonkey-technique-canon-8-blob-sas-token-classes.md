# Blob SAS token classes

- source canon: `spydermonkey/technique-canon-8.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-06

## The technique

SAS tokens in client code: long expiry, wide scope, no IP lock. Decisive test: parsed token's scope/expiry fields = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
