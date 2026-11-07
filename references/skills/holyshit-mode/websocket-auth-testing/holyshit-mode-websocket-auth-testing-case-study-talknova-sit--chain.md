# Case Study: talknova.site (2026-10-04) — chain composition

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-case-study-talknova-sit.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- WebSocket at `/api/voice/socket` accepts 101 upgrade with NO auth headers.
- First frame without valid token → server sends CLOSE 1008 (Policy Violation).
- Auth flow: `POST /api/voice/session` → returns `{token, usage}` → client opens
  WS → first frame is `{type:"authenticate", token: r.token}` → server replies
  `{type:"ready"}`.
- `/api/voice/session` is properly auth-gated: 401 "Sign in to use Voice Mode"
  with uniform error regardless of body shape.
- **Result**: no auth bypass; WebSocket auth is correctly token-bound.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
