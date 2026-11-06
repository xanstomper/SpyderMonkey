# 9.6 Drift oracles — fire FIRST on every re-entry (score 90, mandatory) — chain composition

- source canon: `3am-shinjitsu/arsenal-09-breach-osint.md`
- base technique: `3am-shinjitsu-arsenal-09-breach-osint-9-6-drift-oracles-fire.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- PTOK drift (LLM targets): 3× identical 1-word requests → `usage.prompt_tokens`: constant =
  stateless/patched; drifting = shared buffer re-emerged (highest-value re-find).
- Bundle-hash diff (§2.8), wayback CDX diff (§2.3), wall-shape re-verify (403 → 500 drift).
- TOP prior compromisables were patched between sessions — re-asserting without a fresh test
  is a stale-finding ERROR.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
