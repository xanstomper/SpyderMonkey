# Trial reset and signup-limit bypass

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-BUSL-05** · **CWE-285** · **ATT&CK T1068**
- generated: 2026-11-06

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Trial entitlement tied to a client-controllable identity fragment (device id, email alias) is a logic seam. Decisive test: second trial via email+1 alias on your OWN address — entitlement granted = the finding (the abuse class, not the grant).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
