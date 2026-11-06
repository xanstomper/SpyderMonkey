# 0. HOLY SHIT — Unauthenticated SSRF → internal service reach on `wm.xplabs.ai` (score 82) — chain composition

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-0-holy-shit-unauthent.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
