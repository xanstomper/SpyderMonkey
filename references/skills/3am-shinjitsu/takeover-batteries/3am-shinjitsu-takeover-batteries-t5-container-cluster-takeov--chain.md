# T5 — Container/cluster takeover — chain composition

- source canon: `3am-shinjitsu/takeover-batteries.md`
- base technique: `3am-shinjitsu-takeover-batteries-t5-container-cluster-takeov.md`
- chain role: **final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it**

## Chain roles

- final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- kubelet unauth → pod list → pod token → kube-apiserver (one read-only call with the
  token); Docker socket → exec (one `id`); etcd keys → service-account secrets; registry
  pull → image secrets; CI runner token → pipelines.
- **DECISIVE PROOF:** API server accepts the harvested token read-only, `docker exec id`,
  or etcd key read. Then STOP.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
