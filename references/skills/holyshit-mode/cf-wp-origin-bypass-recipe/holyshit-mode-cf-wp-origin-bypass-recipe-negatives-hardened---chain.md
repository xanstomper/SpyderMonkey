# Negatives / hardened (log as coverage, don't re-probe) — chain composition

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- base technique: `holyshit-mode-cf-wp-origin-bypass-recipe-negatives-hardened-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
