# Kubernetes API anonymous and service-account exposure — edge-node / service

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-kubernetes-api-anonymous-and-se.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **edge-node** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

API server reachable anonymously (system:anonymous binding) or a leaked SA token with cluster-scope list. Decisive test: GET /api/v1/namespaces with the token/anonymous — read-only listing = the finding.

## Probe adjustment (edge-node × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
