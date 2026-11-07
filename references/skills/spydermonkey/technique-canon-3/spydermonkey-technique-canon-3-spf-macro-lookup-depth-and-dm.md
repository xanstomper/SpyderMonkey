# SPF macro/lookup-depth and DMARC report-only

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

SPF +all/?all, macro abuse, lookup>10 failures; DMARC p=none with no rua = spoofable-posture. Decisive test: record parse arithmetic — the record IS the evidence (no spoofed mail sent).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
