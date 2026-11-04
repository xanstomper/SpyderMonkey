# WSTG-APIT-02 Rate Limiting

- source canon: `spydermonkey/wstg-deep-canon.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-04

## The technique

- class: missing/naive rate limits
- probe: 3-request timing differential on the lab replica — the limit SHAPE, never a flood
- wall: proof is the missing counter, not an outage

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
