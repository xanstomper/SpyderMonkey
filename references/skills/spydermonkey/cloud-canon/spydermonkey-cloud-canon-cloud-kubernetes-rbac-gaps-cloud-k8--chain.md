# Cloud Kubernetes RBAC Gaps (CLOUD-K8S-01) — chain composition

- source canon: `spydermonkey/cloud-canon.md`
- base technique: `spydermonkey-cloud-canon-cloud-kubernetes-rbac-gaps-cloud-k8.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- class: over-broad service accounts, default SA with verbs
- probe: read-only authn-can-i inventory against the declared cluster
- wall: read-only enumeration, crown the exposure

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
