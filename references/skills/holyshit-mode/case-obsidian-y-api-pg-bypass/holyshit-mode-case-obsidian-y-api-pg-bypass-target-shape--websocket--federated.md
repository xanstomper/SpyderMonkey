# Target shape — websocket / federated

- source canon: `holyshit-mode/case-obsidian-y-api-pg-bypass.md`
- base technique: `holyshit-mode-case-obsidian-y-api-pg-bypass-target-shape.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **websocket** · auth **federated** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

"Obsidian Y API" — OpenAI-compatible multi-provider gateway on Render (Flask-class: 405s return
`<h1>Method Not Allowed</h1>` HTML, app-JSON 404s are `{"error":...}` 60-byte). Three hand-rolled
pages: `/docs`, `/playground`, `/status`. No openapi.json (not FastAPI). Docs advertise:
"Requests without a key still work but are rate-limited per IP address" (on /v1 — turned out
FALSE: 401 regardless of IP-based fallback), Bearer keys issued per user.

## Probe adjustment (websocket × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
