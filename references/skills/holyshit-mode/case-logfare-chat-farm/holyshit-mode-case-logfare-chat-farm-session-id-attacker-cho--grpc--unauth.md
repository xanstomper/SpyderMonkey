# Session-ID attacker-chosen acceptance (score 50, confirmed) — grpc / unauth

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- base technique: `holyshit-mode-case-logfare-chat-farm-session-id-attacker-cho.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **grpc** · auth **unauth** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Server accepts ANY client-supplied `lfc_session` uuid **verbatim** — no entropy check, no re-mint: send `Cookie: lfc_session=11111111-2222-4333-8444-555566667777` and the server persists it via Set-Cookie, then creates conversations + settings on the chosen id. Cookie-fixation class; brute is closed (uuid v4, 122-bit) but issuance has zero integrity. Weaponization needs an injection vector or parent-domain cookie-toss (sibling subdomain setting cookies for `.logfare.ai`) — subdomain sweep is the open follow-up.

## Probe adjustment (grpc × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
