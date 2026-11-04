# Stage 1 — Catalog leak reveals the fleet — android / low-priv

- source canon: `holyshit-mode/hardened-gateway-internal-fleet-proto-surface.md`
- base technique: `holyshit-mode-hardened-gateway-internal-fleet-proto-surface-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **android** · auth **low-priv** · chain role **pivot**

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

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

## Probe adjustment (android × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
