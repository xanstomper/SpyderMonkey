# E. CLIENT — grpc / unauth

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-e-client.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **grpc** · auth **unauth** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- XSS: stored/reflected/DOM, every sink (innerHTML, eval, document.write, postMessage targets)
- postMessage: wildcard targetOrigin, unvalidated origin on receive
- DOM clobbering / CSS injection / clickjacking (missing XFO/frame-ancestors)
- Sourcemaps deployed (.map) — full source recovery
- Service worker / cache poisoning of asset URLs
- Client-side secrets: API keys, feature flags, internal hostnames in bundles
- Dependency rot: dead third-party scripts/invites/widgets (hijackable references)

## Probe adjustment (grpc × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
