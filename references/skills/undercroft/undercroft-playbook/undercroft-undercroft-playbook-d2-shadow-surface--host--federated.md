# D2 — SHADOW-SURFACE — host / federated

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-d2-shadow-surface.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **host** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| route fuzz | documented conventions + wordlist on declared origin (chunked) | undocumented route answers |
| verb misuse | OPTIONS/PUT/PATCH/DELETE on documented routes | unexpected handler branch |
| legacy/versioned | /v1 /v2, /admin, /internal from bundle strings + CT history | legacy route live |
| method-of-admin | bundle/admin docs revealing internal call shapes | internal endpoint reachable |
| debug telemetry | /metrics /health /debug /actuator-class endpoints | info-leak/exec surface |

One request per candidate; bulk fuzz chunked within family noise budgets.

## Probe adjustment (host × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
