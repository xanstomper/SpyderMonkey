# Linux — escalation classes (validation-only) — mesh / guest

- source canon: `spydermonkey/privesc-canon.md`
- base technique: `spydermonkey-privesc-canon-linux-escalation-classes-validati.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **mesh** · auth **guest** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

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

## Probe adjustment (mesh × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
