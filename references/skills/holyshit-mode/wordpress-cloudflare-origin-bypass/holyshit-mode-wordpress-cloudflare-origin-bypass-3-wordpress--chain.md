# 3. WordPress fingerprint — the open thing leaks everything — chain composition

- source canon: `holyshit-mode/wordpress-cloudflare-origin-bypass.md`
- base technique: `holyshit-mode-wordpress-cloudflare-origin-bypass-3-wordpress.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Chain roles

- entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
