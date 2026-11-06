# The harvest surface (GET-only, `hunt --live`) — mobile-api / low-priv

- source canon: `shukaku/harvest-playbook.md`
- base technique: `shukaku-harvest-playbook-the-harvest-surface-get-only-hunt-l.md`
- bindings: **WSTG-INPV-05** · **CWE-89** · **ATT&CK T1190**
- context: **mobile-api** · auth **low-priv** · chain role **final**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

backup archives (`backup.zip|tar.gz|sql`, `dump.sql`, `db.sqlite`…), env/config
leaks (`.env`, `.git/config`, `config.*.bak`), admin/admin-export paths,
`api/export(s)`, `debug/vars`, `server-status`. Data plane only — route probing is
UNDERCROFT's. 200s register CONFIRMED with body sizes; **nothing is downloaded**.

## Probe adjustment (mobile-api × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
