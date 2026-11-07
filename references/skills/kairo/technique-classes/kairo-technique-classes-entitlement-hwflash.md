# ENTITLEMENT — HWFLASH

- source canon: `kairo/technique-classes.md`
- bindings: **WSTG-BUSL-05** · **CWE-285** · **ATT&CK T1068**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- ENTITLEMENT
- HWFLASH
- provisioning order — entitlement flag before its check

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
