# Negatives (hardened) — mobile-api / unauth

- source canon: `holyshit-mode/case-logfare-reengagement2.md`
- base technique: `holyshit-mode-case-logfare-reengagement2-negatives-hardened.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **mobile-api** · auth **unauth** · chain role **pivot**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Discord OAuth: forged state → 400; state cookie HttpOnly/Secure/Lax/path-scoped JWT;
`redirect_uri` on `/v1/auth/discord/start` NOT client-controllable. Login rate limit works
(5×401 → 429). OAuth/device/SSO client probes give no enumeration oracle. `/api/conversations`
and `/api/settings` 200 on anon sessions are per-session state, not leaks.

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
