# 2. WordPress xmlrpc credential-oracle + CDN burst behavior (

- source canon: `holyshit-mode/control-escalation-negatives.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
