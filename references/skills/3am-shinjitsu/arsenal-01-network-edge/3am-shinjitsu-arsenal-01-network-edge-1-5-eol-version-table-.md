# 1.5 EOL version table (match everything §1.1/§1.4 leaks)

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Component | EOL since | Where it leaks |
|---|---|---|
| PHP 5.x | 2015-2018 | `X-Powered-By`, VestaCP-era 301 path leaks |
| PHP 7.0–7.3 | 2019-2021 | same |
| MariaDB 5.5/10.0 | 2017-2019 | `:3306` greeting |
| MySQL 5.6/5.7 | 2021/2023 | greeting |
| Node <12/14 | 2019/2021 | error pages, `Server: Node` |
| nginx <1.18 | 2020 | `Server` line |
| Apache 2.2 | 2017 | `Server` line |
| OpenSSH <7.7 | 2018 | `ssh` banner |
| vsFTPd 2.x | 2015 | `21` banner |
| Exim <4.92 | 2019 | `25` banner |
| Tomcat 7/8 | 2021 | error pages |
| GoTrue <2.100 | version-pinned CVEs | `/auth/v1/health` |
| Kong <2.x | CVE-2020-11710 class | `x-kong-*` headers |

- WORKFLOW: `searchsploit <component> <version>` for EVERY fingerprinted EOL version →
  documented-PoC adaptation only (§15 wall). Log each match with its exact version string.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
