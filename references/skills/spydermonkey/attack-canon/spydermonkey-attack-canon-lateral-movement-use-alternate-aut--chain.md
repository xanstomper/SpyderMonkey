# Lateral Movement Use Alternate Authentication Material (T1550) — chain composition

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-lateral-movement-use-alternate-aut.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- class: pass-the-hash/ticket, session hijack
- probe: session-id enumeration class only (sequential/weak ids — CWE-384)
- wall: the SESSION tester proves structure weakness; no replay against prod

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
