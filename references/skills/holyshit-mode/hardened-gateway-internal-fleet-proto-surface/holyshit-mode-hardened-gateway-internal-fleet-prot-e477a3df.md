# Stage 1 — Catalog leak reveals the fleet

- source canon: `holyshit-mode/hardened-gateway-internal-fleet-proto-surface.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- `GET /api/models` and `GET /api/models/<slug>` are commonly **keyless catalog reads**. Each model's
  provider rows carry `base_url`, `route_id`, `provider_connection_id`, `connection_alias`, region,
  `api_version`. **Diff these columns for non-null internal hosts.** On e***REDACTED*** the
  `experiential_cloud` self-hosted lane leaked 8 real internal URLs:
  `gateway.x***REDACTED***.ai/glm|glm3|qwen`, `wm.x***REDACTED***.ai`, `clef.x***REDACTED***.ai(/flash)`.
- Resolve the leaked host family (DNS + crt.sh). These are usually on cloud provider IP ranges
  (GCP 34.44.x, Azure 20.125.x, 136.112.x) — publicly routable.
- Probe each internal host for **distinct auth behavior** vs the public host. The misconfigured one
  will answer unauth where the others 401.
- **Discriminator:** if `gateway.x***REDACTED***.ai`'s GLM/Qwen lanes return `401 Invalid API Key` but
  `wm.x***REDACTED***.ai` is open, it is a **deployment misconfiguration on one worker**, not platform-wide.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
