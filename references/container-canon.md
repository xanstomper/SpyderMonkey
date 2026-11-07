# SPYDERMONKEY — Container & Kubernetes Canon (v6.0)

Container- and cluster-surface classes as read-only decisive tests in the
OPERATOR'S OWN cluster/containers (or in-scope estate declared in scope.json).
Bindings: CWE-250/1188 · ATT&CK T1610/T1622.

## Container host surface

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

## Kubernetes surface

| Probe | Test | Confirmed-when |
|---|---|---|
| Cluster reach | `kubectl cluster-info` (own cluster) | API reachable |
| RBAC inventory | `kubectl auth can-i --list -A` (own SA) | over-privileged verbs |
| SA tokens | `cat /var/run/secrets/...` inside own pod | mounted token readable |
| etcd exposure | `kubectl get pods -n kube-system` (own cluster) | etcd in known namespace |
| Kubelet API | `kubeletctl pods --kubelet X` (own node) | anonymous kubelet endpoint |
| Dashboards | `kubectl get svc -A` (own cluster) | dashboard/monitoring svc exposed |
| Helm secrets | `helm ls -A` + `helm get values` (own cluster) | secrets in values |
| Image pull secrets | `kubectl get secrets -A` (own cluster) | registry creds retrievable |
| Network policies | `kubectl get netpol -A` (own cluster) | no policies isolating namespaces |
| Pod security | `kubectl get psp/podsecurity` (own cluster) | permissive policies |
| Mutating admission | `kubectl get mutatingwebhookconfigurations` (own) | injectable webhooks |
| Cloud metadata | `curl http://169.254.169.254/latest/meta-data/` timeout (own pod) | IMDS reachable from pod |

## Attack-path classes (validation)

| Probe | Test | Confirmed-when |
|---|---|---|
| RBAC → secret read | `kubectl get secret -A` with the operator's SA (own) | secrets readable with current verbs |
| SA token reuse | use own pod token against API (own cluster) | token carries extra permissions |
| Pod create → host | `kubectl run` privileged pod spec (own lab ns) | hostPath mount succeeds |
| Supply chain confusion | `osv-scanner`/`govulncheck` on own repos | malicious typosquat candidate |
| Registry pull-through | `crane catalog` own registry | public buckets/list surface |
| kube-bench | `kube-bench` against own nodes | CIS violations |

Walls: all operations are in the operator's OWN cluster/containers; anything
that writes (pod creation, image pull into cluster namespaces) happens in a
throwaway lab namespace and is torn down after proof. No third-party clusters.