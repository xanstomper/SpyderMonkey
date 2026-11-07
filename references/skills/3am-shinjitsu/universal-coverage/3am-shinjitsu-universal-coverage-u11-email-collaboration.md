# U11 Email & collaboration

- source canon: `3am-shinjitsu/universal-coverage.md`
- bindings: **WSTG-CONF-09** · **CWE-350** · **ATT&CK T1584**
- generated: 2026-11-07

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- [ ] MX/SPF/DKIM/DMARC/MTA-STS/TLS-RPT checked and aligned
- [ ] Mailbox/SaaS sharing links, external guests, helpdesk/reset trust reviewed
- [ ] Anti-phishing controls and reporting paths validated (documentation only unless RoE)
- [ ] Domain spoofing/lookalike domains and tenant takeover risks documented
- [ ] Audit logs and retention for collaboration platforms reviewed

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
