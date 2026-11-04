# CONFIRMED HOLYSHIT #2 — hidden-layer tactical intel via plain REST (score 85)

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

`GET /event/contestants` (unauth) exposes what the public map does NOT render: exact HP/maxHP of every remaining player, full inventories (EMPs, invisibility cloaks, machetes, guardian angels), active effects (mirror_forcefield, shield, invisible), live-on-Kick flag, last_damaged_at timestamps. Cause: `stats_visible: true` in event config broadcasts the hidden layer. `/event/config` dumps full game rules (nuke 300m target/100m blast/20dmg/60s, c4, poison, trade rules, zombie counts).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
