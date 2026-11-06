# Resource-exhaustion class (validation-only) — external / unauth

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-resource-exhaustion-class-valid.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- context: **external** · auth **unauth** · chain role **final**

## Context

- platform: passive-first; the dossier feeds everything downstream
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Unbounded expensive endpoints (report generation, image resize) — characterize as the class with ONE request's measured cost delta, never a sustained drain.

## Probe adjustment (external × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
