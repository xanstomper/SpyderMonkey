# The gate

- source canon: `barbican/protection-playbook.md`
- bindings: **PTES-OPSEC** · **CWE-200** · **ATT&CK T1070**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`posture` must exist before the family engages (`assess` warns; the operator owns
the go). At engagement end: `wipe`. Between: `sanitize` after every artifact-heavy
phase. The first layer never sleeps.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
