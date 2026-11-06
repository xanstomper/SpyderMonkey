# Cookie jar depth — chain composition

- source canon: `spydermonkey/technique-canon-6.md`
- base technique: `spydermonkey-technique-canon-6-cookie-jar-depth.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

__Host- enforcement (canon-I), SameSite=None sprawl, cookie-count overflow eviction (forced-logout class), chstate/confusion via name collisions. Decisive test: your own cookie jar manipulations in the lab browser — the eviction/collision behavior is the finding.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
