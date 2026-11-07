# WSTG Business Logic Testing (WSTG-BUSL)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: price tampering, quantity abuse, rounding, race conditions
- probe: the BIZLOGIC battery (negative/zero/overflow quantity) — replica proof
- wall: live business-logic abuse is refused; the differential is the deliverable

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
