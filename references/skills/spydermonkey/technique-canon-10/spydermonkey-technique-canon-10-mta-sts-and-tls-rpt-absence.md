# MTA-STS and TLS-RPT absence

- source canon: `spydermonkey/technique-canon-10.md`
- bindings: **WSTG-INFO** · **CWE-359** · **ATT&CK T1584**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Missing policies = downgrade-tolerance posture. Decisive test: policy fetch = the rows.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
