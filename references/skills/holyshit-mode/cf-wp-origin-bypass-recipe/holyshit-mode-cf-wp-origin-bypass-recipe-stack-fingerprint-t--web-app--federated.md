# Stack fingerprint trick — web-app / federated

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- base technique: `holyshit-mode-cf-wp-origin-bypass-recipe-stack-fingerprint-t.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **web-app** · auth **federated** · chain role **entry**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

Repeated `Server:` flips (LiteSpeed ↔ openresty/1.31.1.1) across connections = **multi-instance
load-balanced backend**, not a misread. Note both versions; CVE-match against the larger
surface (WordPress 6.7.3 / WooCommerce 9.5.1 / Elementor 3.26.4+Pro / HT Mega 2.7.8 / The Plus
6.2.2 / Qi Addons 1.8.9 / Funnel Builder 3.8.0 / Blocksy 2.0.84 / wp-statistics).

## Probe adjustment (web-app × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
