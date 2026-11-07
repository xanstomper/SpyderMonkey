# Container host surface

- source canon: `spydermonkey/container-canon.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
