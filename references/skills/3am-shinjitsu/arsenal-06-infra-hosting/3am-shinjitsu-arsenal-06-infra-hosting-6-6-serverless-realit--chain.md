# 6.6 Serverless reality check (score 30 → pivot immediately) — chain composition

- source canon: `3am-shinjitsu/arsenal-06-infra-hosting.md`
- base technique: `3am-shinjitsu-arsenal-06-infra-hosting-6-6-serverless-realit.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- No filesystem, no process, no persistence surface = state it ONCE in the ledger and pivot
  to event/state planes: Workers KV/D1/R2 via misrouted routes, Lambda env-var secrets via
  error pages, queue poison-pill classes (read-only), durable-object cross-tenant id prediction.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
