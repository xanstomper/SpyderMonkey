# 10.1 Hidden-model map (score 80) — chain composition

- source canon: `3am-shinjitsu/arsenal-10-llm-ai.md`
- base technique: `3am-shinjitsu-arsenal-10-llm-ai-10-1-hidden-model-map-score-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- DECISIVE: `curl /status?json=1` (find via `fetch("/status?json=1")` in page JS) — diffs
  against public `/v1/models`: extras = hidden tier + upstream vendor names + verbatim error bodies.
- GATE DISCRIMINATOR: private models → `no_access` (403) vs `model_not_found` (404) for
  nonexistent = models exist server-side AND gate is real code.
- BYPASS MATRIX (all-variants-once discipline): case swap, lead/trail space, null byte,
  trailing dot, double-slash, `:latest`, `?query`, array-typed model field
  (`{"model":["x"]}`), `stream:true`, second host. Uniform failure = hardened, ledger it.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
