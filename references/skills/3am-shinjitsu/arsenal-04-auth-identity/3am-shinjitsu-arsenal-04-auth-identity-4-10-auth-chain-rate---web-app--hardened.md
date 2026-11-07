# 4.10 Auth-chain rate sweep (score 75) — web-app / hardened

- source canon: `3am-shinjitsu/arsenal-04-auth-identity.md`
- base technique: `3am-shinjitsu-arsenal-04-auth-identity-4-10-auth-chain-rate-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **web-app** · auth **hardened** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- The WHOLE chain, not just login: `/auth/v1/verify`, handoff exchange, token code brute,
  forgot-password, resend-verification (no captcha + no limit = mail-bomb pump vector even
  with uniform no-enumeration responses). One working limiter (signup 60s) proves nothing
  about the others. 15-26 rapid garbage inputs per endpoint, `-w '%{http_code}'`, once.

## Probe adjustment (web-app × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
