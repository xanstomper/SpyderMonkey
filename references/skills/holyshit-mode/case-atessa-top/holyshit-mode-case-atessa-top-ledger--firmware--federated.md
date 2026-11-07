# Ledger — firmware / federated

- source canon: `holyshit-mode/case-atessa-top.md`
- base technique: `holyshit-mode-case-atessa-top-ledger.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **firmware** · auth **federated** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

`holyleadger/atessa.top.json` — confirmed: routing-oracle 45, count_tokens-DoS 50, forgot 40, resend 35, trust-split 30, quota-429 10; negatives: turnstile 20, oauth 15, stripe 15, cors 10, admin 10, ghosts 5; chain `preauth-routing-oracle` (hypothesis).

## Probe adjustment (firmware × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
