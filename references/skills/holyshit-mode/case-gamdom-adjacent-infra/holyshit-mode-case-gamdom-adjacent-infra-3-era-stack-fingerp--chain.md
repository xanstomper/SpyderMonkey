# 3. Era-stack fingerprint recipe (the Holy Shit shape) — chain composition

- source canon: `holyshit-mode/case-gamdom-adjacent-infra.md`
- base technique: `holyshit-mode-case-gamdom-adjacent-infra-3-era-stack-fingerp.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

On a live mirror/entrance box:

- `curl -sI https://<host>/` — `X-Powered-By: PHP/5.4.45` = EOL Sep 2015, 11 years unpatched.
- Follow any 301s with `-w "%{redirect_url}"` — a redirect leaking
  `/home/<user>/web/<domain>/public_html/...` = stock VestaCP/HestiaCP layout; also a
  standalone absolute-path disclosure finding.
- Read-only TCP connect scan of common ports: 21,22,25,53,80,110,143,443,465,587,993,995,
  2222,3306,5432,6379,8080,8083,8443,8888,10000.
- Banner-grab the answers:
  - `:8083` — title `Vesta`/`Hestia` = exposed EOL hosting panel. POST `/api/` with
    `cmd=v-list-sys-info&user=admin&password=wrong` → uniform `Error: authentication failed`
    = API live, auth-gated, no user enumeration. Map known-CVE surface; do NOT brute creds.
  - `:3306` — raw connect + recv leaks the MariaDB/MySQL version in the greeting
    (`5.5.x-MariaDB` = EOL Oct 2018). Internet-reachable EOL DB = the finding itself.
  - `:110/:143` Dovecot, `:21` vsFTPd — normal panel stack, note exposure.
- Probe the web layer: `/phpmyadmin/`, `/server-status`, `/phpinfo.php` — 301/403 = exists.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
