# TECHNIQUE CANON VII — MASTG depth, binary & protocol RE, edge/CDN classes

_Every block is one technique: probe shape, decisive test, walls. MASTG/CWE-anchored, validation-only, NO-GAIN. Feeds skilltree.py — one `###` = one technique file._

## Mobile — MASTG depth

### Local storage classes (files, prefs, caches)
Secrets/PII in app files, sqlite dbs, shared prefs, caches readable from your own build (the SPY-013 id-adopted-session family is the session twin). Decisive test: your build's data dump — live secret/PII material = the finding.

### Clipboard and logging exposure
Sensitive strings in clipboard and logcat — the runtime leak class. Decisive test: your build's logcat during one sensitive action — the echoed material = the row.

### Certificate transparency of mobile APIs
API tiers never in web CT logs appear in the APK's endpoint map (the cashier.ggpoker discovery class). Decisive test: decompiled endpoint inventory + live-host resolution — hidden tiers = the finding.

### API-key extraction from the build
Embedded API keys/tokens in the binary/resources (the merchant-key class at mobile tier). Decisive test: strings/manifest analysis of your build — the key + its use-site pairing = the finding.

### Root/jailbreak detection and integrity checks (placement class)
Client-only checks are the placement finding (canon-III); integrity attestation absence (no Play Integrity / DeviceCheck) is the posture row. Decisive test: manifest/API-analysis of your build — the absent attestation = the class.

### Network-layer security of mobile APIs
APIs accepting TLS-stripped traffic, ignoring cert errors, or trusting user CAs in release builds. Decisive test: your build's traffic through a local CA — accepted = the class (MASTG-NET).

### Mobile deep-link and app-link hijack (depth)
App-links without domain verification (assetlinks absent) = hijack-prep. Decisive test: the verification file's absence on the domain — 404/missing = the class.

### Backup/cloud-sync exposure
Backed-up secrets via adb/ iCloud sync classes on your own build. Decisive test: pulled backup content — secret material = the finding.

## Binary & protocol RE (read-only canon)

### Bundle/chunk extraction discipline (the engagement-ops recipe)
Loader-stub hosts hide the logic one layer deep: follow import graphs into chunks/ — the env→host map, default-env constants, query-string auth readers live there (SPY-095 recipe). Decisive test: the extracted map verbatim from the served binary.

### String-table decoder replay
Obfuscated chunk string arrays (New Relic-style regex, i18n maps, feature flags) decode deterministically offline. Decisive test: the decoded route/feature list against the live app — leaked-internal-naming = the finding.

### Runtime crypto hook (own-build/lab)
Hooking crypto APIs of YOUR OWN build to observe signing material flow (the mkey/securityKey class) — the dataflow map is the finding; the hook runs on your device only.

### Wire-format replication recipe
Custom-binary protocol replication (the bc.game t1→/test/→t2 chain): mirror the app's packet TYPES exactly — mis-framing reads as a false gate (the SPY-069 lesson). Decisive test: handshake ACCEPTED with sid issued = protocol replication proven; wrong-ack ≠ server gate.

### WASM module execution in-page
Signing modules as WASM executed in-page for the replication chain — the module's exported functions map is the finding (execution happens in YOUR browser session on the page's own code).

### Packet-type taxonomy before conclusions
Connect-ack vs data-gate vs event-layer — misread packets manufactured the SPY-053 refutation. Rule: characterize the ack taxonomy FIRST, then interpret gates. Decisive test: the ack map itself — every gate claim cites its packet type.

### Dangling/superseded client versions
Older app versions still served (APK mirrors, cached chunks) exposing retired endpoints/auth shapes. Decisive test: old-version bundle diff against live — retired-surface presence = the finding.

## Edge & CDN classes

### Host-header routing at the edge (vhost collision)
Default/catch-all vhosts serving sibling brands (the oncasi :80 catch-all class). Decisive test: Host: sibling-brand on the origin IP — the wrong-site response = shared-origin evidence.

### Origin-cert exposure (the CF Origin Cert class)
Origin certs naming OTHER domains installed on the same box = tri-brand shared origin (SPY-012). Decisive test: TLS handshake cert chain on the ORIGIN IP — foreign SANs = the crown.

### 526/origin-TLS incident classes
CF 526 on a valid-edge-cert host = broken ORIGIN TLS (the KYC/file-tier incident). Decisive test: edge vs origin handshake comparison — the origin chain is the evidence.

### Cache-key manipulation at CDN tiers
Vary/Age/Cache-Control behaviors, query-string normalization gaps — the poisoning/deception family (canon-I) at the CDN layer. Decisive test: header telemetry over paced requests — the cache-key model is the finding.

### Geoblocking/WAF-tier inconsistency
Differential treatment by region/ASN (the partial-remediation drift class, SPY-096): a 503-gated transport with a still-200 sibling mint = partial closure. Decisive test: same probe, two regions/ASNs on the sanctioned vantages — the matrix is the finding.

### Header posture inventory
CSP/HSTS/SRI/X-Frame/X-Content-Type on every in-scope tier — the posture matrix is a generalizing recon row (one row, not hundreds — report discipline).

## Reporting-fairness classes (ledger discipline)

### Dedupe-by-leading-word discipline
Two rows sharing a leading word collide — title every finding with a distinct leading word (the engagement-ops rule). Decisive test: `ledger list` post-registration shows both rows — the survival check.

### Hypothesis-vs-CONFIRMED grading
No baseline/attack/diff = HYPOTHESIS conf 0.4, never suppressed, never CONFIRMED. Decisive test: the row's status field matches the evidence it carries — the grading integrity check.

### Honest-ceiling disclosure
When the read-only space is exhausted, the ceiling is STATED with the inventory of lanes tried — the negative-with-value finding (the SPY-091 secret-hunt closure class). Decisive test: the coverage gap-list names every closed lane.
