# 8. Impersonated WS clients in practice (curl_cffi) — graphql / low-priv

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-8-impersonated-ws-clien.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **graphql** · auth **low-priv** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

`Session(impersonate="chrome110")` is the practical client for CF-fronted WS testing:

- **Warm the jar before the upgrade**: a bare `ws_connect` with browser TLS but no
  cookie history gets CF 403; the SAME Session after one `GET https://target/`
  (which receives `__cf_bm`) passes the upgrade. The clearance is cookie-carried,
  not TLS-carried — an "impersonation failed" verdict without a warmed jar is a
  false negative.
- **One Session per probe**: session jars accumulate CF cookies until requests die
  with 431 "Header Value Too Long" (the error names the culprit header).
- **Cookies iterate as name strings**, not Cookie objects — `dict(s.cookies)` for
  name→value.
- **Capture the handshake without raw CDP**: playwright `page.on('websocket')` →
  `ws.on('framesent')`/`ws.on('framereceived')` on a real page load reveals the
  client's exact opening bytes — replicate those byte-for-byte instead of guessing
  packet shapes.

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
