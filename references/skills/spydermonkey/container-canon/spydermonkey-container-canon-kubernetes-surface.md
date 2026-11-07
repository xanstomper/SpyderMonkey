# Kubernetes surface

- source canon: `spydermonkey/container-canon.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-07

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
