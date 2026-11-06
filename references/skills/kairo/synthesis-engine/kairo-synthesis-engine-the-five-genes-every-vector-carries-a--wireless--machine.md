# The five genes (every vector carries all five) — wireless / machine

- source canon: `kairo/synthesis-engine.md`
- base technique: `kairo-synthesis-engine-the-five-genes-every-vector-carries-a.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **wireless** · auth **machine** · chain role **pivot**

## Context

- platform: LAB-ONLY — your own radios and stations; third-party airwaves are the absolute wall
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

| Gene | Content | Source |
|---|---|---|
| TRIGGER | the source finding (what was observed) | ingested from family states |
| PRECONDITION | declared estate + access level | P0 record |
| PRIMITIVE | the technique class's mechanism | the class table |
| IMPACT-GATE | the exact proof condition | the class table |
| Δ | the documented-class adaptation for THIS target | synthesized; no Δ = no vector |

## Probe adjustment (wireless × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
