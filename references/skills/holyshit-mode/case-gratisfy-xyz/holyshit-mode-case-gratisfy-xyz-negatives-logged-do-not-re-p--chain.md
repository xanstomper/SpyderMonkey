# Negatives (logged, do not re-probe without redeploy) — chain composition

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- base technique: `holyshit-mode-case-gratisfy-xyz-negatives-logged-do-not-re-p.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- PostgREST RLS holds for anon: `profiles`+`chat_messages` return `[]`; column oracle works (42703 wrong column; 22P02 bad uuid = type confirmation) but rows gated. Other tables PGRST205. No public RPC (PGRST202).
- Email-enum oracles dead: password grant 400 uniform, recover always 200 `{}`, alg:none JWT rejected, admin API 403 `not_admin`.
- SMS OTP dead server-side (`500 Unable to get SMS provider`) — no SMS-pump vector. Email signup rate-limited (~60s).
- Realtime WS: handshake returns 401 BEFORE frame exchange (stronger gate than the CDN-passthrough 101 pattern).
- `/api/*` routes exist only on chat+platform hosts; api.gratisfy.xyz only serves `/v1/*` OpenAI-compat (nginx 404 text/html elsewhere — different origin stack; note the split).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
