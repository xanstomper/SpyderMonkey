# Exfiltration Over Web Service (T1567) — azure / unauth

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-exfiltration-over-web-service-t156.md`
- bindings: **WSTG-BUSL-02** · **CWE-840** · **ATT&CK T1565**
- context: **azure** · auth **unauth** · chain role **pivot**

## Context

- platform: identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- class: data out through trusted clouds
- probe: never exercised; the IMPACT LEG is priced by shukaku instead
- wall: NO-GAIN — exfiltration is priced hypothetically, never performed

## Probe adjustment (azure × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
