# Two-salt and ticket-mint traps

- source canon: `spydermonkey/technique-canon-6.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

The t1 ticket = clock-embedded identity-mint (not input echo); salt pairs that LOOK like PF are server traps — characterize the mint anatomy from the bundle before claiming any prediction class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
