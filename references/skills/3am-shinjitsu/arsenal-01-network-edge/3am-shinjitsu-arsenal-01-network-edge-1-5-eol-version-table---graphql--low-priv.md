# 1.5 EOL version table (match everything §1.1/§1.4 leaks) — graphql / low-priv

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-1-5-eol-version-table-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **graphql** · auth **low-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

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

## Probe adjustment (graphql × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
