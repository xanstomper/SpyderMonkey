# D2 — SHADOW-SURFACE — chain composition

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-d2-shadow-surface.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Probe | Test | Confirmed-when |
|---|---|---|
| route fuzz | documented conventions + wordlist on declared origin (chunked) | undocumented route answers |
| verb misuse | OPTIONS/PUT/PATCH/DELETE on documented routes | unexpected handler branch |
| legacy/versioned | /v1 /v2, /admin, /internal from bundle strings + CT history | legacy route live |
| method-of-admin | bundle/admin docs revealing internal call shapes | internal endpoint reachable |
| debug telemetry | /metrics /health /debug /actuator-class endpoints | info-leak/exec surface |

One request per candidate; bulk fuzz chunked within family noise budgets.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
