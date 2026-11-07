# Webhook URL exposure (chat platforms) — gateway / unauth

- source canon: `spydermonkey/technique-canon-9.md`
- base technique: `spydermonkey-technique-canon-9-webhook-url-exposure-chat-pla.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **gateway** · auth **unauth** · chain role **pivot**

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

Discord/Slack/Telegram webhook URLs in client bundles/repos — possession = forge-class. Decisive test: URL string + provider-format validation = the finding (never posted to).

## Probe adjustment (gateway × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
