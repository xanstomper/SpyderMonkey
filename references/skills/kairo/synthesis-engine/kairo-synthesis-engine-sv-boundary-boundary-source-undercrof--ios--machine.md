# SV-…-BOUNDARY — BOUNDARY (source: undercroft) — ios / machine

- source canon: `kairo/synthesis-engine.md`
- base technique: `kairo-synthesis-engine-sv-boundary-boundary-source-undercrof.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **ios** · auth **machine** · chain role **final**

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- target: …
- attack: …
- proof: …
- Δ: …
```

**KAIRO** (hardware vectors stay in the plane ledger — its own synthesis domain).

## Probe adjustment (ios × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
