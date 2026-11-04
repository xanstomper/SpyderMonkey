# Cloud Serverless Event Injection (CLOUD-LAMBDA-01) — azure / low-priv

- source canon: `spydermonkey/cloud-canon.md`
- base technique: `spydermonkey-cloud-canon-cloud-serverless-event-injection-cl.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- context: **azure** · auth **low-priv** · chain role **pivot**

## Context

- platform: identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- class: unsanitized event fields reaching the runtime
- probe: the INJECTION battery aimed at the documented event surface (lab functions)
- wall: lab functions only for live proof; prod is inventory-only

## Probe adjustment (azure × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
