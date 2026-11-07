# 3. WordPress fingerprint — the open thing leaks everything — web-app / machine

- source canon: `holyshit-mode/wordpress-cloudflare-origin-bypass.md`
- base technique: `holyshit-mode-wordpress-cloudflare-origin-bypass-3-wordpress.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **web-app** · auth **machine** · chain role **entry**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

The homepage body (even under a 503/maintenance shell) carries the whole stack:
- `<meta name="generator" content="WordPress 6.7.3" />`, `WooCommerce 9.5.1`, `Elementor 3.26.4`.
- Asset paths in the HTML enumerate installed plugins:
  `re.findall(r'wp-content/(?:themes|plugins|uploads)/[\w\.\-]+', html)` →
  `elementor, pro-elements, ht-mega-for-elementor, qi-addons-for-elementor, funnel-builder, …`.
- Exact plugin versions from readme.txt: `GET /wp-content/plugins/<slug>/readme.txt` → regex
  `Stable tag[:：]\s*([0-9][\w\.\-]+)`. Some plugin readmes return 503/maintenance-shell; those
  are the ones to note as "version unknown, version file blocked".
- Server header inconsistency = multi-instance backend (flipped `LW_speed` ↔ `openresty/1.31.1.1`
  across requests) — a signal the app is load-balanced / partially in maintenance.

## Probe adjustment (web-app × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
