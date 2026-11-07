# Windows — identity & posture — chain composition

- source canon: `spydermonkey/privesc-canon.md`
- base technique: `spydermonkey-privesc-canon-windows-identity-posture.md`
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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
