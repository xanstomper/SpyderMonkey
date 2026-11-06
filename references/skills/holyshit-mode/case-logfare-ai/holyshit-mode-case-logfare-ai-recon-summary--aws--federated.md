# Recon Summary — aws / federated

- source canon: `holyshit-mode/case-logfare-ai.md`
- base technique: `holyshit-mode-case-logfare-ai-recon-summary.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **aws** · auth **federated** · chain role **entry**

## Context

- platform: IAM/identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- **Stack:** FastAPI backend, nginx reverse proxy, SvelteKit frontends (`chat.`, `rp.`), Postgres
- **Auth:** Discord OAuth + native register/login + SSO (`/v1/sso/approve`, `/v1/sso/token`)
- **API:** OpenAI/Anthropic-compatible LLM inference, self-service API keys
- **Subdomains:** `chat.logfare.ai`, `rp.logfare.ai` (SvelteKit), `logfare.logorhythms.dev` (SAN)
- **Cloudflare:** chat.logfare.ai fronted by Cloudflare (cf-ray, cf-cache-status DYNAMIC)
- **Register flow requires Discord server membership** (not just OAuth)

## Probe adjustment (aws × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
