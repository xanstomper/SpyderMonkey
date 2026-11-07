# Stage 1 — Catalog leak reveals the fleet — wasm / federated

- source canon: `holyshit-mode/hardened-gateway-internal-fleet-proto-surface.md`
- base technique: `holyshit-mode-hardened-gateway-internal-fleet-proto-surface-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **wasm** · auth **federated** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

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

## Probe adjustment (wasm × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
