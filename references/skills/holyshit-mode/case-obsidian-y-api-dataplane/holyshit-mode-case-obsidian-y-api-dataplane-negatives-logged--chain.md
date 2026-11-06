# Negatives (logged as coverage) — chain composition

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- base technique: `holyshit-mode-case-obsidian-y-api-dataplane-negatives-logged.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- 47-path secret/source-map/env/backup/admin-panel sweep: all 404/403. Playground + docs HTML
  contain ONLY `YOUR_API_KEY` placeholder; no hardcoded secrets, no admin panel exists
  (`/admin, /panel, /dashboard, /console, /internal` all 404).
- `/v1/chat/completions` uniform `invalid_api_key` 401 for ALL JWT/Bearer/alg-none/Basic/key-prefix
  variants — no JWT auth path, no key-format oracle, no SQL/NoSQL/SSTI/XXE/command-injection/
  path-traversal/SSRF on key or model fields.
- Private Anthropic fleet (`claude-opus-4-8` etc.) stays 403 `no_access`; 21+ gate-bypass variants
  blocked. `kallme/`, `muse/` prefix aliases not routable (404) — gate keys on exact `anthropic/`.
- No shared/cross-user data read in this pass (proxy requests stateless; `user`/`session_id`
  fields accepted but ignored).
- Upstream provider endpoints (`gonka-api.org` = Lovable 403; `router.kiosapi.com` = unreachable)
  not directly attackable without the operator's upstream credentials.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
