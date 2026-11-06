# Holyleadger schema (per-target JSON) — android / high-priv

- source canon: `spydermonkey/ledger-dump.md`
- base technique: `spydermonkey-ledger-dump-holyleadger-schema-per-target-json.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **android** · auth **high-priv** · chain role **pivot**

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- `classes`: dict class-name -> `{status: confirmed|negative|hypothesis, probe_count, technique, score, last_probed}`
- `chains`: list of `{crown_jewel, steps[], status, impact, recorded}`
- `meta`: `{created, updated, total_probes, confirmed_count, findings_total, severity {per-sev counts}, risk_score, notes}`
- SOME files are engagement-state, not class data (`directrouter.pages.dev`,
  `talknova.site`): keys are `{target, phase, wall, next_decisive_test,
  kill_chain_position, remote_vector_attempt, ...}` — no classes/chains/meta.
  Check for `classes`/`chains`/`meta` keys first; fall back to printing raw keys.
- Expect stray empties (`gratisfy_xyz.json` duplicates `gratisfy.xyz.json` with
  zero classes) — skip files with empty classes dict without treating as missing.

## Probe adjustment (android × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
