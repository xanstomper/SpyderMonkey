# 7.7 Client supply-chain (score 70)

- source canon: `3am-shinjitsu/arsenal-07-supply-chain.md`
- bindings: **WSTG-BUSL-02** · **CWE-840** · **ATT&CK T1565**
- generated: 2026-11-04

## The technique

- Third-party integrations in the page (payment SDKs, analytics, chat widgets): version drift
  vs vendor advisories; postMessage contracts with them (→ §5.1); script `integrity`
  attribute absence on critical integrations.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
