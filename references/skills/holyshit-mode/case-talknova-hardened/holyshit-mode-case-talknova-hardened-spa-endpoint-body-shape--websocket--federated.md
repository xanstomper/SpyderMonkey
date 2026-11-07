# SPA endpoint + body-shape mining (minified bundle) — websocket / federated

- source canon: `holyshit-mode/case-talknova-hardened.md`
- base technique: `holyshit-mode-case-talknova-hardened-spa-endpoint-body-shape.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **websocket** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

1. `grep -oE '"/[a-zA-Z0-9_/.-]{2,60}"' app.js | sort -u` → route + endpoint list.
2. All fetch calls: `grep -oE 'fetch\("[a-z0-9/_-]+"' app.js | sort -u`.
3. Body shapes live at CALL SITES of the wrapper fn, not the fetch itself — find the wrapper
   (e.g. `async function Y8(e,t){fetch("/api/chat"...}`), then grep its callers:
   `grep -oE 'Y8\(\{[^}]{0,150}' app.js` → reveals real body keys (`{modelId, message}` not
   the guessed `{model, messages}`). Server error strings are the oracle.
4. **Code-split chunk discovery**: `grep -oE '"\./[A-Za-z0-9_-]+\.js"' app.js` → fetch each chunk, mine for endpoints.

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
