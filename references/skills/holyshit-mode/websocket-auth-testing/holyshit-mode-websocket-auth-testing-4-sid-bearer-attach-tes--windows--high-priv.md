# 4. Sid bearer-attach test — windows / high-priv

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-4-sid-bearer-attach-tes.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **windows** · auth **high-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: token/session confusion classes; read-only enumeration, NO-GAIN
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

engine.io sessions authenticate by sid alone unless the app binds them server-side:
open a SECOND websocket against a LIVE session's sid (`?...&sid=<victim sid>`).
`101 Switching Protocols` + answered pings = the sid is a single-secret bearer
credential. The websocket Origin allowlist is client-asserted (header VALUE
comparison at handshake) — trivially faked from non-browser clients, so it does not
protect the session. A leaked sid (access logs, any reflection) on an AUTHED socket
= full event-stream takeover. Remediation to state: bind socket sessions to the HTTP
session cookie server-side (reject connections whose cookie doesn't match the
handshake session).

## Probe adjustment (windows × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
