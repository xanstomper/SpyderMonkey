# SDR capture classes (lab) — chain composition

- source canon: `spydermonkey/technique-canon-5.md`
- base technique: `spydermonkey-technique-canon-5-sdr-capture-classes-lab.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Rolling-code capture-replay characterization on YOUR OWN remotes — documented class, lab proof only. The deliverable is the mechanism writeup.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
