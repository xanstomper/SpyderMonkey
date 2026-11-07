# Results (negatives are results — log them) — api / low-priv

- source canon: `holyshit-mode/case-talknova-hardened.md`
- base technique: `holyshit-mode-case-talknova-hardened-results-negatives-are-r.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **api** · auth **low-priv** · chain role **pivot**

## Route

- probes: `dalfox`, `xsstrike`, `xsser`
- chains: `web`, `api`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

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

## Probe adjustment (api × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
