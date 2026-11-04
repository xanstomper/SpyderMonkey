# 1.14 Passive-DNS bare-IP fleet classification (score 85, zero target traffic) — chain composition

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-1-14-passive-dns-bare-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- DECISIVE: hackertarget hostsearch ∩ crt.sh CT names → `dig +short A <host> @1.1.1.1`
  each, classify by owner: CF ranges (104.16-104.19/172.64/188.114/162.159/198.41) =
  WAF'd; everything else = DIRECT-ORIGIN surface invisible to the edge WAF.
- Bare survivors (DO/EC2/Linode/AGA) get the §1.4 banner battery immediately — the cartel
  move: message queues and internal services hide on exactly these hosts.
- AGA tell: PTR `*.awsglobalaccelerator.com` = static anycast fronting; SNI-pin with
  `curl --resolve <host>:443:<ip>` even when public DNS no longer resolves the hostname.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
