# Reasoning-only empty-content failover (general upstream-proxy hardening) — chain composition

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- base technique: `holyshit-mode-case-obsidian-y-api-dataplane-reasoning-only-e.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

The biggest "models aren't working in Hermes" trap: upstream returns 200 with non-zero
`completion_tokens` but **`message.content: ""`** — the model burned tokens on the CoT/reasoning
field and never populated `content`. Any client that requires text (Hermes, SDKs) sees an
"empty answer" and looks broken. Two fixes in the proxy:
1. `_salvage_reasoning`: if `content` empty but `reasoning_content`/`reasoning` present, promote
   it to `content` (mark `_from_reasoning`). muse's real answer lives in `reasoning_content`.
2. `_is_empty_completion` must flag empty-`content` even when tokens>0 (`completion_tokens>0`
   is NOT evidence of a usable answer), then fail over to next host / mark model dead (TTL'd)
   rather than serve a blank 200.
3. **Upstream availability churns HARD on free vectors** — a model serving content at 06:00 can
   502/degrade within 15 min. The dead-cache TTL (fail-open: re-probe after TTL, return 200 if
   upstream recovered) is the correct recovery, not a permanent hard-502. Assert that in tests
   (a "model now 200" after a prior fail is the fail-open working, NOT a regression).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
