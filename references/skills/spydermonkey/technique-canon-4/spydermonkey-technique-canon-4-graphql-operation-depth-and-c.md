# GraphQL operation-depth and cost classes

- source canon: `spydermonkey/technique-canon-4.md`
- bindings: **WSTG-APIT-10** · **CWE-1321** · **ATT&CK T1190**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Depth/cost limiting absent → the CLASS is the missing guard, characterized with a bounded depth-10 introspection-style query (one request), never a sustained flood.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
