# holyleadger chain-splitter gotcha

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`chain <jewel> "A→B→C:confirmed"` splits steps on the unicode `→` via
`steps_status.rpartition(":")`. If the arg arrives with the arrow mangled or with no valid
`:status` suffix, the chain records `steps:[""]` (1 empty step) — appears to "work" (rc 0)
but is empty. Reliable workaround: write `data["chains"]` directly into the ledger JSON, or
pass the chain string through Python (not a shell that may mangle `→`). Don't burn time on
the CLI quirk mid-engagement; set the chain by hand in the JSON.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
