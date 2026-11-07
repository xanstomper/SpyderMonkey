# 2. Capture the live game feed unauth — worker / root

- source canon: `holyshit-mode/provably-fair-verification.md`
- base technique: `holyshit-mode-provably-fair-verification-2-capture-the-live-.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **worker** · auth **root** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

- Find the game's websocket namespace (socket.io `/crash`, `/dice`, ... — see
  references/websocket-auth-testing.md for namespace discovery and rejection semantics).
- Listen ≥ full round cycles (~20-40s each; a 10s window catches only ticks).
- Record EVERY event + payload. socket.io events may split across engine.io frames —
  buffer raw bytes for the window and parse with a frame state machine; naive
  per-recv JSON parses fail at ~4KB TCP boundaries and produce phantom truncations.

## Probe adjustment (worker × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
