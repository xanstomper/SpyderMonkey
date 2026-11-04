# Changelog

All notable changes to SPYDERMONKEY, newest first. Dates are UTC; versions are
the dispatcher release (`SKILL.md` frontmatter).

## v4.0.0 — THE CONTROL PLANE (2026-11-04)

- **One scope authority.** New `scripts/scope_authority.py` is the single estate
  verdict for the dispatcher, Arsenal, the MCP server, the live bench, and every
  live probe. Exact host, subdomain, `*` wildcard, CIDR, URL-path, and port
  matching; deny precedence; expiry; lab allowance; rate rules; audit history;
  atomic `0600` writes. `scope add|remove|extend|history` and `doctor --fix`
  complete the lifecycle.
- **Campaign lifecycle.** `campaign init|list|show|timeline|archive|purge|close`
  with a manifest, append-only `events.jsonl`, timestamped archives, and a purge
  that refuses without `--force`. Target names are normalized before any path is
  built — traversal is closed.
- **Ten machine-checked mandate contracts.** `references/mandates/00-barbican.md`
  … `09-dojo.md`, each with axis · law · handoff · evidence · fleet · failure.
  `mandates list|show|verify` checks presence, numbering, phase, and sections;
  the same registry drives `tree`/`route`/`fleet`/`next`.
- **Machine-readable by default.** `--json` works on any command in any position;
  `--scope-file` and `--version` are global; structured errors stay on stderr.
  Exit codes: `0` ok · `1` gate/scope/verify · `2` usage · `130` interrupted.
- **Tamper-evident, exportable ledger.** Findings are hash-chained; `ledger
  verify` checks integrity, `--strict` requires signatures, and `export` emits
  JSON/JSONL/CSV/markdown/SARIF. Dedupe attaches evidence instead of dropping it;
  scope-refused rows never enter the file.
- **The kernel.** `next` emits the one state-driven directive (phase, mandate,
  exact argv, why, expect, walls), `absorb` validates an agent result through
  scope + ledger + evidence gates, and `loop` runs plan → execute → absorb with
  the engines as the state machine. `--plan-only` is free. The old phase action
  remains as `next-phase`.
- **Self-test.** `selftest` runs 27 checks in a throwaway `HOME`: scope allow/
  deny, ledger evidence/dedupe/integrity, a live 3-gate proof on the built-in
  lab, testers, chains, phases, coverage, report, campaign lifecycle, contracts,
  MCP, Arsenal, and the live bench. `selftest --quick` is the 14-check fast gate.
- **Hardening and fixes.** `bench_live.py` now uses a throwaway `HOME` and a
  dynamic port — it can never overwrite or delete the operator's real
  `~/.redteam/scope.json`. Arsenal honors CIDR, deny rules, expiry, and
  per-target normalization. The HTTP gate no longer follows redirects and caps
  response bodies. Engine self-checks that collide on lab ports are retried
  serially instead of reporting a healthy engine red. Reports default to the
  campaign directory; `--output` still overrides.
