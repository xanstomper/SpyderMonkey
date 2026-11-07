# Kubernetes API anonymous and service-account exposure

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

API server reachable anonymously (system:anonymous binding) or a leaked SA token with cluster-scope list. Decisive test: GET /api/v1/namespaces with the token/anonymous — read-only listing = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
