# Parameter entities and OOB variants

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-INPV-07** · **CWE-611** · **ATT&CK T1190**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`%remote;` parameter-entity exfil for filteredXXE contexts, error-based local read. Decisive test: OOB arrival at your listener from the parameter entity; error-message file reflection as the alternate channel.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
