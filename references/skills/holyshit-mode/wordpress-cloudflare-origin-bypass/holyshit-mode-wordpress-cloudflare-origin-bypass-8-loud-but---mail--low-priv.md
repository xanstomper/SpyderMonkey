# 8. Loud-but-hardened: `wp-admin/install.php` and xmlrpc — mail / low-priv

- source canon: `holyshit-mode/wordpress-cloudflare-origin-bypass.md`
- base technique: `holyshit-mode-wordpress-cloudflare-origin-bypass-8-loud-but-.md`
- bindings: **WSTG-CONF-09** · **CWE-350** · **ATT&CK T1584**
- context: **mail** · auth **low-priv** · chain role **pivot**

## Context

- platform: spf/dkim/dmarc record surface — spoofing and spoofability live in the record math
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- `wp-admin/install.php` returning 200 with "WordPress Already Installed" = DB configured, no
  installer takeover (a 200 with the actual install form = critical).
- `xmlrpc.php` returning `405` = blocked (no XML-RPC brute/pingback). `401/403` on
  `wp-login.php?action=lostpassword` etc. = username-oracle closed.

## Probe adjustment (mail × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
