# Ledger state — container / unauth

- source canon: `holyshit-mode/case-obsidian-y-api-pg-bypass.md`
- base technique: `holyshit-mode-case-obsidian-y-api-pg-bypass-ledger-state.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **container** · auth **unauth** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

`holyleadger` target `obsidian-y-api-r4xe.onrender.com`:
- `pg_chat_unauthenticated_free_ai` confirmed score 90
- `pg_chat_no_rate_limit` confirmed score 70
- `pg_hidden_50k_system_prompt` hypothesis score 55 (decisive next: reasoning-field extraction)
- `pg_stream_passthrough` confirmed score 35
- Chain: `free_ai_abuse`: pg_chat_no_auth → unlimited_completions → no_rate_limit →
  free_upstream_inference (confirmed)

## Probe adjustment (container × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
