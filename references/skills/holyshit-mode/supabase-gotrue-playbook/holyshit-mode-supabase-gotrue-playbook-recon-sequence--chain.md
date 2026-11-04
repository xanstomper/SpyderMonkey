# Recon sequence — chain composition

- source canon: `holyshit-mode/supabase-gotrue-playbook.md`
- base technique: `holyshit-mode-supabase-gotrue-playbook-recon-sequence.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. `GET /auth/v1/settings` with anon key reveals `phone_autoconfirm`, `mailer_autoconfirm`, enabled providers. `phone_autoconfirm:true` = POST `/auth/v1/signup` with `{phone, password}` returns a FULL confirmed session (access+refresh JWT, no OTP). This is the master key — mint unlimited accounts in seconds.
2. Mine all SPA bundles (main + lazy chunks) for the real API route table — actual surface (`/api/account/session`, `/api/auth/platform-handoff/*`, `/api/media/*`) differs from advertised docs.
3. Probe all subdomains found in handoff `redirectUrl`s (chat.*, platform.*, etc.) — each has its own API surface and often weaker gates.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
