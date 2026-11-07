# WSTG-BUSL-02 Discount and Refund Logic

- source canon: `spydermonkey/wstg-deep-canon.md`
- bindings: **WSTG-BUSL** · **CWE-840** · **ATT&CK T1499**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: negative/refund abuse in order flows
- probe: the BIZLOGIC battery — negative/zero/overflow on the lab checkout replica
- wall: lab replica; live order flows are inventory-only

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
