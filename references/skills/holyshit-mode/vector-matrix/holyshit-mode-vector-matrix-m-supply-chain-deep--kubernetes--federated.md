# M. SUPPLY-CHAIN DEEP — kubernetes / federated

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-m-supply-chain-deep.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **kubernetes** · auth **federated** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- Package registry: dependency confusion on operator's namespace, typosquat detection
- CI/CD runners: self-hosted runner isolation, workflow secret exposure, artifact signing
- Container registries: anonymous pull, :latest overwrite, image-signing verification gaps
- SBOM completeness: phantom dependencies, license-compliance gaps as attack surface
- Git ops: branch-protection bypass, signed-commit enforcement, deploy-key scoping
- Binary provenance: reproducible-build validation, compiler-flag analysis for backdoors

## Probe adjustment (kubernetes × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
