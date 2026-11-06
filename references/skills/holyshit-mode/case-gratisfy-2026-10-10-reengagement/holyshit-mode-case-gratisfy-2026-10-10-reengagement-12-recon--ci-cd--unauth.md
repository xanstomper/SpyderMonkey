# 12. Recon recipe that found the key endpoints (reusable) — ci-cd / unauth

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-reengagement.md`
- base technique: `holyshit-mode-case-gratisfy-2026-10-10-reengagement-12-recon.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **ci-cd** · auth **unauth** · chain role **entry**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Platform SPA is a marketing shell — API paths hide in the JS bundle: fetch `/assets/platform-*.js`, then grep template-literal fetches: `` grep -oE '\(`/api/account/[a-zA-Z0-9/_-]*`' `` → found `/api/account/platform-keys`, `/billing/checkout-session`, `/api/public/billing/config`. SPA catch-all returns 200 HTML for ANY path — use a gibberish-path control to distinguish real endpoints (real = 401 JSON `invalid_session_token`, fake = 200 HTML).

## Probe adjustment (ci-cd × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
