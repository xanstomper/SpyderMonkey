# Negatives (logged, do not re-probe without redeploy) — mobile-api / low-priv

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- base technique: `holyshit-mode-case-gratisfy-xyz-negatives-logged-do-not-re-p.md`
- bindings: **WSTG-SESS-01** · **CWE-347** · **ATT&CK T1552**
- context: **mobile-api** · auth **low-priv** · chain role **pivot**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- PostgREST RLS holds for anon: `profiles`+`chat_messages` return `[]`; column oracle works (42703 wrong column; 22P02 bad uuid = type confirmation) but rows gated. Other tables PGRST205. No public RPC (PGRST202).
- Email-enum oracles dead: password grant 400 uniform, recover always 200 `{}`, alg:none JWT rejected, admin API 403 `not_admin`.
- SMS OTP dead server-side (`500 Unable to get SMS provider`) — no SMS-pump vector. Email signup rate-limited (~60s).
- Realtime WS: handshake returns 401 BEFORE frame exchange (stronger gate than the CDN-passthrough 101 pattern).
- `/api/*` routes exist only on chat+platform hosts; api.gratisfy.xyz only serves `/v1/*` OpenAI-compat (nginx 404 text/html elsewhere — different origin stack; note the split).

## Probe adjustment (mobile-api × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
