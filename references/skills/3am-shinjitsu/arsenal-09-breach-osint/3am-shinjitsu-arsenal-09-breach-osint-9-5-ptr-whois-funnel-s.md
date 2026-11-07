# 9.5 PTR/whois funnel (score 65)

- source canon: `3am-shinjitsu/arsenal-09-breach-osint.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- PTR-reverse EVERY infra IP, then whois every name in the funnel — panel boxes and vendor
  mail servers identify themselves. Unregistered-but-linked names = registration takeover
  executable same-day for the price of a domain.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
