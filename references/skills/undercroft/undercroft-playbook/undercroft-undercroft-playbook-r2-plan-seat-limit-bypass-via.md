# R2 — Plan/seat-limit bypass via client-supplied scope ids (SaaS)

- source canon: `undercroft/undercroft-playbook.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-04

## The technique

1. From the bundle, find the scope id the client sends (`scan` flags `org_id`/
   `tenant_id`/`workspace_id` in client calls).
2. On your own tenant at plan limit, send the upgrade/invite/seat request with a
   forged scope id in the BODY (server should read it from the session).
3. Decisive test: create limit+1 resources; count.
4. CONFIRMED when limit+1 exists. Reverse: delete the extra resources.
5. `craft` as IDOR (scope trust), `export`.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
