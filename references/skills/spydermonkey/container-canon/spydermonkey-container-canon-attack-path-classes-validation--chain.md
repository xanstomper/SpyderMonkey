# Attack-path classes (validation) — chain composition

- source canon: `spydermonkey/container-canon.md`
- base technique: `spydermonkey-container-canon-attack-path-classes-validation.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
