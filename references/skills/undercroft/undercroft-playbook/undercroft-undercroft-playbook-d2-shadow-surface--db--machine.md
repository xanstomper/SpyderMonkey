# D2 — SHADOW-SURFACE — db / machine

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-d2-shadow-surface.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **db** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the engine's own handshake/banner first — auth-stage reachability is the inventory row
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| route fuzz | documented conventions + wordlist on declared origin (chunked) | undocumented route answers |
| verb misuse | OPTIONS/PUT/PATCH/DELETE on documented routes | unexpected handler branch |
| legacy/versioned | /v1 /v2, /admin, /internal from bundle strings + CT history | legacy route live |
| method-of-admin | bundle/admin docs revealing internal call shapes | internal endpoint reachable |
| debug telemetry | /metrics /health /debug /actuator-class endpoints | info-leak/exec surface |

One request per candidate; bulk fuzz chunked within family noise budgets.

## Probe adjustment (db × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
