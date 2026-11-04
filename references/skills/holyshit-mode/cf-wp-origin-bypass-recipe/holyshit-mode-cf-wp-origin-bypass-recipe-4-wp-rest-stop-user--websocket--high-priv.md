# 4. WP REST: stop-user-enumeration does NOT block embedded author leak — websocket / high-priv

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- base technique: `holyshit-mode-cf-wp-origin-bypass-recipe-4-wp-rest-stop-user.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **websocket** · auth **high-priv** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

The `stop-user-enumeration` plugin blocks `/wp-json/wp/v2/users`, `/?author=N` (403/401), and
author pages — but **`/wp-json/wp/v2/posts?_embed` (and pages, any post type) leaks the admin's
username via the `_embedded.author` object**:

```json
"_embedded": {"author": [{"id":1, "name":"nk":"/author/geo/"}]}
```

`slug` IS the WordPress username. One request gets you the target admin account for
credential/CVE work even on a "hardened" install.

## Probe adjustment (websocket × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
