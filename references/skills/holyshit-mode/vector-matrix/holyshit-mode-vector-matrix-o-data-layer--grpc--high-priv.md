# O. DATA LAYER — grpc / high-priv

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-o-data-layer.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **grpc** · auth **high-priv** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Graph databases: Cypher injection, traversal-based authz bypass
- Time-series: InfluxDB/Prometheus unauthenticated writes, metric poisoning
- Vector DBs: embedding-space manipulation, nearest-neighbor authz leaks
- Message queues: Kafka/RabbitMQ anonymous produce/consume, poison-pill injection
- Caches: Redis unauthenticated access, cache-key prediction, cache-side-channel leaks
- Search engines: Elasticsearch anonymous access, index-level authz gaps

## Probe adjustment (grpc × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
