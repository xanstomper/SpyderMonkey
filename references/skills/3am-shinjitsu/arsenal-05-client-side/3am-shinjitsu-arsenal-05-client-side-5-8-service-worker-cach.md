# 5.8 Service worker / cache-asset poisoning (score 55)

- source canon: `3am-shinjitsu/arsenal-05-client-side.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## The technique

- SW registration scope, cache-first strategies on hashed assets; asset-URL injection points.
- Clickjacking: missing XFO/frame-ancestors on state-changing pages.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
