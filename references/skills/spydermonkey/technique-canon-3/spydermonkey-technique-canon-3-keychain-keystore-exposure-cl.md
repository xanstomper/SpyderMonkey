# Keychain/keystore exposure class

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## The technique

Secrets in keychain SharedPreferences/UserDefaults readable post-install. Decisive test: your own build's storage dump — live secret material = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
