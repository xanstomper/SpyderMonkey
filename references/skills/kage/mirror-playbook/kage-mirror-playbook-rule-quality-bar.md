# Rule quality bar

- source canon: `kage/mirror-playbook.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-04

## The technique

- One attack class per rule (no kitchen-sink detection).
- Match on BEHAVIOR (hash/window/diff), not indicators — rules survive tool swaps.
- Every rule carries a re-fire test: the family re-fires the attack read-only
  and the rule MUST fire; a rule that cannot fire is a hypothesis.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
