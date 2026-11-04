---
name: spydermonkey
description: "Trigger `spydermonkey`. SPYDERMONKEY — master dispatcher of the HolyShit family: the tree, the router, the full pipeline. Any agent, one skill, the whole war."
version: 3.0.0
author: Hermes Agent
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [redteam, offensive-security, dispatcher, orchestration, meta, authorized-testing]
    related_skills: [barbican, holyshit-mode, 3am-shinjitsu, undercroft, kairo, kaisha, shukaku, shiki, kage, dojo]
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
| 6 | **KAISHA** (v1.1) | The Ladder | `ladder --host H` builds R1–R5 from confirmed access: identity/surface inventories (read-only) → era-stack banner mapping → 4 privesc batteries (sudo/SUID/token-reuse/unit-trust) → lateral reuse plans (harvest-priced, one-shot, reversed) · `revert` records the reversal evidence — the no-persistence wall, machine-checked. **No persistence, no implants, NO-GAIN** | Owns DEPTH: everything below the foothold — what it can SEE and BECOME |
| 7 | **SHUKAKU** (v1.2) | The Harvester | `reason` (infer what SHOULD be harvestable from confirmed access) → `hunt` (read-only proofs: exact static probes or GET-only live surface probes) → `crown` register (evidence-chain enforced, ladder-priced) → `disclose` (6 playbook triggers) → `feed` (3AM vectors + undercroft surface + holyshit recipes → the loop closes) → `report`. Catalog-only: counts, never corpora | Owns AFTER/GAIN: turns compromises into business verdicts AND arms the family with what the harvest reveals |
| 8 | **KAGE** (v2.0) | The Mirror — the purple layer | `mirror --target C` — every CONFIRMED attack becomes a REAL Sigma rule (15 patterns · stable ids · falsepositives) · `export` writes .yml files · `validate` (rc=1 while any rule lacks live telemetry) · `refire` RE-FIRES the attack and requires the rule to fire (FIRED = purple loop closed) · `report` (the defense deliverable) | Owns DETECTABLE: the offense, proven visible — the family hands the defender the eyes |
| 9 | **DOJO** (v2.0) | The Range | `catalog`/`build --class C`/`bench --class C`/`teach --class C` — 15 buildable vulnerable replicas (BOUNDARY/REPLAY/HARVEST/TRAVERSAL/DIRECTORY/XSS/REDIRECT/CRYPTO/NETWORK/MASSASSIGN/INJECTION/SSRF/JWT/AUTHN/SESSION), lab-bound 127.0.0.1, every replica SELF-VERIFIES (bench strikes it and requires the flaw to confirm), each lesson ends in a kage rule | Owns TRAINING: the bench ground — where the family drills before it hunts |

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
    ↓ confirmed footholds
KAISHA: the ladder — era-stack · privesc rungs · lateral    (DEPTH below the foothold)
    ↓ what the depth reaches
SHUKAKU: crown register — catalog · price · disclose     (what the attacker GAINED)
    ↓ the P5 impact layer
KAGE: mirror every confirmed attack → detection rules · purple validation
    ↓ the defender gets the eyes
