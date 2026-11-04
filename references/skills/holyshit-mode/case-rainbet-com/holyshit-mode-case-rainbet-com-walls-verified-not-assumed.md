# Walls (verified, not assumed)

- source canon: `holyshit-mode/case-rainbet-com.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- `staging`/`dashboard`/`ds`/`aiostaging` = Cloudflare Access walls.
- `slot-integrations.rainbet.com` = NestJS, `/docs` → CF Access; all guessed paths 404
  (real routing, "Cannot GET").
- `api.rainbet.com` + `staging-api` = IP-reputation hard block (even real chromium).
- Sign-up = Turnstile `secure_token` + edge managed challenge on the auth plane.
- `staging-mono`/`dev-mono` = AWS ELB (`awselb/2.0`) 504 — orphaned backends.
- Game verifier = fully client-side (no bet-lookup oracle).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
