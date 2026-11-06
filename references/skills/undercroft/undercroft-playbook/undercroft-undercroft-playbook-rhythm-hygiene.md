# Rhythm & hygiene

- source canon: `undercroft/undercroft-playbook.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## The technique

- Seams probed clean: EXHAUSTED with exact test string; never re-fired without a
  change in target state.
- Drift: re-verify before re-asserting a CONFIRMED seam from an earlier session.
- Chunking + noise budgets: family §12; bundles parsed locally, never uploaded.
- PII minimality inherited; samples ≤3, redacted.
- PITFALL: `undercroft run` executes on the local machine, NOT the vantage VM. The
  engine's exit IP is the local residential IP — for targets where exit IP matters
  (geo-restrictions, origin IP logging, cross-brand recon), run the engine via
  `ssh vermes` instead. Always verify `barbican posture` shows the correct exit IP
  before trusting undercroft findings that depend on IP-specific behavior.
- PITFALL: `undercroft run`'s live route probe reports HTTP 200 for ALL paths that
  return the SPA shell (e.g. `/admin`, `/debug`, `/internal` — they all return 200
  index.html). A 200 status code proves NOTHING on SPA targets. Always verify the
  response Content-Type: `application/json` means a real endpoint; `text/html` means
  the SPA catch-all. Do not register SPA-shell responses as confirmed routes.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
