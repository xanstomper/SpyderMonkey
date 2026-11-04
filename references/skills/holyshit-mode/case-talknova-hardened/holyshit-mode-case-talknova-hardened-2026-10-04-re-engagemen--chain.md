# 2026-10-04 re-engagement — new surface found, still zero confirmed vulns — chain composition

- source canon: `holyshit-mode/case-talknova-hardened.md`
- base technique: `holyshit-mode-case-talknova-hardened-2026-10-04-re-engagemen.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Bundle hash `DwftPOeS` (same architecture, new code-split chunks). Key discovery: **always
fetch code-split chunks** — the main bundle only lazy-loads page components; the real API
surface lives in the chunks.

New endpoints NOT in 2026-10-03 case:
- `/api/apikey`, `/api/apikey/regenerate`, `/api/apikey/rotate` — personal OpenAI-compatible key CRUD
- `/v1/models`, `/v1/chat/completions` — key-authenticated API
- `/api/admin/{session,login,logout,stats,logs,users,grants,apikeys,custom-keys}` — full admin portal
- `/api-access` — SPA route for key management (not an API endpoint)

Admin portal map (from `AdminPage-Cgkb504W.js`):
- Login: `POST /api/admin/login` with `{username, password}` (not email)
- User management: `GET /api/admin/users?q=&page=&filter=`, `PATCH /api/admin/users/:id`, `DELETE /api/admin/users/:id`
- Plan grants: `POST /api/admin/grants` `{email, plan, days}`, `DELETE /api/admin/grants/:id`
- Custom API keys: `POST /api/admin/custom-keys` `{label, balanceDollars, allowedModels}`, `PATCH /api/admin/custom-keys/:id` (top-up, model restrict), `DELETE /api/admin/custom-keys/:id`
- Audit: `GET /api/admin/logs`, `GET /api/admin/stats`

All admin endpoints return 401 without server-side admin session. Rate limiter on
`/api/admin/login` is aggressive: 4 failed attempts → 429 with 30-minute decay.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
