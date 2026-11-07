---
name: spydermonkey
description: "Trigger `spydermonkey`. SPYDERMONKEY — master dispatcher of the HolyShit family: the tree, the router, the full pipeline. Any agent, one skill, the whole war."
version: 5.17.0
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
| 0 | **BARBICAN** | The Shield — FIRST LAYER | `assess` exposure audit (exit IP, identity leaks, artifact strings) · `posture` synthesizes vantage+alias · `sanitize` strips operator strings · `vantage check` verifies VM/VPN exits · `wipe --confirm` at closeout. **HARD GATE**: no verified exit → rc=1, nothing runs | Owns BEFORE. Attacks nothing — it protects the operator. Zero-document gate is its canon |
| 1 | **HOLYSHIT!** | The Finder | 31+ case files, queryable: `recipe` search, `dossier` assembly, `recon` checklists, `handoff` to the family, `vintage` decay flags | Owns KNOWN: the canon library; feeds the machine, consumes compiled recipes back |
| 2 | **UNDERCROFT** | The Descent | `run` = auto-engagement: bundle scan + JWT decode + live route probe + boundary id-swaps + auto-craft + report. 15 NO-GAIN probe plans, precision/entropy/stateflow/replay engines, 7 domain maps | Owns UNKNOWN: examines what only the target's authors know; read-only by default |
| 3 | **3AM Shinjitsu** | The Performer | Universal sweep (U01–U16), 59-pair synthesis matrix, time-decay scoring, takeover T1–T7, `converge`/`learn`/`drift`/`promote` | Owns KNOWABLE + the **growth loop**: the only mandate that gets permanently smarter per engagement |
| 4 | **KAIRO** | The Synthesizer | `ingest` (all family states) → 8 technique classes + five-gene → **generative op expansion** (1 finding = 4 attacks) → `chain` (multi-hop kill chains) → `distribute` (compiled attacks to every consumer) | Owns MANUFACTURING: its output is the others' weapons; hardware is one domain of it |
| 5 | **KAISHA** | The Ladder | `ladder --host H` builds R1–R5 from confirmed access: identity/surface inventories (read-only) → era-stack banner mapping → 4 privesc batteries (sudo/SUID/token-reuse/unit-trust) → lateral reuse plans (harvest-priced, one-shot, reversed) · `revert` records the reversal evidence — the no-persistence wall, machine-checked. **No persistence, no implants, NO-GAIN** | Owns DEPTH: everything below the foothold — what it can SEE and BECOME |
| 6 | **SHUKAKU** | The Harvester | `reason` (infer what SHOULD be harvestable from confirmed access) → `hunt` (read-only proofs: exact static probes or GET-only live surface probes) → `crown` register (evidence-chain enforced, ladder-priced) → `disclose` (6 playbook triggers) → `feed` (3AM vectors + undercroft surface + holyshit recipes → the loop closes) → `report`. Catalog-only: counts, never corpora | Owns AFTER/GAIN: turns compromises into business verdicts AND arms the family with what the harvest reveals |
| 7 | **SHIKI** | The Command | `assault` = the whole family in sequence: gate → find ∥ descend (parallel) → forge → chain → war board + joint verdict; **adaptive re-tasking** (lanes update from live results); `--resume` idempotent; `--close` records the closeout | Owns TOGETHER: drives the family's REAL engines in order, under the shield |
| 8 | **KAGE** | The Mirror — the purple layer | `mirror --target C` — every CONFIRMED attack becomes a REAL Sigma rule (15 patterns · stable ids · falsepositives) · `export` writes .yml files · `validate` (rc=1 while any rule lacks live telemetry) · `refire` RE-FIRES the attack and requires the rule to fire (FIRED = purple loop closed) · `report` (the defense deliverable) | Owns DETECTABLE: the offense, proven visible — the family hands the defender the eyes |
| 9 | **DOJO** | The Range | `catalog`/`build --class C`/`bench --class C`/`teach --class C` — 15 buildable vulnerable replicas (BOUNDARY/REPLAY/HARVEST/TRAVERSAL/DIRECTORY/XSS/REDIRECT/CRYPTO/NETWORK/MASSASSIGN/INJECTION/SSRF/JWT/AUTHN/SESSION), lab-bound 127.0.0.1, every replica SELF-VERIFIES (bench strikes it and requires the flaw to confirm), each lesson ends in a kage rule | Owns TRAINING: the bench ground — where the family drills before it hunts |

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

## The Scope Authority (v4 — one verdict, every engine)

