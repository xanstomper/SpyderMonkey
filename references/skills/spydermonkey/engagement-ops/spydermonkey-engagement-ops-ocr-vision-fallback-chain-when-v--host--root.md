# OCR/vision fallback chain (when vision_analyze backend is down) — host / root

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-ocr-vision-fallback-chain-when-v.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **host** · auth **root** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

vision_analyze (bad/absent key → 502) → FreeForge `:8700` (PUBLIC=0; Bearer key; master in
its sqlite `meta` table, mint via POST /v1/keys) → silkroute `:8760` (Bearer) → for
SVG/graphic content: `rsvg-convert` to big PNG + `tesseract --psm 7/8/13` → PIL ASCII
render (170 cols, 2:1 aspect) as the human-eye fallback. unset proxy env for every
localhost/f***REDACTED*** call.

## Probe adjustment (host × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
