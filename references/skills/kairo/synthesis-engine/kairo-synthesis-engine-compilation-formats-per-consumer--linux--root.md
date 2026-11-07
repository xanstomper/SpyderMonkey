# Compilation formats (per consumer) — linux / root

- source canon: `kairo/synthesis-engine.md`
- base technique: `kairo-synthesis-engine-compilation-formats-per-consumer.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **linux** · auth **root** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: read-only inventory first (kaisha rungs), then the documented class match
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

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

## Probe adjustment (linux × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
