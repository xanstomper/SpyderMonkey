# L3 — ARTIFACTS — ci-cd / machine

- source canon: `barbican/protection-playbook.md`
- base technique: `barbican-protection-playbook-l3-artifacts.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **ci-cd** · auth **machine** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

| Audit | Synthesis |
|---|---|
| reports/logs/states containing identity strings | single compartment: ~/.redteam/ only — never Desktop/Documents/cloud-synced paths |
| canon files (learned-vectors, recipes, chains) | sanitize covers canon TOO (the alias rule is family-wide) |
| scratch/tmp leftovers | wipe at engagement end (24h-prune catches the rest) |

## Probe adjustment (ci-cd × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
