# Stage 1 — Catalog leak reveals the fleet

- source canon: `holyshit-mode/hardened-gateway-internal-fleet-proto-surface.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- `GET /api/models` and `GET /api/models/<slug>` are commonly **keyless catalog reads**. Each model's
  provider rows carry `base_url`, `route_id`, `provider_connection_id`, `connection_alias`, region,
  `api_version`. **Diff these columns for non-null internal hosts.** On experientiallabs the
  `experiential_cloud` self-hosted lane leaked 8 real internal URLs:
  `gateway.xplabs.ai/glm|glm3|qwen`, `wm.xplabs.ai`, `clef.xplabs.ai(/flash)`.
- Resolve the leaked host family (DNS + crt.sh). These are usually on cloud provider IP ranges
  (GCP 34.44.x, Azure 20.125.x, 136.112.x) — publicly routable.
- Probe each internal host for **distinct auth behavior** vs the public host. The misconfigured one
  will answer unauth where the others 401.
- **Discriminator:** if `gateway.xplabs.ai`'s GLM/Qwen lanes return `401 Invalid API Key` but
  `wm.xplabs.ai` is open, it is a **deployment misconfiguration on one worker**, not platform-wide.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
