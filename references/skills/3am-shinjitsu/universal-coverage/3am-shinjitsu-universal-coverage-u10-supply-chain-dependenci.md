# U10 Supply chain & dependencies

- source canon: `3am-shinjitsu/universal-coverage.md`
- bindings: **WSTG-CONF-04** · **CWE-798** · **ATT&CK T1552**
- generated: 2026-11-07

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- [ ] SBOM generated for every deployed artifact
- [ ] Direct/transitive dependencies matched to current advisories
- [ ] CI/CD permissions, runners, caches, artifacts, and deployment approvals reviewed
- [ ] Source repo protections, signing, provenance, and secret scanning verified
- [ ] Third-party packages/build actions pinned and reviewed

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
