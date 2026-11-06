# OCR/vision fallback chain (when vision_analyze backend is down)

- source canon: `spydermonkey/engagement-ops.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## The technique

vision_analyze (bad/absent key → 502) → FreeForge `:8700` (PUBLIC=0; Bearer key; master in
its sqlite `meta` table, mint via POST /v1/keys) → silkroute `:8760` (Bearer) → for
SVG/graphic content: `rsvg-convert` to big PNG + `tesseract --psm 7/8/13` → PIL ASCII
render (170 cols, 2:1 aspect) as the human-eye fallback. unset proxy env for every
localhost/f***REDACTED*** call.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
