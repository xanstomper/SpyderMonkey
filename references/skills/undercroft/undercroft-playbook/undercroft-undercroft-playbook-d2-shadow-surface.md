# D2 — SHADOW-SURFACE

- source canon: `undercroft/undercroft-playbook.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| route fuzz | documented conventions + wordlist on declared origin (chunked) | undocumented route answers |
| verb misuse | OPTIONS/PUT/PATCH/DELETE on documented routes | unexpected handler branch |
| legacy/versioned | /v1 /v2, /admin, /internal from bundle strings + CT history | legacy route live |
| method-of-admin | bundle/admin docs revealing internal call shapes | internal endpoint reachable |
| debug telemetry | /metrics /health /debug /actuator-class endpoints | info-leak/exec surface |

One request per candidate; bulk fuzz chunked within family noise budgets.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
