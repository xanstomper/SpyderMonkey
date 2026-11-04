# Rate Limiter Behavior (2026-10-09 updated)

- source canon: `holyshit-mode/case-logfare-ai.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- `/v1/auth/login`: 10 requests then 429 (retry-after header present)
- `/v1/auth/register`: 429 after burst, blocked by IP (retry-after: 45)
- `/v1/chat/completions`: No rate limit on 15 rapid requests with Bearer token
- `/v1/models`: No rate limit (public endpoint)
- X-Forwarded-For spoofing → Cloudflare 403 error 1000 (rate limiter bound to real IP, not spoofable header)
- **429 responses include CORS headers** → brute-force from browser can read rate-limit timing

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
