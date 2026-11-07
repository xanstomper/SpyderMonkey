# 1.4 EOL-panel port banner set (score 85, banner-only)

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- DECISIVE: one connect + read per port, 5s timeout: 21, 25, 110, 143, 3306, 5432, 6379,
  8083, 9200, 2379, 10250, 5984
- SIGNATURES: `:8083` title "Vesta"/"Hestia" (EOL panel); `:3306` greeting `5.5.x`/`5.6.x`
  MariaDB/MySQL (EOL 2018/2020, internet-reachable = the finding); `6379` Redis greeting
  (anon = instant read class); `9200` ES cluster name; `2379` etcd; `10250` kubelet.
- HARD RULE: greeting/banner read only. Zero credentialed attempts without RoE.
- CONFIRMED WHEN: EOL service + internet-reachable + version leaks in banner.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
