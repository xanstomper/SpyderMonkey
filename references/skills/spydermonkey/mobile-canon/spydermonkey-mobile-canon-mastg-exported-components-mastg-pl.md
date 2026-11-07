# MASTG Exported Components (MASTG-PLATFORM-03)

- source canon: `spydermonkey/mobile-canon.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: exported activities/providers/receivers callable cross-app
- probe: static manifest inventory + lab-device intent probes
- wall: lab device; no third-party interaction

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
