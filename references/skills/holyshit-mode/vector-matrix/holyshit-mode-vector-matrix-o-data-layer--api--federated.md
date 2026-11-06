# O. DATA LAYER — api / federated

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-o-data-layer.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **api** · auth **federated** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- Graph databases: Cypher injection, traversal-based authz bypass
- Time-series: InfluxDB/Prometheus unauthenticated writes, metric poisoning
- Vector DBs: embedding-space manipulation, nearest-neighbor authz leaks
- Message queues: Kafka/RabbitMQ anonymous produce/consume, poison-pill injection
- Caches: Redis unauthenticated access, cache-key prediction, cache-side-channel leaks
- Search engines: Elasticsearch anonymous access, index-level authz gaps

## Probe adjustment (api × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
