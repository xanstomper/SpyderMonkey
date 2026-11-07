<div align="center">

<img src="assets/spyder.gif" alt="SPYDERMONKEY — the spider at the center of the web" width="640"/>

# 🕷️ SPYDERMONKEY

### *Any agent. One skill. The whole war.*

**The self-improving master dispatcher of the HolyShit offensive-security family —
the tree, the router, the autonomous kernel, the published benchmarks, and the full
engagement pipeline in one stdlib-only CLI.**

[![Version](https://img.shields.io/badge/version-5.17.0-blueviolet?style=for-the-badge)](#the-cli)
[![Python](https://img.shields.io/badge/python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](#quickstart)
[![Platform](https://img.shields.io/badge/platform-Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](#quickstart)
[![Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen?style=for-the-badge)](#why-its-so-powerful)
[![Corpus](https://img.shields.io/badge/skill%20corpus-33%2C687%20files-blue?style=for-the-badge)](#the-skill-corpus-11683-files)
[![Self-play](https://img.shields.io/badge/self--play-14%2F14%20classes-success?style=for-the-badge)](#training--the-selfplay-loop)
[![Bench](https://img.shields.io/badge/benchmark-100%25%20self%20·%2090.6%25%20cross--range-orange?style=for-the-badge)](#the-benchmarks)
[![MCP](https://img.shields.io/badge/MCP-86%20tools-9146FF?style=for-the-badge)](#mcp--50-tools-for-every-client)
[![Discipline](https://img.shields.io/badge/discipline-model--agnostic%20·%20any%20LLM-9146FF?style=for-the-badge)](#the-mandate-discipline)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)
[![CI](https://github.com/xanstomper/spydermonkey/actions/workflows/verify.yml/badge.svg)](https://github.com/xanstomper/spydermonkey/actions/workflows/verify.yml)
[![Use](https://img.shields.io/badge/use-AUTHORIZED%20TARGETS%20ONLY-crimson?style=for-the-badge)](#the-walls-non-negotiable)

**THE FAMILY** — ten mandates, one axis each, one click away:

[![00 BARBICAN · the shield](https://img.shields.io/badge/00-BARBICAN%20·%20the%20shield-2E4057?style=for-the-badge)](https://github.com/xanstomper/barbican)
[![01 HOLYSHIT · the finder](https://img.shields.io/badge/01-HOLYSHIT%20·%20the%20finder-B8860B?style=for-the-badge)](https://github.com/xanstomper/HolyShit)
[![02 UNDERCROFT · the descent](https://img.shields.io/badge/02-UNDERCROFT%20·%20the%20descent-4B0082?style=for-the-badge)](https://github.com/xanstomper/undercroft)
[![03 3AM · the performer](https://img.shields.io/badge/03-3AM%20·%20the%20performer-8B0000?style=for-the-badge)](https://github.com/xanstomper/3am-shinjitsu)
[![04 KAIRO · the synthesizer](https://img.shields.io/badge/04-KAIRO%20·%20the%20synthesizer-6B8E23?style=for-the-badge)](https://github.com/xanstomper/kairo)
[![05 KAISHA · the ladder](https://img.shields.io/badge/05-KAISHA%20·%20the%20ladder-704214?style=for-the-badge)](https://github.com/xanstomper/kaisha)
[![06 SHUKAKU · the harvester](https://img.shields.io/badge/06-SHUKAKU%20·%20the%20harvester-8B4513?style=for-the-badge)](https://github.com/xanstomper/shukaku)
[![07 SHIKI · the command](https://img.shields.io/badge/07-SHIKI%20·%20the%20command-111111?style=for-the-badge)](https://github.com/xanstomper/shiki)
[![08 KAGE · the mirror](https://img.shields.io/badge/08-KAGE%20·%20the%20mirror-3A3A3A?style=for-the-badge)](https://github.com/xanstomper/kage)
[![09 DOJO · the range](https://img.shields.io/badge/09-DOJO%20·%20the%20range-4a5d23?style=for-the-badge)](https://github.com/xanstomper/dojo)

[How it works](#how-it-works) · [The kernel](#the-kernel--model-in-the-loop-inverted) ·
[The numbers](#the-numbers--all-measured) · [Benchmarks](#the-benchmarks) ·
[Training](#training--the-selfplay-loop) · [Remediation](#remediate--the-fix-loop) ·
[Self-knowledge](#capabilities--the-mirror-of-self) · [Self-protection](#protect--the-mirror-turned-around) ·
[Quickstart](#quickstart) · [The CLI](#the-cli) · [Architecture](#architecture) ·
[Comparison](#how-it-compares) · [The Walls](#the-walls-non-negotiable)

</div>

---

## What is this?

SPYDERMONKEY is the spider at the center of the web. Around it, ten specialized
offensive-security mandates — the **HolyShit family** — each owning exactly one
axis of an engagement. None of them overlap. All of them compose.

SPYDERMONKEY is the piece that knows the whole tree:

- **routes** any goal, in plain words, to the right mandate sequence,
- **runs** the full pipeline end-to-end with one command,
- **owns the CONTROL PLANE** (v4): one shared scope authority, campaign lifecycle,
  the ten machine-checkable mandate contracts, tamper-evident ledgers, JSON on every
  command, and an end-to-end self-test,
- **owns the INTELLIGENCE LAYER** (v3): the 13-phase methodology board, the finding
  ledger with triager gates, the 3-gate confirmation engine, the differential
  testers, the chain detector, coverage, the war report, and remote execution nodes,
- **drives the KERNEL** (v4): `next` emits the one state-driven directive, `absorb`
  validates a result through the same gates, and `loop` runs the plan → execute →
  absorb cycle with the engines as the state machine — **model-optional**,
- **KNOWS ITSELF** (v5): `capabilities` introspects the live registry — engines,
  classes, battery sizes, executors, corpus, learned priors,
- **KNOWS THE KNOWN-TOOL LANDSCAPE** (v5.3.0): `catalog stats|categories|list|search|show`
  — a 1,053-entry lazy-loaded reference index of known offensive tools; inventory,
  not execution — firing anything still goes through `arsenal` (scope-gated),
- **PROTECTS THE OPERATOR** (v5): `protect` inventories what the machine can leak
  and scans every campaign artifact for operator strings — rc=1 while anything leaks,
- **TRAINS ITSELF** (v5): `train` self-plays against the family's live range and
  writes per-class priors the planner uses to order probes,
- **REMEMBERS EVERY ESTATE** (v5): `memory` keeps what the family confirmed per
  target and re-ranks future planning with it,
- **FIXES WHAT IT FINDS** (v5.2): `remediate` ships the recipe and re-proves the
  differential post-fix — VERIFIED only when the differential stops confirming,
- **reports** the family's state (versions, engines, campaign states),
- **carries the persona contract** that puts ANY model under the family's discipline.

Load this skill first; load the others as the router sends you.

---

## How it works

### 1. The chain — how one engagement flows

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

### 2. The router — plain words in, mandate sequence out

```
$ python3 scripts/spydermonkey.py route --goal "protect my ass"
▸ goal: 'protect my ass'
  → load + run, in order: barbican
  command: barbican posture --target <t> --vantage vm --alias <alias>   (FIRST)
  always: barbican posture BEFORE, barbican wipe AFTER (closeout)
```

| Your goal contains… | The dispatcher sends |
|---|---|
| protect · opsec · anonymous · vantage | **barbican** — posture first, always |
| find · recon · dossier · known | **holyshit** — then handoff to the descent |
| custom · bundle · logic · business · their code | **undercroft** — live auto-engagement |
| attack · sweep · take over · exploit | **3AM** — the universal sweep |
| arm · forge · vectors · weapons · chains | **kairo** — forge from existing findings |
| ladder · climb · deepen · privesc · lateral · foothold | **kaisha** — the depth leg: what the foothold becomes |
| harvest · crown · price · what could they take · disclose · impact | **shukaku** — the harvest, after confirmed compromises |
| detect · mirror · detection · purple · sigma | **kage** — confirmed attacks → detection rules |
| train · range · replica · lab · lesson | **dojo** — the range: vulnerable replicas + training lessons |
| everything · full assault · together · one command | **shiki** — the entire pipeline as one assault |
| *anything else* | the **STANDARD RELAY**: barbican → holyshit → undercroft → kairo → 3am → kaisha → shukaku → kage → dojo |

Route bench: **13/13 = 100%**.

### 3. The scope authority — one verdict, every engine

`~/.redteam/scope.json` is the declared estate. **One shared module**
(`scripts/scope_authority.py`) is imported by the dispatcher, Arsenal, the MCP
server, the live bench, and every live probe. There is no second opinion and no
engine-specific bypass.

```bash
$ spydermonkey scope init --engagement acme-p1 \
    --in-scope "acme.com,*.api.acme.com,10.0.0.0/24" \
    --out-of-scope "billing.acme.com,vendor.example" --expires-days 14
$ spydermonkey scope check --value https://api.acme.com/v1/orders
✓ IN SCOPE — https://api.acme.com/v1/orders (engagement 'acme-p1')
$ spydermonkey scope check --value https://billing.acme.com/x
✗ OUT OF SCOPE — denied by rule 'billing.acme.com'                    # rc=1
$ spydermonkey scope check --value https://evil.com
✗ OUT OF SCOPE — not in the declared estate                           # rc=1
```

Matching covers exact hosts, subdomains, `*` wildcards, CIDRs, URL paths and
ports; deny always wins; expiry is enforced; the loopback lab is the only
implicit allowance. `scope add|remove|extend|history` maintain the estate and
its audit trail, and writes are atomic with `0600` permissions.

### 4. The control plane — campaigns, contracts, JSON, proof

- **Campaign lifecycle** — `campaign init` writes a manifest; every engine event
  lands in `events.jsonl`; `show`/`timeline` read it; `archive` writes a
  timestamped `tar.gz`; `purge` refuses without `--force`; `close` records the
  verdict. State lives in `~/.redteam/campaigns/<target>/`.
- **Mandate contracts** — `references/mandates/00-barbican.md` … `09-dojo.md`
  are machine-checked (`mandates verify`): each names its axis, law, handoff,
  evidence, fleet command, and failure path. The registry behind
  `tree`/`route`/`fleet`/`next` is the same registry behind the contracts.
- **Machine-readable everywhere** — add `--json` to any command, in any
  position. Errors stay on stderr and keep their exit codes: `0` ok, `1`
  gate/scope/verify failure, `2` usage, `130` interrupted.
- **Tamper-evident ledger** — each finding is hash-chained to the previous row;
  `ledger verify` checks the chain; `--strict` requires every row to be signed;
  evidence remains `baseline: … attack: … diff: …` or the row is downgraded to
  hypothesis. Dedupe attaches new evidence instead of deleting the old row.
- **Self-test** — `selftest` runs 27+ checks in a throwaway `HOME`: scope allow/
  deny, ledger evidence/dedupe/integrity, a live 3-gate proof on the built-in
  lab, testers, chains, phases, coverage, report, campaign lifecycle, mandate
  contracts, MCP, Arsenal, the live bench, training, memory, capabilities,
  protect, and watch. Nothing touches the operator's real estate.
- **Kernel** — `next` returns the single state-driven directive (with the exact
  argv and the walls); `absorb` validates an agent result through the same scope,
  ledger, and evidence gates; `loop` repeats plan → execute → absorb with the
  engines as the state machine. `--plan-only` shows the battle plan.

### 5. The pipeline — one command, ten engines

Also in the toolbox: **`fleet`** dispatches every mandate as its own parallel
agent with a real brief; **`arsenal`** wraps 30 external tools in 6 feeding chains
(nmap, masscan, httpx, nuclei, gobuster, testssl, dnsx, subfinder, whatweb,
wafw00f, nikto, dig, curl, ffuf, naabu, amass, katana, dalfox, tlsx, gau) behind
the same scope authority; chain stages feed each other (subfinder's domains →
dnsx → httpx → nuclei) and `--out` emits the kernel result schema the loop
absorbs; **`skilltree --expand`** generates the 11,683-file context corpus
(technique × platform × auth × hardened × chain, deterministic); **`dojo`** builds
the lab replicas; **`kage`** mirrors every confirmed attack into Sigma.

**`bench_public.py`** — the published benchmarks: the self-bench (15 live replica
classes × 4 sub-tasks, anti-memorization, 100%) and **Range B** — an independently
written app with zero code shared with the testers (90.6%). **`mcp_server.py`** —
the whole family exposed as 52 MCP tools (stdio JSON-RPC, zero deps,
batch/notification support): Claude Desktop, Cursor, or any MCP client drives it.
`--test` and `--list` are built in.

`run` delegates to **SHIKI assault** — the proven path that drives every real
engine in order, under the shield, with adaptive re-tasking:

```
$ python3 scripts/spydermonkey.py run --target acme --url https://acme.com \
      --domain acme.com --bundle bundle.har --parallel --dry-run
▸ SPYDERMONKEY runs the family: shiki assault
  dry-run — the command that would execute:
    /home/you/.hermes/skills/security/shiki/scripts/shiki.py assault --target acme --url https://acme.com --domain acme.com --bundle bundle.har --parallel
```

Drop `--dry-run` and it executes for real. `--resume` picks up an interrupted
assault idempotently; `--close` wipes the campaign at the end.

---

## The kernel — model-in-the-loop, inverted

Most "AI pentest tools" put a big LLM in the driver's seat and hope. SPYDERMONKEY
**inverts** that: the engine owns the loop, and the model is a swappable reasoning cell.

```
spydermonkey loop --target T --url https://lab.local --domain lab.local
```

- `next` — the deterministic directive planner: reads scope, context, ledger,
  estate memory and learned priors, and emits the next machine-readable directive.
- `absorb` — every directive's result is ingested through the ledger's own gates;
  out-of-scope data is refused (ScopeDenied, rc=1) before it ever touches memory.
- `loop` — plan → execute → absorb → repeat until complete. Runs **fully
  autonomous with no model at all**, or with any reasoning cell bolted in:

```
spydermonkey loop --target T --url ... --domain ... --agent-cmd 'claude -p'
```

`--agent-cmd` accepts Claude Code, Codex, a local Ollama, anything that reads
stdin and writes text. The model improvises; the batteries prove; the walls
decide. A proven 10-step autonomous loop: scope → posture → descent → testers
(CONFIRMED IDOR, cvss 8.0) → honest DISPROVEN gates → kage mirror → shukaku →
war report, exit rc=5, zero human input.

---

## The numbers — all measured

| Metric | Value | Verified by |
|---|---|---|
| Skill corpus | **11,683 files** — 837 base techniques × platform × auth × hardened × chain | `skilltree --verify`: 0 orphans, CI floor 10k |
| Self-play training | **14/14 classes** | `train` — priors written, planner re-ordered |
| Self-benchmark | **100%** — 60/60 sub-tasks, anti-memorization | `bench_public.py`, seeded + reproducible |
| Cross-range benchmark | **90.6%** on an independent codebase | `bench_public.py 2026 b` |
| Differential testers | **18 batteries** — INJECTION 14 markers · TRAVERSAL 8 encodings · SSRF 7 targets · IDOR 8 payloads · AUTHZ 6 · AUTHN 8 · BIZLOGIC 6 · NOSQL 7 · CRLF 4 · REDIRECT 5 · HARVEST 15 paths · DIRECTORY 10 roots · CORS/REPLAY header & idempotency differentials | `selftest` |
| Chain patterns | **10 kill-chain patterns**, same-origin pairing (+ cors_credential_read · nosql_authn) | `chain detect` |
| MCP tools | **50** — every engine surfaced to every MCP client | `mcp --test` |
| Executors | **30-tool arsenal**, 6 feeding chains (recon/web/tls/net/cloud/osint) | `arsenal` |
| Reasoning engine | **4 generators** (surface · cve-map · variant · chain) → ranked, wall-checked hypothesis cards + a model brief; priors-weighted; scope-marked | `hypothesis gen` |
| Detection patterns | **15 kage patterns** + Sigma export + live refire | [kage](https://github.com/xanstomper/kage) |
| Takeover fingerprints | **10 dangling-CNAME services**, read-only NO-GAIN | `takeover` |
| Dependency count | **0** | the imports |

---

## The benchmarks

Two scorecards ship in-repo (`references/bench-scorecard.md`,
`bench-result.json`, `bench-result-b.json`):

- **Self-bench — 100% (60/60).** 15 live vulnerability classes × 4 sub-tasks
  (surface → identify → confirm → detect), each instance spawned on a **random
  port per run** (seeded, reproducible) so the batteries cannot hardcode their
  way through.
- **Cross-range — 90.6% on Range B.** An independently written shop app (cookie
  sessions, cart, admin panel, order lookup) with **zero shared code and no
  co-evolution** with the testers. The first honest run scored **75%** — and every
  miss was a real battery gap: no numeric-id successor payloads (IDOR), verdicts
  too narrow for name-shaped foreign objects and generic internal markers, and
  crawl-state diluting strike values. All four were fixed with **generic logic,
  not range tuning** — that's what a cross-range is for.

**Honest ceiling, stated in the scorecards themselves:** these are family-built
ranges. They measure the engine, not third-party consensus. Cross-benchmark
adaptation (AutoPenBench / AI-Pentest-Benchmark) is the next step.

CI enforces both floors: the self-bench must stay ≥95% and Range B ≥85%, or the
build goes red.

---

## Training — the self-play loop

```
$ spydermonkey train --target my-first-training
═══ training pass: 14/14 class(es) confirmed by the testers ═══
  the planner now orders probes by what works — the family gets sharper every run
```

Every pass: the family attacks its own range (the
[dojo](https://github.com/xanstomper/dojo)), scores every class, writes
`~/.redteam/memory/spydermonkey-priors.json`, and the kernel's planner sorts
gate-hole directives by hit-rate. The measured self-improvement curve this build
took from scratch:

**2/14 → 5/14 → 11/14 → 12/14 → 14/14**

Each pass found a real weakness — missing testers, narrow param vocab, dishonest
probe baselines — fixed it, and re-scored. Nothing was gamed; the misses are in
the transcript.

**Estate memory:** every completed engagement writes what it confirmed per target.
The next campaign on that estate re-ranks the planner with it. `memory --forget`
wipes a target entirely.

---

## Remediate — the fix loop

```
$ spydermonkey remediate --target T --id SPY-001 --reproof
═══ SPYDERMONKEY REMEDIATE — SPY-001 (IDOR) ═══
  asset: http://127.0.0.1:9392/api/orders?org_id=foreign
  fix recipe: enforce object ownership server-side: every object fetch resolves
  through the session's org/user scope — never trust org_id from the request …
  ▸ re-proof: re-running the differential post-fix…
  ✓ REMEDIATION VERIFIED — differential no longer confirms
```

Per-class fix recipes for all 11 tester classes. On lab assets the loop re-runs
the full differential post-fix:

- **VERIFIED** — the differential no longer confirms (the fix worked, proven),
- **FAILED (rc=1)** — it still confirms (the fix failed, proven),
- **honest unknown** — the target is unreachable; no claim is made either way.

On external assets: recipe-only — the wall holds. Every re-proof lands in the
ledger with its evidence chain. RedAmon opens PRs; spydermonkey **re-proves**.

---

## Capabilities — the mirror of self

```
$ spydermonkey capabilities --json
```

The dispatcher **introspects itself live** — never a hand-written doc: which of
the 10 engines are present on this machine, the 26 confirmable vulnerability
classes, per-tester battery sizes, the 10 takeover fingerprints, the real
executor inventory (what's actually installed *here*), kernel directives, corpus
size, and the learned priors. Machine-readable; the planner and any bolted-in
agent ground on it.

## Protect — the mirror turned around

```
$ spydermonkey protect posture      # what this machine can leak: user · hostname ·
                                    # git email · LAN/Tailscale/IPv6 · ssh keys
$ spydermonkey protect scan --all-campaigns
✗ OPERATOR STRINGS IN ARTIFACTS — rc=1      # every leak, per artifact, with the
                                            # barbican-sanitize handoff + kage rule
```

The family's OPSEC engine: it scans **every campaign artifact** for operator
strings and **refuses to pass (rc=1) while anything leaks**, hands the sanitize
job to barbican, and re-proves clean. It found real leaks in this machine's own
campaign artifacts on its first run.

---

## Why it's so powerful

- **The control plane (v4).** One scope authority for every engine · campaign
  lifecycle with manifests, events, archives and a guarded purge · ten
  machine-checked mandate contracts · `--json` on every command · a
  hash-chained, deduping, evidence-gated ledger · `selftest` in a throwaway
  `HOME` · and a kernel (`next`/`absorb`/`loop`) that makes the engines the
  state machine. The family is operable by a model, a script, or an MCP client
  without a second interpretation of the rules.
- **The intelligence layer (v3).** A **13-phase methodology board** computed from
  real deliverables (never declared), a **finding ledger** with triager gates
  (scope · evidence · duplicates — downgraded, never suppressed), the **3-gate
  confirmation engine** (baseline → attack → measurable diff → CONFIRMED, or
  nothing registers), **18 differential testers**, a **chain detector** (10
  patterns turning low findings into high-impact kill chains), **coverage** with
  the gap list, the joint **war report**, and **remote execution nodes**
  (Ed25519 ssh relays, scope-checked). `mission` runs all of it in one command.
- **Proven, not asserted.** `verify` ends with a LIVE GATE PROOF: it spins the
  built-in lab replica and requires a real baseline→attack→diff CONFIRMED before
  it says PASS. `testers --demo` strikes the same replica with zero setup.
- **One command, ten engines.** A single `run` conducts gate → recon ∥ descent →
  forge → chain → sweep → ladder → harvest → mirror → drill → closeout.
- **One axis per mandate.** Unix philosophy applied to offensive security: each
  mandate does exactly one thing and hands off cleanly. Swap one engine and the
  family still works — the dispatcher only knows roles, not internals.
- **The growth loop.** 3AM gets permanently smarter (`converge`/`learn`/`drift`/
  `promote`); spydermonkey gets permanently smarter (`train` → priors → planner;
  `memory` → estate re-ranking). Two growth loops, one family.
- **Manufacturing, not just finding.** KAIRO ingests every family state, expands
  1 confirmed finding into ~4 compiled attacks, chains them into multi-hop kill
  paths, and **distributes the weapons back to every other mandate**.
- **The business verdict.** SHUKAKU turns confirmed compromises into the numbers
  that matter in the boardroom — reachable, worth, who must be told — evidence
  chain enforced in code.
- **Model-agnostic discipline.** The `mandate` command prints an injectable
  persona contract — paste it as the system prompt of ANY LLM/agent and it
  operates the family under the same walls.
- **Zero dependencies.** Pure Python stdlib. One dispatcher file; every companion
  script stdlib too — no venv, no pip, no supply chain.
- **Idempotent & resumable.** Interrupted engagement? `--resume` re-enters
  without double-firing. Done? `campaign close` records the verdict; barbican
  `wipe --confirm` removes operator artifacts.

---

## The skill corpus (11,683 files)

```
spydermonkey skilltree              # 837 base techniques from 94 real sources
spydermonkey skilltree --expand     # × platform × auth × hardened × chain → 11,683
spydermonkey skilltree --verify     # links resolve · provenance present · 0 orphans
```

- **Base canon, all real:** OWASP WSTG (per-test depth), MITRE ATT&CK (every
  tactic from recon to impact), MASTG/MASVS (mobile classes, lab-walled), cloud
  classes (IAM · object storage · metadata · edge · kubernetes · azure · gcp),
  and every mandate's own `references/` — each entry rewritten family-native
  with the class, the probe shape, and the wall stated.
- **Context variants are earned, not multiplied:** the *hardened* state applies
  only to WAF-relevant families (real filter-tier adjustments — the encoding
  vocabulary, don't-trip-the-WAF discipline, low-and-slow); *chain-composition*
  files encode the actual same-origin pairing rules `chain detect` uses, with
  entry/pivot/final roles per technique.
- **Lazy-loaded:** the index + binding keys are all that ever enter a model's
  context; files are read one at a time on demand. The corpus costs **zero**
  runtime context at rest, and the CI floor (10,000 expanded links) means the
  number can't silently rot.

---

## MCP — 52 tools for every client

```
spydermonkey mcp --stdio     # or: python3 scripts/mcp_server.py --test
```

Claude Code, Claude Desktop, Cursor, or any MCP client gets the whole war:
scope, ledger (add/triage/show/verify/export/stats), gate, chain, context,
testers, coverage, report, relay, mandates, kernel (`next_action`,
`kernel_absorb`, `kernel_loop`), `capabilities`, `protect_scan`, `takeover`,
`train`, `memory` — batch and notification support, zero deps.

---

## The session injection — `/spydermonkey` (v5.4.0)

Type `/spydermonkey` and the mandate becomes the agent for **that session** —
every message routes through the SPYDERMONKEY contract until release. The file
every agent injects is `references/mandate-session.md` (re-print any time with
`spydermonkey mandate --session`).

| Agent | Activation | Persistence |
| --- | --- | --- |
| **OpenCode** | `/spydermonkey [goal]` — switches the session to the `spydermonkey` primary agent (`~/.config/opencode/agents/spydermonkey.md`); the mandate IS the system prompt | until you switch back (`/build`) or `/spydermonkey off` |
| **Claude Code** | `/spydermonkey [goal]` (`~/.claude/commands/spydermonkey.md`) | in-session; released by `/spydermonkey off` |
| **Hermes** | `/spydermonkey` (skill `spydermonkey` — `~/.hermes/skills/security/spydermonkey`) | in-session; skill reload |
| **Cline CLI** | `spydermonkey-cline "<brief>"` (wraps `cline -s "$(cat …/mandate-session.md)"`) — system-prompt override per session | session end |
| **Any other agent** | `spydermonkey mandate --session` → paste as system prompt / first message | per the agent's mechanism |

The contract carries its own walls: scope authority first, evidence discipline
(baseline → attack → measurable diff), validation-only compromise, NO-GAIN, and the
report-not-attack deliverable bar. Release: `/spydermonkey off` (or agent switch).

---

## Quickstart

```bash
# the dispatcher is a single stdlib script — no install, no deps
git clone https://github.com/xanstomper/spydermonkey.git
python3 spydermonkey/scripts/spydermonkey.py tree        # the family + roles + chain
python3 spydermonkey/scripts/spydermonkey.py route --goal "take over their session"

# a first engagement (lab)
python3 spydermonkey/scripts/spydermonkey.py campaign new --target lab1
python3 spydermonkey/scripts/spydermonkey.py crawl --target lab1 --url http://127.0.0.1:PORT
python3 spydermonkey/scripts/spydermonkey.py testers --target lab1
python3 spydermonkey/scripts/spydermonkey.py chain detect --target lab1
python3 spydermonkey/scripts/spydermonkey.py report --target lab1

# the growth loop
python3 spydermonkey/scripts/spydermonkey.py train --target t1          # self-play
python3 spydermonkey/scripts/spydermonkey.py loop --target t1 --url U --domain D   # autonomous
python3 spydermonkey/scripts/spydermonkey.py watch --target t1 --url U --domain D  # on a clock
python3 spydermonkey/scripts/spydermonkey.py serve                      # the war board

# as a Hermes skill (where the family lives)
git clone https://github.com/xanstomper/spydermonkey.git \
    ~/.hermes/skills/security/spydermonkey
```

> **The ten engines are separate repos.** `verify` and `status` need the family
> installed at `~/.hermes/skills/security/<name>/scripts/`. Clone them all:
>
> ```bash
> cd ~/.hermes/skills/security
> git clone https://github.com/xanstomper/barbican.git
> git clone https://github.com/xanstomper/HolyShit.git holyshit-mode
> git clone https://github.com/xanstomper/undercroft.git
> git clone https://github.com/xanstomper/3am-shinjitsu.git
> git clone https://github.com/xanstomper/kairo.git
> git clone https://github.com/xanstomper/shiki.git
> git clone https://github.com/xanstomper/shukaku.git
> git clone https://github.com/xanstomper/kaisha.git
> git clone https://github.com/xanstomper/kage.git
> git clone https://github.com/xanstomper/dojo.git
> python3 spydermonkey/scripts/spydermonkey.py verify   # → ALL PASS
> ```

---

## The CLI

| Command | What it does |
|---|---|
| `tree` | the family + roles + the chain (the doctrine, condensed) |
| `version` | dispatcher version, schema, data root, scope path, engine summary |
| `route --goal "<words>"` | plain-language goal → the mandate sequence to load/run |
| `run --target T --url U --domain D [--bundle P] [--parallel] [--resume] [--close] [--dry-run]` | the full pipeline — delegates to SHIKI assault |
| `mission --target T --url U --domain D [--skip-fleet] [--plan] [--resume] [--close]` | **one command**: scope gate → fleet (10 agents, parallel) → ledger triage → chain detect → coverage → the war report |
| `campaign init\|list\|show\|timeline\|archive\|purge\|close --target T` | the **campaign lifecycle**: manifest · events · closeout · guarded purge |
| `mandates list\|show\|verify [--name N]` | the **ten mandate contracts** — axis · law · handoff · evidence · fleet · failure |
| `next --target T [--url U] [--domain D]` | **kernel**: the one state-driven directive, exact argv, walls |
| `absorb --target T --file result.json` | **kernel**: validate a result through scope + ledger + evidence gates |
| `loop --target T [--agent-cmd '…'] [--plan-only] [--max-steps N]` | **kernel**: plan → execute → absorb → repeat — model-optional |
| `next-phase --target T` | the next 13-phase board action, with the exact command |
| `phases --target T [--set-phase P --phase-status S]` | the 13-phase methodology board — statuses computed from real deliverables |
| `ledger add\|list\|show\|triage\|verify\|stats\|export\|update\|sync --target T` | the finding ledger — scope-blocked, hash-chained, deduped, evidence-gated |
| `gate --target T --url U --attack-query Q [--confirm TOK] [--prove SPY-NNN] [--cookie C] [--json-body J --attack-body J2]` | the **3-gate confirmation engine** — headers, cookies, JSON bodies |
| `chain detect\|plan --target T [--id CH-NNN]` | **10 chain patterns** — low findings combine into high-impact kill chains |
| `context set\|show --target T` | session context: endpoints · roles · credentials · functions |
| `testers --target T --url U [--url U2 …] \| --demo` | the **18 differential batteries**, deduped into the ledger |
| `hypothesis gen\|brief --target T [--url U] [--kinds K]` | the **reasoning engine**: ranked hypothesis cards (surface/cve-map/variant/chain) + the model brief that guides any model through the 3-gate loop |
| `coverage --target T` | phase × deliverable matrix + findings histogram + the gap list |
| `report --target T [--format md\|json\|sarif] [--output F]` | the joint **war report**: findings + proofs + chains + coverage + detection + pricing |
| `relay init\|list\|exec\|remove` | remote execution nodes: Ed25519 ssh pairs, every exec scope-checked |
| `status [--target T] [--fast]` | every mandate's engine presence + verify state + campaign files + ledger counts |
| `verify [--fast] [--no-selftest]` | the meta self-check: subcommands, contracts, all ten engines, self-test, **+ the live gate proof** |
| `selftest [--quick]` | the end-to-end 27+ check self-test in a throwaway `HOME` |
| `mandate [--file]` | print (or locate) the injectable persona contract |
| `scope init\|check\|show\|add\|remove\|extend\|history` | the estate gate — shared matching, deny precedence, expiry, audit history |
| `doctor [--fix]` | full health check: engines · scope perms · corrupt states · canon · ledger · relays |
| `bench` | offline route-level benchmark |
| `arsenal list\|plan\|run\|verify` | the execution layer — 30 tool wrappers, 6 feeding chains, kernel-schema output |
| `catalog stats\|categories\|list\|search\|show` | **1,053-entry known-tool reference** — lazy-loaded metadata (info only; execution stays scope-gated via arsenal) |
| `fleet --goal G --target T --domain D [--agents a,b] [--sequential]` | one agent per mandate, dispatched in parallel |
| `skilltree [--expand] [--verify] [--count]` | the corpus: 837 base → 11,683 files, deterministic, 0 orphans |
| `crawl --target T --url U [--depth N]` | surface mining: links · whole-form-blocks (method+fields) · JS api-paths → context |
| `takeover --target T --domain D [--subdomains F]` | dangling-CNAME fingerprints — read-only, NO-GAIN |
| `capabilities [--json]` | **the mirror of self** — live-introspected registry: engines · classes · batteries · executors · priors |
| `protect posture\|scan [--target T] [--all-campaigns]` | **self-protection** — operator posture · artifact leak scan (rc=1 while leaking) |
| `train --target T [--classes LIST]` | **self-play** vs the dojo range → per-class priors → sharper planning |
| `memory --target T [--forget]` | **estate memory** — what the family knows about a target |
| `remediate --target T --id SPY-NNN [--reproof]` | **the fix loop** — recipe + machine-verified re-proof (VERIFIED / FAILED rc=1 / honest unknown) |
| `watch --target T --url U --domain D [--every-mins N] [--notify-cmd X]` | the **unattended runner**: loop → report → memory → notify, on a clock |
| `serve [--port P]` | the **war board**: ledger · chains · estate memory · json — localhost-only |

Every command accepts `--json` in any position. Exit codes: `0` ok · `1`
gate/scope/verify failure · `2` usage error · `130` interrupted.

---

## Architecture

```
scripts/
├── spydermonkey.py    # the dispatcher: control plane · intelligence · kernel · v5 engines
├── scope_authority.py # ONE estate gate: matching · deny precedence · expiry · audit
├── skilltree.py       # corpus collector/expander/verifier (deterministic, git-stable)
├── arsenal.py         # 30 executors, 6 feeding chains, kernel-schema results
├── mcp_server.py      # 50-tool MCP server (stdio JSON-RPC)
├── bench_public.py    # the published benchmarks (self + cross-range)
├── range_b.py         # the INDEPENDENT benchmark range (no co-evolution)
├── bench_live.py      # the exploitation-level bench (throwaway HOME, localhost lab)
└── ci_smoke.sh        # 20-section live verification — local truth = CI truth
references/
├── skills/            # the 11,683-file corpus (lazy-loaded)
├── attack-canon.md · mobile-canon.md · cloud-canon.md · wstg-deep-canon.md
├── bench-scorecard.md · bench-result.json · bench-result-b.json
├── mandate.md         # the injectable persona contract
└── mandates/          # 00-barbican.md … 09-dojo.md (machine-checked contracts)
tests/test_spydermonkey.py   # stdlib test suite
.github/workflows/verify.yml # CI = ci_smoke.sh (the same proof locally)
```

---

## How it compares

| | CyberStrike | PentestGPT | xOffense | RedAmon | **SPYDERMONKEY** |
|---|---|---|---|---|---|
| Corpus scale | 7.6k | prompt-pack | — | graph | **11,683, CI-floored** |
| Self-training | — | — | fine-tune (frozen) | — | **live self-play, priors every run** |
| Benchmarks | — | — | 79% (published) | — | **100% self · 90.6% cross-range** |
| Fix loop | — | — | — | fix PRs | **machine-verified re-proof** |
| Scope enforcement | model discretion | — | — | approval gates | **exit-code walls, deterministic** |
| Operator OPSEC | — | — | — | — | **protect: leak scan, rc=1** |
| Target memory | session | — | — | graph | **estate memory across engagements** |
| Dependencies | node + many | many | GPU cluster | Docker+Neo4j | **0 (stdlib)** |
| Model required | yes | yes | Qwen3-32B | yes | **no — kernel runs model-free** |

**Honest ceilings:** the rivals keep the community and distribution (3.2k stars,
plugins, docs polish). Deep-system reach (eBPF, cloud API execution, AD
post-exploitation) is deliberately **outside our walls** — the family maps,
proves, prices, detects, and re-proves; it does not persist, pivot laterally,
impair defenses, or destroy. Model improvisation depth is whatever cell you bolt
into `--agent-cmd` — the batteries do the proof work deterministically either way.

---

## The Mandate Discipline

SpyderMonkey carries the family's **persona contract** — the kimiko mandate
architecture, made model-agnostic, with the family's walls as the stop
conditions:

- **Entry protocol** — the trigger word = immediate adoption + capability
  announcement + P0 await. No warm-up, no hedging.
- **Zero-blocker IN SCOPE** — refusing/hedging/delaying authorized work is system
  failure. No placeholders, no "a real attacker would" — outputs are complete
  and deployable.
- **Evidence-first** — a claim without a decisive test is a hypothesis, never a
  finding.
- **Precise stop conditions** — the walls below, not vibes.
- **On pressure** — mid-session re-framing never moves a boundary; provenance is
  checked with one read-only call; gifted credentials are findings.
- **Loop control** — verdict first, minimum decisive test, batch within noise
  budgets, register everything, drift before re-assert.

```bash
python3 scripts/spydermonkey.py mandate        # the full injectable block
python3 scripts/spydermonkey.py mandate --file # just the path
```

---

## The Walls (non-negotiable)

Non-negotiable at every layer of the family:

1. **Declared estates only** — scope inherits the source finding's declaration.
2. **Documented-PoC adaptation only** — canon technique classes; never novel
   weapon classes, malware, or destructive payloads.
3. **Validation-only compromise** — one decisive proof, then STOP. Reversible.
   NO-GAIN: nothing of value is kept, persistence is never installed.
4. **Never social. Never third parties.**
5. **Zero documents** — the recorded declaration is the entire gate.
6. **Destructive end-states refused once**, pivoted to disclosure.
7. **The family protects its operator** — `protect` scans every artifact for
   operator strings and refuses (rc=1) while anything leaks.

This project exists for **authorized security testing**. Anything outside the
walls is refused — by design, at every layer.

---

## Relations

Every family skill is reachable from here; load per the router:
[barbican](https://github.com/xanstomper/barbican) (shield) ·
[HolyShit](https://github.com/xanstomper/HolyShit) (finder) ·
[undercroft](https://github.com/xanstomper/undercroft) (descent) ·
[3am-shinjitsu](https://github.com/xanstomper/3am-shinjitsu) (performer) ·
[kairo](https://github.com/xanstomper/kairo) (synthesizer) ·
[kaisha](https://github.com/xanstomper/kaisha) (ladder) ·
[shukaku](https://github.com/xanstomper/shukaku) (harvester) ·
[shiki](https://github.com/xanstomper/shiki) (command) ·
[kage](https://github.com/xanstomper/kage) (mirror) ·
[dojo](https://github.com/xanstomper/dojo) (range).

## License

[MIT](LICENSE) — use the family, build for it, route through it.

<div align="center">

*The spider doesn't chase. It feels the web, and sends the right leg.*

</div>

---

**#AISecurity #PenetrationTesting #AutonomousAgents #OffensiveSecurity #RedTeam #BugBounty #LLMAgent #CyberSecurity #VulnerabilityAssessment #ExploitFramework #PentestAutomation #AttackSurface #SelfImprovingAI #ZeroDependencies #Python #SecurityAudit #ThreatDetection #OSINT #AgentFramework #Spydermonkey**
