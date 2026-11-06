# Refund/partial-refund idempotency

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-06

## The technique

A refund endpoint without idempotency key dedupe re-issues on retry. Decisive test: identical refund request twice on a test order (sandbox) — second success vs idempotent replay = the class. This is REPLAY canon: same key, server state advanced twice.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
