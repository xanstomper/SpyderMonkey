# M. SUPPLY-CHAIN DEEP

- source canon: `holyshit-mode/vector-matrix.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Package registry: dependency confusion on operator's namespace, typosquat detection
- CI/CD runners: self-hosted runner isolation, workflow secret exposure, artifact signing
- Container registries: anonymous pull, :latest overwrite, image-signing verification gaps
- SBOM completeness: phantom dependencies, license-compliance gaps as attack surface
- Git ops: branch-protection bypass, signed-commit enforcement, deploy-key scoping
- Binary provenance: reproducible-build validation, compiler-flag analysis for backdoors

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
