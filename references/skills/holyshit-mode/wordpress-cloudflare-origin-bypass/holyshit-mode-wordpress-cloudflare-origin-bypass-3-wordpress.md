# 3. WordPress fingerprint — the open thing leaks everything

- source canon: `holyshit-mode/wordpress-cloudflare-origin-bypass.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
