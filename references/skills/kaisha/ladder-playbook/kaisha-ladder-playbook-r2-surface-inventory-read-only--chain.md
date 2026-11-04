# R2 — surface inventory (read-only) — chain composition

- source canon: `kaisha/ladder-playbook.md`
- base technique: `kaisha-ladder-playbook-r2-surface-inventory-read-only.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- listening services: address:port + process name (own host)
- banners: exact strings → feed `kaisha cve --banner`

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
