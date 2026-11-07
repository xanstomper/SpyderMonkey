# Holyleadger schema (per-target JSON)

- source canon: `spydermonkey/ledger-dump.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
