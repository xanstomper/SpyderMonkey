# 8.4 Public personnel surface (score 50)

- source canon: `3am-shinjitsu/arsenal-08-human-identity.md`
- bindings: **WSTG-ATHN-04** · **CWE-307** · **ATT&CK T1110**
- generated: 2026-11-07

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Email-format deduction from public sources (press releases, public docs), leadership pages,
  generic-role addresses (support@, billing@) — used ONLY to rate phishing exposure and to
  write the remediation section.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
