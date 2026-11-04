# Worked case numbers ( — api / low-priv

- source canon: `holyshit-mode/wordpress-cloudflare-origin-bypass.md`
- base technique: `holyshit-mode-wordpress-cloudflare-origin-bypass-worked-case.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **api** · auth **low-priv** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- origin_ip_exposed = confirmed 90, wp_admin_username_enum = confirmed 70 (slug **geo**, ID 1,
  sole admin), wordpress_stack_inventory = confirmed 55.
- auth_surface_hardened = negative 85, site_in_coming_soon = negative 70 (blocks the login chain).
- Control chain recorded: origin_ip_exposed → CF WAF bypass → direct-origin wp-admin → admin
  "geo" credential access → wp-admin → plugin/theme RCE → full control. Presently blocked by
  maintenance mode.

## Probe adjustment (api × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
