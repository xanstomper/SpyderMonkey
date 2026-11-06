# Idempotency-key reuse across intents

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-06

## The technique

The same idempotency key replayed for a DIFFERENT operation that the server accepts = cross-intent replay. Decisive test: key K on op-A then op-B — op-B returns op-A's cached result = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
