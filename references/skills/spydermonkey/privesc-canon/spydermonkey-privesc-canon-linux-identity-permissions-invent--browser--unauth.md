# Linux — identity & permissions inventory — browser / unauth

- source canon: `spydermonkey/privesc-canon.md`
- base technique: `spydermonkey-privesc-canon-linux-identity-permissions-invent.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **browser** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

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

## Probe adjustment (browser × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
