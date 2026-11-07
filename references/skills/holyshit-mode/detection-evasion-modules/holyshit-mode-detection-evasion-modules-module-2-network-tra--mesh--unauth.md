# MODULE 2 — NETWORK TRADECRAFT — mesh / unauth

- source canon: `holyshit-mode/detection-evasion-modules.md`
- base technique: `holyshit-mode-detection-evasion-modules-module-2-network-tra.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **mesh** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

**Objective**: validate network detection of C2 and exfiltration channels.

**Techniques**:
- **Domain fronting**: route C2 through CDN with front domain (aws.amazon.com class) and
  custom domain. Validate: does the proxy inspect the Host header or only the SNI?
- **DNS tunneling**: encode data in TXT/NULL queries with low-and-slow timing (1 query/30s).
  Validate: does DNS analytics flag entropy/volume or only known-bad domains?
- **HTTPS beacon jitter**: vary sleep 30–90s, randomize URI paths, mimic browser JA3.
  Validate: does the NDR flag periodicity, JA3 anomalies, or URI entropy?
- **ICMP/SMB exfil**: tunnel data through ICMP echo or SMB named pipes on isolated segments.
  Validate: does the IDS inspect non-HTTP protocols or only port 80/443?
- **Dead-drop resolvers**: store C2 instructions in public paste/gist, poll infrequently.
  Validate: does egress filtering flag paste sites or only known C2 domains?

**Detection surface to report**: NDR flow analytics, JA3/JA3S fingerprinting, DNS analytics,
egress allow-listing, TLS inspection coverage, protocol anomaly detection.

---

## Probe adjustment (mesh × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
