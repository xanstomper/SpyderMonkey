# D3 — PROTOCOL — chain composition

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-d3-protocol.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Class (documented) | Crafted input (Δ) | Confirmed-when |
|---|---|---|
| parsing ambiguity | double-encoded/overlapping tokens in declared formats | server consumes two meanings |
| deserialization class | type-confused field in declared schema | unexpected object/error path |
| length/precision | boundary ints, negative/NaN, max-precision floats | divergent handling |
| split/merge race | concurrent chunked submits on the same logical unit | duplicate/desync accepted |
| state machine | out-of-order transitions on declared flows | illegal-but-accepted state |

Δ must state the class + the modification. Never craft for unknown parser internals
beyond observed behavior (black-box adaptation stays within documented classes).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
