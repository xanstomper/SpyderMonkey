# Stack fingerprint trick — chain composition

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- base technique: `holyshit-mode-cf-wp-origin-bypass-recipe-stack-fingerprint-t.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Chain roles

- entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Repeated `Server:` flips (LiteSpeed ↔ openresty/1.31.1.1) across connections = **multi-instance
load-balanced backend**, not a misread. Note both versions; CVE-match against the larger
surface (WordPress 6.7.3 / WooCommerce 9.5.1 / Elementor 3.26.4+Pro / HT Mega 2.7.8 / The Plus
6.2.2 / Qi Addons 1.8.9 / Funnel Builder 3.8.0 / Blocksy 2.0.84 / wp-statistics).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
