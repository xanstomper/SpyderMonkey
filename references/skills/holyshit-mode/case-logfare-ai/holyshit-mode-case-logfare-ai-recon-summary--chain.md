# Recon Summary — chain composition

- source canon: `holyshit-mode/case-logfare-ai.md`
- base technique: `holyshit-mode-case-logfare-ai-recon-summary.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- **Stack:** FastAPI backend, nginx reverse proxy, SvelteKit frontends (`chat.`, `rp.`), Postgres
- **Auth:** Discord OAuth + native register/login + SSO (`/v1/sso/approve`, `/v1/sso/token`)
- **API:** OpenAI/Anthropic-compatible LLM inference, self-service API keys
- **Subdomains:** `chat.logfare.ai`, `rp.logfare.ai` (SvelteKit), `logfare.logorhythms.dev` (SAN)
- **Cloudflare:** chat.logfare.ai fronted by Cloudflare (cf-ray, cf-cache-status DYNAMIC)
- **Register flow requires Discord server membership** (not just OAuth)

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
