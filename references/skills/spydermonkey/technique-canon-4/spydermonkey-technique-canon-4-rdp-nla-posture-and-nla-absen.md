# RDP/NLA posture and NLA-absent classes

- source canon: `spydermonkey/technique-canon-4.md`
- bindings: **PTES-RA** · **CWE-287** · **ATT&CK T1078**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

NLA required vs not (documented class), banner/tls posture. Decisive test: protocol handshake reaching the NLA stage — the stage reached IS the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
