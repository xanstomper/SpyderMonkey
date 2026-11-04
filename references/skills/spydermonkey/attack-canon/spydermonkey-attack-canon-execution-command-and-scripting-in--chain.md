# Execution Command and Scripting Interpreter (T1059) — chain composition

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-execution-command-and-scripting-in.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- class: shell/powershell/python interpreters as the execution primitive
- probe: the cmd-injection battery (`;id`, `$(id)`, backticks) — echo differential only
- wall: proof = a benign marker echoed; never a destructive command

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
