# 3. Era-stack fingerprint recipe (the Holy Shit shape) — ci-cd / federated

- source canon: `holyshit-mode/case-gamdom-adjacent-infra.md`
- base technique: `holyshit-mode-case-gamdom-adjacent-infra-3-era-stack-fingerp.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **ci-cd** · auth **federated** · chain role **entry**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

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

## Probe adjustment (ci-cd × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
