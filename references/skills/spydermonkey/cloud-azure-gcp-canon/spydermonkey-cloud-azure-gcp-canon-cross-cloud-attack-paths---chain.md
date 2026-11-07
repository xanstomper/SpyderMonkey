# Cross-cloud attack paths (own estate) — chain composition

- source canon: `spydermonkey/cloud-azure-gcp-canon.md`
- base technique: `spydermonkey-cloud-azure-gcp-canon-cross-cloud-attack-paths-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
