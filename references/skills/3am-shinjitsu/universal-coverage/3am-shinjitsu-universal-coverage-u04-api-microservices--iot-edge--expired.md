# U04 API & microservices — iot-edge / expired

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-u04-api-microservices.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **iot-edge** · auth **expired** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: device-adjacent runtime at the edge — own devices, lab network
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

- [ ] OpenAPI/GraphQL/gRPC/WS schemas captured or reconstructed from public docs
- [ ] Object, function, tenant, and role authorization tested with owned accounts
- [ ] Mass assignment, type coercion, parser differentials, and IDOR classes assessed
- [ ] Rate limits keyed by identity/IP/route/tenant verified
- [ ] Service-to-service trust, tokens, replay, and audience validation reviewed

## Probe adjustment (iot-edge × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
