# Stack map (verified) — websocket / unauth

- source canon: `holyshit-mode/case-packdraw-com.md`
- base technique: `holyshit-mode-case-packdraw-com-stack-map-verified.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **websocket** · auth **unauth** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

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

## Probe adjustment (websocket × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
