# Negative and fractional quantity

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Quantity=-1 or 0.5 submitted to a cart/checkout inverts the math server-side. Decisive test: quantity=-1 on the cheapest line, read the recalculated total — negative TOTAL is the crown; rejected = bank the negative.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
