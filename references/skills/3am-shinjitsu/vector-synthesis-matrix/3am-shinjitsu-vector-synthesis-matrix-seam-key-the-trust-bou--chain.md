# Seam key (the trust boundaries that define input position) — chain composition

- source canon: `3am-shinjitsu/vector-synthesis-matrix.md`
- base technique: `3am-shinjitsu-vector-synthesis-matrix-seam-key-the-trust-bou.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Seam | Boundary | Test signature |
|---|---|---|
| A | CDN↔origin | direct-origin reach, WAF vs app behavior split |
| B | Client↔server validation | UI gate vs API enforcement divergence |
| C | Auth↔backend binding | mint vs consumer trust roots (session vs key) |
| D | Limiter↔coercion | counting vs parsing divergence |
| E | WS handshake↔frame auth | 101 passthrough vs gated frames |
| F | OAuth provider↔app | redirect_uri/state binding, callback taxonomy |
| G | Edge-function↔DB | function trust vs RLS scope split |
| H | Multi-host family | sister brands, staging, dead-DNS-live-cert |
| I | i18n/asset plane | chunk subset, env-object, template-literal paths |
| J | LLM layer | shared buffers vs per-request state |
| K | Cloud-policy | object-store / IAM policy vs enforcement gap |
| L | Device-firmware | console/OTA/update path vs signed trust |
| M | Protocol-handshake | network services' pre-auth handshake |
| N | Collab-app | webhook/grant registration trust |
| O | Monitoring-plane | orchestration/monitoring reachable anonymously |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