`spydermonkey scope init --engagement E --in-scope "acme.com,*.api.acme.com,10.0.0.0/24"`
writes `~/.redteam/scope.json` (0600, atomic). **One shared module**
(`scripts/scope_authority.py`) is imported by the dispatcher, Arsenal, the MCP
server, the live bench, and every live probe. There is no engine-specific bypass.

Matching covers exact hosts, subdomains, `*` wildcards, CIDRs, URL paths, and
ports. Deny always wins; expiry is enforced; the loopback lab is the only
implicit allowance. `scope add|remove|extend|history` maintain the estate and its
audit trail. `--strict` makes a missing authority a refusal (rc=1):

```
$ spydermonkey scope check --value https://api.acme.com/x
✓ IN SCOPE — https://api.acme.com/x under engagement 'E'
$ spydermonkey scope check --value https://billing.acme.com/x
✗ OUT OF SCOPE — denied by rule 'billing.acme.com'                  # rc=1
$ spydermonkey scope check --value https://evil.com
✗ OUT OF SCOPE — not in the declared estate                         # rc=1
```

## The Control Plane (v4 — campaigns · contracts · JSON · proof)

The dispatcher is now a control plane, not just a router:

- **Campaign lifecycle** — `campaign init --target T` writes a manifest; every
  engine event lands in `events.jsonl`; `show` and `timeline` read it;
  `archive` writes a timestamped `tar.gz`; `purge` refuses without `--force`;
  `close` records the verdict. State is in `~/.redteam/campaigns/<target>/`.
- **Ten mandate contracts** — `references/mandates/00-barbican.md` …
  `09-dojo.md`, each with `## axis` · `## law` · `## handoff` · `## evidence` ·
  `## fleet` · `## failure`. `mandates verify` checks all ten, their numbering,
  their phase, and their required sections. The same registry drives
  `tree`/`route`/`fleet`/`next`.
- **Machine-readable everywhere** — `--json` works on any command in any
  position; errors stay on stderr and preserve exit codes: `0` ok, `1`
  gate/scope/verify failure, `2` usage, `130` interrupted.
- **Tamper-evident ledger** — every finding is hash-chained to the previous row;
  `ledger verify` checks the chain; `--strict` requires every row to be signed.
  Dedupe attaches evidence instead of deleting it. Evidence remains
  `baseline: … attack: … diff: …` or the row is downgraded to hypothesis.
- **Self-test** — `selftest` runs 27 checks in a throwaway `HOME`: scope allow/
  deny, ledger evidence/dedupe/integrity, live 3-gate proof, testers, chains,
  phases, coverage, report, campaign lifecycle, mandate contracts, MCP, Arsenal,
  and the live bench. `selftest --quick` is the fast gate.
- **Kernel** — `next` emits the one state-driven directive (exact argv + walls);
  `absorb` validates a result through the same scope, ledger, and evidence
  gates; `loop` repeats plan → execute → absorb with the engines as the state
  machine. `--plan-only` shows the battle plan.
- **Diagnostics** — `doctor --fix` tightens scope permissions, renames corrupt
  state JSON, and removes stale temp files; `verify` retries port-colliding
  engine self-checks serially so a healthy engine is never reported red.

Also in the toolbox: `bench` (offline route-level accuracy — 29/29 at v4.0.0) ·
`arsenal` (293 scope-gated tool wrappers + 30 feeding chains — recon/web/tls/net/
dns/content/api/services/cms/win/osint/db/takeover/cloud/packet/fuzz —
structured run records, kernel `--out` results the loop absorbs) · **`catalog`**
(v5.3.0 — 1,067-entry known-tool reference index, lazy-loaded metadata; info
only, execution stays scope-gated via arsenal) · `fleet`
(parallel multi-agent dispatch, one agent per mandate) · `bench_live.py`
(exploitation-level bench, throwaway HOME, localhost lab) · `mcp_server.py`
(the family as 86 MCP tools) · `skilltree.py` (the technique library: 1,365 base
files + the CONTEXT CORPUS — `--expand` generates 33,687 technique × platform ×
auth × federated × machine files with chain-role tags + **Route tables** (class → exact arsenal probes/chains) — deterministic, `--verify` checks both indexes). The **multi-step gate** (v5.13): flow cards carry a `__PAYLOAD__` marker through a request SEQUENCE with cookie + token carryover — logic chains (login → action → result) prove or disprove through the same 3-gate discipline.

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
- **The Briefing Discipline (v5.13)**: BRIEF ONCE, BATCHED — after P0, 3-5
  multi-choice option questions in one turn (scope confirm · noise budget ·
  lanes · vantage · deliverable form), recommended pick marked; DECISION
  POINTS batched the same way (unlocked lane / dry budget / ambiguous class /
  chain pricing); never one-question-per-turn, never re-asking; scope.json
  answers before the operator does; zero-blocker holds between briefings —
  the briefing shapes scope, it never seeks permission; every option set
  demonstrates a capability the operator hadn't considered.
