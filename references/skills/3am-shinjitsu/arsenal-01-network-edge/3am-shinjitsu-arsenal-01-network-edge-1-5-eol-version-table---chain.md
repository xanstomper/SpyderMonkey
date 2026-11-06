# 1.5 EOL version table (match everything §1.1/§1.4 leaks) — chain composition

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-1-5-eol-version-table-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
