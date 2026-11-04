# 4.8 Auth-mode header split (score 75)

- source canon: `3am-shinjitsu/arsenal-04-auth-identity.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- Multi-tenant bundles carry auth-mode selectors (`X-Chat-Auth-Mode: account|platform_key`).
  Error chain enumerates itself: bare → 400 naming the header → each value names the next
  credential. Each branch = its OWN auth surface against its OWN backend.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
