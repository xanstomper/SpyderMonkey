# The gate — host / unauth

- source canon: `barbican/protection-playbook.md`
- base technique: `barbican-protection-playbook-the-gate.md`
- bindings: **PTES-OPSEC** · **CWE-200** · **ATT&CK T1070**
- context: **host** · auth **unauth** · chain role **pivot**

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

`posture` must exist before the family engages (`assess` warns; the operator owns
the go). At engagement end: `wipe`. Between: `sanitize` after every artifact-heavy
phase. The first layer never sleeps.

## Probe adjustment (host × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
