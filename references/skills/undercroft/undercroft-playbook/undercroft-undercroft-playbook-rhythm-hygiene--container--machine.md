# Rhythm & hygiene — container / machine

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-rhythm-hygiene.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **container** · auth **machine** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

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

## Probe adjustment (container × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
