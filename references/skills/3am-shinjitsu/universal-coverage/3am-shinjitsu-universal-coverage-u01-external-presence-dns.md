# U01 External presence & DNS

- source canon: `3am-shinjitsu/universal-coverage.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-04

## The technique

- [ ] CT logs / passive DNS / search index / paste mirrors mapped
- [ ] All apex, wildcard, IPv4/IPv6, mail, CAA, SPF/DKIM/DMARC, NS records reviewed
- [ ] TLS chain, HSTS, cert names, expired/shadow certs, host header behavior mapped
- [ ] CDN/WAF/load-balancer behavior distinguished from origin reachability
- [ ] Dead DNS records with live certificates or stale targets flagged

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
