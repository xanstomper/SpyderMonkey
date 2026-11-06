# Results (negatives are results — log them) — grpc / machine

- source canon: `holyshit-mode/case-talknova-hardened.md`
- base technique: `holyshit-mode-case-talknova-hardened-results-negatives-are-r.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **grpc** · auth **machine** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

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

## Probe adjustment (grpc × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
