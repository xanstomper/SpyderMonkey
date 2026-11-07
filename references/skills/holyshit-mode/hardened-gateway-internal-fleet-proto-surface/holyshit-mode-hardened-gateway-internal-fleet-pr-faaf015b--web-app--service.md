# When to use — web-app / service

- source canon: `holyshit-mode/hardened-gateway-internal-fleet-proto-surface.md`
- base technique: `holyshit-mode-hardened-gateway-internal-fleet-proto-surface-.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **web-app** · auth **service** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

A public OpenAI-compatible gateway / LLM platform is **professionally hardened** — every `/v1/*` and
`/api/*` route keyed, Turnstile on all bootstrap, opaque DB sessions, no JWT in bundles, no IDOR on the
pre-auth management API. The compromisable surface then often lives on the operator's **internal
serving fleet**, reachable because (a) it is publicly IP-addressed and (b) a worker-level proto surface
was left unauthenticated while the public edge is keyed.

## Probe adjustment (web-app × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
