# 2. WordPress xmlrpc credential-oracle + CDN burst behavior ( — gateway / root

- source canon: `holyshit-mode/control-escalation-negatives.md`
- base technique: `holyshit-mode-control-escalation-negatives-2-wordpress-xmlrp.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **gateway** · auth **root** · chain role **pivot**

## Route

- probes: `gobuster`, `ffuf`, `dirsearch`, `dirb`, `feroxbuster`, `wfuzz`, `dirhunt`
- chains: `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

`xmlrpc.php` exposed behind a CDN is a real admin-takeover primitive:

- `wp.getUsersBlogs("user","WrongPass")` → single call returns `faultCode 403 "Incorrect username or password"`.
  That 403 (not 429/locked) = **valid-credential oracle with no observed rate limit on single calls**.
- `system.multicall` exists → amplification primitive. **BUT**: a 3-call batch triggered a
  Cloudflare challenge ("One moment, please..." HTML), while single calls pass straight through.
  => Low-and-slow single-call spraying still works against `admin`; don't rely on burst multicall
  past a WAF. Test both a 1-call and an N-call payload; a malformed multicall that returns
  `parse error. not well formed` (fault -32700) still proves the method is wired (not "not found").
- Confirm the single admin user ID via public REST: `GET /wp-json/wp/v2/media?per_page=20&_fields=id,author,source_url`
  returns full media + `author:1` even when `/wp-json/wp/v2/users` is 401-gated. Author id 1 = admin.
- Upload-backup/env/etc exposures: `/wp-content/debug.log`, `.env`, `*.zip`, `wp-config` backups
  typically 403/404 (protected), and a directory listing of `uploads/` may be empty — don't assume
  the DB-zip filename implies a real dump (see §4).

## Probe adjustment (gateway × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
