# The purple contract — kubernetes / unauth

- source canon: `kage/mirror-playbook.md`
- base technique: `kage-mirror-playbook-the-purple-contract.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **kubernetes** · auth **unauth** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

1. mirror: family CONFIRMED → rule (id, ATT&CK, log source, Sigma YAML)
2. telemetry: the registry of what the operator CAN see
3. validate: rc=1 while any rule lacks a live source — the gap list is the deliverable
4. report: the handoff artifact (rules + telemetry map)

## Probe adjustment (kubernetes × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
