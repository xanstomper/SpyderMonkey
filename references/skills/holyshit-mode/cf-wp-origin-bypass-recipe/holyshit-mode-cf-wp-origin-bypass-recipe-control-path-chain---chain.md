# Control-path chain (what "gaining control" requires here) — chain composition

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- base technique: `holyshit-mode-cf-wp-origin-bypass-recipe-control-path-chain-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

`origin_ip_exposed -> cf_waf_bypassed -> direct_origin_wp_admin -> admin_credential_access ->
wp-admin -> plugin/theme RCE -> full control`. The blocker on this target: native auth enforced
on all data endpoints (orders/customers/payment-gateway secrets need a session), maintenance is
vhost-level, so the remaining levers are (a) a known-CVE plugin exploit landing WAF-less against
the exact inventory, or (b) finding the admin password via sibling-domain/backup/source-mining.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
