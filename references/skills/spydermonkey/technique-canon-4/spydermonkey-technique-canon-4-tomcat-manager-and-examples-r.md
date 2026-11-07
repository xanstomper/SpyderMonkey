# Tomcat manager and examples residue

- source canon: `spydermonkey/technique-canon-4.md`
- bindings: **PTES-PE** · **CWE-522** · **ATT&CK T1555**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

/manager/html, /host-manager, /examples residue with default or weak gate. Decisive test: HTTP 401-vs-404 classification (401 = surface exists — the inventory finding), never a credential push.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
