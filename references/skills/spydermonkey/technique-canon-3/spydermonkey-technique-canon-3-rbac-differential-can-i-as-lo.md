# RBAC differential (can-i as low-priv)

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

`kubectl auth can-i --list` shape as the low-priv principal — the INVENTORY of reachable verbs is the finding. Decisive test: your own service account's verb list.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
