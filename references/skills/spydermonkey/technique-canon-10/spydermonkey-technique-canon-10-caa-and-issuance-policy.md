# CAA and issuance policy

- source canon: `spydermonkey/technique-canon-10.md`
- bindings: **WSTG-CONF** · **CWE-693** · **ATT&CK T1014**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

CAA records restricting issuers — absence = issuance-posture row. Decisive test: record fetch = the posture.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
