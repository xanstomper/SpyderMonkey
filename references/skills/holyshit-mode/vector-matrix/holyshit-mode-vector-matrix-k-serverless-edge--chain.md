# K. SERVERLESS / EDGE — chain composition

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-k-serverless-edge.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Cloudflare Workers: KV/D1/R2 exposure via misrouted routes, secret env-var leakage
- Lambda/Cloud Functions: env-var secrets, IAM over-permission, cold-start side-channels
- Edge functions: geo-IP bypass, header-based routing confusion, A/B test poisoning
- CDN cache poisoning: unkeyed input in cache keys, X-Forwarded-* trust
- Serverless persistence: event rules, cron triggers, queue poison-pill messages
- WASM sandbox escapes: memory-corruption in edge runtimes (operator's own deployments)
- Durable objects / stateful edge: cross-tenant state leakage via ID prediction

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
