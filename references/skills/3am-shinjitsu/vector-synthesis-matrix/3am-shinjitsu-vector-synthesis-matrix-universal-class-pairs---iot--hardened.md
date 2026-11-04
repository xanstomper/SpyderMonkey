# Universal-class pairs — families 13–20 (non-web compromise battery) — iot / hardened

- source canon: `3am-shinjitsu/vector-synthesis-matrix.md`
- base technique: `3am-shinjitsu-vector-synthesis-matrix-universal-class-pairs-.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **iot** · auth **hardened** · chain role **pivot**

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

Every row: decisive test · confirmed-when · field canon. All read-only or
minimal-proof; documented-PoC adaptation only (§15 wall). Load
`universal-coverage.md` §Per-domain decisive tests for the full battery per U-domain.

| Flaw | Seam | Synthesized probe (decisive one-liner) | Confirmed-when | ★ Correlate |
|---|---|---|---|---|
| 13 | K | Public bucket listing: `GET <bucket>?list-type=2` without creds | 200 + object keys with no identity | public-bucket canon (S3/Azure/GCS) |
| 13 | K | IAM privesc path: policy diff for AssumeRole/PassRole abuse | owned identity can escalate | IAM privesc canon (Rhino) |
| 13 | H | Cross-account role assumption: staging identity → prod role | prod reachable from staging | multi-account canon |
| 14 | M | SNMP public walk: `snmpget -v2c -c public` sysDescr | OID values without auth | SNMP canon |
| 14 | M | NFS: `showmount -e` + root-squash state | world-readable export | NFS canon |
| 14 | M | SMB anonymous: `smbclient -N -L //host` | share listing without creds | SMB NULL-session canon |
| 14 | M | VNC/RDP pre-auth handshake auth-type negotiation | None/Plain accepted | RDP/VNC canon |
| 15 | M | Redis anon: connect :6379 → `INFO` | server info without auth | Redis unauth canon |
| 15 | M | Elasticsearch anon: `GET :9200/_cluster/health` + `_cat/indices` | 200 + indices without creds | ES canon |
| 15 | M | Mongo anon (operator-owned only): no-auth connect, list dbs | db list without creds | Mongo canon |
| 15 | L | Backup exposure: web-adjacent `.bak/.sql/.gz/dump` paths | dump readable unauth | backup-leak canon |
| 16 | L | Deep-link tampering: exported activity launch, no permission (owned devices) | activity starts w/o permission | Android exported-activity canon |
| 16 | L | Update-path trust: unsigned/plaintext update package | tamperable artifact | mobile update canon |
| 17 | L | Firmware extraction: update pkg → strings/secrets (operator-provided) | creds/keys in image | firmware autopsy canon |
| 17 | L | Default creds on network gear (vendor lists) | admin login on default | default-creds canon (routerpwn class) |
| 18 | N | WPS PIN brute feasibility: enabled + no lockout (hardware access) | WPS active, no rate-limit | WPS canon |
| 18 | N | Open pairing/broadcast: inquiry without auth | discoverable + auth-free | BT/BLE canon |
| 19 | N | Unauth webhook registration/fetch: URL as SSRF | registration accepts internal URL | webhook-SSRF canon |
| 19 | N | OAuth app over-grant: full-tenant scopes on install | grant > app need | OAuth app-grant canon |
| 20 | O | kubelet unauth: `GET :10250/pods` | pod list without creds | kubelet canon (CVE-2020-8554 class) |
| 20 | O | etcd unauth (operator-owned): `GET :2379/version` + keys | keys readable | etcd canon |
| 20 | O | Docker socket: `GET :2375/containers/json` | container list unauth | Docker API canon |
| 20 | O | Grafana/Prometheus anon: `/api/status`, `/metrics` | dashboards/metrics unauth | observability canon |

Rule: a positive on ANY of these = OP-ESCALATE immediately (the consumer hunt:
bucket keys → credentials; kubelet pods → service tokens; firmware creds →
device pivot; webhook SSRF → internal plane). A compromise without the
consumer hunt is a half-finished chain.

## Probe adjustment (iot × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
