# Why (burned 2026-11-02) — wasm / federated

- source canon: `holyshit-mode/engagement-vantage-policy.md`
- base technique: `holyshit-mode-engagement-vantage-policy-why-burned-2026-11-0.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **wasm** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

The g***REDACTED***.com session ran 54 probes + logError/pageview 1MB floods + socket scraping from the
home Comcast IP (67.163.104.183). Result: app-layer IP ban (302 `/banned?reason=IP+Banned`) —
no account needed, the traffic alone was enough. The residential IP is identity-attached
(ISP account, all personal browsing) — burning it costs real access. A datacenter vantage
costs nothing.

## Probe adjustment (wasm × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
