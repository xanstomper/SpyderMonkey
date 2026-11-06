# OCR/vision fallback chain (when vision_analyze backend is down) — container / hardened

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-ocr-vision-fallback-chain-when-v.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **container** · auth **hardened** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

vision_analyze (bad/absent key → 502) → FreeForge `:8700` (PUBLIC=0; Bearer key; master in
its sqlite `meta` table, mint via POST /v1/keys) → silkroute `:8760` (Bearer) → for
SVG/graphic content: `rsvg-convert` to big PNG + `tesseract --psm 7/8/13` → PIL ASCII
render (170 cols, 2:1 aspect) as the human-eye fallback. unset proxy env for every
localhost/freeinference call.

## Probe adjustment (container × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
