# 2.9 Admin-portal hunt in lazy chunks (score 85)

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- The main bundle holds the route table only. `grep -oE '"/api/admin/[a-z_/]+"' chunk.js` on
  EVERY chunk. Confirmed pattern: full `/api/admin/*` portal (user mgmt, grants, audit logs)
  invisible in main bundle → run the authz matrix on it (§3.3).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
