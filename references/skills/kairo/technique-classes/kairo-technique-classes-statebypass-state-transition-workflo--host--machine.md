# STATEBYPASS — state, transition, workflow, approval — host / machine

- source canon: `kairo/technique-classes.md`
- base technique: `kairo-technique-classes-statebypass-state-transition-workflo.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **host** · auth **machine** · chain role **pivot**

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- STATEBYPASS
- state, transition, workflow, approval
- 5/B
- STATE

## Probe adjustment (host × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
