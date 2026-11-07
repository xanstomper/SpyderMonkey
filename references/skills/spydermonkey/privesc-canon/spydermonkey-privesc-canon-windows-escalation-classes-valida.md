# Windows — escalation classes (validation-only)

- source canon: `spydermonkey/privesc-canon.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-07

## Route

- probes: `smbclient`, `rpcclient`, `ldapsearch`, `netexec`, `enum4linux`, `kerbrute`, `smbmap`, `nmap-smb-security`
- chains: `win`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Unquoted path | writable dir before space in service path | service binary replaceable (lab) |
| Service perms | `accesschk`-class on own services | weak DACL on service |
| SeImpersonate | `seatbelt` → potato-class check (own session) | privilege present (lab POC) |
| Token dup | `pypykatz`/`Seatbelt` on own lsass dump | sensitive tokens in own dump |
| Scheduled task on demand | `schtasks /run` own task | runs as SYSTEM (lab) |

Walls: enumeration is read-only; every exploit-class confirmation runs in the
operator's OWN lab (dojo replicas or own VMs), never against third parties.
NO-GAIN: nothing is taken from a session — the rung is proven, not used.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
