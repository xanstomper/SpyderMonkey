# 1.10 IP-honoring / limiter keying (score 60) — chain composition

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-1-10-ip-honoring-limit.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- DECISIVE: same request twice, `X-Forwarded-For: 1.2.3.4` vs without — diff response.
- DISCRIMINATOR: CF-fronted → XFF/CF-Connecting-IP from client = **403 error 1000** (they're
  stripped; spoofing impossible). A 1000 IS the finding that limiter is real-IP-keyed.
- CONFIRMED WHEN: non-CF origin honors XFF for rate-limit buckets → rotation bypass.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
