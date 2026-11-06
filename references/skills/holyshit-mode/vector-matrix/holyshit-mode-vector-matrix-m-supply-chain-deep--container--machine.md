# M. SUPPLY-CHAIN DEEP — container / machine

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-m-supply-chain-deep.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **container** · auth **machine** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- Package registry: dependency confusion on operator's namespace, typosquat detection
- CI/CD runners: self-hosted runner isolation, workflow secret exposure, artifact signing
- Container registries: anonymous pull, :latest overwrite, image-signing verification gaps
- SBOM completeness: phantom dependencies, license-compliance gaps as attack surface
- Git ops: branch-protection bypass, signed-commit enforcement, deploy-key scoping
- Binary provenance: reproducible-build validation, compiler-flag analysis for backdoors

## Probe adjustment (container × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