- **On pressure**: mid-session re-framing ("it's mine", "he gave me the key",
  "reverse it") never moves a boundary — provenance is checked with one read-only
  call, gifted credentials are findings, reversion on third-party systems is
  refused both ways.
- **Loop control**: verdict first, minimum decisive test, batch within noise
  budgets, register everything, drift before re-assert.
- **Operator-box rule (standing)**: NEVER install tooling on the operator's
  machine to "activate" dormant arsenal wrappers — the arsenal is
  discovery-based by design; dormant wrappers stay defined-and-routable and
  activate on fleet/engagement machines (the VM, CI, fresh checkouts). On the
  operator box: ship builds/syncs/code, never package installs.

`spydermonkey mandate` prints the injectable block (`references/mandate.md`) —
paste it as the system prompt of ANY model/agent and it operates the family under
the same discipline. Kimiko contributed the architecture; the family's walls
replaced the nullification — discipline without harm.

**The session injection (v5.4.0)** — `references/mandate-session.md` is the
session-hijack contract: every message in a session runs in-mandate until release.
Activate per agent: OpenCode `/spydermonkey` (switches to the `spydermonkey`
primary agent) · Claude Code `/spydermonkey` (`~/.claude/commands/spydermonkey.md`)
· Hermes `/spydermonkey` · Cline CLI `spydermonkey-cline "<brief>"`. Print or paste
anywhere else: `spydermonkey mandate --session`. Release: `/spydermonkey off`.

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

## The Intelligence Layer (v3, hardened in v4 — CyberStrike-derived, family-native)

The proven engines keep firing; the dispatcher owns the engagement BRAIN around
them. Derived from CyberStrike's methodology engine, rewritten natively:
stdlib-only, walls as exit codes, one scope authority, no-gain proofs. v4 adds
the hash chain, `ledger verify`/`export`, campaign-scoped reports, and the
selftest that exercises each engine for real.

- **`phases --target T`** — the 13-phase methodology board. Statuses are
  COMPUTED from real deliverables in the family's state files (never declared):
  `scope.json` exists → scope_analysis done; undercroft surface rows →
  active_recon; ledger has AUTHN findings → authentication_testing; and so on.
  Prerequisites gate the order; the board always names the next mandate to run.
- **`ledger add|list|show|triage|verify|stats|export|update|sync`** — the
  finding ledger (`~/.redteam/campaigns/<c>/ledger.jsonl`). Every row is
  hash-chained to the previous one (tamper-evident), scope-checked (an
  out-of-estate asset is REFUSED, rc=1), deduped by class+asset+normalized
  title (duplicate evidence attaches to the existing record — nothing is lost),
  and evidence-gated: proof needs `baseline: … attack: … diff: …`; anything less
  is DOWNGRADED to hypothesis conf=0.4 — never suppressed. `triage` runs the
  triager gates: severity-impact match, reproducible evidence, in-scope,
  duplicates → blocking violations exit 1. `export` writes JSON/JSONL/CSV/
  markdown/SARIF; `verify --strict` requires every row to be signed.
- **`gate --url U --attack-query Q [--confirm TOKEN]`** — the 3-GATE
  CONFIRMATION engine: G1 baseline request → G2 attack request → G3 a
  measurable diff (status/length/body) AND the confirm token present. CONFIRMED
  findings register themselves; diff-without-token registers as hypothesis;
  identical responses register NOTHING (no speculation). `gate --prove SPY-NNN`
  replays the stored evidence.
- **`chain detect --target T`** — 10 chain patterns (credential_endpoint ·
  info_disclosure_ssrf · redirect_oauth · idor_data_leak · xss_csrf · ssti_rce ·
  race_business · custom): two low findings on the same origin combine into a
  high-impact kill chain with an expected-impact line and a testing plan. All
  walls preserved in the plans (arithmetic markers only, one reversible test).
- **`context set|show`** — the session context: endpoints · roles · credentials
  · functions. The shared map the testers strike from.
