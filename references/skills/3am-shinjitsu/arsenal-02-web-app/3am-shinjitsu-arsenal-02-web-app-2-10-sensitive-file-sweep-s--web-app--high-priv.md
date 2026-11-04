# 2.10 Sensitive-file sweep (score 60, ceiling 20 paths, once) — web-app / high-priv

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- base technique: `3am-shinjitsu-arsenal-02-web-app-2-10-sensitive-file-sweep-s.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **web-app** · auth **high-priv** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- SET: `/.git/HEAD`, `/.svn/entries`, `/.env`, `/backup.sql`, `/db.sql`, `/dump.zip`,
  `/debug`, `/actuator`, `/phpinfo.php`, `/server-status`, `/.DS_Store`, `/.well-known/security.txt`
- DISCRIMINATOR: 200 only counts with non-HTML content-type or non-shell body (§2.2).
- `.git/HEAD` 200 with `ref:` = recoverable tree; verify `objects/` reachability before verdict.

## Probe adjustment (web-app × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
