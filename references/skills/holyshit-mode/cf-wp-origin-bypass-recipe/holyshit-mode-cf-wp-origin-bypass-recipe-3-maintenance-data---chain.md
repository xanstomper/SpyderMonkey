# 3. Maintenance/data-plane asymmetry (a mask, not a wall) — chain composition

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- base technique: `holyshit-mode-cf-wp-origin-bypass-recipe-3-maintenance-data-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

A coming-soon/maintenance mode often hard-503s the HTML storefront (`Retry-After: 600`) at
**vhost level** (not plugin-level — so cookie/XFF/IP "bypasses" do nothing) while the
**data plane serves 200**:

| Surface | Status behind 503 |
|---|---|
| `/`, `/wp-login.php`, `/my-account/`, store pages | 503 (masked) |
| `/wp-json/`, `/wp-json/wp/v2/*`, `/wp-json/wc/store/v1/*` | **200 (live)** |
| `/wp-content/..static assets`, `/wp-includes/version.php` | 200 |
| `/wp-admin/admin-post.php`, `/wp-admin/load-scripts.php` | 200 len=0 (execute, no mask) |
| `/wp-admin/*` rest, `/wp-login.php` POST | redirect to `/404/` or 503 |

So: never judge a masked site as "down/empty" from the HTML alone. Enumerate the full REST
surface (`/wp-json/` route index). The backend (products, orders, checkout, plugin endpoints)
is reachable; only the templates are hidden. This is where open-API findings live.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
