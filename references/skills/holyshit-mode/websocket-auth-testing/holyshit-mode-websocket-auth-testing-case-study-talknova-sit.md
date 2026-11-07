# Case Study: talknova.site (2026-10-04)

- source canon: `holyshit-mode/websocket-auth-testing.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- WebSocket at `/api/voice/socket` accepts 101 upgrade with NO auth headers.
- First frame without valid token → server sends CLOSE 1008 (Policy Violation).
- Auth flow: `POST /api/voice/session` → returns `{token, usage}` → client opens
  WS → first frame is `{type:"authenticate", token: r.token}` → server replies
  `{type:"ready"}`.
- `/api/voice/session` is properly auth-gated: 401 "Sign in to use Voice Mode"
  with uniform error regardless of body shape.
- **Result**: no auth bypass; WebSocket auth is correctly token-bound.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
