# Sketch — chain composition

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-sketch.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
