# 3.13 CORS severity discipline — api / high-priv

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- base technique: `3am-shinjitsu-arsenal-03-api-3-13-cors-severity-discipline.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **api** · auth **high-priv** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Reflection `ACAO: <evil>` + `ACAC: true` on cookie-auth endpoints = critical. On Bearer-
  header APIs = config flaw ONLY (no credentials ride CORS). Cookie era: read raw `Set-Cookie`
  — `SameSite=Lax` blocks cross-site POST → downgrade ~7.1. Severity is f(auth-model, SameSite),
  not reflection alone.

## Probe adjustment (api × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
