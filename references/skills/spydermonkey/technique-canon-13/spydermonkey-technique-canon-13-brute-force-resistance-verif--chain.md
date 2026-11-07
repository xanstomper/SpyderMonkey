# Brute-force-resistance verification — chain composition

- source canon: `spydermonkey/technique-canon-13.md`
- base technique: `spydermonkey-technique-canon-13-brute-force-resistance-verif.md`
- chain role: **final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Lockout/rate geometry measured (the canon-I discipline). Decisive test: the counter/lock TTL map = the control's presence/absence.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
