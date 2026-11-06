# Session resumption and renegotiation posture

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-06

## The technique

Resumption across IPs and insecure renegotiation accepted = posture findings. Decisive test: openssl -reconnect session-reuse behavior, renegotiation error class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
