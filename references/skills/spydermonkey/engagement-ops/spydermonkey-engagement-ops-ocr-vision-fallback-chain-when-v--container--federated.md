# OCR/vision fallback chain (when vision_analyze backend is down) — container / federated

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-ocr-vision-fallback-chain-when-v.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **container** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

vision_analyze (bad/absent key → 502) → FreeForge `:8700` (PUBLIC=0; Bearer key; master in
its sqlite `meta` table, mint via POST /v1/keys) → silkroute `:8760` (Bearer) → for
SVG/graphic content: `rsvg-convert` to big PNG + `tesseract --psm 7/8/13` → PIL ASCII
render (170 cols, 2:1 aspect) as the human-eye fallback. unset proxy env for every
localhost/freeinference call.

## Probe adjustment (container × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
