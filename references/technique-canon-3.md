# TECHNIQUE CANON III — cloud, container, AD, mobile, CMS, mail, abuse depth

_Every block is one technique: probe shape, decisive test, walls. MASTG/CIS/PTES-anchored, validation-only, NO-GAIN. Feeds skilltree.py — one `###` = one technique file._

## Cloud — AWS

### IMDS classes (v1 vs v2)
IMDSv1 (tokenless GET) reachable via SSRF = the class; IMDSv2-required = mitigated negative (bank it). Decisive test: SSRF response carrying instance-id/iam-info, or the 401 token-gate — either is a ledger row.

### IAM trust and policy enumeration (read-only)
Instance-profile metadata, `iam:GetUser`-class self-inventory, and policy documents readable with the caller's own context. Decisive test: the account's OWN permissions page/API — inventory of what the foothold can see, never a privilege walk.

### S3 policy-gap classes
Anonymous GET/LIST on bucket or prefix; ACL vs policy divergence; public-CDN origin overlap. Decisive test: anonymous LIST/GET one object (read-only) — the listing is the finding; never PUT/DELETE.

### Lambda/env and secrets-in-plaintext classes
Config exposure revealing plaintext env/secrets (e.g. error pages, config endpoints, downloadable artifacts). Decisive test: the artifact's own content — a live secret in a fetched artifact is the crown.

### CloudFront/CDN origin and behavior gaps
Origin-host mismatch, behavior path overlap (e.g. `/api/*` bypass via encoding at the edge), custom-origin header trust. Decisive test: edge request with encoded path variants — differential status from origin = the class.

### Route53/HostedZone and subdomain delegation
Delegated zones pointing at claimable/dangling NS. Decisive test: NS query chain — NXDOMAIN delegation = the domtake-prep class.

## Cloud — Azure / GCP

### Azure IMDS and SAS-token exposure
IMDS (169.254.169.254/metadata/instance) and SAS tokens in client code (long-lived, broad-scope). Decisive test: metadata response fields; SAS token parsed for scope/expiry — an unexpired broad token in client JS is the crown.

### Azure blob anonymous access
Container-level public access (list/get). Decisive test: anonymous LIST on the container endpoint — the listing is the finding.

### GCP metadata and service-account surface
metadata.google.internal classes + service-account key exposure in artifacts. Decisive test: metadata header requirement (Metadata-Flavor) honored/refused — the delta is the posture.

### GCS anonymous and allUsers grants
Public bucket/prefix listing; uniform-vs-legacy ACL gaps. Decisive test: anonymous listing request — one read-only probe.

## Containers & Kubernetes

### Anonymous API server access
`/api/v1/...` unauthenticated or system:anonymous-bound. Decisive test: GET /api/v1/namespaces anonymous — a 200 listing = the finding (read-only inventory only).

### Service-account token exposure
SA tokens in mounts/configmaps/logs readable from the confirmed foothold. Decisive test: token file readable in YOUR test pod/replica — the lab replica proves the class shape; live proof needs the foothold (kaisha-priced).

### RBAC differential (can-i as low-priv)
`kubectl auth can-i --list` shape as the low-priv principal — the INVENTORY of reachable verbs is the finding. Decisive test: your own service account's verb list.

### Kubelet read-only port and etcd exposure
10255 read-only /pods and etcd 2379 without client cert. Decisive test: GET /pods anonymous; etcd /version probe — read-only responses are the findings.

### Docker socket and registry classes
Socket mounted in a container (the escape CLASS, reported never executed) and registry catalog anonymous. Decisive test: /v2/_catalog 200 = inventory finding; socket presence = the exposure class.

### CI/CD pipeline injection and artifact poisoning (documented classes)
PR-triggered workflows executing fork-controlled code (pull_request_target misuse) and artifact substitution. Decisive test: workflow YAML analysis — the misconfiguration IS the finding (the exploit is reported as the mechanism writeup).

## Active Directory / Kerberos (read-only enum classes)

### Null-session enumeration
samr/querydominfo/userlist via null session — the inventory IS the finding. Decisive test: rpcclient/smbclient anonymous listing (read-only).

### AS-REP roastable and kerberoastable ENUMERATION
Accounts without preauth or with SPNs are ENUMERABLE read-only (the class inventory); the offline crack is the no-gain wall — register the account list, never the cracked material. Decisive test: the enum response naming the accounts.

