# 5. CONFIRMED — GPU fleet internals leak keyless on `clef.xplabs.ai` (score 35) — chain composition

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-5-confirmed-gpu-fleet.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- `GET https://clef.xplabs.ai/health` → 200 `{"status":"ok","max_length":65536,"queued":0,
  "gpu_allocated_gib":29.46,"gpu_peak_gib":36.76,...}` — no auth.
- **IMPACT:** Infra/GPU-fleet capacity disclosure.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
