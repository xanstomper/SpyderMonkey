# Bundle-mining yield (the whole engagement came from here) — api / machine

- source canon: `holyshit-mode/case-atessa-top.md`
- base technique: `holyshit-mode-case-atessa-top-bundle-mining-yield-the-whole-.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **api** · auth **machine** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- Endpoint list via `grep -oE '"/[a-zA-Z0-9_/.-]{2,80}"'` — full app-plane map incl. wrapper call-sites (`QK(i,o,r)` = login(email,pw,captcha_token)).
- i18n strings → voucher format `GIFT-XXXXX-XXXXX-XXXXX`, feature inventory (affiliates, reseller RS keys, credit transfers, image library).
- Lazy chunks → `TurnstileWidget` → public captcha-config.
- No hardcoded secrets / backdoor IDs found.

## Probe adjustment (api × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
