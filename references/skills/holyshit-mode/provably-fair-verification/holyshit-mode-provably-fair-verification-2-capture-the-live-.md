# 2. Capture the live game feed unauth

- source canon: `holyshit-mode/provably-fair-verification.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Find the game's websocket namespace (socket.io `/crash`, `/dice`, ... — see
  references/websocket-auth-testing.md for namespace discovery and rejection semantics).
- Listen ≥ full round cycles (~20-40s each; a 10s window catches only ticks).
- Record EVERY event + payload. socket.io events may split across engine.io frames —
  buffer raw bytes for the window and parse with a frame state machine; naive
  per-recv JSON parses fail at ~4KB TCP boundaries and produce phantom truncations.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
