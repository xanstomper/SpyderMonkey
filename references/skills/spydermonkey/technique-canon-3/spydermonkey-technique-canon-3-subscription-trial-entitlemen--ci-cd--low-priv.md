# Subscription/trial entitlement persistence — ci-cd / low-priv

- source canon: `spydermonkey/technique-canon-3.md`
- base technique: `spydermonkey-technique-canon-3-subscription-trial-entitlemen.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **ci-cd** · auth **low-priv** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Client-held entitlement flags trusted server-side (JWT claim, localStorage sync). Decisive test: expired entitlement replayed with the cached flag on YOUR account — acceptance = the class.

## Probe adjustment (ci-cd × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
