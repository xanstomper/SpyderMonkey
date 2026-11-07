# Attack-path classes (validation)

- source canon: `spydermonkey/container-canon.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
