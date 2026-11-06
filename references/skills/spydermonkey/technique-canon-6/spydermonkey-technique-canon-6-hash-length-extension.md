# Hash length-extension

- source canon: `spydermonkey/technique-canon-6.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-06

## The technique

HMAC-less `hash(secret||data)` schemes fall to length extension — the class is the MAC construction, tested against YOUR OWN captured token pair in the lab.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
