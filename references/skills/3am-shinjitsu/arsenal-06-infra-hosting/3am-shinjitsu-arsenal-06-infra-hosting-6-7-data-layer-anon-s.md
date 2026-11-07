# 6.7 Data-layer anon surfaces (score 80, banner+anon-read only)

- source canon: `3am-shinjitsu/arsenal-06-infra-hosting.md`
- bindings: **WSTG-ADV-01** · **CWE-444** · **ATT&CK T1190**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Redis 6379 (greeting + `INFO` anon), ES 9200 (`/` cluster map, `/_cat/indices`), Kafka/RabbitMQ
  anon produce/consume check (read-only), Mongo 27017 greeting, Memcached 11211 `stats`.
- CONFIRMED WHEN: anon read of ANY data row/index. Write probes = owned only.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
