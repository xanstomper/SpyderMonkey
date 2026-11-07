# Feed-fabrication block-test

- source canon: `spydermonkey/technique-canon-6.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Config-fabricated feeds vs server-settled rounds — the block-test (client-side fabrication refused by the settle path) is the banked negative proving settlement integrity; its absence = the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
