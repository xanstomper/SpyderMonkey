# REST mass assignment depth

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-BUSL-05** · **CWE-285** · **ATT&CK T1068**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Role/entitlement fields beyond the obvious (`role`, `tenantId`, `isStaff`, `quota`) re-bound on PUT/PATCH. Decisive test: unknown-field probe (send one invented field + one plausible) — echoed/persisted = the class; persisted-and-effectful = the crown (your own principal only).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
