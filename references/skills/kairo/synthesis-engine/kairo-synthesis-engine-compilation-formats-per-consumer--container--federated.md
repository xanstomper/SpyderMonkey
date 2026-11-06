# Compilation formats (per consumer) — container / federated

- source canon: `kairo/synthesis-engine.md`
- base technique: `kairo-synthesis-engine-compilation-formats-per-consumer.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **container** · auth **federated** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

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

## Probe adjustment (container × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
