# 8. Loud-but-hardened: `wp-admin/install.php` and xmlrpc

- source canon: `holyshit-mode/wordpress-cloudflare-origin-bypass.md`
- bindings: **WSTG-CONF-09** · **CWE-350** · **ATT&CK T1584**
- generated: 2026-11-04

## The technique

- `wp-admin/install.php` returning 200 with "WordPress Already Installed" = DB configured, no
  installer takeover (a 200 with the actual install form = critical).
- `xmlrpc.php` returning `405` = blocked (no XML-RPC brute/pingback). `401/403` on
  `wp-login.php?action=lostpassword` etc. = username-oracle closed.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
