# Sketch

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-04

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
