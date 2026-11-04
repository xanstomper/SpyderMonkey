# R4 — Trial/TTL boundary crossing (SaaS/booking/anything time-gated)

- source canon: `undercroft/undercroft-playbook.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-04

## The technique

1. Map the documented boundary: trial end, grace period, token TTL.
2. Fire the gated action at boundary−1s, boundary+1s (clock skew only on
   infrastructure you control).
3. CONFIRMED when expired-but-accepted (or pre-expiry grant) occurs.
4. Reverse: revert the granted state. `craft` as TIME, `export`.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
