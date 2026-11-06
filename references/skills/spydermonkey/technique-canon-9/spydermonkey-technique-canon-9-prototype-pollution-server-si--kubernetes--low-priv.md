# Prototype pollution server-side — kubernetes / low-priv

- source canon: `spydermonkey/technique-canon-9.md`
- base technique: `spydermonkey-technique-canon-9-prototype-pollution-server-si.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **kubernetes** · auth **low-priv** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Merge/deep-extend sinks reachable via JSON body __proto__. Decisive test: property-diff observable on your own session object = the class.

## Probe adjustment (kubernetes × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
