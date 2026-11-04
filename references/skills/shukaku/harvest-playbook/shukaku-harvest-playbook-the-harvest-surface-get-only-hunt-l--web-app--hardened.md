# The harvest surface (GET-only, `hunt --live`) — web-app / hardened

- source canon: `shukaku/harvest-playbook.md`
- base technique: `shukaku-harvest-playbook-the-harvest-surface-get-only-hunt-l.md`
- bindings: **WSTG-INPV-05** · **CWE-89** · **ATT&CK T1190**
- context: **web-app** · auth **hardened** · chain role **final**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

backup archives (`backup.zip|tar.gz|sql`, `dump.sql`, `db.sqlite`…), env/config
leaks (`.env`, `.git/config`, `config.*.bak`), admin/admin-export paths,
`api/export(s)`, `debug/vars`, `server-status`. Data plane only — route probing is
UNDERCROFT's. 200s register CONFIRMED with body sizes; **nothing is downloaded**.

## Probe adjustment (web-app × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
