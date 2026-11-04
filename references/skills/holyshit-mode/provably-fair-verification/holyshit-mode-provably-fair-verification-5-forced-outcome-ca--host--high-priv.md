# 5. Forced-outcome capability — host / high-priv

- source canon: `holyshit-mode/provably-fair-verification.md`
- base technique: `holyshit-mode-provably-fair-verification-5-forced-outcome-ca.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **host** · auth **high-priv** · chain role **final**

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

Watch result events for `forced` / manual-control flags. The flag existing in the
PUBLIC event schema = a staff-side outcome-control surface is a system feature (the
chain would not cover a forced round — that is the escape hatch). All-false captures
= capability present, use unproven; a `forced:true` round in anyone's evidence = the
control in use. Either way this is the caveat that must ride the rebuttal package.

## Probe adjustment (host × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
