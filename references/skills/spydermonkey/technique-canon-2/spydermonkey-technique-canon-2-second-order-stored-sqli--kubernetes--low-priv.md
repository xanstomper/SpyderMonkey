# Second-order stored SQLi — kubernetes / low-priv

- source canon: `spydermonkey/technique-canon-2.md`
- base technique: `spydermonkey-technique-canon-2-second-order-stored-sqli.md`
- bindings: **WSTG-INPV-05** · **CWE-89** · **ATT&CK T1190**
- context: **kubernetes** · auth **low-priv** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Payload stored in profile/asset fields, executed by a LATER query (admin render, export job). Decisive test: your own stored payload flipping an error class in a downstream render you can read — the downstream context is the proof.

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
