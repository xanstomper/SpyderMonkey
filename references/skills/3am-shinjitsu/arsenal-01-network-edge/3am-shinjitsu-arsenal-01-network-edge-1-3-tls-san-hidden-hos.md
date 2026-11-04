# 1.3 TLS SAN hidden-host discovery (score 75, T≈2min)

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-04

## The technique

- DECISIVE: `echo \| openssl s_client -connect <host>:443 -servername <host> 2>/dev/null \| openssl x509 -noout -ext subjectAltName`
- CONFIRMED WHEN: SAN names absent from DNS enumeration AND bundle strings.
- DISCRIMINATOR: probe SAN children — JSON 404 = real router; HTML 404 = SPA shell (ghost).
- Wildcard parent may be a live backend while children don't resolve.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
