# SV-…-BOUNDARY — BOUNDARY (source: undercroft) — firmware / low-priv

- source canon: `kairo/synthesis-engine.md`
- base technique: `kairo-synthesis-engine-sv-boundary-boundary-source-undercrof.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **firmware** · auth **low-priv** · chain role **final**

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- target: …
- attack: …
- proof: …
- Δ: …
```

**KAIRO** (hardware vectors stay in the plane ledger — its own synthesis domain).

## Probe adjustment (firmware × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
