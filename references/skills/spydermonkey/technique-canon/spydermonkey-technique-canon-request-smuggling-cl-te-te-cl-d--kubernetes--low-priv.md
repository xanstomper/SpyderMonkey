# Request smuggling CL.TE / TE.CL differential — kubernetes / low-priv

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-request-smuggling-cl-te-te-cl-d.md`
- bindings: **WSTG-ADV-02** · **CWE-444** · **ATT&CK T1190**
- context: **kubernetes** · auth **low-priv** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Two conflicting-header probes with a timing/response-length delta — ONE probe pair, never a burst against a shared edge. Decisive test: the differential timeout/smuggled-response signature in the lab replica first (dojo has the replica).

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