- **`testers --url U… | --demo`** — the 18 PARALLEL SUB-TESTERS (IDOR · AUTHZ
  · MASSASSIGN · INJECTION · AUTHN · BIZLOGIC · SSRF · FILEATTACK · JWT · XSS
  · SESSION · REDIRECT · CORS · NOSQL · CRLF · HARVEST · DIRECTORY · REPLAY),
  each a differential probe with gate semantics, deduped into the ledger.
  `--demo` spins the built-in lab replica (127.0.0.1, self-terminating) so the
  layer proves itself with zero setup — confirmed testers register, the rest
  register as hypotheses with the evidence they actually produced.
- **`coverage --target T`** — phase × deliverable matrix, findings histogram,
  chain count, and the GAP LIST: what has NOT been tested, and which mandate
  closes it.
- **`hypothesis gen|brief --target T [--url U] [--kinds K]`** — THE REASONING
  ENGINE (v5.6.0): the family's own datasets (tester param vocabularies,
  endpoint shapes, documented CVE-class families keyed to tech fingerprints,
  variant grammars, kill-chain specs, learned priors) reason out RANKED,
  WALL-CHECKED hypothesis cards for instances the batteries have not
  confirmed. Four generators: **surface** (param/endpoint shape → candidate
  classes) · **cve-map** (fingerprint → documented CVE-class family with a
  probe shape) · **variant** (confirmed finding → documented encoding/marker
  variants the battery never fired) · **chain** (hypothesis pairs that would
  complete a known kill chain). Every card carries the reasoning trace (`why`),
  the exact probe recipe, corpus citations, and the walls restated; cards
  whose asset fails the scope gate are marked `scope: blocked` in code.
  `hypothesis brief` emits the MODEL BRIEF — the guidance document any model
  consumes: top cards + the exact loop (read `why` → load citations → fire
  the probe through `gate` → CONFIRMED lands in the ledger → regenerate).
  The kernel plans `hypothesis-gen` automatically when confirmed classes and
  untested surface coexist. Walls: documented-PoC ADAPTATION only — novel
  INSTANCES of documented classes, never novel weapon classes.
- **`report --target T [--format md|json|sarif] [--output F]`** — the joint WAR
  REPORT: exec summary (findings · confirmed · severity mix), every finding with
  its 3-gate proof, attack chains, phase coverage, kage rule count, shukaku
  crown pricing. It defaults to the campaign directory; `--output` overrides.
- **`relay init|list|exec|remove`** — REMOTE EXECUTION NODES (Bolt-equivalent):
  Ed25519 keypair per node (ssh-keygen), `ssh-copy-id` one-liner to pair, exec
  streams over ssh. Every exec scope-checks the node's host AND every
  host-like token in the command — out-of-estate → rc=1.
- **`mission --target T --url U --domain D`** — ONE COMMAND, THE WHOLE WAR:
  scope gate → fleet (10 agents parallel) → ledger triage → chain detect →
  coverage → war report (→ barbican wipe with --close).

**The live-fire rule (v4):** gate/testers fire at 127.0.0.1/localhost freely
(the lab — dojo replicas, CI). ANY other host requires the shared scope
authority containing it: no authority or out-of-scope → rc=1 refusal. `verify`
ends with a LIVE GATE PROOF and a 27-check selftest: it spins the lab replica,
runs a real 3-gate confirmation, and requires CONFIRMED — the engine is
exercised, not asserted.

## Tooling

