# 7.2 Abandoned deps (score 70) — chain composition

- source canon: `3am-shinjitsu/arsenal-07-supply-chain.md`
- base technique: `3am-shinjitsu-arsenal-07-supply-chain-7-2-abandoned-deps-sco.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Bundle imports of unmaintained libs (last release >2y) with known CVE classes; dead CDN
  scripts (→ §5.6 hijackable references); `@deprecated` admin scaffolding left deployed.
- DECISIVE: version pin in lockfile/bundle header → advisory cross-check.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
