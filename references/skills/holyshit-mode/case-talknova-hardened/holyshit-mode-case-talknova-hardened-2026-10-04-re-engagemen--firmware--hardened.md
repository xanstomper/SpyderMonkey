# 2026-10-04 re-engagement — new surface found, still zero confirmed vulns — firmware / hardened

- source canon: `holyshit-mode/case-talknova-hardened.md`
- base technique: `holyshit-mode-case-talknova-hardened-2026-10-04-re-engagemen.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **firmware** · auth **hardened** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

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

## Probe adjustment (firmware × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
