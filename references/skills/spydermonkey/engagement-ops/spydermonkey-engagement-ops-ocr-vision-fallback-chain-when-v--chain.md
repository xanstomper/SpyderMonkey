# OCR/vision fallback chain (when vision_analyze backend is down) — chain composition

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-ocr-vision-fallback-chain-when-v.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

vision_analyze (bad/absent key → 502) → FreeForge `:8700` (PUBLIC=0; Bearer key; master in
its sqlite `meta` table, mint via POST /v1/keys) → silkroute `:8760` (Bearer) → for
SVG/graphic content: `rsvg-convert` to big PNG + `tesseract --psm 7/8/13` → PIL ASCII
render (170 cols, 2:1 aspect) as the human-eye fallback. unset proxy env for every
localhost/freeinference call.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
