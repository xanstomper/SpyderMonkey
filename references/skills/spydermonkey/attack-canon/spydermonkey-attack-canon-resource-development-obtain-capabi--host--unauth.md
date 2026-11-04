# Resource Development Obtain Capabilities (T1588) — host / unauth

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-resource-development-obtain-capabi.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- context: **host** · auth **unauth** · chain role **final**

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- class: acquiring existing tooling
- probe: inventory what the operator environment already carries (arsenal.py)
- wall: zero-purchase; the arsenal maps presence, never installs for an engagement

## Probe adjustment (host × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
