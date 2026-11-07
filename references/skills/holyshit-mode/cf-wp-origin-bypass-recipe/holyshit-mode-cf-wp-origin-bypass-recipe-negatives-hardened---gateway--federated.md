# Negatives / hardened (log as coverage, don't re-probe) — gateway / federated

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- base technique: `holyshit-mode-cf-wp-origin-bypass-recipe-negatives-hardened-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **gateway** · auth **federated** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- WP core auth enforced: `/wp/v2/users|settings|plugins`, `/wc/v3/*`, elementor/funnelkit/htmega
  writes all 401/403 (`woocommerce_rest_cannot_view`, `rest_forbidden`).
- xmlrpc.php 405 (blocked); admin-ajax everything 400 `0` (gated); `admin-post.php?action=*`
  → `wp_die` 400.
- Sensitive files (`.env`, `.env.bak`, `.git/config`, `wp-config.php.bak`, `*.sql`, `*.zip`)
  all return a **generic soft-404 HTML shell** (200 text/html `charset=utf8` + `viewport`),
  NOT real content. An all-200-on-every-path result = custom 404 template, not leaked files.
- `wp-admin/install.php` correctly shows "WordPress Already Installed" (no installer takeover).
- Maintenance 503 is vhost-level: XFF `127.0.0.1`/`localhost`, forged logged-in cookies, and
  wp-preview all fail to bypass.

## Probe adjustment (gateway × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
