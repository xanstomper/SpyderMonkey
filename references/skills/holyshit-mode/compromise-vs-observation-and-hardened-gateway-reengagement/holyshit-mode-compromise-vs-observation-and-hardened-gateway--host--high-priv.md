# Hardened-LLM-gateway fast re-engagement ladder (all fresh, live, ~40 requests) — host / high-priv

- source canon: `holyshit-mode/compromise-vs-observation-and-hardened-gateway-reengagement.md`
- base technique: `holyshit-mode-compromise-vs-observation-and-hardened-gateway.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **host** · auth **high-priv** · chain role **pivot**

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

When re-engaging a gateway whose proxy-layer surface was previously "confirmed" but which
you suspect is actually hardened, run THIS set — it decisively closes the compromise classes:

## Probe adjustment (host × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
