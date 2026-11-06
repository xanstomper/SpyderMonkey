# Holyleadger schema (per-target JSON) — chain composition

- source canon: `spydermonkey/ledger-dump.md`
- base technique: `spydermonkey-ledger-dump-holyleadger-schema-per-target-json.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- `classes`: dict class-name -> `{status: confirmed|negative|hypothesis, probe_count, technique, score, last_probed}`
- `chains`: list of `{crown_jewel, steps[], status, impact, recorded}`
- `meta`: `{created, updated, total_probes, confirmed_count, findings_total, severity {per-sev counts}, risk_score, notes}`
- SOME files are engagement-state, not class data (`directrouter.pages.dev`,
  `talknova.site`): keys are `{target, phase, wall, next_decisive_test,
  kill_chain_position, remote_vector_attempt, ...}` — no classes/chains/meta.
  Check for `classes`/`chains`/`meta` keys first; fall back to printing raw keys.
- Expect stray empties (`gratisfy_xyz.json` duplicates `gratisfy.xyz.json` with
  zero classes) — skip files with empty classes dict without treating as missing.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
