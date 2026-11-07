# Cross-cloud attack paths (own estate)

- source canon: `spydermonkey/cloud-azure-gcp-canon.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-07

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
