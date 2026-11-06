# Coverage mapping to the ten surface classes — chain composition

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-coverage-mapping-to-the-ten.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Existing class | Universal domains |
|---|---|
| 1 Network/Edge | U01, U02 |
| 2 Web app | U03 |
| 3 API | U04 |
| 4 Auth/Identity | U05 |
| 5 Client-side | U06 |
| 6 Infra/Hosting | U07, U08, U09 |
| 7 Supply-chain/Deps | U10 |
| 8 Human/Identity | U11, U12, U16 |
| 9 Breach/OSINT | U01, U10, U11, U14, U15 |
| 10 LLM/AI | U13 |

The universal file expands coverage without weakening the ten-class contract. An
engagement may merge domains in its ledger, but all sixteen must be probed or N/A'd.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
