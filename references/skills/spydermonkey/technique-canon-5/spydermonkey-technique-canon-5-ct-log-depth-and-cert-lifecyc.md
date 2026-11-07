# CT-log depth and cert-lifecycle intel

- source canon: `spydermonkey/technique-canon-5.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Precertificates naming internal tiers, revoked-expired certs mapping retired infra, SAN-mining (canon-I) — the lifecycle timeline IS the inventory. Decisive test: log query + live-cert SAN diff.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
