# L3 — ARTIFACTS

- source canon: `barbican/protection-playbook.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Audit | Synthesis |
|---|---|
| reports/logs/states containing identity strings | single compartment: ~/.redteam/ only — never Desktop/Documents/cloud-synced paths |
| canon files (learned-vectors, recipes, chains) | sanitize covers canon TOO (the alias rule is family-wide) |
| scratch/tmp leftovers | wipe at engagement end (24h-prune catches the rest) |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
