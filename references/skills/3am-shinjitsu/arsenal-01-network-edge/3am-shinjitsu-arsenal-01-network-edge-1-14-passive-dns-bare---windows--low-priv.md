# 1.14 Passive-DNS bare-IP fleet classification (score 85, zero target traffic) — windows / low-priv

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-1-14-passive-dns-bare-.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **windows** · auth **low-priv** · chain role **pivot**

## Context

- platform: token/session confusion classes; read-only enumeration, NO-GAIN
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- DECISIVE: hackertarget hostsearch ∩ crt.sh CT names → `dig +short A <host> @1.1.1.1`
  each, classify by owner: CF ranges (104.16-104.19/172.64/188.114/162.159/198.41) =
  WAF'd; everything else = DIRECT-ORIGIN surface invisible to the edge WAF.
- Bare survivors (DO/EC2/Linode/AGA) get the §1.4 banner battery immediately — the cartel
  move: message queues and internal services hide on exactly these hosts.
- AGA tell: PTR `*.awsglobalaccelerator.com` = static anycast fronting; SNI-pin with
  `curl --resolve <host>:443:<ip>` even when public DNS no longer resolves the hostname.

## Probe adjustment (windows × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
