# 4. CORS arbitrary origin reflection (score 72)

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-reengagement.md`
- bindings: **WSTG-CLNT-03** · **CWE-942** · **ATT&CK T1557**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

access-control-allow-origin reflects ALL origins on /v1/* endpoints.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
