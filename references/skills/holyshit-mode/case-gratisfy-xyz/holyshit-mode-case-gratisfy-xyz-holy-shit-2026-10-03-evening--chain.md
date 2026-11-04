# HOLY SHIT (2026-10-03 evening session): `/auth/v1/authorize` redirect_uri forwarding (score 70) — chain composition

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- base technique: `holyshit-mode-case-gratisfy-xyz-holy-shit-2026-10-03-evening.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

```
GET https://auth.gratisfy.xyz/auth/v1/authorize?provider=discord&redirect_uri=https://evil.com/cb
→ 302 Location: discord.com/api/oauth2/authorize?client_id=1308596927759126548&redirect_uri=https://evil.com/cb&scope=email+identify&state=<server nonce>
```
GoTrue forwards the CLIENT-controlled `redirect_uri` to the provider instead of hardcoding the registered callback — same for `provider=google` (client_id 359907877461-…). Provider validation split (decisive): **Google** hard-rejects unregistered URIs at render (follow the redirect chain → `redirect_uri_mismatch` error page); **Discord renders its authorize page 200 regardless** because it validates redirect_uri at token-exchange, not render — the 200 is NOT proof of acceptance. Impact gate = whether the Discord app has a loose/wildcard URI registered; proving that needs one browser login (operator to watch). Rate the GoTrue-side flaw ~8.1 regardless. Callback hardened separately: `/auth/v1/callback` without state → `400 bad_oauth_callback` error redirect.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
