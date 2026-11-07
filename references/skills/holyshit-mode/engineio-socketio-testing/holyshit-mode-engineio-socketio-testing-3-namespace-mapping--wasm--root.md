# 3. Namespace mapping — wasm / root

- source canon: `holyshit-mode/engineio-socketio-testing.md`
- base technique: `holyshit-mode-engineio-socketio-testing-3-namespace-mapping.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **wasm** · auth **root** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

- Send `40/nsp,` (v4; v2 accepts with/without trailing comma). The bare `40` = engine ack; the namespace ack FOLLOWS — wait 2-4s and read frames in order. `40/nsp,` = LIVE; `44/nsp,"Invalid namespace"` = rejected.
- Live namespaces push an initialize/state event on connect (leaderboards, players online, prize data) — capture it; it is often the most data-rich unauth feed on the platform.
- Fuzz extra names (`/admin`, `/mod`, `/staff`, `/internal`, `/prediction`, `/sports`) — expect `44` on hardened stacks; log as negative coverage.

## Probe adjustment (wasm × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
