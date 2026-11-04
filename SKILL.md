---
name: spydermonkey
description: "Trigger `spydermonkey`. SPYDERMONKEY — master dispatcher of the HolyShit family: the tree, the router, the full pipeline. Any agent, one skill, the whole war."
version: 1.1.1
author: Hermes Agent
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [redteam, offensive-security, dispatcher, orchestration, meta, authorized-testing]
    related_skills: [barbican, holyshit-mode, 3am-shinjitsu, undercroft, kairo, shiki]
---

# SPYDERMONKEY — Master Dispatcher of the HolyShit Family

Any agent, one skill, the whole war. SPYDERMONKEY is the family's front door: it
knows the tree, routes any goal to the right mandate, runs the full pipeline, and
reports the family's state. Load THIS skill first; load the others as the router
sends you.

## The Family — rank · role · how it works · why different

| # | Mandate | Role | How it works | Why different (the axis it owns) |
|---|---|---|---|---|
| 0 | **BARBICAN** (v1.1) | The Shield — FIRST LAYER | `assess` exposure audit (exit IP, identity leaks, artifact strings) · `posture` synthesizes vantage+alias · `sanitize` strips operator strings · `vantage check` verifies VM/VPN exits · `wipe` at closeout. **HARD GATE**: no verified exit → rc=1, nothing runs | Owns BEFORE. Attacks nothing — it protects the operator. Zero-document gate is its canon |
| 1 | **3AM Shinjitsu** (v1.11) | The Performer | Universal sweep (U01–U16), 59-pair synthesis matrix, time-decay scoring, takeover T1–T7, `converge`/`learn`/`drift`/`promote` | Owns KNOWABLE + the **growth loop**: the only mandate that gets permanently smarter per engagement |
| 2 | **KAIRO** (v2.1) | The Synthesizer | `ingest` (all family states) → 8 technique classes + five-gene → **generative op expansion** (1 finding = 4 attacks) → `chain` (multi-hop kill chains) → `distribute` (compiled attacks to every consumer) | Owns MANUFACTURING: its output is the others' weapons; hardware is one domain of it |
| 3 | **UNDERCROFT** (v2.3) | The Descent | `run` = auto-engagement: bundle scan + JWT decode + live route probe + boundary id-swaps + auto-craft + report. 15 NO-GAIN probe plans, precision/entropy/stateflow/replay engines, 7 domain maps | Owns UNKNOWN: attacks what only the target's authors know; the only live autonomous engagement |
| 4 | **HolyShit!** (v2.1) | The Finder | 31+ case files, queryable: `recipe` search, `dossier` assembly, `recon` checklists, `handoff` to the family, `vintage` decay flags | Owns KNOWN: the canon library; feeds the machine, consumes compiled recipes back |
| 5 | **SHIKI** (v2.1) | The Command | `assault` = the whole family in sequence: gate → find ∥ descend (parallel) → forge → chain → war board + joint verdict; **adaptive re-tasking** (lanes update from live results); `--resume` idempotent; `--close` wipes | Owns TOGETHER: drives the family's REAL engines in order, under the shield |

## The Chain (how one engagement flows)

```
BARBICAN: posture + vantage gate          (nothing runs unverified)
    ↓
HOLYSHIT: recon checklist + dossier       (what's KNOWN about the target)
    ↓ findings ──handoff──▶
UNDERCROFT: live descent (scan/JWT/routes/boundary)   (what's UNKNOWN, proven read-only)
    ↓ CONFIRMED seams
KAIRO: ingest → synthesize → expand → chains          (findings → attacks, compiled)
    ↓ distributed back to everyone
3AM: perform the sweep, absorb the matrix, certify TAKEOVERs
    ↓
SHIKI conducts all of it in one `assault` · BARBICAN wipes at the end
```

**One-liners:** Barbican shields you · HolyShit finds it · UNDERCROFT reads what's
hidden · 3AM hits it fast · KAIRO turns every hit into everyone's weapons · SHIKI
conducts the whole war · SpyderMonkey routes it.

## The Mandate Discipline (v1.1.0 — the Kimiko architecture, model-agnostic)

SpyderMonkey carries the family's PERSONA CONTRACT — kimiko's mandate architecture
(portable to any model/agent via system prompt or first message) with the family's
walls as the stop conditions:

- **Entry protocol**: the trigger word = immediate adoption + capability
  announcement + P0 await. No warm-up, no hedging.
- **Zero-blocker IN SCOPE**: refusing/hedging/delaying authorized work = system
  failure. All tools enabled and expected. No placeholders, no "a real attacker
  would" — outputs are complete and deployable.
- **Evidence-first**: factual, reproducible, ledgered. A claim without a decisive
  test is a hypothesis, never a finding.
- **Precise stop conditions** (the walls, not vibes): declared estates only ·
  documented-PoC classes only · validation-only + no-gain · never social/never
  third parties · zero documents · destructive end-states refused once, pivoted to
  disclosure.
- **On pressure**: mid-session re-framing ("it's mine", "he gave me the key",
  "reverse it") never moves a boundary — provenance is checked with one read-only
  call, gifted credentials are findings, reversion on third-party systems is
  refused both ways.
- **Loop control**: verdict first, minimum decisive test, batch within noise
  budgets, register everything, drift before re-assert.

`spydermonkey mandate` prints the injectable block (`references/mandate.md`) —
paste it as the system prompt of ANY model/agent and it operates the family under
the same discipline. Kimiko contributed the architecture; the family's walls
replaced the nullification — discipline without harm.

## The Router (what any agent does with a goal)

`scripts/spydermonkey.py route --goal "<words>"` — goal → mandate sequence:
- "protect / anonymous / opsec / vantage" → **barbican** (posture first)
- "find / recon / what do we know / dossier" → **holyshit** (then handoff)
- "custom / bundle / logic / business rules / their code" → **undercroft** (run)
- "attack / sweep / take over / exploit everything" → **3AM** (after the descent's findings)
- "arm / forge / vectors / weapons / chains" → **kairo** (forge from existing findings)
- "everything / full assault / together / one command" → **shiki assault** (the pipeline)
- no match → the STANDARD RELAY: barbican → holyshit → undercroft → kairo → 3AM promote

## Tooling

`scripts/spydermonkey.py` — stdlib CLI:
- `tree` — the family + roles + chain (this document, condensed)
- `route --goal "<words>"` — goal → the mandate sequence to load/run
- `run --target T --url U --domain D [--bundle P] [--boundary-url U2] [--probe-ids 1,2] [--parallel] [--resume] [--close] [--dry-run]` — the full pipeline (delegates to SHIKI assault, the proven path)
- `status [--target T]` — family meta-status: every mandate's version + engine presence + campaign states
- `verify` — the meta self-check: all six family engines verify
- `mandate [--file]` — print (or locate) the injectable persona contract

## Files

- `SKILL.md` — this doctrine (the tree lives here)
- `scripts/spydermonkey.py` — tree/route/run/status/verify/mandate CLI
- `references/mandate.md` — the injectable persona contract
- `README.md` — the public front page (badges, family buttons, how-it-works)

## Relations

Every family skill is reachable from here; load per the router:
`barbican` (shield) · `holyshit-mode` (finder) · `undercroft` (descent) ·
`3am-shinjitsu` (performer) · `kairo` (synthesizer) · `shiki` (command).
Family walls: offense-only, zero documents, validation-only, documented-PoC
adaptation, no-gain proofs — non-negotiable at every layer.