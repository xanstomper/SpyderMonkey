# Database plaintext classes

- source canon: `spydermonkey/technique-canon-10.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-06

## The technique

SQLite db inside app data with unencrypted sensitive columns. Decisive test: pulled db row readable — plaintext credential/session material = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
