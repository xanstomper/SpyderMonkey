# 6. sid = bearer credential (attach test) — host / low-priv

- source canon: `holyshit-mode/engineio-socketio-testing.md`
- base technique: `holyshit-mode-engineio-socketio-testing-6-sid-bearer-credent.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **host** · auth **low-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- A second websocket using an EXISTING sid attaches to that session (101 accepted, ping answered). The origin allowlist is client-asserted — it stops cross-site browser JS, NOT a scripted attacker who fakes the header.
- Mechanism test: obtain a live sid (page-context hook capturing socket OPEN frames, or your own session), attach a second socket from python, send `2` (v2 ping), expect pong. Do NOT emit application frames on an attached session.
- Impact gate: only AUTHED sockets carry personal events — the sid-attach is the mechanism finding; severity lives in what rides authed sessions.

## Probe adjustment (host × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
