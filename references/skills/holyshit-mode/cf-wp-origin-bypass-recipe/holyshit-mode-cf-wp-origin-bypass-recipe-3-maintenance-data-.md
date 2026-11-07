# 3. Maintenance/data-plane asymmetry (a mask, not a wall)

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
