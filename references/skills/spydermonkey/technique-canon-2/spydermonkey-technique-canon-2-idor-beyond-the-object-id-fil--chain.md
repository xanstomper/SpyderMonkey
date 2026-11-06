# IDOR beyond the object id — filter/sort leakage — chain composition

- source canon: `spydermonkey/technique-canon-2.md`
- base technique: `spydermonkey-technique-canon-2-idor-beyond-the-object-id-fil.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Enumeration via filter operators (`?sort=-balance`) and range queries reading relative order without direct object access. Decisive test: sort/filter on a field across two of YOUR objects revealing a third's rank — the oracle is the finding.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
