# HOLY SHIT (2026-10-03 evening session): `/auth/v1/authorize` redirect_uri forwarding (score 70)

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

```
GET https://auth.gratisfy.xyz/auth/v1/authorize?provider=discord&redirect_uri=https://evil.com/cb
→ 302 Location: discord.com/api/oauth2/authorize?client_id=1308596927759126548&redirect_uri=https://evil.com/cb&scope=email+identify&state=<server nonce>
```
GoTrue forwards the CLIENT-controlled `redirect_uri` to the provider instead of hardcoding the registered callback — same for `provider=google` (client_id 359907877461-…). Provider validation split (decisive): **Google** hard-rejects unregistered URIs at render (follow the redirect chain → `redirect_uri_mismatch` error page); **Discord renders its authorize page 200 regardless** because it validates redirect_uri at token-exchange, not render — the 200 is NOT proof of acceptance. Impact gate = whether the Discord app has a loose/wildcard URI registered; proving that needs one browser login (operator to watch). Rate the GoTrue-side flaw ~8.1 regardless. Callback hardened separately: `/auth/v1/callback` without state → `400 bad_oauth_callback` error redirect.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
