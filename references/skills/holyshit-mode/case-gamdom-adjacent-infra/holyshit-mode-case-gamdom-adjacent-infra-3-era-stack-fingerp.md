# 3. Era-stack fingerprint recipe (the Holy Shit shape)

- source canon: `holyshit-mode/case-gamdom-adjacent-infra.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
