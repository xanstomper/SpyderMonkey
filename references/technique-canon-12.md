# TECHNIQUE CANON XII — MASTG check canon (the mobile standard, claimed)

_Every block maps one MASTG/MASVS check: probe shape, decisive test, walls. LAB-ONLY for device work on your own builds; validation-only, NO-GAIN. Feeds skilltree.py._

## Storage classes

### Local-storage inventory
Files/db/prefs/caches holding credentials or PII (canon-X depth per-location). Decisive test: the dump row containing live material = the finding.

### Keychain-keystore inventory
Secrets outside hardware-backed keystores. Decisive test: software-backed key material on your build = the row.

### IPC data leakage
Sensitive data across app boundaries via intents/providers. Decisive test: the provider/intent path readable from your harness = the class.

### Backup extraction
adb backup / iCloud-class pull yielding secrets. Decisive test: the archive contents = the finding.

### Clipboard/caches/logs exposure
Runtime leak lanes (canon-X). Decisive test: the captured material = the rows.

## Crypto classes

### Hardcoded secrets
Keys/tokens in the binary/resources paired with use-sites. Decisive test: the key+use-site pairing = the finding.

### Weak-mode crypto
ECB/static-IV/deprecated digests in app crypto paths. Decisive test: the two-ciphertext prefix test = the class.

### Random-source classes
Non-CSPRNG token generation. Decisive test: sequence prediction on your build = the finding.

### Key-management posture
Key rotation/derivation absent. Decisive test: static keys across versions = the row.

## Auth classes

### Biometric bypass class
Biometric gates fall-backable to client secrets. Decisive test: the fallback path on your build = the class.

### Session-request handling
Cookies/tokens carried across trust boundaries unguarded. Decisive test: the cross-tier replay on your build = the row.

### Two-factor placement
OTP/MFA enforced client-side only. Decisive test: the server accepting the skip = the class.

### Auth-token integrity
Tokens verifiable client-side only (signature absent). Decisive test: forged-but-benign token accepted = the finding.

## Network classes

### TLS-validation classes
Pinning/cert-error/cleartext posture (canon-X network depth). Decisive test: the local-CA acceptance = the class.

### Endpoint inventory
Hidden API tiers from the build (the cashier class). Decisive test: resolved endpoints absent from public intel = the crown.

### Trust-anchor hygiene
Custom CAs accepted in release builds. Decisive test: user-CA traffic readable = the row.

## Platform classes

### App-patching posture
No integrity/patch-level checks (root-detection placement twin). Decisive test: modified build runs unflagged on your device = the class.

### WebView hardening
JS bridges/file-access/mixed-content classes. Decisive test: the bridge inventory + file-access flags = the rows.

### Component exposure
Exported activities/receivers/providers/deep-links (canon-X). Decisive test: the harness invocation = the class.

### App-permission posture
Over-privileged permission sets vs used APIs. Decisive test: manifest-vs-usage diff = the row.

### Code-quality exposure
Debuggable/packaged-with-symbols release builds. Decisive test: manifest debuggable=true / symbol-rich binary = the row.

### Anti-tamper absence
No root/integrity/emulator checks OR client-only placement. Decisive test: the check inventory + placement = the class.

## Resilience classes

### Update-channel security
Unsigned/HTTP update sources. Decisive test: the channel scheme audit = the row.

### Third-party dependency hygiene
Vulnerable SDK versions embedded (fingerprinted from the build). Decisive test: the version inventory vs known-CVE list = the finding.

### Data-retention posture
Sensitive data surviving logout/uninstall. Decisive test: post-logout storage state on your build = the class.

### Compliance telemetry
Analytics/trackers receiving PII. Decisive test: the traffic map on your build = the row.
