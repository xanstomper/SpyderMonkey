# Worked case numbers (

- source canon: `holyshit-mode/wordpress-cloudflare-origin-bypass.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- origin_ip_exposed = confirmed 90, wp_admin_username_enum = confirmed 70 (slug **geo**, ID 1,
  sole admin), wordpress_stack_inventory = confirmed 55.
- auth_surface_hardened = negative 85, site_in_coming_soon = negative 70 (blocks the login chain).
- Control chain recorded: origin_ip_exposed → CF WAF bypass → direct-origin wp-admin → admin
  "geo" credential access → wp-admin → plugin/theme RCE → full control. Presently blocked by
  maintenance mode.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
