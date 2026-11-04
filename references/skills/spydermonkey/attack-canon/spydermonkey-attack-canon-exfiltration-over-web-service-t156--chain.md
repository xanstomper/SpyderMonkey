# Exfiltration Over Web Service (T1567) — chain composition

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-exfiltration-over-web-service-t156.md`
- chain role: **final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- class: data out through trusted clouds
- probe: never exercised; the IMPACT LEG is priced by shukaku instead
- wall: NO-GAIN — exfiltration is priced hypothetically, never performed

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
