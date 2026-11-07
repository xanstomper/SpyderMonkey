# PHASE 2 — INFRASTRUCTURE MAPPING — wasm / expired

- source canon: `holyshit-mode/full-teardown-playbook.md`
- base technique: `holyshit-mode-full-teardown-playbook-phase-2-infrastructure-.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **wasm** · auth **expired** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

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

## Probe adjustment (wasm × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
