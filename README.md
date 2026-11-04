<div align="center">

<img src="assets/spyder.gif" alt="SPYDERMONKEY — the spider at the center of the web" width="640"/>

# 🕷️ SPYDERMONKEY

### *Any agent. One skill. The whole war.*

**The master dispatcher of the HolyShit offensive-security family —
the tree, the router, and the full engagement pipeline in one stdlib-only CLI.**

[![Version](https://img.shields.io/badge/version-1.3.0-blueviolet?style=for-the-badge)](#-the-cli)
[![Python](https://img.shields.io/badge/python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](#quickstart)
[![Platform](https://img.shields.io/badge/platform-Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](#quickstart)
[![Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen?style=for-the-badge)](#why-its-so-powerful)
[![Discipline](https://img.shields.io/badge/discipline-model--agnostic%20·%20any%20LLM-9146FF?style=for-the-badge)](#the-mandate-discipline)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)
[![CI](https://github.com/xanstomper/spydermonkey/actions/workflows/verify.yml/badge.svg)](https://github.com/xanstomper/spydermonkey/actions/workflows/verify.yml)
[![Use](https://img.shields.io/badge/use-AUTHORIZED%20TARGETS%20ONLY-crimson?style=for-the-badge)](#the-walls-non-negotiable)

**THE FAMILY** — six mandates, one axis each, one click away:

[![00 BARBICAN · the shield](https://img.shields.io/badge/00-BARBICAN%20·%20the%20shield-2E4057?style=for-the-badge)](https://github.com/xanstomper/barbican)
[![01 3AM · the performer](https://img.shields.io/badge/01-3AM%20·%20the%20performer-8B0000?style=for-the-badge)](https://github.com/xanstomper/3am-shinjitsu)
[![02 KAIRO · the synthesizer](https://img.shields.io/badge/02-KAIRO%20·%20the%20synthesizer-6B8E23?style=for-the-badge)](https://github.com/xanstomper/kairo)
[![03 UNDERCROFT · the descent](https://img.shields.io/badge/03-UNDERCROFT%20·%20the%20descent-4B0082?style=for-the-badge)](https://github.com/xanstomper/undercroft)
[![04 HOLYSHIT · the finder](https://img.shields.io/badge/04-HOLYSHIT%20·%20the%20finder-B8860B?style=for-the-badge)](https://github.com/xanstomper/HolyShit)
[![05 SHIKI · the command](https://img.shields.io/badge/05-SHIKI%20·%20the%20command-111111?style=for-the-badge)](https://github.com/xanstomper/shiki)
[![06 KAISHA · the ladder](https://img.shields.io/badge/06-KAISHA%20·%20the%20ladder-704214?style=for-the-badge)](https://github.com/xanstomper/kaisha)
[![07 SHUKAKU · the harvester](https://img.shields.io/badge/07-SHUKAKU%20·%20the%20harvester-8B4513?style=for-the-badge)](https://github.com/xanstomper/shukaku)

[How it works](#how-it-works) · [Why it's so powerful](#why-its-so-powerful) ·
[Quickstart](#quickstart) · [The CLI](#the-cli) ·
[The Mandate Discipline](#the-mandate-discipline) · [The Walls](#the-walls-non-negotiable)

</div>

---

## What is this?

SPYDERMONKEY is the spider at the center of the web. Around it, eight specialized
offensive-security mandates — the **HolyShit family** — each owning exactly one
axis of an engagement. None of them overlap. All of them compose.

SPYDERMONKEY is the piece that knows the whole tree:

- **routes** any goal, in plain words, to the right mandate sequence,
- **runs** the full pipeline end-to-end with one command,
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
SHIKI conducts all of it in one `assault` · BARBICAN wipes at the end
```

**One-liners:** Barbican shields you · HolyShit finds it · UNDERCROFT reads what's
hidden · 3AM hits it fast · KAIRO turns every hit into everyone's weapons · SHUKAKU
prices the gain · SHIKI conducts the whole war · SpyderMonkey routes it.

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
| harvest · crown · price · what could they take · disclose · impact | **shukaku** — the harvest, after confirmed compromises |
| ladder · climb · deepen · privesc · lateral · foothold | **kaisha** — the depth leg: what the foothold becomes |
| everything · full assault · together · one command | **shiki** — the entire pipeline as one assault |
| *anything else* | the **STANDARD RELAY**: barbican → holyshit → undercroft → kairo → 3am → kaisha → shukaku |

### 3. The scope authority — the machine-checkable estate gate

```bash
$ spydermonkey scope init --engagement acme-p1 --in-scope "acme.com,10.0.0.0/24"
$ spydermonkey scope check --value https://api.acme.com/x
✓ IN SCOPE — https://api.acme.com/x under engagement 'acme-p1'
$ spydermonkey scope check --value https://evil.com
✗ OUT OF SCOPE — https://evil.com is not in the declared estate      # rc=1
```

Every live-probing engine honors `~/.redteam/scope.json` — default-deny with
`--strict`. Plus: **`doctor`** (full health check) and **`bench`** (offline
route-accuracy benchmark — the family's first measurable metric).

### 4. The pipeline — one command, eight engines

Also since v1.3: **`bench_live.py`** — the LIVE exploitation benchmark: stdlib
vulnerable mini-targets (IDOR · replay · exposed-backup) spun up on localhost,
the family's real engines engage them, sub-task completion scored (3/3 verified).
And **`mcp_server.py`** — the whole family exposed as 12 MCP tools (stdio
JSON-RPC, zero deps): Claude Desktop, Cursor, or any MCP client drives it. And
**`skilltree.py`** — generates the technique library from the family's real
canon: 600+ per-technique skill files, WSTG/CWE/ATT&CK-bound, lazy-loaded via
`references/skilltree-index.md`.

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

- **One command, eight engines.** A single `run` conducts gate → recon ∥ descent →
  forge → chain → sweep → ladder → harvest → closeout. You stop babysitting eight
  CLIs; the conductor handles ordering, parallelism, and re-tasking from live results.
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
- **Zero dependencies.** Pure Python stdlib, one file, ~9 KB. Clone and run on
  any box with `python3` — no venv, no pip, no supply chain.
- **Idempotent & resumable.** Interrupted engagement? `--resume` re-enters
  without double-firing. Done? `--close` wipes. Campaign state lives on disk in
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

> **The six engines are separate repos.** `verify` and `status` need the family
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
> python3 spydermonkey/scripts/spydermonkey.py verify   # → ALL PASS
> ```

---

## The CLI

| Command | What it does |
|---|---|
| `tree` | the family + roles + the chain (the doctrine, condensed) |
| `route --goal "<words>"` | plain-language goal → the mandate sequence to load/run |
| `run --target T --url U --domain D [--bundle P] [--boundary-url U2] [--probe-ids 1,2] [--parallel] [--resume] [--close] [--dry-run]` | the full pipeline — delegates to SHIKI assault |
| `status [--target T]` | every mandate's engine presence + verify state + campaign files |
| `verify` | the meta self-check: subcommands, mandate file, all six engines |
| `mandate [--file]` | print (or locate) the injectable persona contract |

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
├── scripts/
│   └── spydermonkey.py       # tree · route · run · status · verify · mandate
├── references/
│   └── mandate.md            # the injectable persona contract (any model)
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
[shukaku](https://github.com/xanstomper/shukaku) (harvester) ·
[shiki](https://github.com/xanstomper/shiki) (command).

## License

[MIT](LICENSE) — use the family, build for it, route through it.

<div align="center">

*The spider doesn't chase. It feels the web, and sends the right leg.*

</div>
