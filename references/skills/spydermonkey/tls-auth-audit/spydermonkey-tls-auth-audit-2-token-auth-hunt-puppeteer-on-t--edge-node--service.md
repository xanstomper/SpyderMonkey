# 2. Token/auth hunt (puppeteer on the VM) — edge-node / service

- source canon: `spydermonkey/tls-auth-audit.md`
- base technique: `spydermonkey-tls-auth-audit-2-token-auth-hunt-puppeteer-on-t.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **edge-node** · auth **service** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

1. Pass the CF challenge first: `page.goto` the main page, wait 10s+ (see
   SKILL.md SPA-probing note).
2. Capture auth-relevant traffic: `page.on('request')` / `page.on('response')`,
   keep headers matching `auth|token|jwt|bearer|session|device|x-|cookie`, dedupe
   by url + sorted header names.
3. Dump `localStorage` / `sessionStorage` / `document.cookie`; regex-hunt for
   JWTs (`eyJ….….`); decode hits via base64url (header.alg + payload claims).
4. Scan EVERY JS chunk with auth patterns: JWT literal, `Authorization`/`Bearer`
   usage, token storage keys, WS auth query params, jwt decode/verify code,
   `alg` hints, `x-api-key`-style headers. Filter placeholder/library false
   positives (axios emits generic `Authorization: Basic` builder code — it is
   not app usage).
5. **JWT-absence across the whole stack is itself a finding** — opaque-token
   design; state it, don't keep hunting for JWTs that don't exist.

## Probe adjustment (edge-node × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
