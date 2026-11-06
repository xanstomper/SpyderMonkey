# U04 API & microservices — cloud / low-priv

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-u04-api-microservices.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **cloud** · auth **low-priv** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- [ ] OpenAPI/GraphQL/gRPC/WS schemas captured or reconstructed from public docs
- [ ] Object, function, tenant, and role authorization tested with owned accounts
- [ ] Mass assignment, type coercion, parser differentials, and IDOR classes assessed
- [ ] Rate limits keyed by identity/IP/route/tenant verified
- [ ] Service-to-service trust, tokens, replay, and audience validation reviewed

## Probe adjustment (cloud × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
