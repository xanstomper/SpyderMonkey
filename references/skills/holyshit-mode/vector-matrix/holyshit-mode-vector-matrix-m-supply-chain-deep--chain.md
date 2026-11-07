# M. SUPPLY-CHAIN DEEP — chain composition

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-m-supply-chain-deep.md`
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

- Package registry: dependency confusion on operator's namespace, typosquat detection
- CI/CD runners: self-hosted runner isolation, workflow secret exposure, artifact signing
- Container registries: anonymous pull, :latest overwrite, image-signing verification gaps
- SBOM completeness: phantom dependencies, license-compliance gaps as attack surface
- Git ops: branch-protection bypass, signed-commit enforcement, deploy-key scoping
- Binary provenance: reproducible-build validation, compiler-flag analysis for backdoors

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
