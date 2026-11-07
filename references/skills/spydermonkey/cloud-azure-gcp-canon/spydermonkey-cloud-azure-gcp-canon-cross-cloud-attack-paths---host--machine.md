# Cross-cloud attack paths (own estate) — host / machine

- source canon: `spydermonkey/cloud-azure-gcp-canon.md`
- base technique: `spydermonkey-cloud-azure-gcp-canon-cross-cloud-attack-paths-.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **host** · auth **machine** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

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

## Probe adjustment (host × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
