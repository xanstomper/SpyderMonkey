# Sketch — azure / machine

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-sketch.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **azure** · auth **machine** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

```
platform.experientiallabs.ai (Next.js web, Cloudflare)
  └─ signin-gated /admin/* + management API
api.experientiallabs.ai (public gateway, FastAPI edge + Rust worker)
  └─ /v1/* inference       -> 401 without xpl_ key (hardened)
  └─ /api/* management     -> 401 / session-gated (hardened)
*.xplabs.ai (INTERNAL serving fleet, publicly IP-addressed)
  ├─ gateway.xplabs.ai     -> /usage.json + /usage KEYLESS ledger leak
  │                         -> /openapi.json + /docs 200
  ├─ wm.xplabs.ai          -> /scale_elastic_ep KEYLESS control-plane WRITE (HOLY SHIT)
  │                         -> /is_scaling_elastic_ep, /kv_event_sources, /generative_scoring KEYLESS
  │                         -> /openapi.json KEYLESS (242KB full vLLM surface)
  └─ clef.xplabs.ai        -> /health KEYLESS GPU-fleet metrics
```

## Probe adjustment (azure × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
