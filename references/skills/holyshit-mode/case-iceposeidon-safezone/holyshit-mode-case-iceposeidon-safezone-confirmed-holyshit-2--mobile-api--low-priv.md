# CONFIRMED HOLYSHIT #2 — hidden-layer tactical intel via plain REST (score 85) — mobile-api / low-priv

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- base technique: `holyshit-mode-case-iceposeidon-safezone-confirmed-holyshit-2.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **mobile-api** · auth **low-priv** · chain role **pivot**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

`GET /event/contestants` (unauth) exposes what the public map does NOT render: exact HP/maxHP of every remaining player, full inventories (EMPs, invisibility cloaks, machetes, guardian angels), active effects (mirror_forcefield, shield, invisible), live-on-Kick flag, last_damaged_at timestamps. Cause: `stats_visible: true` in event config broadcasts the hidden layer. `/event/config` dumps full game rules (nuke 300m target/100m blast/20dmg/60s, c4, poison, trade rules, zombie counts).

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
