# TECHNIQUE CANON X — mobile, binary-RE, DNS & email canon

_Every block is one technique: probe shape, decisive test, walls. MASTG/CWE-anchored, validation-only, NO-GAIN. Feeds skilltree.py — one `###` = one technique file._

## MASTG — storage classes

### App-files secret scan
App-private storage (files/, databases/, shared_prefs) holding tokens/PII on your own build. Decisive test: your build's data dump showing live secret material outside keychain.

### Database plaintext classes
SQLite db inside app data with unencrypted sensitive columns. Decisive test: pulled db row readable — plaintext credential/session material = the finding.

### Cache and temp leakage
Sensitive responses cached to disk caches surviving app close. Decisive test: cache dump after one authenticated action on your build — the response body on disk = the row.

### Logs secret echo
Logcat echoing tokens/PII during normal use (SPY-532 canon). Decisive test: logcat capture during one action — the echoed secret = the finding.

### Clipboard exposure
Sensitive values copied to clipboard readable by any app until replaced. Decisive test: clipboard read after your own copy action — the material = the row.

### Backup archive classes
allowBackup/autoBackup pulling private data via adb backup on your build. Decisive test: extracted archive containing secrets = the class.

## MASTG — crypto & key classes

### Hardcoded key inventory
API keys/signing secrets embedded in binary or resources. Decisive test: string scan pairing the key with its live use-site = the finding.

### Keychain/keystore posture
Credentials reachable outside hardware-backed storage on your build. Decisive test: key inventory showing software-backed secrets = the row.

### Weak local crypto classes
ECB mode, static IV, MD5/SHA1 for tokens in the app's own code. Decisive test: decompiled crypto-site inventory + two-ciphertext prefix test = the class.

### Random-source weakness
Math.random/java.util.Random generating security tokens. Decisive test: token sequence prediction from sampled outputs on your build = the finding.

## MASTG — network classes

### TLS-pinning placement
Pinning absent or implemented only in debug builds. Decisive test: your build's traffic through a local CA accepted = the class.

### Certificate-error tolerance
App proceeds on invalid certs (WebView handler returning true). Decisive test: local MITM cert accepted on your build = the row.

### Cleartext traffic posture
usesCleartextTraffic true / http endpoints live. Decisive test: manifest flag + one http call observed = the finding.

### API tier discovery via build
Endpoint hosts in the build absent from web CT/DNS intel (the hidden-cashier class). Decisive test: decompiled endpoint list + live resolution = the inventory crown.

## MASTG — platform classes

### Exported component reach
Exported activities/services/receivers callable from any app. Decisive test: local intent harness invoking your build's component = the class.

### Deep-link hijack prep
App links without assetlinks verification. Decisive test: the verification file 404 on the domain = hijack-prep row.

### WebView bridge exposure
addJavascriptInterface exposing native methods to remote content. Decisive test: bridge method inventory from the build + the remote-content reach path = the class.

### IPC pending-intent leakage
Mutable pending intents carrying sensitive extras. Decisive test: intent interception in your harness = the finding.

### Root-detection placement
Client-only checks with no remote attestation. Decisive test: absent Play Integrity/DeviceCheck calls in the build = the posture row.

### Screenshot masking absence
FLAG_SECURE absent on sensitive screens. Decisive test: task-switcher thumbnail shows account data on your build = the row.

## Binary RE — read-only intel

### Symbol-table posture
Stripped vs symbol-rich binaries revealing internal naming. Decisive test: symbol inventory of your own build — the naming map = the recon row.

### Embedded config extraction
Default config/env tables in the binary (the env→socket map class). Decisive test: config block extracted verbatim — the map is the finding.

### Updater channel disclosure
Update URLs/version endpoints in the binary exposing internal tiers. Decisive test: the URL list + live resolution = the intel row.

### Padding/signature posture
Binary integrity checks absent (no signature validation on update). Decisive test: update-channel behavior analysis on your build = the class.

## Protocol RE — replication discipline

### Protobuf schema mining
Proto definitions embedded in binaries/bundles reveal full message surface. Decisive test: descriptor parse — the field map = the finding.

### Thrift/flatbuffers schema paths
IDL definitions or generated codecs exposing the same. Decisive test: schema constants recovered = the inventory.

### Custom wire-format replication
The t1→/test/→t2 chain recipe: mirror packet TYPES exactly before concluding any gate. Decisive test: handshake accepted with sid issued = replication proven; mis-framing is operator error, never a server gate.

### Packet-type taxonomy rule
Connect-ack vs data-gate vs event-layer distinguished BEFORE interpretation (the SPY-053 refutation lesson). Decisive test: the ack map — every gate claim cites its packet type.

### WASM module mapping
Signing/verification WASM exports enumerated from the served module. Decisive test: export table + call-site pairing = the finding.

### Dangling client versions
Retired app versions/chunks still served exposing old auth shapes. Decisive test: old-version bundle diff vs live = the drift row.

## DNS depth

### DNSSEC walking classes
NSEC/NSEC3 enumeration of the zone (the walking-oracle class). Decisive test: NSEC next-name disclosure listing real names = the finding.

### Wildcard behavior mapping
Wildcard responses masking enumeration — the wildcard-detection discipline (fierce/dnswalk canon). Decisive test: random-label response uniformity = the negative/positive row.

### Registrar and NS intel
Registrar transfer-lock posture, NS provider tiering, DS record presence. Decisive test: WHOIS/NS/DS queries = the posture rows.

### DNS-cookie and anycast classes
EDNS-cookie support and anycast divergence affecting enumeration honesty. Decisive test: cookie echo behavior = the measurement note.

### Captive-portal classes (lab)
Lab captive-portal redirect behavior characterization only. Decisive test: your lab portal's redirect path = the class row.

### CAA and issuance policy
CAA records restricting issuers — absence = issuance-posture row. Decisive test: record fetch = the posture.

## Email infrastructure depth

### SMTP extension inventory
EHLO response extensions (STARTTLS, AUTH, SIZE) — the posture map. Decisive test: capability response = the finding.

### STARTTLS/DANE posture
TLS support and TLSA/DANE records for mail tiers. Decisive test: handshake + TLSA lookup = the posture rows.

### Header-leak classes
Inbound mail headers revealing internal hostnames/IPs of the estate (your own mailbox). Decisive test: header analysis of a self-sent test = the intel row.

### Mailing-list archive leakage
Public archives exposing estate artifacts (zero-document: estate content only, never people). Decisive test: archive search for domain strings = the harvest row.

### SPF macro and lookup-depth classes
Macro usage and >10 lookup failure modes weakening SPF. Decisive test: record parse arithmetic = the posture finding.

### DKIM rotation gaps
Stale selectors and missing rotation (canon-III at depth). Decisive test: selector sweep + published-key size = the row.

### MTA-STS and TLS-RPT absence
Missing policies = downgrade-tolerance posture. Decisive test: policy fetch = the rows.

### BIMI/VMDM posture
BIMI record without verification = cosmetic-security row. Decisive test: record parse = the posture.
