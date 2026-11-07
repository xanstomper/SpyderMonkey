# h2c smuggling and header-based downgrade

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-ADV-02** · **CWE-444** · **ATT&CK T1190**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Upgrade: h2c accepted on a proxy front = smuggling class. Decisive test: lab-replica h2c handshake through the front, one probe pair, timing delta — never a burst at a shared edge.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
