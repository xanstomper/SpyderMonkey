# 6. Coming-soon / maintenance-mode discriminator (login brute NOT viable) — edge-node / guest

- source canon: `holyshit-mode/wordpress-cloudflare-origin-bypass.md`
- base technique: `holyshit-mode-wordpress-cloudflare-origin-bypass-6-coming-so.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **edge-node** · auth **guest** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

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

## Probe adjustment (edge-node × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
