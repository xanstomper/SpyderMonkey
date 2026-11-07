# Windows — identity & posture — container / expired

- source canon: `spydermonkey/privesc-canon.md`
- base technique: `spydermonkey-privesc-canon-windows-identity-posture.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **container** · auth **expired** · chain role **pivot**

## Route

- probes: `smbclient`, `rpcclient`, `ldapsearch`, `netexec`, `enum4linux`, `kerbrute`, `smbmap`, `nmap-smb-security`
- chains: `win`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

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

## Probe adjustment (container × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
