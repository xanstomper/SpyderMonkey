# BOUNDARY — HWFLASH — ios / unauth

- source canon: `kairo/technique-classes.md`
- base technique: `kairo-technique-classes-boundary-hwflash.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **ios** · auth **unauth** · chain role **pivot**

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- BOUNDARY
- HWFLASH
- scope-id trust on update/extract paths — swapped slot ids (lab, owned device)

## Probe adjustment (ios × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
