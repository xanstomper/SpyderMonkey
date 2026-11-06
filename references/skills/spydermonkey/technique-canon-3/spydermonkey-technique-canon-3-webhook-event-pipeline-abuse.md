# Webhook/event pipeline abuse

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-06

## The technique

Unsigned or replayable events (the SPY-102 class family) — event-name freedom + spoofed actor ids poisoning downstream automation. Decisive test: accepted event with a spoofed field on a test endpoint — the acceptance is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
