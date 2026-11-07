# 8. Loud-but-hardened: `wp-admin/install.php` and xmlrpc

- source canon: `holyshit-mode/wordpress-cloudflare-origin-bypass.md`
- bindings: **WSTG-CONF-09** · **CWE-350** · **ATT&CK T1584**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- `wp-admin/install.php` returning 200 with "WordPress Already Installed" = DB configured, no
  installer takeover (a 200 with the actual install form = critical).
- `xmlrpc.php` returning `405` = blocked (no XML-RPC brute/pingback). `401/403` on
  `wp-login.php?action=lostpassword` etc. = username-oracle closed.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
