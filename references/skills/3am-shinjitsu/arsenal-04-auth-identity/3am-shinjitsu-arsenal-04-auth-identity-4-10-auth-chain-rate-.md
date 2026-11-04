# 4.10 Auth-chain rate sweep (score 75)

- source canon: `3am-shinjitsu/arsenal-04-auth-identity.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- The WHOLE chain, not just login: `/auth/v1/verify`, handoff exchange, token code brute,
  forgot-password, resend-verification (no captcha + no limit = mail-bomb pump vector even
  with uniform no-enumeration responses). One working limiter (signup 60s) proves nothing
  about the others. 15-26 rapid garbage inputs per endpoint, `-w '%{http_code}'`, once.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
