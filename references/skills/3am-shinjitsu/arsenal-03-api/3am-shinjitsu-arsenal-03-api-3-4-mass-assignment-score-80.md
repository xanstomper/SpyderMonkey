# 3.4 Mass-assignment (score 80)

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- DECISIVE: signup/write with `data:{role:"admin",is_admin:true,tier:"enterprise",balance:999999}`.
- THE GATE (3 targets confirmed negative): persistence into `user_metadata`/JWT ≠ escalation.
  Exploitability = does ANY backend authorize on the planted key? Check the real table read +
  RLS `auth.jwt()->>'sub'` scoping + DTO discard. Persisted-but-untrusted = hardening note ~55.
- PostgREST UPDATE discriminator: 204 ≠ rows changed — send
  `Prefer: return=representation,count=exact`, read `content-range: */0` = ZERO rows. INSERT
  blocks = `42501`.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