### LDAP anonymous and rootDSE recon
Anonymous binds revealing naming contexts, schema, and object classes. Decisive test: rootDSE fetch — the disclosure depth is the finding.

### AD DNS and zone dump classes
DNS rpc/dll class zones readable anonymously (the recon layer of AD). Decisive test: zone listing — host inventory = the finding.

## Mobile — MASTG classes

### SSL pinning bypass class (runtime, own app)
Frida/objection pinning defeats on YOUR OWN app builds — the class writeup maps the app's trust chain. Decisive test: pinning observable and the defeat reproducible on your build.

### Keychain/keystore exposure class
Secrets in keychain SharedPreferences/UserDefaults readable post-install. Decisive test: your own build's storage dump — live secret material = the finding.

### WebView JS-bridge exposure
addJavascriptInterface/WebViewAssetLoader exposing native methods to remote content. Decisive test: bridge methods listed from the decompiled build — the reachable-native-surface map is the finding.

### Exported components and deep-link hijack
Exported activities/receivers and deep links accepting foreign intents. Decisive test: manifest analysis + a local intent harness on YOUR build — the hijack shape is the class.

### Backup extraction and root-detection gaps
allowBackup=true and client-only root/jail checks. Decisive test: adb backup pull of your build; the bypass shim on your device — the class is the check's client-side placement.

### IPC and pending-intent classes
Implicit intents/pending intents carrying sensitive data between exported components. Decisive test: intent interception in your harness — the data path is the finding.

## CMS depth

### WordPress REST user and wp-json exposure
/api/wp/v2/users leaking identity; wp-json route exposure beyond default. Decisive test: REST users GET anonymous — the enumeration is the finding.

### WordPress plugin/theme exposure classes
Vulnerable plugin presence (version-fingerprint via assets/readme), debug logs, upload-path listing. Decisive test: asset-path fingerprint — version+plugin map = the inventory crown.

### Joomla/Drupal config and update-server classes
configuration.php exposure class, update-server MitM posture, Drupal services endpoints anonymous. Decisive test: config-path probe distinct from the SPA-control; services endpoint anonymous response.

### CMS staging/debug artifacts
debug.log, install.php residual, backup SQL dumps under webroot. Decisive test: control-path differential (never trust a 200 shell) — distinct content = the harvest finding.

## Mail & DNS depth

### SMTP open-relay and auth-posture classes
Open relay (characterized with ONE test mail to YOURSELF), STARTTLS downgrade posture, VRFY/EXPN disclosure. Decisive test: banner + the single self-addressed relay test — the acceptance is the finding.

### SPF macro/lookup-depth and DMARC report-only
SPF +all/?all, macro abuse, lookup>10 failures; DMARC p=none with no rua = spoofable-posture. Decisive test: record parse arithmetic — the record IS the evidence (no spoofed mail sent).

### DKIM rollover gaps and weak keys
Stale selectors, sub-1024 keys, missing rotation. Decisive test: selector enumeration + published-key parse — key size is the finding.

### BIMI/MTA-STS/TLS-RPT posture
Missing MTA-STS = downgrade-tolerance posture; TLS-RPT absent = no visibility. Decisive test: record fetch — posture rows, info-class.

### DNSSEC and CAA absence
Unsigned zones and missing CAA = issuance-posture classes. Decisive test: record lookups — the absence documented as the posture row.

## Business-abuse depth

### Webhook/event pipeline abuse
Unsigned or replayable events (the SPY-102 class family) — event-name freedom + spoofed actor ids poisoning downstream automation. Decisive test: accepted event with a spoofed field on a test endpoint — the acceptance is the finding.

### Concurrent-session and piggyback policy
No session revocation on password change / unlimited parallel sessions = replay-window classes. Decisive test: old session alive after rotation on YOUR accounts — the window is the finding.

### Gift/voucher entropy and sequential structure
Code space sampled from your own purchases — sequential/predictable structure = enumerable class (register the arithmetic; never brute the live range).

### Subscription/trial entitlement persistence
Client-held entitlement flags trusted server-side (JWT claim, localStorage sync). Decisive test: expired entitlement replayed with the cached flag on YOUR account — acceptance = the class.

### Referral/cashback self-pairing arithmetic
A-refers-A and circular cashback — the arithmetic the server should refuse. Decisive test: self-pair on your own accounts — the granted credit is the finding (registered, never spent).
