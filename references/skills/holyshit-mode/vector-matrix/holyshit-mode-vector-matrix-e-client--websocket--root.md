# E. CLIENT — websocket / root

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-e-client.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **websocket** · auth **root** · chain role **pivot**

## Route

- probes: `dalfox`, `xsstrike`, `xsser`
- chains: `web`, `api`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

- XSS: stored/reflected/DOM, every sink (innerHTML, eval, document.write, postMessage targets)
- postMessage: wildcard targetOrigin, unvalidated origin on receive
- DOM clobbering / CSS injection / clickjacking (missing XFO/frame-ancestors)
- Sourcemaps deployed (.map) — full source recovery
- Service worker / cache poisoning of asset URLs
- Client-side secrets: API keys, feature flags, internal hostnames in bundles
- Dependency rot: dead third-party scripts/invites/widgets (hijackable references)

## Probe adjustment (websocket × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
