# 1.3 TLS SAN hidden-host discovery (score 75, T≈2min) — container / unauth

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-1-3-tls-san-hidden-hos.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- context: **container** · auth **unauth** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- DECISIVE: `echo \| openssl s_client -connect <host>:443 -servername <host> 2>/dev/null \| openssl x509 -noout -ext subjectAltName`
- CONFIRMED WHEN: SAN names absent from DNS enumeration AND bundle strings.
- DISCRIMINATOR: probe SAN children — JSON 404 = real router; HTML 404 = SPA shell (ghost).
- Wildcard parent may be a live backend while children don't resolve.

## Probe adjustment (container × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
