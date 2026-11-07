# Windows — escalation classes (validation-only) — edge-node / high-priv

- source canon: `spydermonkey/privesc-canon.md`
- base technique: `spydermonkey-privesc-canon-windows-escalation-classes-valida.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **edge-node** · auth **high-priv** · chain role **pivot**

## Route

- probes: `smbclient`, `rpcclient`, `ldapsearch`, `netexec`, `enum4linux`, `kerbrute`, `smbmap`, `nmap-smb-security`
- chains: `win`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

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

## Probe adjustment (edge-node × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
