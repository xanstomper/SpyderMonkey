# 6. Coming-soon / maintenance-mode discriminator (login brute NOT viable) — chain composition

- source canon: `holyshit-mode/wordpress-cloudflare-origin-bypass.md`
- base technique: `holyshit-mode-wordpress-cloudflare-origin-bypass-6-coming-so.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

A site in LiteSpeed/coming-soon maintenance serves bulk `503 Retry-After: 600` on `/` and store
pages while still serving REST + assets. **The decisive test for "is the login backend actually
processing auth":** POST a bogus credential to `wp-login.php` and `/my-account/`:
- Real login → `302` redirect, or `200` with `#login_error` div / `woocommerce-error`, a
  `set-cookie` test cookie, and the `name="log"`/`name="user_login"` field.
- **Maintenance-shell auth** → `200` with the generic "DOCTYPE html / charset=utf8 / viewport"
  page, **no login form, no error oracle, no set-cookie**. The login backend is NOT reachable
  even at the origin → **credential brute is a dead end right now**, regardless of username or
  origin access. Document it as a negative blocker and route the control chain to the
  maintenance-bypass or plugin-CVE instead.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
