# MSSQL xp/error channel and stacked-query detection

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-INPV-05** · **CWE-89** · **ATT&CK T1190**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`CONVERT` errors and batched `;WAITFOR DELAY` acceptance differ per driver. Decisive test: error reflection first; stacked-query acceptance only if the driver evidence suggests it (one probe).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
