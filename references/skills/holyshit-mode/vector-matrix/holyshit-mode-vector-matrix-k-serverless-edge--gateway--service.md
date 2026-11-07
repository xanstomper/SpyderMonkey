# K. SERVERLESS / EDGE — gateway / service

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-k-serverless-edge.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **gateway** · auth **service** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

- Cloudflare Workers: KV/D1/R2 exposure via misrouted routes, secret env-var leakage
- Lambda/Cloud Functions: env-var secrets, IAM over-permission, cold-start side-channels
- Edge functions: geo-IP bypass, header-based routing confusion, A/B test poisoning
- CDN cache poisoning: unkeyed input in cache keys, X-Forwarded-* trust
- Serverless persistence: event rules, cron triggers, queue poison-pill messages
- WASM sandbox escapes: memory-corruption in edge runtimes (operator's own deployments)
- Durable objects / stateful edge: cross-tenant state leakage via ID prediction

## Probe adjustment (gateway × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
