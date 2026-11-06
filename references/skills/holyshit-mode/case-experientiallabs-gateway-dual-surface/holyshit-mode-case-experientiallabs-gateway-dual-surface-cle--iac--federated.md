# Clean negatives (do not re-probe) — iac / federated

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- base technique: `holyshit-mode-case-experientiallabs-gateway-dual-surface-cle.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **iac** · auth **federated** · chain role **pivot**

## Context

- platform: template/state files are the infrastructure inventory — read-only crown of the exposure
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- SSRF via inference params: `url`/`endpoint` -> timeout, `base_url` ignored.
- Cloud-role/metadata: `/metadata`, `/logs`, `/internal/status`, `/debug/zpages` all 404
  under `Host:127.0.0.1` (the Caddy loopback site returns a 200 shell, not a real proxy).
- `/kv_event_sources`: GET 200 `{}`, POST 405. No enumeration.
- Web + public-edge management: EVERY `/api/*` + `/api/orgs/<id>/*` + `/admin/*` + `/auth/*`
  server-side 401/Turnstile/session-gated. No unauth IDOR/broken-authz/mass-assignment.

## Probe adjustment (iac × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
