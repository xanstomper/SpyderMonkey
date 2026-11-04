# L2 — IDENTITY

- source canon: `barbican/protection-playbook.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## The technique

| Audit | Synthesis |
|---|---|
| git user.email: personal = CRITICAL; noreply form = acceptable | engagement alias in posture; commits carry alias@users.noreply |
| username in file paths (reports, logs, JSON states) | sanitize rewrites /home/<user> → /home/<alias> |
| shell env markers (AI_AGENT, HERMES_AGENT) | engagement shells: `env -i bash -lc` |
| hostname strings in artifacts | sanitize rewrites to "op-host" |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
