# Custom wire-format replication

- source canon: `spydermonkey/technique-canon-10.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

The t1→/test/→t2 chain recipe: mirror packet TYPES exactly before concluding any gate. Decisive test: handshake accepted with sid issued = replication proven; mis-framing is operator error, never a server gate.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
