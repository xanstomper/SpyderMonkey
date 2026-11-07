# Hygiene — wasm / high-priv

- source canon: `kairo/synthesis-engine.md`
- base technique: `kairo-synthesis-engine-hygiene.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **wasm** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Vectors are marked `distributed` after a supply drop — never double-shipped.
- EXHAUSTED findings never enter the queue (negatives don't synthesize).
- Every compiled attack inherits its source finding's P0 scope. No scope, no ship.

## Probe adjustment (wasm × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
