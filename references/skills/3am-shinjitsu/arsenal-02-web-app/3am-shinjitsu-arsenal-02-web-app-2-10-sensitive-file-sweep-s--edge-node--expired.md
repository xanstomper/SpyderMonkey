# 2.10 Sensitive-file sweep (score 60, ceiling 20 paths, once) — edge-node / expired

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- base technique: `3am-shinjitsu-arsenal-02-web-app-2-10-sensitive-file-sweep-s.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **edge-node** · auth **expired** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

- SET: `/.git/HEAD`, `/.svn/entries`, `/.env`, `/backup.sql`, `/db.sql`, `/dump.zip`,
  `/debug`, `/actuator`, `/phpinfo.php`, `/server-status`, `/.DS_Store`, `/.well-known/security.txt`
- DISCRIMINATOR: 200 only counts with non-HTML content-type or non-shell body (§2.2).
- `.git/HEAD` 200 with `ref:` = recoverable tree; verify `objects/` reachability before verdict.

## Probe adjustment (edge-node × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
