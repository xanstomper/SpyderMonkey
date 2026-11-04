# L6 — CLEANUP

- source canon: `barbican/protection-playbook.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-04

## The technique

| Audit | Synthesis |
|---|---|
| campaign dirs left full | `wipe --confirm` = campaign + posture removed; canon rows survive BY DESIGN |
| sim/test rows in canon | stripped same-session (family hygiene, formalized) |
| shell history carrying engagement commands | engagement shells: HISTFILE=/dev/null or clean-env shells |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
