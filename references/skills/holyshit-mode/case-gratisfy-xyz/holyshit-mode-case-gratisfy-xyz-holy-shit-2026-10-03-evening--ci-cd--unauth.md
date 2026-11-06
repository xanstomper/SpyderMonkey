# HOLY SHIT (2026-10-03 evening session): `/auth/v1/authorize` redirect_uri forwarding (score 70) — ci-cd / unauth

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- base technique: `holyshit-mode-case-gratisfy-xyz-holy-shit-2026-10-03-evening.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **ci-cd** · auth **unauth** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

```
GET https://auth.gratisfy.xyz/auth/v1/authorize?provider=discord&redirect_uri=https://evil.com/cb
→ 302 Location: discord.com/api/oauth2/authorize?client_id=1308596927759126548&redirect_uri=https://evil.com/cb&scope=email+identify&state=<server nonce>
```
GoTrue forwards the CLIENT-controlled `redirect_uri` to the provider instead of hardcoding the registered callback — same for `provider=google` (client_id 359907877461-…). Provider validation split (decisive): **Google** hard-rejects unregistered URIs at render (follow the redirect chain → `redirect_uri_mismatch` error page); **Discord renders its authorize page 200 regardless** because it validates redirect_uri at token-exchange, not render — the 200 is NOT proof of acceptance. Impact gate = whether the Discord app has a loose/wildcard URI registered; proving that needs one browser login (operator to watch). Rate the GoTrue-side flaw ~8.1 regardless. Callback hardened separately: `/auth/v1/callback` without state → `400 bad_oauth_callback` error redirect.

## Probe adjustment (ci-cd × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
