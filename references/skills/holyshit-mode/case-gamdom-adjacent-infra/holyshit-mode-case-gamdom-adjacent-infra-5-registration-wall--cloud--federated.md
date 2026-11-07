# 5. Registration walls — verify both layers before documenting — cloud / federated

- source canon: `holyshit-mode/case-gamdom-adjacent-infra.md`
- base technique: `holyshit-mode-case-gamdom-adjacent-infra-5-registration-wall.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **cloud** · auth **federated** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- **Edge layer:** Fastly VCL returns `400 ... Error 54113` on non-browser TLS for sensitive
  POSTs (`/signup`) while the same client passes on other endpoints. Python/curl replicas
  die here regardless of headers.
- **Browser layer:** replicate the flow in a real-browser harness (shadow-DOM forms need
  recursive shadow-root piercing; native value-setter + input/change events for React
  inputs; real `.click()` on controlled checkboxes — a failed checkbox blocks submit
  SILENTLY with no error text). If invisible Turnstile never initializes
  (`window.turnstile` undefined, no challenges.cloudflare.com scripts/iframes, no request
  fires on submit), the wall is verified.
- Document the wall, write a ready-made cookie-driven test script for the operator, and
  stop. Never forge captcha tokens.

## Probe adjustment (cloud × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
