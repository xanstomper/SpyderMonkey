# 8. Loud-but-hardened: `wp-admin/install.php` and xmlrpc — edge / machine

- source canon: `holyshit-mode/wordpress-cloudflare-origin-bypass.md`
- base technique: `holyshit-mode-wordpress-cloudflare-origin-bypass-8-loud-but-.md`
- bindings: **WSTG-CONF-09** · **CWE-350** · **ATT&CK T1584**
- context: **edge** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: rate/segmentation differences — masscan-class first, then the app layer
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- `wp-admin/install.php` returning 200 with "WordPress Already Installed" = DB configured, no
  installer takeover (a 200 with the actual install form = critical).
- `xmlrpc.php` returning `405` = blocked (no XML-RPC brute/pingback). `401/403` on
  `wp-login.php?action=lostpassword` etc. = username-oracle closed.

## Probe adjustment (edge × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
