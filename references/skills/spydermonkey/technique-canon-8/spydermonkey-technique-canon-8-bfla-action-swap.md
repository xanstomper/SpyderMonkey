# BFLA action-swap

- source canon: `spydermonkey/technique-canon-8.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-06

## The technique

An action endpoint (export/invite/execute) executes for a lower-priv principal. Decisive test: the action POST replayed with the low-priv token — acceptance = the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
