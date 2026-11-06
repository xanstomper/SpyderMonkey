# PHASE 2 — INFRASTRUCTURE MAPPING — chain composition

- source canon: `holyshit-mode/full-teardown-playbook.md`
- base technique: `holyshit-mode-full-teardown-playbook-phase-2-infrastructure-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- **DNS dump**: A/AAAA/CNAME/MX/TXT/NS/SRV + zone-attempt. CNAME chains → dangling subdomain
  takeover (CNAME → deprovisioned cloud service = HOLY SHIT: takeover).
- **Port/service surface**: only within scope. Map CDN/WAF (headers, ASN, TLS fingerprint).
  Origin discovery via: historical DNS (SecurityTrails-class), old cert SANs, old Wayback
  references, direct IP scans of known netblocks, mail-header leaks.
- **WAF fingerprinting**: response header quirks, block-page signatures, challenge behavior.
  Record what evasion class is even necessary.
- **Cloud posture**: public buckets (S3/GCS/Azure blob naming patterns), exposed object
  listings, metadata endpoints, Cloudflare-only vs origin-direct behavior.
- Deliverable: asset graph, origin map, WAF/CDN posture, dangling-takeover candidates.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
