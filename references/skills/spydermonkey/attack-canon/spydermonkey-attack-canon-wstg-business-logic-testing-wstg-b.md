# WSTG Business Logic Testing (WSTG-BUSL)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- generated: 2026-11-04

## The technique

- class: price tampering, quantity abuse, rounding, race conditions
- probe: the BIZLOGIC battery (negative/zero/overflow quantity) — replica proof
- wall: live business-logic abuse is refused; the differential is the deliverable

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
