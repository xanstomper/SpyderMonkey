# Resource Development Compromise Infrastructure (T1584) — host / machine

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-resource-development-compromise-in.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- context: **host** · auth **machine** · chain role **final**

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- class: staging through third-party/compromised infra
- probe: out of family walls — detection classes only (kage rules for the pattern)
- wall: REFUSED live; detection-side only

## Probe adjustment (host × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
