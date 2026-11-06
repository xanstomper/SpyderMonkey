# CT-log depth and cert-lifecycle intel — chain composition

- source canon: `spydermonkey/technique-canon-5.md`
- base technique: `spydermonkey-technique-canon-5-ct-log-depth-and-cert-lifecyc.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Precertificates naming internal tiers, revoked-expired certs mapping retired infra, SAN-mining (canon-I) — the lifecycle timeline IS the inventory. Decisive test: log query + live-cert SAN diff.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
