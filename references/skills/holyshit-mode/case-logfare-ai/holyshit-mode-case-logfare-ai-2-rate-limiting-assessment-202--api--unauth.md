# 2. Rate Limiting Assessment (2026-10-09 verified) — api / unauth

- source canon: `holyshit-mode/case-logfare-ai.md`
- base technique: `holyshit-mode-case-logfare-ai-2-rate-limiting-assessment-202.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **api** · auth **unauth** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

**Login (`/v1/auth/login`):** 10 rapid sequential requests → all 401 (no 429), then 429 at request 11. Rate limiter is present but kicks in after 10 attempts.

**Register (`/v1/auth/register`):** 429 after burst. Returns `retry-after: 45` header.

**API endpoints (`/v1/chat/completions`, `/v1/models`):** No rate limit observed — 15 rapid requests all returned expected responses (401 for chat without valid key, 200 for /v1/models) with zero 429s.

**Rate Limiter Behavior (2026-10-09):**
- `/v1/auth/login`: 10 requests then 429 (retry-after header present)
- `/v1/auth/register`: 429 after burst (retry-after: 45)
- `/v1/chat/completions`: No rate limit on 15 rapid requests with Bearer token
- `/v1/models`: No rate limit (public endpoint, 15/15 returned 200)

## Probe adjustment (api × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
