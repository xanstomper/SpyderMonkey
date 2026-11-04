# New confirmed findings (2026-10-10)

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-reengagement.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

### 1. GoTrue redirect_uri full override — CONFIRMED (score 85)
GET /auth/v1/authorize?provider=discord&redirect_uri=<attacker_url forwards attacker URI verbatim to Discord OAuth. No HTTPS enforcement, no path normalization.

### 2. Unthrottled brute surfaces (score 50-55)
/auth/v1/verify, /auth/v1/token, /auth/v1/signup, /api/auth/platform-handoff/exchange — all zero 429 on rapid POSTs.

### 3. Email confirmation broken (score 55)
POST /auth/v1/signup returns HTTP 500 but user row IS created with role:authenticated.

### 4. CORS arbitrary origin reflection (score 72)
access-control-allow-origin reflects ALL origins on /v1/* endpoints.

### 5. Internal provider fleet disclosure (score 60)
GET /api/status and /api/providers return 34-provider registry unauthenticated. Discord OAuth client_id: 1308596927759126548.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
