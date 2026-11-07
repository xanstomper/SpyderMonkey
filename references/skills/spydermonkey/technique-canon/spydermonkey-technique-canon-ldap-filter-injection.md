# LDAP filter injection

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- generated: 2026-11-06

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

(&(objectClass=*)) metachar reflection into an LDAP filter. Decisive test: value=*)(uid=* — a changed result count = filter injection.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
