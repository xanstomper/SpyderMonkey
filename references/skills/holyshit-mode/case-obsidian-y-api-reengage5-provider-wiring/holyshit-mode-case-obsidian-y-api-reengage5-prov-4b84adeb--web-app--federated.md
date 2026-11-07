# Proxy upgrades (~/obsidian-proxy/obsidian_proxy.py) — web-app / federated

- source canon: `holyshit-mode/case-obsidian-y-api-reengage5-provider-wiring.md`
- base technique: `holyshit-mode-case-obsidian-y-api-reengage5-provider-wiring-.md`
- bindings: **WSTG-ADV-01** · **CWE-444** · **ATT&CK T1190**
- context: **web-app** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- `resolve_model()`: flat alias → slashed upstream id (Hermes chokes on slashed ids; bare
  `kimi-k3` maps to `hyb/kimi-k3` by suffix match over the model list).
- Dead-model pruning: 502/404 → cache model→ts, typed `proxy_model_dead` 502, hidden from
  `/v1/models`, TTL 900s so redeploys recover.
- Tool-capability tracking: server learns from real responses, exposes `tools: yes|none|unknown`
  per model in `/v1/models`.
- `sse_wrap` try/finally guarantees `data: [DONE]` even when upstream truncates — truncated
  streams otherwise hang the browser reader loop forever.

## Probe adjustment (web-app × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
