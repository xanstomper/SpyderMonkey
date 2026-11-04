# Bundle-mining yield (the whole engagement came from here) — websocket / unauth

- source canon: `holyshit-mode/case-atessa-top.md`
- base technique: `holyshit-mode-case-atessa-top-bundle-mining-yield-the-whole-.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **websocket** · auth **unauth** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- Endpoint list via `grep -oE '"/[a-zA-Z0-9_/.-]{2,80}"'` — full app-plane map incl. wrapper call-sites (`QK(i,o,r)` = login(email,pw,captcha_token)).
- i18n strings → voucher format `GIFT-XXXXX-XXXXX-XXXXX`, feature inventory (affiliates, reseller RS keys, credit transfers, image library).
- Lazy chunks → `TurnstileWidget` → public captcha-config.
- No hardcoded secrets / backdoor IDs found.

## Probe adjustment (websocket × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
