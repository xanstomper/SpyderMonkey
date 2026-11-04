# 4. WP REST: stop-user-enumeration does NOT block embedded author leak

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

The `stop-user-enumeration` plugin blocks `/wp-json/wp/v2/users`, `/?author=N` (403/401), and
author pages — but **`/wp-json/wp/v2/posts?_embed` (and pages, any post type) leaks the admin's
username via the `_embedded.author` object**:

```json
"_embedded": {"author": [{"id":1, "name":"nk":"/author/geo/"}]}
```

`slug` IS the WordPress username. One request gets you the target admin account for
credential/CVE work even on a "hardened" install.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
