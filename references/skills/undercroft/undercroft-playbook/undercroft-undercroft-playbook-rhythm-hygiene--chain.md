# Rhythm & hygiene — chain composition

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-rhythm-hygiene.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
