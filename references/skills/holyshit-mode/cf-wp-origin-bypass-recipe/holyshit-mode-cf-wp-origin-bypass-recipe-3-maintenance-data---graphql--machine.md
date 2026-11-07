# 3. Maintenance/data-plane asymmetry (a mask, not a wall) — graphql / machine

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- base technique: `holyshit-mode-cf-wp-origin-bypass-recipe-3-maintenance-data-.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **graphql** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

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

## Probe adjustment (graphql × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
