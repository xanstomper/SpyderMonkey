# SWEEP DISCIPLINE — chain composition

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-sweep-discipline.md`
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

- One decisive probe per cell. A negative result IS a result — log it as coverage evidence.
- Escalate only on signal. No blind CVE spam, no spray-and-pray.
- HOLY SHIT = confirmed cell with impact narrative + kill-chain position. Everything else
  is documented coverage.
- All probes respect the mandate scope gate: scoped targets only, non-destructive, revert
  map before any state change, disclosure path for anything outside own infrastructure.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
