# 1.6 Nuclei exposure sweep (score 70, T≈4min, ceiling 1 run) — chain composition

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-1-6-nuclei-exposure-sw.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- DECISIVE: `nuclei -u https://<target> -tags cve,exposure,panel -rl 10 -severity medium,high,critical -silent`
- RULE: one run, rate-limited. Never re-run without a target change (ledger).
- FP: template matches on CDN-edge paths — verify each match by hand before verdict.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
