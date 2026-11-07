# Docker socket and registry classes

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **PTES-CON** · **CWE-250** · **ATT&CK T1611**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Socket mounted in a container (the escape CLASS, reported never executed) and registry catalog anonymous. Decisive test: /v2/_catalog 200 = inventory finding; socket presence = the exposure class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
