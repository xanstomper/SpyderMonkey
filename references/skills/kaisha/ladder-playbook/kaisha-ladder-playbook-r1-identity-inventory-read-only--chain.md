# R1 — identity inventory (read-only) — chain composition

- source canon: `kaisha/ladder-playbook.md`
- base technique: `kaisha-ladder-playbook-r1-identity-inventory-read-only.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- whoami-class: current principal, groups count (descriptions only)
- key files: `~/.ssh/` count + fingerprints (never private material)
- env markers: count of credential-bearing vars (names only)

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
