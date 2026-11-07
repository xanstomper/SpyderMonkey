# Process-timing classes

- source canon: `spydermonkey/technique-canon-11.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-07

## Route

- probes: `smbclient`, `rpcclient`, `ldapsearch`, `netexec`, `enum4linux`, `kerbrute`, `smbmap`, `nmap-smb-security`
- chains: `win`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Race/replay windows on state transitions (the REPLAY canon). Decisive test: the idempotency/replay differential = confirmed.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
