# The two stores — chain composition

- source canon: `spydermonkey/ledger-dump.md`
- base technique: `spydermonkey-ledger-dump-the-two-stores.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. **Holyleadger** — `~/.hermes/scripts/holyleadger/<domain>.json`, one file per TARGET DOMAIN.
2. **Campaign ledgers** — `~/.redteam/campaigns/<target>/ledger.jsonl`, one per CAMPAIGN DIR.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
