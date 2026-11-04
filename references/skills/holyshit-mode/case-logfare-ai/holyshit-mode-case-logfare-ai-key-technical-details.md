# Key Technical Details

- source canon: `holyshit-mode/case-logfare-ai.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## The technique

### Discord OAuth Flow
- State cookie: HS256 JWT with `nonce` claim
- Purpose: `discord_signup`
- Expiry: 10 minutes
- redirect_uri: Hardcoded server-side
- alg:none attack: Rejected

### Rate Limiter Behavior (2026-10-09 updated)
- `/v1/auth/login`: 10 requests then 429 (retry-after header present)
- `/v1/auth/register`: 429 after burst, blocked by IP (retry-after: 45)
- `/v1/chat/completions`: No rate limit on 15 rapid requests with Bearer token
- `/v1/models`: No rate limit (public endpoint)
- X-Forwarded-For spoofing → Cloudflare 403 error 1000 (rate limiter bound to real IP, not spoofable header)
- **429 responses include CORS headers** → brute-force from browser can read rate-limit timing

### CORS on Error Responses
The CORS headers (`access-control-allow-origin: <any>`, `access-control-allow-credentials: true`)
are present on ALL response codes including 401/403/404/405/429. This means a malicious site
can send requests to destructive endpoints and read the error responses, confirming server-side
processing even when blocked.

### CSRF Bypass via Origin Spoofing

The server's CSRF validation accepts `Origin: https://logfare.ai`. While browsers cannot set
this from a cross-origin context, this reveals the CSRF check is **Origin-only** with no token:
- `POST /v1/auth/logout` → 200, **NO CSRF CHECK AT ALL** (confirmed: works cross-origin from any origin)
- `POST /connections/revoke` → Origin check only (bypassable via curl with `Origin: https://logfare.ai`)
- `POST /v1/me/delete` → Origin check only
- `POST /v1/auth/regenerate-key` → Origin check only

**Logout endpoint is the critical CSRF gap: zero protection.** A malicious page can call
`fetch('https://logfare.ai/v1/auth/logout', {method:'POST', credentials:'include'})` and log out
any logged-in user who visits. CORS headers on the 200 response let the attacker confirm success.

If Origin check is ever bypassed (via Origin spoofing, Referer manipulation, or another bug),
the full destructive chain is exposed: account deletion, connection revocation, API key regeneration,
force logout — all reachable cross-origin with victim's session.

### CORS Scope
- Vulnerable: `logfare.ai` (main API)
- NOT vulnerable: `chat.logfare.ai`, `rp.logfare.ai`

### postMessage Pattern
- Callback uses: `window.opener.postMessage(data, window.location.origin)`
- This is CORRECT (targets sender origin)
- Not a vulnerability

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
