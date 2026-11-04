# Probe recipes that paid off (reusable)

- source canon: `holyshit-mode/case-talknova-hardened.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-04

## The technique

### SPA endpoint + body-shape mining (minified bundle)
1. `grep -oE '"/[a-zA-Z0-9_/.-]{2,60}"' app.js | sort -u` → route + endpoint list.
2. All fetch calls: `grep -oE 'fetch\("[a-z0-9/_-]+"' app.js | sort -u`.
3. Body shapes live at CALL SITES of the wrapper fn, not the fetch itself — find the wrapper
   (e.g. `async function Y8(e,t){fetch("/api/chat"...}`), then grep its callers:
   `grep -oE 'Y8\(\{[^}]{0,150}' app.js` → reveals real body keys (`{modelId, message}` not
   the guessed `{model, messages}`). Server error strings are the oracle.
4. **Code-split chunk discovery**: `grep -oE '"\./[A-Za-z0-9_-]+\.js"' app.js` → fetch each chunk, mine for endpoints.

### OAuth state-binding test (5 curls, decisive)
1. GET `/api/auth/google/start?attempt=x1` → capture state cookie A.
2. GET start again → cookie B. Then `callback?state=A&code=fake` with cookie B → hardened if `Invalid OAuth state`.
3. Matched cookie + fake code → expect token-exchange failure.
4. `returnTo=https://evil.com` on /start → hardened if Location still goes only to Google.
5. Callback with no cookie / no state → expect 400.

### Origin-lock matrix (cookie-auth endpoints)
For each POST endpoint, fire: attacker Origin, `Origin: null`, and NO Origin — all should 403.

### Ghost-route discrimination
404s returning `application/json` = real routing layer (not SPA fallback). Only `text/html`
404/200s are ghosts. Check `/openapi.json`, `/docs`, `/api/docs` — but expect them genuinely absent on hardened non-FastAPI targets.

### Admin authz matrix (when admin endpoints are discovered)
- GET unauth → expect 401
- POST unauth → expect 401
- PATCH/DELETE unauth → expect 401
- IDOR by numeric ID (`/users/1`, `/grants/1`, `/custom-keys/1`) → expect 401
- Mass assignment probe (`{"plan":"max","is_admin":true}`) → expect 401 or validation error
- Rate-limit probe on login → note decay time (talknova: 30 min)

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
