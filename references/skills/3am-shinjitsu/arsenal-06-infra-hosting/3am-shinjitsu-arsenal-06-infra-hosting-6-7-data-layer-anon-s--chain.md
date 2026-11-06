# 6.7 Data-layer anon surfaces (score 80, banner+anon-read only) — chain composition

- source canon: `3am-shinjitsu/arsenal-06-infra-hosting.md`
- base technique: `3am-shinjitsu-arsenal-06-infra-hosting-6-7-data-layer-anon-s.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Redis 6379 (greeting + `INFO` anon), ES 9200 (`/` cluster map, `/_cat/indices`), Kafka/RabbitMQ
  anon produce/consume check (read-only), Mongo 27017 greeting, Memcached 11211 `stats`.
- CONFIRMED WHEN: anon read of ANY data row/index. Write probes = owned only.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
