# 5.5 Stored XSS in trusted UI (score 85, validation only)

- source canon: `3am-shinjitsu/arsenal-05-client-side.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-04

## The technique

- Only on CONFIRMED injection points, in-scope, dalfox allowed; payloads minimal, self-owned
  accounts; evidence = reflected execution in the operator's own session, screenshot + path.
- Sinks: `innerHTML`, `eval`, `document.write`, postMessage targets, markdown renderers.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
