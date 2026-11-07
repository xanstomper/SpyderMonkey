# Rails render-params

- source canon: `spydermonkey/technique-canon-9.md`
- bindings: **WSTG-INPV** · **CWE-1321** · **ATT&CK T1190**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

render params[] legacy acceptance = the LFI class (detection). Decisive test: the error-class delta on your own request.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
