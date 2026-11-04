# Stack map (verified)

- source canon: `holyshit-mode/case-packdraw-com.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- **Vercel + Next.js App Router (Turbopack**, immutable chunk hashing), SSR-heavy.
- **Pusher 8.0.2** realtime: public channel `pack-result` (live packs counter),
  `private-encrypted-user-*` channels behind `/api/pusher/auth` (403 without session —
  REAL route; `/pusher/auth` + `/pusher/user-auth` = SPA-fallback ghosts, not routes).
- **TokenEx** card tokenization iframe (`/api/tokenize/iframe/config` — 404 GET; POST
  untested), **ImageKit** CDN (account `hr727kunx`, path `community_packs/...`),
  **reCAPTCHA Enterprise** on auth (sitekey `6LcfH48qAAAAAOnZqFXlOGJmJHGYJtNBFbfpbAsg`),
  Axiom telemetry, Vercel observability beacon `/monitoring?o=...&p=...`.
- **Auth: email/password + Google + Apple** (no phone). Register = modal, not a route
  (`/en-us/register` = 404). Login fields: email/password/checkbox (+ reCAPTCHA).
- Money: crypto deposit/cashout ("withdraw value in crypto", "no daily withdrawal
  limit"), card deposits via TokenEx iframe. Deposit promo code PACKDRAW +5%.
- Legal: Packdraw Limited (Cyprus HE 445177) + PackDraw US LLC (Delaware 7571319).
- DNS: Vercel NS, MX Google (smtp.google.com), SPF google+sendgrid+mailgun, fb+google
  verification TXT. Wildcard cert `*.packdraw.com`.
- Subdomains (CT): status.packdraw.com (Vercel status-page SPA, all paths 200, one
  monitored service slug `command`), howitworks/battles (DNS only, Vercel 404s),
  UUID subdomain = deleted Vercel deployment (503), www (checkpoint).
- Business surface: packs (Pokemon TCG heavy + MTG), battles (NORMAL/SHARE/JACKPOT,
  up to $1.2K entries, live "unboxed" values via Pusher), deals, rewards, events,
  user-created packs ("Create Pack": packName + item catalog incl. $700K cars).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
