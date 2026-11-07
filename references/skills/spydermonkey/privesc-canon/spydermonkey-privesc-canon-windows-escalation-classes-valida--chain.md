# Windows — escalation classes (validation-only) — chain composition

- source canon: `spydermonkey/privesc-canon.md`
- base technique: `spydermonkey-privesc-canon-windows-escalation-classes-valida.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `smbclient`, `rpcclient`, `ldapsearch`, `netexec`, `enum4linux`, `kerbrute`, `smbmap`, `nmap-smb-security`
- chains: `win`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
