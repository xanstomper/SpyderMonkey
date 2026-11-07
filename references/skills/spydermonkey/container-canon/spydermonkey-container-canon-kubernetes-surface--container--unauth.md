# Kubernetes surface — container / unauth

- source canon: `spydermonkey/container-canon.md`
- base technique: `spydermonkey-container-canon-kubernetes-surface.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **container** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

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

## Probe adjustment (container × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
