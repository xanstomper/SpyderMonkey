# 6. Coming-soon / maintenance-mode discriminator (login brute NOT viable)

- source canon: `holyshit-mode/wordpress-cloudflare-origin-bypass.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
