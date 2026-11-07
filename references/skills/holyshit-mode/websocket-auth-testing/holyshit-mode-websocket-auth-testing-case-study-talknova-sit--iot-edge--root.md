# Case Study: talknova.site (2026-10-04) — iot-edge / root

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-case-study-talknova-sit.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **iot-edge** · auth **root** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: device-adjacent runtime at the edge — own devices, lab network
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

- WebSocket at `/api/voice/socket` accepts 101 upgrade with NO auth headers.
- First frame without valid token → server sends CLOSE 1008 (Policy Violation).
- Auth flow: `POST /api/voice/session` → returns `{token, usage}` → client opens
  WS → first frame is `{type:"authenticate", token: r.token}` → server replies
  `{type:"ready"}`.
- `/api/voice/session` is properly auth-gated: 401 "Sign in to use Voice Mode"
  with uniform error regardless of body shape.
- **Result**: no auth bypass; WebSocket auth is correctly token-bound.

## Probe adjustment (iot-edge × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
