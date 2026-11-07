# 3. Namespace mapping

- source canon: `holyshit-mode/engineio-socketio-testing.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Send `40/nsp,` (v4; v2 accepts with/without trailing comma). The bare `40` = engine ack; the namespace ack FOLLOWS — wait 2-4s and read frames in order. `40/nsp,` = LIVE; `44/nsp,"Invalid namespace"` = rejected.
- Live namespaces push an initialize/state event on connect (leaderboards, players online, prize data) — capture it; it is often the most data-rich unauth feed on the platform.
- Fuzz extra names (`/admin`, `/mod`, `/staff`, `/internal`, `/prediction`, `/sports`) — expect `44` on hardened stacks; log as negative coverage.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
