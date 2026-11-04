<div align="center">

<img src="assets/spyder.gif" alt="SPYDERMONKEY — the spider at the center of the web" width="640"/>

# 🕷️ SPYDERMONKEY

### *Any agent. One skill. The whole war.*

**The master dispatcher of the HolyShit offensive-security family —
the tree, the router, and the full engagement pipeline in one stdlib-only CLI.**

[![Version](https://img.shields.io/badge/version-4.0.0-blueviolet?style=for-the-badge)](#-the-cli)
[![Python](https://img.shields.io/badge/python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](#quickstart)
[![Platform](https://img.shields.io/badge/platform-Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](#quickstart)
[![Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen?style=for-the-badge)](#why-its-so-powerful)
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

[How it works](#how-it-works) · [Why it's so powerful](#why-its-so-powerful) ·
[Quickstart](#quickstart) · [The CLI](#the-cli) ·
[The Mandate Discipline](#the-mandate-discipline) · [The Walls](#the-walls-non-negotiable)

</div>

---

## What is this?

SPYDERMONKEY is the spider at the center of the web. Around it, ten specialized
offensive-security mandates — the **HolyShit family** — each owning exactly one
axis of an engagement. None of them overlap. All of them compose.

SPYDERMONKEY is the piece that knows the whole tree:

- **routes** any goal, in plain words, to the right mandate sequence,
- **runs** the full pipeline end-to-end with one command,
- **owns the CONTROL PLANE** (v4): one shared scope authority, campaign
  lifecycle, the ten machine-checkable mandate contracts, tamper-evident
  ledgers, JSON on every command, and an end-to-end self-test,
- **owns the INTELLIGENCE LAYER** (v3): the 13-phase methodology board, the
  finding ledger with triager gates, the 3-gate confirmation engine, the
  8 parallel sub-testers, the chain detector, coverage, the war report, and
  remote execution nodes,
- **drives the KERNEL** (v4): `next` emits the one state-driven directive,
  `absorb` validates a result through the same gates, and `loop` runs the
  plan → execute → absorb cycle with the engines as the state machine,
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

v4 turns the dispatcher from a router into a **control plane**:

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
- **Self-test** — `selftest` runs 27 checks in a throwaway `HOME`: scope allow/
  deny, ledger evidence/dedupe/integrity, a live 3-gate proof on the built-in
  lab, testers, chains, phases, coverage, report, campaign lifecycle, mandate
  contracts, MCP, Arsenal, and the live bench. `selftest --quick` is the fast
  gate. Nothing touches the operator's real estate.
- **Kernel** — `next` returns the single state-driven directive (with the exact
  argv and the walls); `absorb` validates an agent result through the same scope,
  ledger, and evidence gates; `loop` repeats plan → execute → absorb with the
  engines as the state machine. `--plan-only` shows the battle plan.

### 5. The pipeline — one command, ten engines

Also in the toolbox: **`fleet`** dispatches every mandate as its own parallel
agent with a real brief; **`arsenal`** wraps 13 external tools
(nmap, masscan, httpx, nuclei, gobuster, testssl, dnsx, subfinder, whatweb,
wafw00f, nikto, dig, curl) behind the same scope authority and a structured
`run` record; **`dojo`** builds the lab replicas; **`kage`** mirrors every
confirmed attack into Sigma.

**`bench_live.py`** — the LIVE exploitation benchmark: stdlib vulnerable
mini-targets (IDOR · replay · exposed-backup) spun up on localhost, the family's
real engines engage them, sub-task completion scored (10/10 with engines, 9/9
without). It always uses a throwaway `HOME` and a dynamic port, so it can never
overwrite the operator's real scope or collide with a running daemon.
**`mcp_server.py`** — the whole family exposed as 43 MCP tools (stdio
JSON-RPC, zero deps, batch/notification support): Claude Desktop, Cursor, or any
MCP client drives it. `--test` and `--list` are built in.
**`skilltree.py`** — generates the technique library from the family's real
canon: 722 per-technique skill files, WSTG/CWE/ATT&CK-bound, lazy-loaded via
`references/skilltree-index.md`; `--verify` proves index ↔ files ↔ bindings,
and `--count --json` is the machine-readable count.

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

## Why it's so powerful

- **The control plane (v4).** One scope authority for every engine · campaign
  lifecycle with manifests, events, archives and a guarded purge · ten
  machine-checked mandate contracts · `--json` on every command · a
  hash-chained, deduping, evidence-gated ledger · `selftest` in a throwaway
  `HOME` · and a kernel (`next`/`absorb`/`loop`) that makes the engines the
  state machine. The family is now operable by a model, a script, or an MCP
  client without a second interpretation of the rules.
- **The intelligence layer (v3).** CyberStrike-style engagement brain, family-native:
  a **13-phase methodology board** computed from real deliverables (never declared),
  a **finding ledger** with triager gates (scope · evidence · duplicates — downgraded,
  never suppressed), the **3-gate confirmation engine** (baseline → attack →
  measurable diff → CONFIRMED, or nothing registers), **8 parallel sub-testers**
  (IDOR · AUTHZ · MASSASSIGN · INJECTION · AUTHN · BIZLOGIC · SSRF · FILEATTACK),
  a **chain detector** (8 patterns turning low findings into high-impact kill chains),
  **coverage** with the gap list, the joint **war report**, and **remote execution
  nodes** (Ed25519 ssh relays, scope-checked). `mission` runs all of it in one command.
- **Proven, not asserted.** `verify` ends with a LIVE GATE PROOF and a 27-check
  self-test in a throwaway `HOME`: it spins the built-in lab replica and requires
  a real baseline→attack→diff CONFIRMED before it says PASS. `testers --demo`
  strikes the same replica with zero setup. Engine self-checks that collide on
  lab ports are retried serially, so a healthy engine cannot be reported red by
  a race.
- **One command, ten engines.** A single `run` conducts gate → recon ∥ descent →
  forge → chain → sweep → ladder → harvest → mirror → drill → closeout. You stop
  babysitting ten CLIs; the conductor handles ordering, parallelism, and re-tasking
  from live results.
- **One axis per mandate.** Unix philosophy applied to offensive security: each
  mandate does exactly one thing and hands off cleanly. Swap one engine and the
  family still works — the dispatcher only knows roles, not internals.
- **The growth loop.** 3AM is the only member that gets permanently smarter:
  every engagement feeds `converge`/`learn`/`drift`/`promote`, so the sweep you
  run next week is sharper than this week's.
- **Manufacturing, not just finding.** KAIRO ingests every family state, expands
  1 confirmed finding into ~4 compiled attacks, chains them into multi-hop kill
  paths, and **distributes the weapons back to every other mandate**. Findings
  never die in one report.
- **The business verdict — and the loop.** SHUKAKU turns confirmed compromises into
  the numbers that matter in the boardroom — what was reachable, what it's worth,
  who must be told — with the evidence chain enforced in code. And it doesn't stop
  at pricing: `reason` infers what else SHOULD be harvestable, `hunt` proves it
  read-only, and `feed` hands every discovery back to 3AM/undercroft/holyshit as
  attack material. The register keeps counts, never corpora.
- **Model-agnostic discipline.** The `mandate` command prints an injectable
  persona contract — paste it as the system prompt of ANY LLM/agent and it
  operates the family under the same walls. The discipline travels; the model
  doesn't matter.
- **The gate.** BARBICAN hard-gates the pipeline on a verified exit vantage and
  strips operator strings before anything runs. No verified exit → rc=1 and
  **nothing** executes. OpSec is not a step; it's a precondition.
- **Zero dependencies.** Pure Python stdlib. The dispatcher is one file; the
  companion scripts (`scope_authority` · `arsenal` · `bench_live` · `mcp_server`
  · `skilltree`) are stdlib too — no venv, no pip, no supply chain.
- **Idempotent & resumable.** Interrupted engagement? `--resume` re-enters
  without double-firing. Done? `campaign close` records the verdict;
  `campaign archive` writes a verifiable closeout; barbican `wipe --confirm`
  removes operator artifacts. Campaign state lives on disk in
  `~/.redteam/campaigns/`.

---

## Quickstart

```bash
# the dispatcher is a single stdlib script — no install, no deps
git clone https://github.com/xanstomper/spydermonkey.git
python3 spydermonkey/scripts/spydermonkey.py tree        # the family + roles + chain
python3 spydermonkey/scripts/spydermonkey.py route --goal "take over their session"

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
| `route --goal "<words>"` | plain-language goal → the mandate sequence to load/run |
| `run --target T --url U --domain D [--bundle P] [--boundary-url U2] [--probe-ids 1,2] [--parallel] [--resume] [--close] [--dry-run]` | the full pipeline — delegates to SHIKI assault |
| `mission --target T --url U --domain D [--skip-fleet] [--close]` | **v3 one command**: scope gate → fleet (10 agents, parallel) → ledger triage → chain detect → coverage → the war report |
| `phases --target T` | the 13-phase methodology board — statuses computed from real deliverables, never declared |
| `ledger add\|list\|show\|triage --target T` | the finding ledger — scope-blocked, deduped, evidence-gated (`baseline:/attack:/diff:` or downgraded to hypothesis, never suppressed) |
| `gate --target T --url U --attack-query Q [--confirm TOK] [--prove SPY-NNN]` | the **3-gate confirmation engine**: baseline → attack → measurable diff (+ token) → CONFIRMED |
| `chain detect\|plan --target T [--id CH-NNN]` | **8 chain patterns** — low findings on one origin combine into high-impact kill chains with testing plans |
| `context set\|show --target T` | session context: endpoints · roles · credentials · functions |
| `testers --target T --url U [--url U2 …] \| --demo` | the **8 parallel sub-testers** (IDOR · AUTHZ · MASSASSIGN · INJECTION · AUTHN · BIZLOGIC · SSRF · FILEATTACK), differential + deduped into the ledger |
| `coverage --target T` | phase × deliverable matrix + findings histogram + the gap list |
| `report --target T [--output F]` | the joint **war report** (markdown): findings + proofs + chains + coverage + detection + pricing |
| `relay init\|list\|exec\|remove` | remote execution nodes (Bolt-equivalent): Ed25519 ssh pairs, every exec scope-checked |
| `status [--target T]` | every mandate's engine presence + verify state + campaign files + ledger counts |
| `verify` | the meta self-check: subcommands, mandate file, all ten engines **+ the live gate proof** |
| `mandate [--file]` | print (or locate) the injectable persona contract |
| `scope init\|check\|show` | the estate gate — `~/.redteam/scope.json`, domain-suffix/CIDR match, default-deny with `--strict` |
| `doctor` | full health check: engines · scope · corrupt states · canon · ledger · relays |
| `bench` | offline route-level benchmark (route accuracy; 13/13 at v3.0.0) |
| `arsenal list\|plan\|run\|verify` | the execution layer — 13 tool wrappers, scope-gated, canon-classified findings |
| `fleet --goal G --target T --domain D [--agents a,b]` | one agent per mandate, dispatched in parallel |

Exit codes: `0` ok · `1` gate/verify failure · `2` usage error.

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

Print it and paste it as the system prompt of any model:

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

This project exists for **authorized security testing**. Anything outside the
walls is refused — by design, at every layer.

---

## Files

```
spydermonkey/
├── SKILL.md                  # the doctrine — the tree lives here
├── CHANGELOG.md              # release notes
├── scripts/
│   ├── spydermonkey.py       # tree · route · run · status · verify · mandate · scope · doctor · bench · arsenal · fleet
│   ├── arsenal.py            # the execution layer — 13 tool wrappers, scope-gated
│   ├── bench_live.py         # the exploitation-level bench (localhost lab)
│   ├── mcp_server.py         # the family as 12 MCP tools (stdio JSON-RPC)
│   └── skilltree.py          # regenerate references/skills/ from the family canon
├── references/
│   ├── mandate.md            # the injectable persona contract (any model)
│   ├── skilltree-index.md    # the generated technique library index (722 entries)
│   └── skills/               # 722 lazy-loaded technique files (WSTG/CWE/ATT&CK-bound)
├── .github/workflows/verify.yml
└── assets/
    └── spyder.gif            # the spider at the center of the web
```

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
