# .NET ObjectStateFormatter / ViewState

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

MAC-enabled vs legacy ViewState — the `__VIEWSTATE` parameter with tamper acceptance is the class. Decisive test: modified viewstate → distinct MAC error vs acceptance (acceptance = crown; never execute the gadget).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
