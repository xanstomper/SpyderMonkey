# 4. WP REST: stop-user-enumeration does NOT block embedded author leak — graphql / machine

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- base technique: `holyshit-mode-cf-wp-origin-bypass-recipe-4-wp-rest-stop-user.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **graphql** · auth **machine** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

The `stop-user-enumeration` plugin blocks `/wp-json/wp/v2/users`, `/?author=N` (403/401), and
author pages — but **`/wp-json/wp/v2/posts?_embed` (and pages, any post type) leaks the admin's
username via the `_embedded.author` object**:

```json
"_embedded": {"author": [{"id":1, "name":"nk":"/author/geo/"}]}
```

`slug` IS the WordPress username. One request gets you the target admin account for
credential/CVE work even on a "hardened" install.

## Probe adjustment (graphql × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
