# U04 API & microservices

- source canon: `3am-shinjitsu/universal-coverage.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- [ ] OpenAPI/GraphQL/gRPC/WS schemas captured or reconstructed from public docs
- [ ] Object, function, tenant, and role authorization tested with owned accounts
- [ ] Mass assignment, type coercion, parser differentials, and IDOR classes assessed
- [ ] Rate limits keyed by identity/IP/route/tenant verified
- [ ] Service-to-service trust, tokens, replay, and audience validation reviewed

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
