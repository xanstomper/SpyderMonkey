# 1.4 EOL-panel port banner set (score 85, banner-only) — chain composition

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-1-4-eol-panel-port-ban.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- DECISIVE: one connect + read per port, 5s timeout: 21, 25, 110, 143, 3306, 5432, 6379,
  8083, 9200, 2379, 10250, 5984
- SIGNATURES: `:8083` title "Vesta"/"Hestia" (EOL panel); `:3306` greeting `5.5.x`/`5.6.x`
  MariaDB/MySQL (EOL 2018/2020, internet-reachable = the finding); `6379` Redis greeting
  (anon = instant read class); `9200` ES cluster name; `2379` etcd; `10250` kubelet.
- HARD RULE: greeting/banner read only. Zero credentialed attempts without RoE.
- CONFIRMED WHEN: EOL service + internet-reachable + version leaks in banner.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