SHIKI conducts all of it in one `assault` · BARBICAN wipes at the end
```

**One-liners:** Barbican shields you · HolyShit finds it · UNDERCROFT reads what's
hidden · 3AM hits it fast · KAIRO turns every hit into everyone's weapons · KAISHA
climbs the ladder · SHUKAKU prices the gain · KAGE mirrors it · DOJO drills it ·
SHIKI conducts the whole war · SpyderMonkey routes it.

## The Scope Authority (v1.3.0 — the machine-checkable estate gate)

`spydermonkey scope init --engagement E --in-scope "acme.com,10.0.0.0/24"` writes
`~/.redteam/scope.json` — every live-probing engine (shiki gate · shukaku hunt
--live · the run pipeline) checks it BEFORE firing. Domain-suffix + CIDR matching,
default-deny, `--strict` mode closes everything undeclared:

```
$ spydermonkey scope check --value https://api.acme.com/x
✓ IN SCOPE — https://api.acme.com/x under engagement 'E'
$ spydermonkey scope check --value https://evil.com
✗ OUT OF SCOPE — https://evil.com is not in the declared estate     # rc=1
```

Also in the toolbox: `doctor` (full health check: engines · scope · corrupt states ·
canon stats) · `bench` (offline route-level accuracy — 11/11 at v1.8.0) · `arsenal`
(v1.6.0 — the execution layer: 13 scope-gated tool wrappers, findings canon-classified)
· `fleet` (v1.4.0 — parallel multi-agent dispatch, one agent per mandate) ·
`bench_live.py` (exploitation-level bench, localhost lab) · `mcp_server.py` (the
family as 12 MCP tools) · `skilltree.py` (722-file technique library).

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
- "harvest / crown / price / what could they take / disclose / impact" → **shukaku** (after confirmed compromises)
- "detect / mirror / detection / purple / sigma" → **kage** (confirmed attacks → detection rules)
- "train / range / replica / lab / lesson" → **dojo** (the range, before it hunts)
- "everything / full assault / together / one command" → **shiki assault** (the pipeline)
- no match → the STANDARD RELAY: barbican → holyshit → undercroft → kairo → 3AM → kaisha → shukaku → kage → dojo

## The Intelligence Layer (v3.0.0 — CyberStrike-derived, family-native)

The proven engines keep firing; the dispatcher now owns the engagement BRAIN
around them. Derived from CyberStrike's methodology engine, rewritten natively:
stdlib-only, walls as exit codes, scope authority default-deny, no-gain proofs.

- **`phases --target T`** — the 13-phase methodology board. Statuses are
  COMPUTED from real deliverables in the family's state files (never declared):
  `scope.json` exists → scope_analysis done; undercroft surface rows →
  active_recon; ledger has AUTHN findings → authentication_testing; and so on.
  Prerequisites gate the order; the board always names the next mandate to run.
- **`ledger add|list|show|triage`** — the finding ledger
  (`~/.redteam/campaigns/<c>/ledger.jsonl`). Every entry is scope-checked
  (an out-of-estate asset is REFUSED, rc=1), deduped by class+asset+normalized
  title (duplicate evidence attaches to the existing record — nothing is lost),
  and evidence-gated: proof needs `baseline: … attack: … diff: …`; anything less
  is DOWNGRADED to hypothesis conf=0.4 — never suppressed. `triage` runs the
  triager gates: severity-impact match, reproducible evidence, in-scope,
  duplicates → blocking violations exit 1.
- **`gate --url U --attack-query Q [--confirm TOKEN]`** — the 3-GATE
  CONFIRMATION engine: G1 baseline request → G2 attack request → G3 a
  measurable diff (status/length/body) AND the confirm token present. CONFIRMED
  findings register themselves; diff-without-token registers as hypothesis;
  identical responses register NOTHING (no speculation). `gate --prove SPY-NNN`
  replays the stored evidence.
- **`chain detect --target T`** — 8 chain patterns (credential_endpoint ·
  info_disclosure_ssrf · redirect_oauth · idor_data_leak · xss_csrf · ssti_rce ·
  race_business · custom): two low findings on the same origin combine into a
  high-impact kill chain with an expected-impact line and a testing plan. All
  walls preserved in the plans (arithmetic markers only, one reversible test).
- **`context set|show`** — the session context: endpoints · roles · credentials
  · functions. The shared map the testers strike from.
- **`testers --url U… | --demo`** — the 8 PARALLEL SUB-TESTERS (IDOR · AUTHZ
  · MASSASSIGN · INJECTION · AUTHN · BIZLOGIC · SSRF · FILEATTACK), each a
  differential probe with gate semantics, deduped into the ledger. `--demo`
  spins the built-in lab replica (127.0.0.1, self-terminating) so the layer
  proves itself with zero setup — 7/8 testers confirm on it out of the box.
- **`coverage --target T`** — phase × deliverable matrix, findings histogram,
  chain count, and the GAP LIST: what has NOT been tested, and which mandate
  closes it.
- **`report --target T`** — the joint WAR REPORT: exec summary (findings ·
  confirmed · severity mix), every finding with its 3-gate proof, attack
  chains, phase coverage, kage rule count, shukaku crown pricing — one markdown.
- **`relay init|list|exec|remove`** — REMOTE EXECUTION NODES (Bolt-equivalent):
  Ed25519 keypair per node (ssh-keygen), `ssh-copy-id` one-liner to pair, exec
  streams over ssh. Every exec scope-checks the node's host AND every
  host-like token in the command — out-of-estate → rc=1.
- **`mission --target T --url U --domain D`** — ONE COMMAND, THE WHOLE WAR:
  scope gate → fleet (10 agents parallel) → ledger triage → chain detect →
  coverage → war report (→ barbican wipe with --close).

**The live-fire rule (v3):** gate/testers fire at 127.0.0.1/localhost freely
(the lab — dojo replicas, CI). ANY other host requires a scope authority
containing it: no authority or out-of-scope → rc=1 refusal. `verify` now ends
with a LIVE GATE PROOF: it spins the lab replica, runs a real 3-gate
confirmation, and requires CONFIRMED — the engine is exercised, not asserted.

## The Scope Authority

`scope init` writes ~/.redteam/scope.json (the declared estate + rules); `scope
check --value` matches domains/CIDRs — default-deny with --strict. Every
live-probing engine honors it. `doctor` = the health check; `bench` = the offline
route-accuracy benchmark.

## Tooling

`scripts/spydermonkey.py` — stdlib CLI:
- `tree` — the family + roles + chain (this document, condensed)
- `route --goal "<words>"` — goal → the mandate sequence to load/run
- `run --target T --url U --domain D [--bundle P] [--boundary-url U2] [--probe-ids 1,2] [--parallel] [--resume] [--close] [--dry-run]` — the full pipeline (delegates to SHIKI assault, the proven path)
- `mission --target T --url U --domain D [--skip-fleet] [--close]` — v3 one command: fleet + the intelligence layer + the war report
- `phases --target T [--set-phase P --phase-status S]` — the 13-phase methodology board (computed from real deliverables)
- `ledger add|list|show|triage --target T` — the finding ledger (scope-blocked · deduped · evidence-gated)
- `gate --target T --url U --attack-query Q [--confirm TOK] [--prove SPY-NNN]` — the 3-gate confirmation engine
- `chain detect|plan --target T [--id CH-NNN]` — the 8-pattern chain detection engine
- `context set|show --target T [--kind K --value V]` — session context (endpoints · roles · credentials · functions)
- `testers --target T --url U [--url U2 …] | --demo` — the 8 parallel sub-testers
- `coverage --target T` — coverage matrix + gap list
- `report --target T [--output F]` — the joint war report
- `relay init|list|exec|remove` — remote execution nodes (Ed25519 ssh pairs, scope-gated)
- `status [--target T]` — family meta-status: every mandate's version + engine presence + campaign states + ledger counts
- `verify` — the meta self-check: all ten family engines verify + the LIVE gate proof
- `mandate [--file]` — print (or locate) the injectable persona contract
- `scope init|check|show` — the estate gate (`~/.redteam/scope.json`); default-deny with `--strict`
- `doctor` — full health check (engines · scope · corrupt states · canon · ledger · relays)
- `bench` — offline route-level benchmark (13/13 at v3.0.0)
- `arsenal list|plan|run|verify` — the execution layer: 13 tool wrappers (nmap · masscan · httpx · nuclei · gobuster · testssl · dnsx · subfinder · whatweb · wafw00f · nikto · dig · curl), scope-gated (rc=1 refusal), canon-classified
- `fleet --goal G --target T --domain D [--agents a,b]` — one agent per mandate, dispatched in PARALLEL

Companion scripts (stdlib too):
- `scripts/bench_live.py` — exploitation-level bench: stdlib vulnerable mini-targets on localhost, real engines scored
- `scripts/mcp_server.py` — the family as 18 MCP tools (stdio JSON-RPC); any MCP client drives it
- `scripts/skilltree.py` — regenerate `references/skills/` + `references/skilltree-index.md` from the family canon (722 technique files)

## Files

- `SKILL.md` — this doctrine (the tree lives here)
- `CHANGELOG.md` — release notes
- `scripts/spydermonkey.py` — the dispatcher CLI
- `scripts/arsenal.py` — the execution layer (13 scope-gated tool wrappers)
- `scripts/bench_live.py` — the exploitation-level bench
- `scripts/mcp_server.py` — the family as MCP tools (stdio JSON-RPC)
- `scripts/skilltree.py` — the technique-library generator
- `references/mandate.md` — the injectable persona contract
- `references/skilltree-index.md` + `references/skills/` — the 722-file technique library
- `README.md` — the public front page (badges, family buttons, how-it-works)

## Relations

Every family skill is reachable from here; load per the router:
`barbican` (shield) · `holyshit-mode` (finder) · `undercroft` (descent) ·
`3am-shinjitsu` (performer) · `kairo` (synthesizer) · `kaisha` (ladder) ·
`shukaku` (harvester) · `shiki` (command) · `kage` (mirror) · `dojo` (range).
Family walls: offense-only, zero documents, validation-only, documented-PoC
adaptation, no-gain proofs — non-negotiable at every layer.