# Service-account token exposure — chain composition

- source canon: `spydermonkey/technique-canon-3.md`
- base technique: `spydermonkey-technique-canon-3-service-account-token-exposur.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

SA tokens in mounts/configmaps/logs readable from the confirmed foothold. Decisive test: token file readable in YOUR test pod/replica — the lab replica proves the class shape; live proof needs the foothold (kaisha-priced).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
