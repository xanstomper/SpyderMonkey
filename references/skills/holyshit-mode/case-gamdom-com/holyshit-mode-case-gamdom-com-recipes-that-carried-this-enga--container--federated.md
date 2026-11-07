# Recipes that carried this engagement — container / federated

- source canon: `holyshit-mode/case-gamdom-com.md`
- base technique: `holyshit-mode-case-gamdom-com-recipes-that-carried-this-enga.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **container** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- EIO=3 websocket-first handshake (`GET /socket.io/?EIO=3&transport=websocket`, NO sid → server
  mints over websocket; polling dies on CDN node affinity with `Session ID unknown`) — unlocked
  the REAL protocol and both top finds. v2 frames: connect `40/nsp`, events `42/nsp,["ev",args]`.
- CDP `Page.addScriptToEvaluateOnNewDocument` hooking `window.WebSocket` — post-load hooks miss
  the bundled client (constructor captured at module init). Idle sockets capture nothing: drive
  the UI (open chat / games) to generate traffic.
- Shadow-DOM form driving (Dynamic SDK widget): pierce shadow roots, native value setter +
  input/change events, REAL clicks on checkboxes (silent client validation blocks submit
  otherwise — `isValidAge` checkValidity was the hidden blocker).
- Schema-library extraction: all request shapes live in ONE util chunk; `snake_case` method
  names = API methods; enums defined as var-ternary chains (`(n=>(n.COINS="COINS",...)).
- CT logs → wayback → whois → PTR chain for forgotten-edge hunting; hackertarget hostsearch for
  passive DNS (found td.gamdom.com + incoming-callbacks.gamdom.com); banner-grab everything
  (MariaDB version, Exim version, SSH version = the age of the box in one call).
- Kernel-state caution in execute_code: variable collisions across cells produce phantom type
  errors ('str' has no .get) — fresh names per cell, read responses to EOF, never trust a parse
  of a truncated body.

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
