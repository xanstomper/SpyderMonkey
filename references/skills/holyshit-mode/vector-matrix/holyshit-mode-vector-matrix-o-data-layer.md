# O. DATA LAYER

- source canon: `holyshit-mode/vector-matrix.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Graph databases: Cypher injection, traversal-based authz bypass
- Time-series: InfluxDB/Prometheus unauthenticated writes, metric poisoning
- Vector DBs: embedding-space manipulation, nearest-neighbor authz leaks
- Message queues: Kafka/RabbitMQ anonymous produce/consume, poison-pill injection
- Caches: Redis unauthenticated access, cache-key prediction, cache-side-channel leaks
- Search engines: Elasticsearch anonymous access, index-level authz gaps

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
