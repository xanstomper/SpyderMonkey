# HOLY SHIT SIGNATURES — highest-yield quick checks (one probe each) — gateway / unauth

- source canon: `holyshit-mode/full-teardown-playbook.md`
- base technique: `holyshit-mode-full-teardown-playbook-holy-shit-signatures-hi.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **gateway** · auth **unauth** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

1. Dangling CNAME → takeover
2. Deployed .map sourcemap → full source
3. Ghost route with no auth (content-type verified)
4. ?token= / ?discord_token= URL param session fixation
5. Metadata endpoint SSRF (169.254.169.254)
6. Stateless claim/verification gate (no server callback anywhere)
7. Client-only payment/credits/permission gate
8. Zero-call-site auth scaffolding (unwired gate = lockout or bypass depending on direction)
9. Public bucket with creds/backups
10. Rate limiter keyed to a header you control (X-Forwarded-For honored = unlimited budget)

## Probe adjustment (gateway × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
