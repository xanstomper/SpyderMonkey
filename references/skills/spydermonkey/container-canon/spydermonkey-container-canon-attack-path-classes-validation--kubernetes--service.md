# Attack-path classes (validation) — kubernetes / service

- source canon: `spydermonkey/container-canon.md`
- base technique: `spydermonkey-container-canon-attack-path-classes-validation.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **kubernetes** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

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

## Probe adjustment (kubernetes × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
