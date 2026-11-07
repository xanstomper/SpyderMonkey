# Defense Evade Impair Defenses (T1562)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: disabling logging/AV/EDR
- probe: NEVER — the opposite: protect scan proves the family leaves logs intact
- wall: REFUSED; impairing defenses violates every family law

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
