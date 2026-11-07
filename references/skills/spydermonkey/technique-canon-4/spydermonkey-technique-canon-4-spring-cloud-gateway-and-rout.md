# Spring Cloud Gateway and routing-injection classes

- source canon: `spydermonkey/technique-canon-4.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- generated: 2026-11-06

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Documented actuator-driven route injection is REPORTED as the mechanism writeup; decisive test is the config-diff endpoint's presence, not the executed reroute.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
