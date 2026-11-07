# R4 — Trial/TTL boundary crossing (SaaS/booking/anything time-gated) — chain composition

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-r4-trial-ttl-boundary-crossin.md`
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

1. Map the documented boundary: trial end, grace period, token TTL.
2. Fire the gated action at boundary−1s, boundary+1s (clock skew only on
   infrastructure you control).
3. CONFIRMED when expired-but-accepted (or pre-expiry grant) occurs.
4. Reverse: revert the granted state. `craft` as TIME, `export`.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
