# Spring Boot actuator exposure

- source canon: `spydermonkey/technique-canon-4.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

/env, /heapdump, /actuator/env, /actuator/gateway — the actuators leak config/secrets/heap. Decisive test: GET each actuator path — JSON config with secret keys = the crown (values masked in the report to their presence, length-masked — NO-GAIN on the material itself).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
