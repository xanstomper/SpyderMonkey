# 4. WP REST: stop-user-enumeration does NOT block embedded author leak — chain composition

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- base technique: `holyshit-mode-cf-wp-origin-bypass-recipe-4-wp-rest-stop-user.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

The `stop-user-enumeration` plugin blocks `/wp-json/wp/v2/users`, `/?author=N` (403/401), and
author pages — but **`/wp-json/wp/v2/posts?_embed` (and pages, any post type) leaks the admin's
username via the `_embedded.author` object**:

```json
"_embedded": {"author": [{"id":1, "name":"nk":"/author/geo/"}]}
```

`slug` IS the WordPress username. One request gets you the target admin account for
credential/CVE work even on a "hardened" install.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
