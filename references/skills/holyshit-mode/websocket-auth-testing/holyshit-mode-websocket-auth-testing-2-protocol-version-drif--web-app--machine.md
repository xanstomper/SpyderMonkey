# 2. Protocol-version drift — test BOTH EIO versions — web-app / machine

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-2-protocol-version-drif.md`
- bindings: **WSTG-CLNT-05** · **CWE-345** · **ATT&CK T1557**
- context: **web-app** · auth **machine** · chain role **pivot**

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

Servers frequently expose socket.io v2 (`EIO=3`) AND v4 (`EIO=4`) simultaneously,
and the production client often speaks the OLDER one. Synthetic testing against the
wrong protocol version tests a surface the real app doesn't use. Grab the production
URL from page traffic (`wss://host/socket.io/?EIO=3&transport=websocket&sid=...`)
and mirror its version.

## Probe adjustment (web-app × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
