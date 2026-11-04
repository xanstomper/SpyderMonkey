# Cloud Cross-Account Resource Share (CLOUD-IAM-04) — azure / high-priv

- source canon: `spydermonkey/cloud-canon.md`
- base technique: `spydermonkey-cloud-canon-cloud-cross-account-resource-share-.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **azure** · auth **high-priv** · chain role **final**

## Context

- platform: identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- class: shares/principal policies open to foreign accounts
- probe: read-only share inventory
- wall: read-only

## Probe adjustment (azure × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
