# L4 — TRAIL

- source canon: `barbican/protection-playbook.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Audit | Synthesis |
|---|---|
| which upstream providers the engagement touches | sanctioned providers named in posture; personal accounts forbidden for engagement traffic |
| authorization paperwork | zero documents (family canon): nothing exists to subpoena/leak |
| payment trails for engagement infra | lab/free-tier only, or alias-separated accounts |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
