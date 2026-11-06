# Results (negatives are results — log them) — mobile-api / high-priv

- source canon: `holyshit-mode/case-talknova-hardened.md`
- base technique: `holyshit-mode-case-talknova-hardened-results-negatives-are-r.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **mobile-api** · auth **high-priv** · chain role **pivot**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

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

## Probe adjustment (mobile-api × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
