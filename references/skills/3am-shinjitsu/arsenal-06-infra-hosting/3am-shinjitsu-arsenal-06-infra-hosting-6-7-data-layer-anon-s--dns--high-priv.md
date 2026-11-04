# 6.7 Data-layer anon surfaces (score 80, banner+anon-read only) — dns / high-priv

- source canon: `3am-shinjitsu/arsenal-06-infra-hosting.md`
- base technique: `3am-shinjitsu-arsenal-06-infra-hosting-6-7-data-layer-anon-s.md`
- bindings: **WSTG-ADV-01** · **CWE-444** · **ATT&CK T1190**
- context: **dns** · auth **high-priv** · chain role **pivot**

## Context

- platform: record/cname surface — the domtake chain starts here
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Redis 6379 (greeting + `INFO` anon), ES 9200 (`/` cluster map, `/_cat/indices`), Kafka/RabbitMQ
  anon produce/consume check (read-only), Mongo 27017 greeting, Memcached 11211 `stats`.
- CONFIRMED WHEN: anon read of ANY data row/index. Write probes = owned only.

## Probe adjustment (dns × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
