# 2. Rate Limiting Assessment (2026-10-09 verified) — chain composition

- source canon: `holyshit-mode/case-logfare-ai.md`
- base technique: `holyshit-mode-case-logfare-ai-2-rate-limiting-assessment-202.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

**Login (`/v1/auth/login`):** 10 rapid sequential requests → all 401 (no 429), then 429 at request 11. Rate limiter is present but kicks in after 10 attempts.

**Register (`/v1/auth/register`):** 429 after burst. Returns `retry-after: 45` header.

**API endpoints (`/v1/chat/completions`, `/v1/models`):** No rate limit observed — 15 rapid requests all returned expected responses (401 for chat without valid key, 200 for /v1/models) with zero 429s.

**Rate Limiter Behavior (2026-10-09):**
- `/v1/auth/login`: 10 requests then 429 (retry-after header present)
- `/v1/auth/register`: 429 after burst (retry-after: 45)
- `/v1/chat/completions`: No rate limit on 15 rapid requests with Bearer token
- `/v1/models`: No rate limit (public endpoint, 15/15 returned 200)

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
