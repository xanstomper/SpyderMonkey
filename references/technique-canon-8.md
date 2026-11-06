# TECHNIQUE CANON VIII — API & cloud deep canon

_Every block is one technique: probe shape, decisive test, walls. Validation-only, NO-GAIN. Feeds skilltree.py — one `###` = one technique file._

## API Top-10 classes

### BOLA object-swap
Endpoint returning objects by id accepts another tenant's/owner's id (the IDOR family). Decisive test: baseline with your object, attack with a sibling id you control — swapped content = CONFIRMED.

### BFLA action-swap
An action endpoint (export/invite/execute) executes for a lower-priv principal. Decisive test: the action POST replayed with the low-priv token — acceptance = the class.

### Unrestricted resource consumption
A query param (size/depth/page) without caps — one request measuring a bounded cost delta. Decisive test: the response cost curve's knee documented — no sustained drain.

### API broken-auth context
Endpoint trusting a client header (X-User-Id class) for identity. Decisive test: header override on your own session changing the returned identity = the class.

### API field-level authorization
Response filtering hides fields the server still accepts on write (the mass-assign twin). Decisive test: hidden-field write on your own record = the finding.

### API versioning drift
Deprecated version still live with the patched behavior missing. Decisive test: same request across /v1,/v2 — the policy delta = the row.

### API scope confusion
Token scopes checked per-endpoint inconsistently. Decisive test: narrow-scope token accepted on a wider endpoint = the class.

### API SSRF via import/url fields
Endpoints accepting callback/import URLs (webhook twin at API tier). Decisive test: fetch to YOUR listener = the proof.

### API batch abuse
Batch/multi-endpoint accepting N operations in one call, bypassing per-op checks. Decisive test: 2-op batch where op-2 alone would 403 = the class.

### API key lineage leakage
Keys accepted in query/legacy headers (SPY-048 family) — the acceptance is the finding; crown = the key's cross-service reach.

## AWS per-service classes

### S3 policy-gap matrix
Anonymous GET/LIST/PREFIX-divergence and policy-vs-ACL conflict classes. Decisive test: anonymous LIST on the bucket, one object GET — read-only rows.

### S3 prefix divergence
Public prefix (`/public/*`) with private siblings sharing the bucket policy. Decisive test: anonymous listing at the public prefix vs bucket root — the divergence = the finding.

### IAM assume-role trust exposure
Role trust policies naming external accounts/wildcards (read-only via your own principal's visibility). Decisive test: trust policy document fetch where permitted — the wildcard = the finding.

### Lambda env/event classes
Function config exposure (env vars in artifacts) and unauth event-ingestion endpoints. Decisive test: config artifact fetch — the plaintext env = the crown.

### DynamoDB unauth indices
Table scans/index reads with no auth on the API lane. Decisive test: one bounded scan against YOUR test table = the class.

### SQS/SNS policy gaps
Queue/topic policies with wildcard principals or open HTTP notification endpoints. Decisive test: policy doc where readable + one subscribe-probe to YOUR endpoint = the class.

### CloudFront behavior gaps
Path-handling divergences (encoding, case) bypassing behavior restrictions at the edge. Decisive test: encoded variant of a restricted path — origin 200 = the finding.

### Route53 delegation drift
Hosted-zone records pointing at retired/dead targets (the domtake-prep class). Decisive test: record-by-record resolution sweep = the inventory.

### Secrets Manager paths
Secrets referenced in plaintext configs/artifacts (the path, not the material). Decisive test: config reference + the tier's auth posture = the row.

## Azure per-service classes

### Blob SAS token classes
SAS tokens in client code: long expiry, wide scope, no IP lock. Decisive test: parsed token's scope/expiry fields = the finding.

### Blob anonymous access
Container public-access levels (blob/container). Decisive test: anonymous container LIST = the inventory.

### AD app-registration exposure
App registrations exposing redirect URIs/secrets-rotation posture (read-only via your tenant view). Decisive test: the registration's reply-URL list = the class.

### Key Vault posture
Vaults with public network access + soft-delete absent. Decisive test: public reachability of the vault endpoint = the posture row.

### Function-app default hosts
scm/ftp/kudu endpoints default posture. Decisive test: endpoint reachability + auth-class = the inventory.

## GCP per-service classes

### IAM service-account keys
User-managed keys aging/stale (readable from your own project view). Decisive test: key inventory with old keyIds = the finding.

### GCS policy classes
allUsers/allAuthenticatedUsers grants on buckets/objects. Decisive test: policy doc + one anonymous GET = the class.

### Metadata classes
metadata.google.internal with flavor-header enforcement — the guard's presence/absence IS the row. Decisive test: SSRF probe honoring the header = the posture.

### Cloud Functions ingress
Function HTTP ingress set to all. Decisive test: unauth invoke reaching the function's auth stage = the class.

## Kubernetes per-resource classes

### RBAC verb inventory
The reachable verb set of a given principal (can-i list shape). Decisive test: your own service account's verb list = the inventory finding.

### Pod security classes
privileged/hostPID/hostNetwork pods present (readable from the workload spec). Decisive test: spec listing = the posture row.

### Service exposure matrix
NodePort/LoadBalancer surfaces mapping internal services externally. Decisive test: svc listing + external reachability of one = the finding.

### Ingress misroute classes
Ingress path precedence letting encoded paths reach internal services. Decisive test: the encoded variant through the edge = the class.

### ConfigMap/Secret exposure
Sensitive material in ConfigMaps (not Secrets) readable cluster-wide. Decisive test: your own namespace's cm listing = the row.

### etcd exposure
2379 reachable without client certs. Decisive test: /version probe — the response = the finding (read-only, never a dump).

### Kubelet API classes
10250 auth bypass classes / 10255 read-only port. Decisive test: /pods anonymous = the inventory.

### Admission-policy absence
No PSA/admission webhooks — privileged workloads accepted. Decisive test: policy listing absent + your test pod accepted in a LAB cluster = the class.

## Serverless & gateway classes

### Function URL auth-absence
Cloud function URLs / lambda-function-urls public. Decisive test: one anonymous invoke reaching the handler's auth stage = the row.

### API-gateway bypass classes
Stage/path quirks (trailing slash, encoding, method override) reaching routes unauth. Decisive test: the variant through the gateway = the class.

### Gateway authorizer gaps
Custom authorizers caching identity by wrong key (the identity-mixup class). Decisive test: two principals sharing a cached response = the finding (your own test pair).

### Edge-worker injection surface
Worker scripts reading request material into responses (the SDK class at edge tier). Decisive test: passive capture of the worker's transforms = the map.
