# 4.10 Auth-chain rate sweep (score 75) — windows / unauth

- source canon: `3am-shinjitsu/arsenal-04-auth-identity.md`
- base technique: `3am-shinjitsu-arsenal-04-auth-identity-4-10-auth-chain-rate-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **windows** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: token/session confusion classes; read-only enumeration, NO-GAIN
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- The WHOLE chain, not just login: `/auth/v1/verify`, handoff exchange, token code brute,
  forgot-password, resend-verification (no captcha + no limit = mail-bomb pump vector even
  with uniform no-enumeration responses). One working limiter (signup 60s) proves nothing
  about the others. 15-26 rapid garbage inputs per endpoint, `-w '%{http_code}'`, once.

## Probe adjustment (windows × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
