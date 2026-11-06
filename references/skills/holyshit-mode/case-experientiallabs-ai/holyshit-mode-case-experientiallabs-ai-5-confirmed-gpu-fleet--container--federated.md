# 5. CONFIRMED — GPU fleet internals leak keyless on `clef.xplabs.ai` (score 35) — container / federated

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-5-confirmed-gpu-fleet.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **container** · auth **federated** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- `GET https://clef.xplabs.ai/health` → 200 `{"status":"ok","max_length":65536,"queued":0,
  "gpu_allocated_gib":29.46,"gpu_peak_gib":36.76,...}` — no auth.
- **IMPACT:** Infra/GPU-fleet capacity disclosure.

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
