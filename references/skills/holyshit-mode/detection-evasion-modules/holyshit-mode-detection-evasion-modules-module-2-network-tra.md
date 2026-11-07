# MODULE 2 — NETWORK TRADECRAFT

- source canon: `holyshit-mode/detection-evasion-modules.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-04

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
