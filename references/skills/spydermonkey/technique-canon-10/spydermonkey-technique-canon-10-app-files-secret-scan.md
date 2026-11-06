# App-files secret scan

- source canon: `spydermonkey/technique-canon-10.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-06

## The technique

App-private storage (files/, databases/, shared_prefs) holding tokens/PII on your own build. Decisive test: your build's data dump showing live secret material outside keychain.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
