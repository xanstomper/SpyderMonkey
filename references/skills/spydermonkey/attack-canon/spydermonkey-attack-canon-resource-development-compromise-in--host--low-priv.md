# Resource Development Compromise Infrastructure (T1584) — host / low-priv

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-resource-development-compromise-in.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- context: **host** · auth **low-priv** · chain role **final**

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- class: staging through third-party/compromised infra
- probe: out of family walls — detection classes only (kage rules for the pattern)
- wall: REFUSED live; detection-side only

## Probe adjustment (host × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
