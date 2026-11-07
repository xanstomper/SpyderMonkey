# SMTP open-relay and auth-posture classes

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Open relay (characterized with ONE test mail to YOURSELF), STARTTLS downgrade posture, VRFY/EXPN disclosure. Decisive test: banner + the single self-addressed relay test — the acceptance is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
