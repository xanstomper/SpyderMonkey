# L3 — ARTIFACTS — host / high-priv

- source canon: `barbican/protection-playbook.md`
- base technique: `barbican-protection-playbook-l3-artifacts.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **host** · auth **high-priv** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

| Audit | Synthesis |
|---|---|
| reports/logs/states containing identity strings | single compartment: ~/.redteam/ only — never Desktop/Documents/cloud-synced paths |
| canon files (learned-vectors, recipes, chains) | sanitize covers canon TOO (the alias rule is family-wide) |
| scratch/tmp leftovers | wipe at engagement end (24h-prune catches the rest) |

## Probe adjustment (host × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
