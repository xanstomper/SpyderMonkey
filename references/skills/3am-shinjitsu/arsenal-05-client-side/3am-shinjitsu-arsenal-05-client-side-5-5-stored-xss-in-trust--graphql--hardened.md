# 5.5 Stored XSS in trusted UI (score 85, validation only) — graphql / hardened

- source canon: `3am-shinjitsu/arsenal-05-client-side.md`
- base technique: `3am-shinjitsu-arsenal-05-client-side-5-5-stored-xss-in-trust.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **graphql** · auth **hardened** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- Only on CONFIRMED injection points, in-scope, dalfox allowed; payloads minimal, self-owned
  accounts; evidence = reflected execution in the operator's own session, screenshot + path.
- Sinks: `innerHTML`, `eval`, `document.write`, postMessage targets, markdown renderers.

## Probe adjustment (graphql × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
