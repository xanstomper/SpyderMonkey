# 12. Recon recipe that found the key endpoints (reusable)

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-reengagement.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Platform SPA is a marketing shell — API paths hide in the JS bundle: fetch `/assets/platform-*.js`, then grep template-literal fetches: `` grep -oE '\(`/api/account/[a-zA-Z0-9/_-]*`' `` → found `/api/account/platform-keys`, `/billing/checkout-session`, `/api/public/billing/config`. SPA catch-all returns 200 HTML for ANY path — use a gibberish-path control to distinguish real endpoints (real = 401 JSON `invalid_session_token`, fake = 200 HTML).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
