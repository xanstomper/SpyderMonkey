# 1.14 Passive-DNS bare-IP fleet classification (score 85, zero target traffic)

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## The technique

- DECISIVE: hackertarget hostsearch ∩ crt.sh CT names → `dig +short A <host> @1.1.1.1`
  each, classify by owner: CF ranges (104.16-104.19/172.64/188.114/162.159/198.41) =
  WAF'd; everything else = DIRECT-ORIGIN surface invisible to the edge WAF.
- Bare survivors (DO/EC2/Linode/AGA) get the §1.4 banner battery immediately — the cartel
  move: message queues and internal services hide on exactly these hosts.
- AGA tell: PTR `*.awsglobalaccelerator.com` = static anycast fronting; SNI-pin with
  `curl --resolve <host>:443:<ip>` even when public DNS no longer resolves the hostname.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
