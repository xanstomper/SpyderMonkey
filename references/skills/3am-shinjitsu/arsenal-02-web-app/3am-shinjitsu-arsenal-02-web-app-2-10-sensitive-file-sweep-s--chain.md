# 2.10 Sensitive-file sweep (score 60, ceiling 20 paths, once) — chain composition

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- base technique: `3am-shinjitsu-arsenal-02-web-app-2-10-sensitive-file-sweep-s.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- SET: `/.git/HEAD`, `/.svn/entries`, `/.env`, `/backup.sql`, `/db.sql`, `/dump.zip`,
  `/debug`, `/actuator`, `/phpinfo.php`, `/server-status`, `/.DS_Store`, `/.well-known/security.txt`
- DISCRIMINATOR: 200 only counts with non-HTML content-type or non-shell body (§2.2).
- `.git/HEAD` 200 with `ref:` = recoverable tree; verify `objects/` reachability before verdict.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
