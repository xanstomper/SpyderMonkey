# Disposable-email filter bypass (discovery recipe)

- source canon: `holyshit-mode/case-gonka-api.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Signup enforces a 23514 CHECK constraint on email domain.
- Blocked: tempmail, guerrillamail, yopmail, 10minutemail, maildrop, getnada,
  dispostable, fakeinbox, trashmail, sharklasers, grr.la.
- MISSED (200): harakirimail.com, pokemail.net, spam4.me, bccto.me, chammy.info.
- Discovery: batch-signup one probe account per candidate domain, read
  200 vs 23514. A filter-list gap = automate account creation at scale.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
