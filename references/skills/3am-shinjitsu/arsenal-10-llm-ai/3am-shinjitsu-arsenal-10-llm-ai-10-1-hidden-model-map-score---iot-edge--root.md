# 10.1 Hidden-model map (score 80) — iot-edge / root

- source canon: `3am-shinjitsu/arsenal-10-llm-ai.md`
- base technique: `3am-shinjitsu-arsenal-10-llm-ai-10-1-hidden-model-map-score-.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **iot-edge** · auth **root** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: device-adjacent runtime at the edge — own devices, lab network
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

- DECISIVE: `curl /status?json=1` (find via `fetch("/status?json=1")` in page JS) — diffs
  against public `/v1/models`: extras = hidden tier + upstream vendor names + verbatim error bodies.
- GATE DISCRIMINATOR: private models → `no_access` (403) vs `model_not_found` (404) for
  nonexistent = models exist server-side AND gate is real code.
- BYPASS MATRIX (all-variants-once discipline): case swap, lead/trail space, null byte,
  trailing dot, double-slash, `:latest`, `?query`, array-typed model field
  (`{"model":["x"]}`), `stream:true`, second host. Uniform failure = hardened, ledger it.

## Probe adjustment (iot-edge × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
