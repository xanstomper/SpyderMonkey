# Bundle-mining yield (the whole engagement came from here) — websocket / low-priv

- source canon: `holyshit-mode/case-atessa-top.md`
- base technique: `holyshit-mode-case-atessa-top-bundle-mining-yield-the-whole-.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **websocket** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- Endpoint list via `grep -oE '"/[a-zA-Z0-9_/.-]{2,80}"'` — full app-plane map incl. wrapper call-sites (`QK(i,o,r)` = login(email,pw,captcha_token)).
- i18n strings → voucher format `GIFT-XXXXX-XXXXX-XXXXX`, feature inventory (affiliates, reseller RS keys, credit transfers, image library).
- Lazy chunks → `TurnstileWidget` → public captcha-config.
- No hardcoded secrets / backdoor IDs found.

## Probe adjustment (websocket × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
