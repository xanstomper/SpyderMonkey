# TECHNIQUE CANON V — OSINT depth, wireless/hardware (lab), supply-chain, ICS pointers

_Every block is one technique: probe shape, decisive test, walls. Validation-only, NO-GAIN. Feeds skilltree.py — one `###` = one technique file._

## OSINT & recon depth

### Breach-correlation row discipline
Leak claims need ROW-LEVEL correlation (the engagement-ops rule): decisive test is `username == masked` AND `display_username == real` on the SAME row — counts alone are hypothesis. Report masked → correlated → unique-id funnel.

### Paste/site and dump-index sweeps
Paste-site keyword sweeps and dump-index catalogs tied to the estate (LeakRadar-class sources) — the row-level rule applies. Decisive test: source URL + correlated row count per source, distinct leading words per title (dedupe discipline).

### Code-search dorking (github/gitlab/gist)
Org-attribution via user-id chains (the SPY-067 class family), deleted-file recovery, committed secrets in value="" attributes, committed CSVs as QA telemetry. Decisive test: the recovered artifact itself (file/blob path) — the artifact is the evidence.

### Git-dorking across branches and dangling objects
`git log --all --diff-filter=D`, dangling blobs via rev-list --objects, deleted verify pages recoverable. Decisive test: the recovered object content — provenance-stamped.

### CT-log depth and cert-lifecycle intel
Precertificates naming internal tiers, revoked-expired certs mapping retired infra, SAN-mining (canon-I) — the lifecycle timeline IS the inventory. Decisive test: log query + live-cert SAN diff.

### ASN/BGP/WHOIS netblock intel
Estate netblocks via ASN, rDNS sweep across the range, WHOIS org pivots — the netblock map extends the scope estate (scope add is the operator's call). Decisive test: rDNS inventory rows for in-scope ranges.

### Passive DNS and historic-resolution
Historic A/CNAME maps exposing retired hosts and takeover-prep (pairs with domtake canon). Decisive test: historic record vs live resolution — retired-but-referenced = the finding.

### Network-device and edge intel
Banner/version on edge tiers (load balancers, firewalls) — era-stack mapping (kaisha). Decisive test: banner fingerprint per edge tier — the era stack is the finding.

### Employee/artifact-string exposure (zero-document boundary)
Public artifact strings (git emails, doc metadata) — barbican's protect/sanitize canon applied OFFENSIVELY as recon: what does the ESTATE leak about itself. Decisive test: the string source URL — each leak is a row. Zero-document rule: no people-targeting, estate-artifacts only.

### Domaintools-class passive-total and sibling-brand mapping
Registration-tree expansion (registrant org → sibling brands) feeding the shared-backend hypothesis (the error-taxonomy canon-I test confirms). Decisive test: whois org field + the sibling's confirmed shared taxonomy.

## Wireless & hardware (LAB-ONLY lanes)

### WiFi posture classes (lab)
Open/guest-network isolation classes, WPA2-Enterprise cert-validation behavior — probed ONLY on lab APs you own. Decisive test: client isolation between your own two lab stations — the reachability delta is the class.

### BLE enumeration (lab)
GATT service/characteristic inventory on lab devices — write-characteristic tests NEVER fired on third-party devices. Decisive test: your lab device's characteristic map — unauth-read characteristics = the class.

### SDR capture classes (lab)
Rolling-code capture-replay characterization on YOUR OWN remotes — documented class, lab proof only. The deliverable is the mechanism writeup.

### NFC/RFID (lab)
UID-tag reads on lab badges — the readable-UID class (static-UID tags = cloneable-class, documented). Decisive test: your own lab badge read twice — identical UID = the class row.

### UART/JTAG/SPI (lab, own hardware)
Console discovery (baud-rate sweep on your own board), JTAG chain enumeration, SPI flash dump — firmware-extraction classes with the no-gain read-only framing (MASTG-RES canon). Decisive test: the extracted image hash + strings inventory of YOUR device.

### Fault-injection and glitching (documented class)
Voltage/clock glitch classes are DOCUMENTED as mechanisms (the writeup), never executed — the lab bench characterizes the defensive-relevance row only.

## Supply-chain & build-integrity

### Dependency-confusion class
Internal package names resolvable from public registries — the CLASS is the name-collision exposure. Decisive test: registry metadata check for an internal-named package (metadata only, never publish) — resolvable = the finding.

### CI artifact and cache poisoning (documented)
Action/plugin supply-chain classes (canon-III) + build-cache key collision classes — characterized from the workflow/config YAML, the mechanism is the deliverable.

### Vendor SDK supply-chain (the SPY-095 class family)
Production pages importing personal/third-party infra (workers.dev class), SDK env-defaults (`mode||"development"`), auth material in URLs. Decisive test: passive capture of the page's OWN traffic (in-scope), the executing SDK pulled and cold-mapped — the env->host map verbatim is the crown.

### SRI/CSP posture on third-party integrations
Script integrations without SRI + CSP none = the injection amplifier (SPY-056 class). Decisive test: header posture + script-tag audit of the live page — the posture row is the finding.

## ICS/SCADA pointers (read-only class inventory)

### Modbus/S7/BACnet exposure classes
Protocol banners reachable unauth (502/102/47808) — the BANNER is the inventory finding; control writes are the absolute wall (never sent). Decisive test: read-only identity/banners on in-scope industrial tiers.

### HMI/historian web surfaces
Vendor HMI web fronts with default-posture banners. Decisive test: banner + auth-gate class — inventory only.
