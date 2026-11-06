# Domaintools-class passive-total and sibling-brand mapping — ios / low-priv

- source canon: `spydermonkey/technique-canon-5.md`
- base technique: `spydermonkey-technique-canon-5-domaintools-class-passive-tot.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **ios** · auth **low-priv** · chain role **pivot**

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Registration-tree expansion (registrant org → sibling brands) feeding the shared-backend hypothesis (the error-taxonomy canon-I test confirms). Decisive test: whois org field + the sibling's confirmed shared taxonomy.

## Probe adjustment (ios × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
