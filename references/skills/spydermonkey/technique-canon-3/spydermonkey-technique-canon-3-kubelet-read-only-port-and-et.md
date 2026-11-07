# Kubelet read-only port and etcd exposure

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **PTES-CON** · **CWE-250** · **ATT&CK T1610**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

10255 read-only /pods and etcd 2379 without client cert. Decisive test: GET /pods anonymous; etcd /version probe — read-only responses are the findings.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
