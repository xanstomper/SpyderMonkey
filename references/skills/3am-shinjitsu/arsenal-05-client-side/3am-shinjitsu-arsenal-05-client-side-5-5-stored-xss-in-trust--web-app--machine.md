# 5.5 Stored XSS in trusted UI (score 85, validation only) — web-app / machine

- source canon: `3am-shinjitsu/arsenal-05-client-side.md`
- base technique: `3am-shinjitsu-arsenal-05-client-side-5-5-stored-xss-in-trust.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **web-app** · auth **machine** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- Only on CONFIRMED injection points, in-scope, dalfox allowed; payloads minimal, self-owned
  accounts; evidence = reflected execution in the operator's own session, screenshot + path.
- Sinks: `innerHTML`, `eval`, `document.write`, postMessage targets, markdown renderers.

## Probe adjustment (web-app × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
