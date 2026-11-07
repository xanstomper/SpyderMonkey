# CI artifact and cache poisoning (documented)

- source canon: `spydermonkey/technique-canon-5.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Action/plugin supply-chain classes (canon-III) + build-cache key collision classes — characterized from the workflow/config YAML, the mechanism is the deliverable.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
