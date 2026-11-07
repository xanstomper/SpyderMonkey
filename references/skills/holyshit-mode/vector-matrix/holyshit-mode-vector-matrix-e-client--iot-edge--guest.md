# E. CLIENT — iot-edge / guest

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-e-client.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **iot-edge** · auth **guest** · chain role **pivot**

## Route

- probes: `dalfox`, `xsstrike`, `xsser`
- chains: `web`, `api`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: device-adjacent runtime at the edge — own devices, lab network
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- XSS: stored/reflected/DOM, every sink (innerHTML, eval, document.write, postMessage targets)
- postMessage: wildcard targetOrigin, unvalidated origin on receive
- DOM clobbering / CSS injection / clickjacking (missing XFO/frame-ancestors)
- Sourcemaps deployed (.map) — full source recovery
- Service worker / cache poisoning of asset URLs
- Client-side secrets: API keys, feature flags, internal hostnames in bundles
- Dependency rot: dead third-party scripts/invites/widgets (hijackable references)

## Probe adjustment (iot-edge × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
