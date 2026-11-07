# Linux — escalation classes (validation-only)

- source canon: `spydermonkey/privesc-canon.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
