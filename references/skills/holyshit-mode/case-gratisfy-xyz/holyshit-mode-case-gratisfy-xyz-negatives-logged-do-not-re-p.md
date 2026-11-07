# Negatives (logged, do not re-probe without redeploy)

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- bindings: **WSTG-SESS-01** · **CWE-347** · **ATT&CK T1552**
- generated: 2026-11-04

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- PostgREST RLS holds for anon: `profiles`+`chat_messages` return `[]`; column oracle works (42703 wrong column; 22P02 bad uuid = type confirmation) but rows gated. Other tables PGRST205. No public RPC (PGRST202).
- Email-enum oracles dead: password grant 400 uniform, recover always 200 `{}`, alg:none JWT rejected, admin API 403 `not_admin`.
- SMS OTP dead server-side (`500 Unable to get SMS provider`) — no SMS-pump vector. Email signup rate-limited (~60s).
- Realtime WS: handshake returns 401 BEFORE frame exchange (stronger gate than the CDN-passthrough 101 pattern).
- `/api/*` routes exist only on chat+platform hosts; api.gratisfy.xyz only serves `/v1/*` OpenAI-compat (nginx 404 text/html elsewhere — different origin stack; note the split).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
