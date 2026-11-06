# Subscription/trial entitlement persistence

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-06

## The technique

Client-held entitlement flags trusted server-side (JWT claim, localStorage sync). Decisive test: expired entitlement replayed with the cached flag on YOUR account — acceptance = the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
