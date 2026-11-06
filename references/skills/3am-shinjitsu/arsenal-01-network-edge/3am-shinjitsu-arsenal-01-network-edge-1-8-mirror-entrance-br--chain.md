# 1.8 Mirror/entrance brands (score 70) — chain composition

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-1-8-mirror-entrance-br.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- PATTERN: `tr.<brand>`, `giris.<brand>` (TR entrance pattern), `<lang>.<brand>`,
  `<brand>-<market>` — separate hosting from CT logs + passive DNS.
- CONFIRMED WHEN: mirror on different ASN/IP-family than main = un-CDN'd, un-WAF'd surface.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
