# Webhook SSRF and replay

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-06

## The technique

User-registered webhooks pointing at internal ranges (SSRF class) and unsigned webhook payloads (replay/forge class). Decisive test: webhook delivered to YOUR listener (SSRF proof), or a replayed payload accepted twice (replay proof).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
