# Recommendations for Future Testing — chain composition

- source canon: `holyshit-mode/case-logfare-ai.md`
- base technique: `holyshit-mode-case-logfare-ai-recommendations-for-future-tes.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. Obtain valid API key for post-auth testing
2. Test IDOR on /v1/me/data with modified user ID
3. Test SSO confusion race condition
4. Test stored XSS in chat completions
5. Test CSRF on state-changing endpoints with session
6. **2026-10-09 session: CSRF bypass via Origin spoofing confirmed** — `Origin: https://logfare.ai` passes CSRF on `/connections/revoke`. Logout endpoint has NO CSRF check at all. Destructive endpoints exposed if Origin check is bypassed.
7. **2026-10-09 session: Cross-origin brute-force confirmed** — login 429 responses include CORS + retry-after, enabling browser-based password brute-force with timing sync.
8. **2026-10-09 session: OpenAPI full enumeration completed** — 60+ endpoints mapped, all checked for CORS. Destructive endpoints: `/v1/me/delete` (GDPR erase), `/connections/revoke`, `/v1/auth/regenerate-key`, `/v1/auth/logout` all have CORS + credentials.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
