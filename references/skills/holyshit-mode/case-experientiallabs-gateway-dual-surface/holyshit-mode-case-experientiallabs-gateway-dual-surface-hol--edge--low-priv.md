# holyleadger chain-splitter gotcha — edge / low-priv

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- base technique: `holyshit-mode-case-experientiallabs-gateway-dual-surface-hol.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **edge** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: rate/segmentation differences — masscan-class first, then the app layer
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

`chain <jewel> "A→B→C:confirmed"` splits steps on the unicode `→` via
`steps_status.rpartition(":")`. If the arg arrives with the arrow mangled or with no valid
`:status` suffix, the chain records `steps:[""]` (1 empty step) — appears to "work" (rc 0)
but is empty. Reliable workaround: write `data["chains"]` directly into the ledger JSON, or
pass the chain string through Python (not a shell that may mangle `→`). Don't burn time on
the CLI quirk mid-engagement; set the chain by hand in the JSON.

## Probe adjustment (edge × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
