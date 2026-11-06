# U01 External presence & DNS — container / federated

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-u01-external-presence-dns.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **container** · auth **federated** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- [ ] CT logs / passive DNS / search index / paste mirrors mapped
- [ ] All apex, wildcard, IPv4/IPv6, mail, CAA, SPF/DKIM/DMARC, NS records reviewed
- [ ] TLS chain, HSTS, cert names, expired/shadow certs, host header behavior mapped
- [ ] CDN/WAF/load-balancer behavior distinguished from origin reachability
- [ ] Dead DNS records with live certificates or stale targets flagged

## Probe adjustment (container × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
