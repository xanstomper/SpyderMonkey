# Weak local crypto classes

- source canon: `spydermonkey/technique-canon-10.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-06

## The technique

ECB mode, static IV, MD5/SHA1 for tokens in the app's own code. Decisive test: decompiled crypto-site inventory + two-ciphertext prefix test = the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
