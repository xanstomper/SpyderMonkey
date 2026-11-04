# 0. HOLY SHIT — Unauthenticated SSRF → internal service reach on `wm.xplabs.ai` (score 82) — gcp / low-priv

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-0-holy-shit-unauthent.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **gcp** · auth **low-priv** · chain role **pivot**

## Context

- platform: IAM/service-account surface — read-only enumeration
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- **VERDICT: CONFIRMED — unauthenticated remote SSRF (server-side fetch) with internal-loopback reach.**
- **EVIDENCE:` POST /invocations` with `image_url: <url>` performs a server-side fetch** and
  reports the fetched HTTP status / connection result in the error message — a live oracle:
  - `image_url: http://169.254.169.254/latest/meta-data/` → `422 "Failed to fetch media from URL:
    HTTP 404 error"` — fetched cloud-metadata endpoint (IMDSv2 → 404 without token = hardened, but
    **reach confirmed**).
  - `127.0.0.1:<port>` acts as a **port/status scanner**: `:8000` → HTTP 404 (a real HTTP service
    answers); closed ports → `500 Cannot connect to host`; loopback TLS listener `:5432` observed.
  - `127.0.0.1:8000/{docs,metrics,openapi.json,health}` → the fetch **received real 200 content**
    (image-decode error, not connect/404) — i.e. **loopback-only endpoints return data via SSRF**
    that the public Host-header ACL blocks (those same paths are 403/empty publicly).
- **IMPACT:** Internal-network + cloud-metadata reach from the public internet through the inference
  endpoint. Reaches the internal worker service (`127.0.0.1:8000` `/docs`, `/metrics`, `/openapi.json`)
  that is intentionally loopback-only. Internal port/service oracle. **Genuine unauthenticated exploit
  (SSRF).** Internal reach is more limited than arbitrary-everywhere (loopback/IMDS-scoped; `gateway.xplabs.ai:8000`
  and `10.0.0.1` hung) — this is the exposure ceiling, tested.
- **CONFIDENCE:** High — live status/connect echoes across targets.

## Probe adjustment (gcp × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
