# Rate Limiter Behavior (2026-10-09 updated) — chain composition

- source canon: `holyshit-mode/case-logfare-ai.md`
- base technique: `holyshit-mode-case-logfare-ai-rate-limiter-behavior-2026-10-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- `/v1/auth/login`: 10 requests then 429 (retry-after header present)
- `/v1/auth/register`: 429 after burst, blocked by IP (retry-after: 45)
- `/v1/chat/completions`: No rate limit on 15 rapid requests with Bearer token
- `/v1/models`: No rate limit (public endpoint)
- X-Forwarded-For spoofing → Cloudflare 403 error 1000 (rate limiter bound to real IP, not spoofable header)
- **429 responses include CORS headers** → brute-force from browser can read rate-limit timing

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
