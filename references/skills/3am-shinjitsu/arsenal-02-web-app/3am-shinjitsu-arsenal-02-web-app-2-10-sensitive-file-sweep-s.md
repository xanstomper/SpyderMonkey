# 2.10 Sensitive-file sweep (score 60, ceiling 20 paths, once)

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## The technique

- SET: `/.git/HEAD`, `/.svn/entries`, `/.env`, `/backup.sql`, `/db.sql`, `/dump.zip`,
  `/debug`, `/actuator`, `/phpinfo.php`, `/server-status`, `/.DS_Store`, `/.well-known/security.txt`
- DISCRIMINATOR: 200 only counts with non-HTML content-type or non-shell body (§2.2).
- `.git/HEAD` 200 with `ref:` = recoverable tree; verify `objects/` reachability before verdict.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
