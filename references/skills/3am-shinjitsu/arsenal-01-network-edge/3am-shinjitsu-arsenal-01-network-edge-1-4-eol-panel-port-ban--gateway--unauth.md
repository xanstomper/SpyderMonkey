# 1.4 EOL-panel port banner set (score 85, banner-only) — gateway / unauth

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-1-4-eol-panel-port-ban.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **gateway** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- DECISIVE: one connect + read per port, 5s timeout: 21, 25, 110, 143, 3306, 5432, 6379,
  8083, 9200, 2379, 10250, 5984
- SIGNATURES: `:8083` title "Vesta"/"Hestia" (EOL panel); `:3306` greeting `5.5.x`/`5.6.x`
  MariaDB/MySQL (EOL 2018/2020, internet-reachable = the finding); `6379` Redis greeting
  (anon = instant read class); `9200` ES cluster name; `2379` etcd; `10250` kubelet.
- HARD RULE: greeting/banner read only. Zero credentialed attempts without RoE.
- CONFIRMED WHEN: EOL service + internet-reachable + version leaks in banner.

## Probe adjustment (gateway × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
