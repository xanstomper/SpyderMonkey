# The five genes (every vector carries all five) — wasm / federated

- source canon: `kairo/synthesis-engine.md`
- base technique: `kairo-synthesis-engine-the-five-genes-every-vector-carries-a.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **wasm** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

| Gene | Content | Source |
|---|---|---|
| TRIGGER | the source finding (what was observed) | ingested from family states |
| PRECONDITION | declared estate + access level | P0 record |
| PRIMITIVE | the technique class's mechanism | the class table |
| IMPACT-GATE | the exact proof condition | the class table |
| Δ | the documented-class adaptation for THIS target | synthesized; no Δ = no vector |

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
