# U01 External presence & DNS — container / machine

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-u01-external-presence-dns.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **container** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- [ ] CT logs / passive DNS / search index / paste mirrors mapped
- [ ] All apex, wildcard, IPv4/IPv6, mail, CAA, SPF/DKIM/DMARC, NS records reviewed
- [ ] TLS chain, HSTS, cert names, expired/shadow certs, host header behavior mapped
- [ ] CDN/WAF/load-balancer behavior distinguished from origin reachability
- [ ] Dead DNS records with live certificates or stale targets flagged

## Probe adjustment (container × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
