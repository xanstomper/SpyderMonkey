# 3.4 Mass-assignment (score 80) — linux / guest

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- base technique: `3am-shinjitsu-arsenal-03-api-3-4-mass-assignment-score-80.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **linux** · auth **guest** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: read-only inventory first (kaisha rungs), then the documented class match
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- DECISIVE: signup/write with `data:{role:"admin",is_admin:true,tier:"enterprise",balance:999999}`.
- THE GATE (3 targets confirmed negative): persistence into `user_metadata`/JWT ≠ escalation.
  Exploitability = does ANY backend authorize on the planted key? Check the real table read +
  RLS `auth.jwt()->>'sub'` scoping + DTO discard. Persisted-but-untrusted = hardening note ~55.
- PostgREST UPDATE discriminator: 204 ≠ rows changed — send
  `Prefer: return=representation,count=exact`, read `content-range: */0` = ZERO rows. INSERT
  blocks = `42501`.

## Probe adjustment (linux × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
