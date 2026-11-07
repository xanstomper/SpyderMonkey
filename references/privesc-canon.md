# SPYDERMONKEY — Privesc Canon (v6.0)

Linux + Windows privilege-escalation classes as decisive read-only tests on
the OPERATOR'S OWN host/session (or confirmed-access sessions in scope).
Kaisha owns the ladder; this canon is the per-rung probe book.

## Linux — identity & permissions inventory

| Probe | Test | Confirmed-when |
|---|---|---|
| Who am I | `id` + `capsh --print` on own session | caps beyond baseline |
| Sudo rights | `sudo -l` (own user) | NOPASSWD entries / command whitelist |
| SUID/SGID | `find / -perm -4000 -o -perm -2000` (own host) | unexpected suid binaries |
| Capabilities | `getcap -r /` (own host) | cap_setuid/cap_dac_override on files |
| Writable PATH | check `$PATH` dirs for own-user write | path hijack candidate |
| Cron/jobs | `crontab -l`, `/etc/cron*`, systemd timers (own host) | user-writable job scripts |
| NFS exports | `showmount -e localhost` (own host) | no_root_squash share |
| Docker group | `id -nG` (own user) | docker group membership |
| Kernel version | `uname -a` cross `linux-exploit-suggester` | known CVE line |
| Environment | `env`, `printenv` (own session) | secret-ish vars, compiler, keys |
| History | `~/.bash_history` (own user) | creds in own history |
| SSH keys | `ls ~/.ssh` + permissions (own user) | readable private keys |
| Backups | `find / -name '*.bak' -o -name '*~'` (own host) | credential files |
| Tmux/screen | `tmux ls`, `/tmp/tmux-*` perms (own host) | attachable root session |

## Linux — escalation classes (validation-only)

| Probe | Test | Confirmed-when |
|---|---|---|
| Sudo command abuse | `sudo -l` → run the listed tool with its `-l`/plan | listed tool reads root-only file (own) |
| SUID exploit | `checksec` + version match on own suid binary | vulnerable version confirmed (POC on own lab) |
| Capability abuse | run cap binary's documented read (own host) | root-only file readable |
| Cron script write | own user can edit the job (own host) | script runs as root |
| PATH hijack | own-writable dir earlier in PATH | root cron invokes bare name |
| Docker escape | `docker ps` → shared socket check (own ctr) | host mounts visible (own lab) |
| systemd unit | own-writable unit in /etc/systemd | unit enabled as root |
| GTFOBins match | `gtfo`-style query for owned binary (own host) | escape confirmed in lab |

## Windows — identity & posture

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

## Windows — escalation classes (validation-only)

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