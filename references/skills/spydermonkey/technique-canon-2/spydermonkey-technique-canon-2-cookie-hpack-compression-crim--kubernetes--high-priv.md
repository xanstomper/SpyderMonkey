# Cookie/HPACK compression crimes-shape — kubernetes / high-priv

- source canon: `spydermonkey/technique-canon-2.md`
- base technique: `spydermonkey-technique-canon-2-cookie-hpack-compression-crim.md`
- bindings: **WSTG-CONF-04** · **CWE-798** · **ATT&CK T1552**
- context: **kubernetes** · auth **high-priv** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

Cross-origin compression oracles (length-differential on secrets echoed into compressed structures). Decisive test: lab replica with a secret + compressed echo — the byte-length oracle is the proof.

## Probe adjustment (kubernetes × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
