# 6. Coming-soon / maintenance-mode discriminator (login brute NOT viable) — mesh / service

- source canon: `holyshit-mode/wordpress-cloudflare-origin-bypass.md`
- base technique: `holyshit-mode-wordpress-cloudflare-origin-bypass-6-coming-so.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **mesh** · auth **service** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

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

## Probe adjustment (mesh × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
