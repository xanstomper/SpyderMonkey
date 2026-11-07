# Cross-cloud attack paths (own estate) — iac / high-priv

- source canon: `spydermonkey/cloud-azure-gcp-canon.md`
- base technique: `spydermonkey-cloud-azure-gcp-canon-cross-cloud-attack-paths-.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **iac** · auth **high-priv** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: template/state files are the infrastructure inventory — read-only crown of the exposure
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Cloud_enum | `cloud_enum -k` (own org) | exposed buckets/domains |
| Stratus detonations | `stratus-red-team detonate` (own account, lab) | detection coverage proof |
| Prowler rows | `prowler aws` (own account) | control failures |
| ScoutSuite | `scoutsuite` (own provider account) | posture summary |
| Pacu exec | `pacu --exec` with own confirmed creds (lab) | post-exploit surface |
| AzureHound | `azurehound` (own tenant) | attack path graph |

Walls: everything runs in the operator's own tenant/project. Nothing touches
third-party cloud estate (scope gate refuses). Detonations run in dedicated
lab subscriptions/projects and are cleaned up after proof.

## Probe adjustment (iac × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
