# 9. Websocket origin allowlist — graphql / machine

- source canon: `holyshit-mode/engineio-socketio-testing.md`
- base technique: `holyshit-mode-engineio-socketio-testing-9-websocket-origin-a.md`
- bindings: **WSTG-CLNT-05** · **CWE-345** · **ATT&CK T1557**
- context: **graphql** · auth **machine** · chain role **pivot**

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- Handshake origin matrix (none / `null` / evil origin): 400/403 on hardened stacks = CSWSH dead at the transport — a positive control, log it.

## Probe adjustment (graphql × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