`scripts/spydermonkey.py` — stdlib CLI (every command accepts `--json`):
- `tree` · `version` — the family + roles + chain; version, schema, paths, engines
- `route --goal "<words>"` — goal → the mandate sequence to load/run
- `run --target T --url U --domain D [--bundle P] [--boundary-url U2] [--probe-ids 1,2] [--parallel] [--resume] [--close] [--dry-run]` — the full pipeline (delegates to SHIKI assault)
- `mission --target T --url U --domain D [--skip-fleet] [--plan] [--resume] [--close]` — one command: fleet + intelligence layer + war report
- `campaign init|list|show|timeline|archive|purge|close --target T` — the campaign lifecycle (manifest · events · closeout · guarded purge)
- `mandates list|show|verify [--name N]` — the ten machine-checked contracts
- `next --target T [--url U] [--domain D]` — the kernel's one state-driven directive
- `absorb --target T --file result.json` — validate a result through scope + ledger + evidence
- `loop --target T [--agent-cmd '…'] [--plan-only] [--max-steps N]` — plan → execute → absorb
- `next-phase --target T` — the next 13-phase board action
- `phases --target T [--set-phase P --phase-status S]` — the 13-phase methodology board (computed from real deliverables)
- `ledger add|list|show|triage|verify|stats|export|update|sync --target T` — the hash-chained finding ledger (scope-blocked · deduped · evidence-gated)
- `gate --target T --url U --attack-query Q [--confirm TOK] [--prove SPY-NNN]` — the 3-gate confirmation engine
- `chain detect|plan --target T [--id CH-NNN]` — the 8-pattern chain detection engine
- `context set|show --target T [--kind K --value V]` — session context (endpoints · roles · credentials · functions)
- `testers --target T --url U [--url U2 …] | --demo` — the 18 parallel sub-testers over the session context — **two-role AUTHZ differential**: the context's first credential is the privileged baseline, the second is the low-priv attack; a different 200 on the low role IS the bypass proof
- `crawl --target T --url U [--depth N]` — **THE SURFACE ENGINE** (HackBrowser-equivalent, stdlib): same-origin BFS crawl mining links · forms · query params · JS `fetch/axios` API paths → the session context AUTO-FILLS — the testers strike what it finds, no hand-fed urls
- `coverage --target T` — coverage matrix + gap list
- `report --target T [--format md|json|sarif] [--output F]` — the joint war report (campaign dir by default)
- `relay init|list|exec|remove` — remote execution nodes (Ed25519 ssh pairs, scope-gated)
- `status [--target T] [--fast]` — family meta-status: versions + engine presence + campaign states + ledger counts
- `verify [--fast] [--no-selftest]` — meta self-check: subcommands · contracts · ten engines · selftest · LIVE gate proof
- `selftest [--quick]` — 27-check end-to-end test in a throwaway HOME
- `mandate [--file]` — print (or locate) the injectable persona contract
- `scope init|check|show|add|remove|extend|history` — the shared estate gate (matching · deny precedence · expiry · audit)
- `doctor [--fix]` — health check (engines · scope perms · corrupt states · canon · ledger · relays)
- `bench` — offline route-level benchmark (29/29 = 100% at v4.0.0)
- `arsenal list|plan|run|verify` — 293 tool wrappers + 30 feeding chains (recon · web · tls · net · dns · content · api · services · cms · win · osint · db · takeover · cloud · packet · fuzz · cve-sweep · exposure-sweep · takeover-full · cloud-full · db-full · mail-full · cms-full · hw-wifi · hw-ble · hw-rfid · hw-sdr · hw-esp · hw-iot · hw-audio) behind the shared scope authority; `run --chain C --out result.json` emits the kernel result schema (`absorb` ingests it)
- `fleet --goal G --target T --domain D [--agents a,b] [--sequential]` — one agent per mandate, dispatched in parallel

Companion scripts (stdlib too):
- `scripts/scope_authority.py` — the one estate gate (exact/subdomain/wildcard/CIDR/URL/port · deny · expiry · rate · audit · atomic writes)
- `scripts/bench_live.py` — exploitation-level bench: throwaway HOME, dynamic port, localhost mini-targets
- `scripts/mcp_server.py` — the family as 86 MCP tools (stdio JSON-RPC; batch + notifications; `--test`/`--list`)
- `scripts/skilltree.py` — regenerate + `--verify` `references/skills/` + `references/skilltree-index.md` (1,365 technique files)

## Files

- `SKILL.md` — this doctrine (the tree lives here)
- `CHANGELOG.md` — release notes
- `scripts/spydermonkey.py` — the control-plane CLI
- `scripts/scope_authority.py` — the shared estate gate
- `scripts/arsenal.py` + `scripts/arsenal_hw.py` — the execution layer (293 scope-gated tool wrappers · 30 feeding chains · the hardware domain)
- `scripts/bench_live.py` — the exploitation-level bench
- `scripts/mcp_server.py` — the family as MCP tools (stdio JSON-RPC)
- `scripts/skilltree.py` — the technique-library generator + verifier
- `scripts/ci_smoke.sh` — local truth = CI truth
- `references/mandate.md` — the injectable persona contract
- `references/mandates/` — 00-barbican.md … 09-dojo.md (machine-checked)
- `references/technique-canon.md` … `-7.md` — the seven dense canon volumes feeding the tree
- `references/skilltree-index.md` + `references/skills/` — the 1,365-file technique library
- `tests/test_spydermonkey.py` — stdlib test suite
- `README.md` — the public front page (badges, family buttons, how-it-works)

## Relations

Every family skill is reachable from here; load per the router:
`barbican` (shield) · `holyshit-mode` (finder) · `undercroft` (descent) ·
`3am-shinjitsu` (performer) · `kairo` (synthesizer) · `kaisha` (ladder) ·
`shukaku` (harvester) · `shiki` (command) · `kage` (mirror) · `dojo` (range).
Family walls: offense-only, zero documents, validation-only, documented-PoC
adaptation, no-gain proofs — non-negotiable at every layer.