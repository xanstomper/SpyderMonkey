# Kubernetes surface — chain composition

- source canon: `spydermonkey/container-canon.md`
- base technique: `spydermonkey-container-canon-kubernetes-surface.md`
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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
