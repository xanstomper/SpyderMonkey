# Negatives / hardened (log as coverage, don't re-probe) — grpc / hardened

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- base technique: `holyshit-mode-cf-wp-origin-bypass-recipe-negatives-hardened-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **grpc** · auth **hardened** · chain role **pivot**

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

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

## Probe adjustment (grpc × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
