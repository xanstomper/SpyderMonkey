# The purple contract

- source canon: `kage/mirror-playbook.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## The technique

1. mirror: family CONFIRMED → rule (id, ATT&CK, log source, Sigma YAML)
2. telemetry: the registry of what the operator CAN see
3. validate: rc=1 while any rule lacks a live source — the gap list is the deliverable
4. report: the handoff artifact (rules + telemetry map)

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
