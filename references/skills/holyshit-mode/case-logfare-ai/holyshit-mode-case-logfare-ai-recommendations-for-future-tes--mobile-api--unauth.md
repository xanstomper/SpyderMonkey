# Recommendations for Future Testing — mobile-api / unauth

- source canon: `holyshit-mode/case-logfare-ai.md`
- base technique: `holyshit-mode-case-logfare-ai-recommendations-for-future-tes.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **mobile-api** · auth **unauth** · chain role **pivot**

## Route

- probes: `dalfox`, `xsstrike`, `xsser`
- chains: `web`, `api`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

1. Obtain valid API key for post-auth testing
2. Test IDOR on /v1/me/data with modified user ID
3. Test SSO confusion race condition
4. Test stored XSS in chat completions
5. Test CSRF on state-changing endpoints with session
6. **2026-10-09 session: CSRF bypass via Origin spoofing confirmed** — `Origin: https://logfare.ai` passes CSRF on `/connections/revoke`. Logout endpoint has NO CSRF check at all. Destructive endpoints exposed if Origin check is bypassed.
7. **2026-10-09 session: Cross-origin brute-force confirmed** — login 429 responses include CORS + retry-after, enabling browser-based password brute-force with timing sync.
8. **2026-10-09 session: OpenAPI full enumeration completed** — 60+ endpoints mapped, all checked for CORS. Destructive endpoints: `/v1/me/delete` (GDPR erase), `/connections/revoke`, `/v1/auth/regenerate-key`, `/v1/auth/logout` all have CORS + credentials.

## Probe adjustment (mobile-api × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
