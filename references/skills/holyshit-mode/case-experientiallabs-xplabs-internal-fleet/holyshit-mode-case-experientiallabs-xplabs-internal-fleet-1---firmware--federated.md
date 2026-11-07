# 1. How to discover the hidden internal fleet (keyless catalog base_url leak) — firmware / federated

- source canon: `holyshit-mode/case-experientiallabs-xplabs-internal-fleet.md`
- base technique: `holyshit-mode-case-experientiallabs-xplabs-internal-fleet-1-.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **firmware** · auth **federated** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

`GET https://<platform>/api/models` is a KEYLESS catalog (public row mode). Model rows include a
`providers[]` array; **self-hosted lanes carry a real `base_url`** where cloud lanes carry `null`.
On experientiallabs, the `experiential_cloud` provider rows leaked 8 real internal serving
endpoints:

```
gateway.xplabs.ai/glm/v1  gateway.xplabs.ai/glm3/v1  gateway.xplabs.ai/qwen/v1
wm.xplabs.ai/v1   clef.xplabs.ai/v1   clef.xplabs.ai/flash/v1
```

- These map to specific model slugs: `glm-5.3-flash`→/glm, `deepseek-v4-flash`→wm,
  `qwen3.8-27b`→/qwen, `clef(-flash)`→clef.
- The public gateway's own docs/`openapi.json` NEVER list these — they're reachable only by
  mining the catalog for non-null `base_url` on provider rows.
- **Sweep all `*.xplabs.ai`-style base domains** (`dig +short <sub>.<base>`), and probe each
  host's `/openapi.json`, `/docs`, `/health`, live/ready probes — internal gateways frequently
  leave FastAPI/Caddy auto-docs ON while the public edge disables them.
- Recipe: `grep base_url in catalog → enumerate <base> subdomain family → probe /openapi.json+/docs → read full internal route map`.

## Probe adjustment (firmware × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
