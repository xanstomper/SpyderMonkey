# Stage 1 — Catalog leak reveals the fleet — mesh / machine

- source canon: `holyshit-mode/hardened-gateway-internal-fleet-proto-surface.md`
- base technique: `holyshit-mode-hardened-gateway-internal-fleet-proto-surface-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **mesh** · auth **machine** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- `GET /api/models` and `GET /api/models/<slug>` are commonly **keyless catalog reads**. Each model's
  provider rows carry `base_url`, `route_id`, `provider_connection_id`, `connection_alias`, region,
  `api_version`. **Diff these columns for non-null internal hosts.** On example-target the
  `experiential_cloud` self-hosted lane leaked 8 real internal URLs:
  `gateway.example-target.ai/glm|glm3|qwen`, `wm.example-target.ai`, `clef.example-target.ai(/flash)`.
- Resolve the leaked host family (DNS + crt.sh). These are usually on cloud provider IP ranges
  (GCP 34.44.x, Azure 20.125.x, 136.112.x) — publicly routable.
- Probe each internal host for **distinct auth behavior** vs the public host. The misconfigured one
  will answer unauth where the others 401.
- **Discriminator:** if `gateway.example-target.ai`'s GLM/Qwen lanes return `401 Invalid API Key` but
  `wm.example-target.ai` is open, it is a **deployment misconfiguration on one worker**, not platform-wide.

## Probe adjustment (mesh × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
