# Container host surface — chain composition

- source canon: `spydermonkey/container-canon.md`
- base technique: `spydermonkey-container-canon-container-host-surface.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
