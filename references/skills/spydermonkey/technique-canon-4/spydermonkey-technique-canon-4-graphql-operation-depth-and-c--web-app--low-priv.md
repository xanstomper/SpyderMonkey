# GraphQL operation-depth and cost classes — web-app / low-priv

- source canon: `spydermonkey/technique-canon-4.md`
- base technique: `spydermonkey-technique-canon-4-graphql-operation-depth-and-c.md`
- bindings: **WSTG-APIT-10** · **CWE-1321** · **ATT&CK T1190**
- context: **web-app** · auth **low-priv** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Depth/cost limiting absent → the CLASS is the missing guard, characterized with a bounded depth-10 introspection-style query (one request), never a sustained flood.

## Probe adjustment (web-app × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
