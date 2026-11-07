# Compilation formats (per consumer)

- source canon: `kairo/synthesis-engine.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

**3AM** (`~/.redteam/learned-vectors.jsonl`, schema-true):
```json
{"flaw": 6, "seam": "C", "probe": "KAIRO SYNTH BOUNDARY :: fire the scoped request…", "confirmed_when": "foreign scope returns 200…"}
```
→ 3AM `promote --apply --verified` merges into the living matrix.

**UNDERCROFT** (campaign `undercroft-state.json` → `pocs`):
```json
{"finding": "SV-…-BOUNDARY", "request": "fire the scoped request…", "proof": "…", "class": "IDOR"}
```

**HolyShit** (`~/.redteam/synthesized-recipes.md`):
```markdown

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
