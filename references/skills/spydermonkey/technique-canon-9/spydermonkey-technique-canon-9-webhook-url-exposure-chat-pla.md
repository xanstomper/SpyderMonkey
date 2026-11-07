# Webhook URL exposure (chat platforms)

- source canon: `spydermonkey/technique-canon-9.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-06

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Discord/Slack/Telegram webhook URLs in client bundles/repos — possession = forge-class. Decisive test: URL string + provider-format validation = the finding (never posted to).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