- **Surfaces.** MCP 18 → 43 tools (`--test`, `--list`, batching, notifications,
  dispatcher/engine adapters, structured content; `kernel_absorb` + `kernel_loop`
  expose the autonomous loop to any MCP client); `skilltree.py` gains
  `--verify` and `--count --json` (722 links/files bindings verified) AND the
  **context corpus**: `--expand` crosses every technique × applicable platform ×
  auth state into 8.8k chain-role-tagged files (deterministic, git-stable,
  sampled verification) — scale parity with the 7.6k-skill competitors, grown
  from real canon instead of a community; `bench` is 29/29 (25 first-hop + 4
  sequence); **`arsenal.py` v5**: 13 → 20 executors (ffuf · naabu · amass ·
  katana · dalfox · tlsx · gau) wired into 4 feeding chains (recon · web ·
  tls · net — subfinder's domains become dnsx's input, katana's urls become
  dalfox's strikes, cap 50/stage) and `run --out` emits the kernel result
  schema the loop absorbs; `arsenal verify` and `bench_live` are green with
  and without engines.
- **Docs and CI.** README, SKILL.md, the persona contract, and this changelog
  describe v4; `ci_smoke.sh` exercises campaigns, contracts, JSON, the kernel,
  the report default, skilltree verify, and the refusal paths; a new stdlib
  `tests/test_spydermonkey.py` runs the same truth locally and in CI.

## v3.0.0 — THE INTELLIGENCE LAYER (2026-11-04)

- **The engagement brain.** Derived from CyberStrike's methodology engine,
  rewritten family-native (stdlib-only, walls as exit codes, scope default-deny):
  `phases` (13-phase methodology board, statuses computed from real state-file
  deliverables), `ledger` (findings: scope-blocked · deduped by class+asset+title ·
  evidence-gated — downgraded to hypothesis, never suppressed; `triage` = triager
  gates with blocking violations), `gate` (the 3-GATE CONFIRMATION engine:
  baseline → attack → measurable diff + confirm token; `--prove` replays evidence),
  `chain` (8 chain patterns: low findings → high-impact kill chains with plans),
  `context` (session context: endpoints/roles/credentials/functions), `testers`
  (the 8 PARALLEL sub-testers — IDOR/AUTHZ/MASSASSIGN/INJECTION/AUTHN/BIZLOGIC/
  SSRF/FILEATTACK — differential probes, deduped into the ledger, `--demo` lab
  replica with zero setup), `coverage` (matrix + histogram + gap list), `report`
  (the joint war report), `relay` (remote execution nodes: Ed25519 ssh pairs,
  scope-checked exec), and `mission` (one command: scope gate → fleet → triage →
  chains → coverage → report).
- **The live-fire rule.** gate/testers fire at localhost freely (the lab); any
  other host requires a scope authority containing it — rc=1 refusal otherwise.
- **verify now proves the engine live**: spins the lab replica, runs a real
  3-gate confirmation, requires CONFIRMED. bench: 13/13 route accuracy.
- **MCP surface 12 → 18 tools** (ledger_triage · chain_detect · phases_board ·
  coverage · relay_list · war_report).
- **CI migrated to `scripts/ci_smoke.sh`** (script = local truth = CI truth):
  the new engines are exercised for real — ledger dedupe, testers demo, chain
  CH-001, kage mirror→Sigma export→refire FIRED against a live dojo replica,
  dojo bench self-verification, kaisha revert evidence, refusal exit codes.

## v1.8.0 — consistency/release polish

- **Docs match the ten-mandate family.** README, SKILL.md, the injectable mandate
  and the MCP server metadata now say ten mandates (KAGE #8 the purple layer and
  DOJO #9 the range were added in v1.5.0/v1.7.0 but never reached the docs).
  Version badges, `related_skills`, family buttons, clone list, relations, chain
  one-liners, router table and STANDARD RELAY all updated.
- **Dispatcher docs/CLI brought up to date.** `spydermonkey.py` docstring, the
  `bench` note, README's CLI table and SKILL's Tooling section now list `scope`,
  `doctor`, `bench`, `arsenal` and `fleet`, plus the companion scripts.
- **Skilltree generator hardened.** `skilltree.py` now folds in the kage and dojo
  canons (all mandate `references/` dirs present on disk), appends a stable hash
  on slug collisions instead of silently overwriting earlier techniques, and
  preserves the `generated:` date of files that already exist. Library
  regenerated: **722** technique files, index deduplicated (722/722 links valid).
- **Bench covers the new legs.** `bench` now asserts the kage and dojo routes;
  11/11 = 100% at v1.8.0.
- **CI mirrors the docs.** Workflow compiles all five scripts, greps the tree for
  KAGE/DOJO, asserts the full relay, and smoke-tests `arsenal verify`,
  `bench_live --help` and `fleet --help`.

## v1.7.0 and earlier

See git history — v1.7.0 DOJO (the Range) · v1.6.0 ARSENAL (the execution layer,
13 scope-gated tool wrappers) · v1.5.0 KAGE (the Mirror, the purple layer) ·
v1.4.0 the agent FLEET · v1.3.0b the MCP server (12 tools) + `bench_live` + the 612-file skilltree · v1.3.0 the scope authority + doctor + bench · v1.2.0 SHUKAKU reason/hunt/feed · v1.1.0 the persona contract · v1.0.0 initial release.
