# 2. Protocol-version drift — test BOTH EIO versions — mobile-api / low-priv

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-2-protocol-version-drif.md`
- bindings: **WSTG-CLNT-05** · **CWE-345** · **ATT&CK T1557**
- context: **mobile-api** · auth **low-priv** · chain role **pivot**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Servers frequently expose socket.io v2 (`EIO=3`) AND v4 (`EIO=4`) simultaneously,
and the production client often speaks the OLDER one. Synthetic testing against the
wrong protocol version tests a surface the real app doesn't use. Grab the production
URL from page traffic (`wss://host/socket.io/?EIO=3&transport=websocket&sid=...`)
and mirror its version.

## Probe adjustment (mobile-api × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
