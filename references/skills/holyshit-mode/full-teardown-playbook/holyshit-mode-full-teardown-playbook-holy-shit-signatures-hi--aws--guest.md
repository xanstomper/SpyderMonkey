# HOLY SHIT SIGNATURES — highest-yield quick checks (one probe each) — aws / guest

- source canon: `holyshit-mode/full-teardown-playbook.md`
- base technique: `holyshit-mode-full-teardown-playbook-holy-shit-signatures-hi.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **aws** · auth **guest** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: IAM/identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

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

## Probe adjustment (aws × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
