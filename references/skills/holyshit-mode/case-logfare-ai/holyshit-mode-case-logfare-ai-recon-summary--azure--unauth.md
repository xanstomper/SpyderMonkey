# Recon Summary — azure / unauth

- source canon: `holyshit-mode/case-logfare-ai.md`
- base technique: `holyshit-mode-case-logfare-ai-recon-summary.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **azure** · auth **unauth** · chain role **entry**

## Context

- platform: identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- **Stack:** FastAPI backend, nginx reverse proxy, SvelteKit frontends (`chat.`, `rp.`), Postgres
- **Auth:** Discord OAuth + native register/login + SSO (`/v1/sso/approve`, `/v1/sso/token`)
- **API:** OpenAI/Anthropic-compatible LLM inference, self-service API keys
- **Subdomains:** `chat.logfare.ai`, `rp.logfare.ai` (SvelteKit), `logfare.logorhythms.dev` (SAN)
- **Cloudflare:** chat.logfare.ai fronted by Cloudflare (cf-ray, cf-cache-status DYNAMIC)
- **Register flow requires Discord server membership** (not just OAuth)

## Probe adjustment (azure × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
