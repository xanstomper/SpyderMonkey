# Container host surface — gateway / expired

- source canon: `spydermonkey/container-canon.md`
- base technique: `spydermonkey-container-canon-container-host-surface.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **gateway** · auth **expired** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Runtime inventory | `docker ps -a` / `podman ps -a` (own host) | images/containers enumerated |
| Socket exposure | `ls -la /var/run/docker.sock` (own host) | write-accessible socket |
| Capabilities | `capsh --print` inside own container | CAP_SYS_ADMIN etc. present |
| Seccomp/apparmor | `docker inspect --format '{{.HostConfig.SecurityOpt}}'` own ctr | seccomp unconfined |
| Root user | `id -u` in own container | uid 0 without userns |
| Bind mounts | `mount` inside own container | host paths mounted rw |
| Privileged flag | `docker inspect` own container | Privileged=true |
| Host PID/net | `cat /proc/1/cgroup`, `ip link` (own ctr) | host network/PID view |
| Escape vectors | `cdk auto-escape` (own container) | escape primitive confirmed (own lab) |
| Image history | `docker history` own images | secrets baked into layers |
| Supply chain | `syft`/`grype`/`trivy` on own images | vulnerable/malicious components |

## Probe adjustment (gateway × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
