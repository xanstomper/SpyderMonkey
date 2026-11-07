# 3. Synthetic sockets: websocket transport only — graphql / guest

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-3-synthetic-sockets-web.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **graphql** · auth **guest** · chain role **pivot**

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

Sequential HTTP polling from a script dies on CDN node affinity — each request lands
on a different backend and the in-memory session returns `"Session ID unknown"`.
One long-lived websocket connection is immune. And on EIO=3 the websocket-FIRST
handshake works with NO polling pre-step: `GET /socket.io/?EIO=3&transport=websocket`
(no sid) returns 101 and the server pushes `0{"sid":...}` as the first frame — own
session in one connection, no affinity problem. (Synthetic `io=<sid>` cookies do NOT
fix polling affinity — the cookie is not honored by the routing layer.)

## Probe adjustment (graphql × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
