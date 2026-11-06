# U08 Compute & containers — chain composition

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-u08-compute-containers.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- [ ] Base images, packages, config, SBOM, and provenance scanned
- [ ] Container users, capabilities, mounts, sockets, seccomp/AppArmor/SELinux reviewed
- [ ] Kubernetes RBAC, network policies, admission controllers, and secrets encryption reviewed
- [ ] Serverless IAM, trigger sources, env vars, and log retention reviewed
- [ ] Build agents and runners isolated from production credentials

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
