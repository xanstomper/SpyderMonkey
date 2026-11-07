# Linux — identity & permissions inventory — chain composition

- source canon: `spydermonkey/privesc-canon.md`
- base technique: `spydermonkey-privesc-canon-linux-identity-permissions-invent.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
