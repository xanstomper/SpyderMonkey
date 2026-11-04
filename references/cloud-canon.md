# The Cloud Canon — cloud service attack classes, family-native (shukaku hunt semantics)

> Real cloud classes, read-only hunting: crown the exposure, never weaponize it.
> Header = technique; body = class, probe, wall. Deterministic.

## Cloud IAM Wildcard Policy (CLOUD-IAM-01)

- class: `*` actions/resources in identity policies — the over-privileged principal
- probe: read-only policy inventory for every principal the scope declares
- wall: shukaku hunt semantics — inventory + pricing only, nothing assumed

## Cloud IAM PassRole Confusion (CLOUD-IAM-02)

- class: a principal that can pass a role to a service it controls
- probe: read-only path analysis of role trust + pass grants — the CHAIN is priced, never walked
- wall: NO-GAIN — the escalation path is a ledger row, not an action

## Cloud Assume-Role Trust Confusion (CLOUD-IAM-03)

- class: trust policies allowing broad external principals
- probe: read-only trust inventory; who can assume what
- wall: read-only

## Cloud Object Storage Public Exposure (CLOUD-OBJ-01)

- class: buckets/containers readable or listable by anyone
- probe: unauthenticated listing + reference probes against the declared estate
- wall: read-only; the HARVEST class rules — files are listed, never downloaded beyond the proof

## Cloud Object Storage CNAME Misassignment (CLOUD-OBJ-02)

- class: the service bucket still claimed — domtake's cloud cousin
- probe: the takeover engine's dangling-fingerprint class against cloud endpoints
- wall: NO-GAIN — claim status is proof; registration is never performed

## Cloud Metadata Service Exposure (CLOUD-SSRF-01)

- class: 169.254.169.254 reachable through an in-scope app — the SSRF crown
- probe: the SSRF battery's metadata targets — the differential proves the reach
- wall: proof-of-reach only; metadata contents beyond the marker are never dumped

## Cloud Serverless Event Injection (CLOUD-LAMBDA-01)

- class: unsanitized event fields reaching the runtime
- probe: the INJECTION battery aimed at the documented event surface (lab functions)
- wall: lab functions only for live proof; prod is inventory-only

## Cloud Serverless Secrets in Environment (CLOUD-LAMBDA-02)

- class: plaintext secrets in function config
- probe: read-only config inventory of the declared functions
- wall: secrets are redacted in the ledger

## Cloud Container Registry Exposure (CLOUD-REG-01)

- class: anonymous pull of images — layers leak source/secrets
- probe: unauth manifest read of the declared registry; layer inventory only
- wall: NO-GAIN — layers are inventoried, not mined wholesale

## Cloud Kubernetes RBAC Gaps (CLOUD-K8S-01)

- class: over-broad service accounts, default SA with verbs
- probe: read-only authn-can-i inventory against the declared cluster
- wall: read-only enumeration, crown the exposure

## Cloud Kubernetes Secret Mounts (CLOUD-K8S-02)

- class: secrets mounted where workloads can read — inventory of WHICH
- probe: read-only workload spec inventory
- wall: values never read; names and bindings only

## Cloud IMDSv1 Class (CLOUD-SSRF-02)

- class: token-less metadata negotiation — the SSRF metadata marker answers
- probe: the SSRF differential against the in-scope app's fetch surface
- wall: proof-of-class only

## Cloud Azure Managed Identity Abuse Surface (CLOUD-AZ-01)

- class: identity-bearing workloads whose endpoints are exposed
- probe: read-only endpoint + identity surface inventory
- wall: nothing tokened; the exposure is priced

## Cloud Azure Storage Keys in Config (CLOUD-AZ-02)

- class: account keys in app settings/repo
- probe: harvest-class scan of declared configs
- wall: redact on capture — the pattern is the finding, never the key

## Cloud Azure AD App Registration Overreach (CLOUD-AZ-03)

- class: app registrations with excessive delegated/application grants
- probe: read-only grants inventory of the declared tenant
- wall: read-only

## Cloud GCP Service Account Keys in Code (CLOUD-GCP-01)

- class: downloadable SA keys committed
- probe: harvest scan of declared repos/buckets for key material
- wall: redact on capture

## Cloud GCP Metadata Flatten (CLOUD-GCP-02)

- class: metadata endpoint reach via SSRF
- probe: SSRF battery metadata targets
- wall: proof-of-reach only

## Cloud GCS Public Exposure (CLOUD-GCP-03)

- class: listable/public GCS buckets
- probe: unauth listing probes
- wall: read-only, HARVEST rules

## Cloud CloudFront Origin Confusion (CLOUD-EDGE-01)

- class: origin that answers any Host — the edge/cache chain opener
- probe: Host-header differentials through the declared distribution
- wall: read-only; cache-poisoning classes are proven lab-side only

## Cloud CloudFront Cache Key Confusion (CLOUD-EDGE-02)

- class: unkeyed headers/params changing the cached object
- probe: lab replica — the caching differential with harmless markers
- wall: lab only; prod cache is never poisoned

## Cloud DNS Zone Misconfig (CLOUD-DNS-01)

- class: public zone records pointing to deprovisioned services
- probe: the takeover engine — dangling record inventory
- wall: NO-GAIN

## Cloud CloudTrail/Log Coverage Gaps (CLOUD-DET-01)

- class: regions/actions without logging — the blind spot map
- probe: read-only trail config inventory
- wall: the finding is the gap, not an action in the gap

## Cloud Cross-Account Resource Share (CLOUD-IAM-04)

- class: shares/principal policies open to foreign accounts
- probe: read-only share inventory
- wall: read-only

## Cloud Backup and Snapshot Exposure (CLOUD-OBJ-03)

- class: public/shared snapshots — the volume class
- probe: read-only snapshot attribute inventory of the declared estate
- wall: values never restored; exposure crowned only
