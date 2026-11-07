# 2026-10-04 re-engagement — new surface found, still zero confirmed vulns

- source canon: `holyshit-mode/case-talknova-hardened.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
