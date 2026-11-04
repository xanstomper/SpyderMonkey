# 4. WP REST `_embed` user-enum bypass (beat stop-user-enumeration) — chain composition

- source canon: `holyshit-mode/wordpress-cloudflare-origin-bypass.md`
- base technique: `holyshit-mode-wordpress-cloudflare-origin-bypass-4-wp-rest-e.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

`/wp-json/wp/v2/users`, `/?author=N`, `?rest_route=/wp/v2/users` are all blocked by the
stop-user-enumeration plugin. BUT REST-embedded author objects still leak the admin:
```
GET /wp-json/wp/v2/posts?per_page=20&_embed
→ _embedded.author[] = {"id":1,"name":"":".../author/geo/"}
```
The `slug` is the **WordPress username** (here: sole admin `geo`). Scan posts/pages/any public
content type with `_embed` and collect every distinct `slug`. Always check the WP REST route
index first: `GET /wp-json/` returns every namespace + route + method (huge recon goldmine —
844 routes on

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
