# Results (negatives are results — log them) — chain composition

- source canon: `holyshit-mode/case-talknova-hardened.md`
- base technique: `holyshit-mode-case-talknova-hardened-results-negatives-are-r.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `dalfox`, `xsstrike`, `xsser`
- chains: `web`, `api`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- CORS arbitrary origin+credentials: NEGATIVE (hard origin lock on all cookie endpoints).
- OAuth state/PKCE/open-redirect/replay: NEGATIVE (textbook hardening).
- Rate limiting on /api/admin/login: CONFIRMED WORKING (4 fails → 429, 30-min decay).
- Authz on admin surface: NEGATIVE (all endpoints 401 without session).
- IDOR on admin user/grant/custom-key endpoints: NEGATIVE (401 on all unauth attempts).
- SQLi/NoSQLi on admin login: NOT TESTED (rate limiter locked us out first).
- Ghost routes: all /api 404s are `application/json` — real routing.
- Backdoors: no client-side ID hardcodes or role gates in the bundle.
- CSP: hash/nonce lockdown; no obvious XSS delivery channel.
- API key auth: NEGATIVE (/v1/models 401 without Bearer).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
