# holyleadger chain-splitter gotcha — chain composition

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- base technique: `holyshit-mode-case-experientiallabs-gateway-dual-surface-hol.md`
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

`chain <jewel> "A→B→C:confirmed"` splits steps on the unicode `→` via
`steps_status.rpartition(":")`. If the arg arrives with the arrow mangled or with no valid
`:status` suffix, the chain records `steps:[""]` (1 empty step) — appears to "work" (rc 0)
but is empty. Reliable workaround: write `data["chains"]` directly into the ledger JSON, or
pass the chain string through Python (not a shell that may mangle `→`). Don't burn time on
the CLI quirk mid-engagement; set the chain by hand in the JSON.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
