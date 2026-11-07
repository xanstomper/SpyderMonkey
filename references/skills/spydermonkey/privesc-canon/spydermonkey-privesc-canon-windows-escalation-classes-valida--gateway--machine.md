# Windows — escalation classes (validation-only) — gateway / machine

- source canon: `spydermonkey/privesc-canon.md`
- base technique: `spydermonkey-privesc-canon-windows-escalation-classes-valida.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **gateway** · auth **machine** · chain role **pivot**

## Route

- probes: `smbclient`, `rpcclient`, `ldapsearch`, `netexec`, `enum4linux`, `kerbrute`, `smbmap`, `nmap-smb-security`
- chains: `win`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

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

## Probe adjustment (gateway × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
