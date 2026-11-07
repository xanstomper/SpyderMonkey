# Windows — identity & posture — cloud / machine

- source canon: `spydermonkey/privesc-canon.md`
- base technique: `spydermonkey-privesc-canon-windows-identity-posture.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **cloud** · auth **machine** · chain role **pivot**

## Route

- probes: `smbclient`, `rpcclient`, `ldapsearch`, `netexec`, `enum4linux`, `kerbrute`, `smbmap`, `nmap-smb-security`
- chains: `win`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Whoami | `whoami /all` (own session) | unusual groups (admins, service) |
| Token | `seatbelt -group=token` (own session) | enabled privileges (SeDebug etc.) |
| Services | `seatbelt -group=services` | unquoted path / writable bin |
| Scheduled tasks | `schtasks /query` (own session) | writable task actions |
| Registry autostart | `reg query HKLM\...\Run` (own host) | writable keys |
| Stored credentials | `cmdkey /list` (own session) | cached creds |
| AlwaysInstallElevated | `reg query` both policies (own host) | both set → msi privesc class |
| Unattend files | `dir /s unattend.xml C:\` (own host) | plaintext admin creds |
| WESNG | `wesng --update && wesng` on own build | known CVE present |
| AppLocker/Defender | `Get-MpComputerStatus`-class (own host) | policy gaps |

## Probe adjustment (cloud × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
